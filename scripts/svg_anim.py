"""Build, lint and preview the small animated SVGs embedded in lecture notes.

Library (import it from a generator script in the work folder):

    import sys; sys.path.insert(0, r"<skill>/scripts")
    from svg_anim import Scene
    sc = Scene(640, 360, cycle=8, title="梯度下降：每一步沿斜坡往下走")
    ax = sc.axes(x=(-3, 3), y=(0, 9), box=(60, 30, 600, 300), xlabel="w", ylabel="L(w)")
    sc.curve(ax, lambda w: w * w)
    pts = [(3, 9), (1.8, 3.24), (1.08, 1.1664)]          # the SAME numbers as the note / verify.py
    sc.mover(ax, pts, times=[1, 3, 5])                    # dot is at pts[i] from times[i]
    sc.trail(ax, pts, times=[1, 3, 5])                    # arrows appear as the dot moves
    sc.captions([(0, "起点 w=3"), (3, "第 1 步后 w=1.8"), (5, "第 2 步后 w=1.08")])
    sc.save("<work>/anim/gd-steps.svg")

Every animation shares ONE timeline: dur = cycle, repeatCount = indefinite, scheduled with
keyTimes. That keeps the parts in sync on every loop and lets `frames` seek to any moment.

CLI:
  lint   SVG [SVG ...]                 structural checks (see LINT RULES below)
  frames SVG OUT [--n 6 | --times 0,2.5,5] [--width 640]
                                       render moments of the animation with headless Chrome
                                       -> OUT/<name>-tX.png and OUT/<name>-strip.png (look at it!)
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

FONT = "Microsoft YaHei, PingFang SC, Noto Sans CJK SC, Source Han Sans SC, sans-serif"
COLORS = {"blue": "#2563eb", "orange": "#ea580c", "green": "#16a34a", "red": "#dc2626",
          "purple": "#7c3aed", "gray": "#6b7280", "ink": "#1f2937", "grid": "#e5e7eb",
          "bg": "#ffffff", "border": "#d1d5db"}


def _c(color):
    return COLORS.get(color, color)


def _n(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


class Axes:
    """Maps data coordinates to pixels inside box=(x0, y0, x1, y1) (pixel y grows downward)."""

    def __init__(self, x, y, box):
        self.xr, self.yr, self.box = x, y, box

    def px(self, x, y):
        (a, b), (c, d), (x0, y0, x1, y1) = self.xr, self.yr, self.box
        return x0 + (x - a) / (b - a) * (x1 - x0), y1 - (y - c) / (d - c) * (y1 - y0)


class Scene:
    def __init__(self, width=640, height=360, cycle=8.0, title=None):
        self.w, self.h, self.cycle = width, height, float(cycle)
        self.parts = []
        self.markers = {}
        if title:
            self.text(width / 2, 22, title, size=16, weight="bold")

    # ---- timeline helpers -------------------------------------------------------------
    def _kt(self, t):
        if not 0 <= t <= self.cycle:
            raise ValueError(f"time {t} outside 0..{self.cycle}")
        return _n(t / self.cycle)

    def _anim(self, attr, times, values, discrete=False):
        """values[i] holds from times[i]; linear glide between keys unless discrete."""
        times, values = list(times), list(values)
        if times[0] > 0:
            times, values = [0] + times, [values[0]] + values
        if times[-1] < self.cycle:
            times, values = times + [self.cycle], values + [values[-1]]
        if any(b < a for a, b in zip(times, times[1:])):
            raise ValueError(f"times must be non-decreasing: {times}")
        mode = ' calcMode="discrete"' if discrete else ""
        if discrete:  # discrete keyTimes: value i shows from keyTimes[i]; drop the closing key
            times, values = times[:-1], values[:-1]
        return (f'<animate attributeName="{attr}" dur="{_n(self.cycle)}s" repeatCount="indefinite"'
                f'{mode} keyTimes="{";".join(self._kt(t) for t in times)}" '
                f'values="{";".join(str(v) for v in values)}"/>')

    def _show(self, show):
        """show=(t0, t1): visible from t0 to t1 (t1=None -> until the loop restarts)."""
        if show is None:
            return ""
        t0, t1 = show
        t1 = self.cycle if t1 is None else t1
        times, vals = [0, t0, t1], [0, 1, 0 if t1 < self.cycle else 1]
        if t0 == 0:
            times, vals = [0, t1], [1, vals[2]]
        return self._anim("opacity", times, vals, discrete=True)

    def _wrap(self, element, show):
        if show is None:
            self.parts.append(element)
        else:
            self.parts.append(f'<g opacity="{0 if show[0] > 0 else 1}">{element}{self._show(show)}</g>')

    def _marker(self, color):
        # one marker per colour: fill="context-stroke" is not supported by older Electron builds
        name = "arrow-" + _c(color).lstrip("#")
        self.markers[name] = (f'<marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                              f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
                              f'fill="{_c(color)}"/></marker>')
        return name

    # ---- drawing ------------------------------------------------------------------------
    def text(self, x, y, s, size=13, color="ink", anchor="middle", weight="normal", show=None):
        self._wrap(f'<text x="{_n(x)}" y="{_n(y)}" font-size="{size}" fill="{_c(color)}" '
                   f'text-anchor="{anchor}" font-weight="{weight}">{escape(str(s))}</text>', show)

    def line(self, x1, y1, x2, y2, color="ink", width=1.5, dash=None, arrow=False, show=None):
        extra = (f' stroke-dasharray="{dash}"' if dash else "") + (f' marker-end="url(#{self._marker(color)})"' if arrow else "")
        self._wrap(f'<line x1="{_n(x1)}" y1="{_n(y1)}" x2="{_n(x2)}" y2="{_n(y2)}" '
                   f'stroke="{_c(color)}" stroke-width="{width}"{extra}/>', show)

    def rect(self, x, y, w, h, fill="none", stroke="ink", rx=4, show=None):
        self._wrap(f'<rect x="{_n(x)}" y="{_n(y)}" width="{_n(w)}" height="{_n(h)}" rx="{rx}" '
                   f'fill="{_c(fill)}" stroke="{_c(stroke)}"/>', show)

    def dot(self, x, y, r=5, color="blue", show=None):
        self._wrap(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{r}" fill="{_c(color)}"/>', show)

    def axes(self, x, y, box, xlabel="", ylabel="", ticks=True):
        ax = Axes(x, y, box)
        x0, y0, x1, y1 = box
        zx = min(max(0, y[0]), y[1])  # draw the x axis at y=0 when it is in range
        zy = min(max(0, x[0]), x[1])
        _, py = ax.px(0, zx)
        px, _ = ax.px(zy, 0)
        self.line(x0, py, x1 + 8, py, color="gray", arrow=True)
        self.line(px, y1, px, y0 - 8, color="gray", arrow=True)
        if xlabel:
            self.text(x1 + 12, py + 4, xlabel, anchor="start", color="gray")
        if ylabel:
            self.text(px + 8, y0 - 2, ylabel, color="gray", anchor="start")
        if ticks:
            for v in _ticks(*x):
                tx, _ = ax.px(v, 0)
                self.line(tx, py, tx, py + 4, color="gray", width=1)
                self.text(tx, py + 16, _n(v), size=10, color="gray")
            for v in _ticks(*y):
                _, ty = ax.px(0, v)
                if v:
                    self.line(px - 4, ty, px, ty, color="gray", width=1)
                    self.text(px - 7, ty + 3, _n(v), size=10, color="gray", anchor="end")
        return ax

    def curve(self, ax, f, n=200, color="gray", width=2, show=None):
        a, b = ax.xr
        pts = []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            y = f(x)
            if ax.yr[0] - 1e9 < y < ax.yr[1] + 1e9:
                pts.append(ax.px(x, min(max(y, ax.yr[0] - (ax.yr[1] - ax.yr[0])), 2 * ax.yr[1])))
        d = " ".join(f"{_n(p)},{_n(q)}" for p, q in pts)
        self._wrap(f'<polyline points="{d}" fill="none" stroke="{_c(color)}" stroke-width="{width}" '
                   f'clip-path="url(#plot{id(ax)})"/>', show)
        self._clip(ax)

    def _clip(self, ax):
        x0, y0, x1, y1 = ax.box
        clip = f'<clipPath id="plot{id(ax)}"><rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/></clipPath>'
        if clip not in self.parts:
            self.parts.insert(0, clip)

    def mover(self, ax, points, times, r=6, color="orange", glide=0.6, label=None):
        """A dot sitting at points[i] from times[i]; it glides for `glide` seconds into each point."""
        keys_t, keys_x, keys_y = [], [], []
        for i, ((x, y), t) in enumerate(zip(points, times)):
            px, py = ax.px(x, y)
            if i:
                keys_t.append(max(t - glide, times[i - 1]))
                keys_x.append(keys_x[-1]); keys_y.append(keys_y[-1])
            keys_t.append(t); keys_x.append(_n(px)); keys_y.append(_n(py))
        cx, cy = keys_x[0], keys_y[0]
        self.parts.append(
            f'<g opacity="{0 if times[0] > 0 else 1}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{_c(color)}" '
            f'stroke="#fff" stroke-width="1.5">{self._anim("cx", keys_t, keys_x)}{self._anim("cy", keys_t, keys_y)}'
            f'</circle>{self._show((times[0], None))}</g>')

    def trail(self, ax, points, times, color="orange", width=2):
        """Arrow from points[i-1] to points[i], appearing when the dot arrives (times[i])."""
        for i in range(1, len(points)):
            (x1, y1), (x2, y2) = ax.px(*points[i - 1]), ax.px(*points[i])
            self.line(x1, y1, x2, y2, color=color, width=width, dash="5 3", arrow=True,
                      show=(times[i], None))

    def captions(self, items, y=None, size=14, color="ink"):
        """items = [(t, text), ...]; each caption replaces the previous one at time t."""
        y = self.h - 14 if y is None else y
        for i, (t, s) in enumerate(items):
            end = items[i + 1][0] if i + 1 < len(items) else None
            self.text(self.w / 2, y, s, size=size, color=color, show=(t, end))

    def raw(self, svg_fragment):
        self.parts.append(svg_fragment)

    def svg(self):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" data-cycle="{_n(self.cycle)}" font-family="{FONT}">'
                f'<defs>{"".join(self.markers.values())}</defs>'
                f'<rect width="{self.w}" height="{self.h}" rx="10" fill="{COLORS["bg"]}" '
                f'stroke="{COLORS["border"]}"/>')
        return head + "\n".join(self.parts) + "</svg>\n"

    def save(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(self.svg(), encoding="utf-8")
        problems = lint_one(path)
        print(json.dumps({"saved": str(path), "problems": problems}, ensure_ascii=False))
        return path


def _ticks(a, b):
    span = b - a
    step = 10 ** math.floor(math.log10(span / 5))
    for m in (1, 2, 5, 10):
        if span / (step * m) <= 8:
            step *= m
            break
    v = math.ceil(a / step) * step
    out = []
    while v <= b + 1e-9:
        out.append(round(v, 10))
        v += step
    return out


# ---- LINT RULES ----------------------------------------------------------------------------
# Obsidian shows ![[x.svg]] as an <img>: no scripts, no events, no external files, and the
# note's theme cannot restyle it. So the SVG must be self-contained and self-running.
def lint_one(path):
    problems = []
    text = Path(path).read_text(encoding="utf-8")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return [f"not well-formed XML: {exc}"]
    ns = "{http://www.w3.org/2000/svg}"
    if root.tag != ns + "svg":
        problems.append("root element is not <svg> in the SVG namespace")
    if not root.get("viewBox"):
        problems.append("missing viewBox")
    if int(float(root.get("width", "0") or 0)) > 900:
        problems.append("width > 900 px: too wide for a note column")
    cycle = root.get("data-cycle")
    anims = [e for e in root.iter() if e.tag in (ns + "animate", ns + "animateTransform", ns + "animateMotion", ns + "set")]
    if anims and not cycle:
        problems.append("animated SVG needs data-cycle=<seconds> on the root")
    for e in root.iter():
        tag = e.tag.replace(ns, "")
        if tag in ("script", "foreignObject"):
            problems.append(f"<{tag}> will not run inside an <img>")
        for k, v in e.attrib.items():
            if k.startswith("on"):
                problems.append(f"event handler {k} on <{tag}> never fires in an <img>")
            if k.endswith("href") and re.match(r"(https?:|file:|[^#])", v or ""):
                problems.append(f"external reference {v!r}: images inside an <img> SVG must be inline")
            if k == "begin" and re.search(r"click|mouse|focus|\.begin|\.end", v):
                problems.append(f"begin={v!r}: use the shared timeline (keyTimes), not events/chaining")
    for e in anims:
        if cycle and e.get("dur") not in (f"{cycle}s", f"{float(cycle):g}s"):
            problems.append(f"<{e.tag.replace(ns, '')} {e.get('attributeName')}> dur={e.get('dur')} != cycle {cycle}s")
        if e.get("repeatCount") != "indefinite":
            problems.append(f"<{e.tag.replace(ns, '')} {e.get('attributeName')}> should repeatCount=indefinite")
        kt, vals = e.get("keyTimes"), e.get("values")
        if kt and vals and len(kt.split(";")) != len(vals.split(";")):
            problems.append(f"keyTimes/values length mismatch on {e.get('attributeName')}")
    if re.search(r"@keyframes|animation\s*:", text):
        problems.append("CSS animation found: use SMIL <animate> so `frames` can seek it")
    if re.search(r"[\u4e00-\u9fff]", text) and "YaHei" not in text and "CJK" not in text:
        problems.append("Chinese text but no CJK font in font-family")
    first = next((e for e in root if e.tag == ns + "rect"), None)
    if first is None or first.get("fill") in (None, "none", "transparent"):
        problems.append("first child should be an opaque background <rect> (dark themes)")
    return problems


def lint(args):
    report = {p: lint_one(p) for p in args.svg}
    print(json.dumps(report, ensure_ascii=False, indent=1))
    sys.exit(1 if any(report.values()) else 0)


# ---- FRAMES --------------------------------------------------------------------------------
def find_browser():
    for p in (os.environ.get("CHROME"),
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/usr/bin/google-chrome", "/usr/bin/chromium"):
        if p and Path(p).exists():
            return p
    sys.exit("no Chrome/Edge found; set $CHROME")


def frames(args):
    import pymupdf  # only needed for the strip

    svg_path = Path(args.svg)
    text = svg_path.read_text(encoding="utf-8")
    root = ET.fromstring(text)
    cycle = float(root.get("data-cycle") or 0)
    w = float(root.get("width") or args.width)
    h = float(root.get("height") or w * 9 / 16)
    if args.times:
        times = [float(t) for t in args.times.split(",")]
    else:
        n = max(args.n, 1)
        times = [round(cycle * i / (n - 1), 3) if n > 1 else 0 for i in range(n)]
        times[-1] = max(times[-1] - 0.01, 0)  # just before the loop restarts
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    browser = find_browser()
    profile = tempfile.mkdtemp(prefix="svgframes-")
    shots = []
    for t in times:
        html = out / f"_{svg_path.stem}-t{t:g}.html"
        html.write_text(
            '<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fff">'
            f'<div style="width:{w:g}px;height:{h:g}px">{text}</div><script>'
            'var s=document.querySelector("svg");s.pauseAnimations();'
            f's.setCurrentTime({t});</script></body>', encoding="utf-8")
        png = out / f"{svg_path.stem}-t{t:g}.png"
        subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                        f"--user-data-dir={profile}", f"--window-size={int(w)},{int(h)}",
                        "--virtual-time-budget=1500", f"--screenshot={png}", html.resolve().as_uri()],
                       capture_output=True, timeout=60)
        html.unlink()
        if not png.exists():
            sys.exit(f"browser produced no screenshot for t={t}")
        shots.append((t, png))

    # contact strip: 2 columns, time label above each frame
    cols = 2
    rows = math.ceil(len(shots) / cols)
    sheet_doc = pymupdf.open()
    page = sheet_doc.new_page(width=cols * (w + 10), height=rows * (h + 30))
    for i, (t, png) in enumerate(shots):
        x, y = (i % cols) * (w + 10), (i // cols) * (h + 30)
        page.insert_text((x + 4, y + 18), f"t = {t:g}s", fontsize=14, color=(0.8, 0, 0))
        page.insert_image(pymupdf.Rect(x, y + 24, x + w, y + 24 + h), filename=str(png))
    strip = out / f"{svg_path.stem}-strip.png"
    page.get_pixmap().save(strip)
    print(json.dumps({"cycle": cycle, "times": times, "strip": str(strip),
                      "frames": [str(p) for _, p in shots]}, ensure_ascii=False, indent=1))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lint")
    p.add_argument("svg", nargs="+")
    p.set_defaults(func=lint)
    f = sub.add_parser("frames")
    f.add_argument("svg")
    f.add_argument("out")
    f.add_argument("--n", type=int, default=6)
    f.add_argument("--times")
    f.add_argument("--width", type=float, default=640)
    f.set_defaults(func=frames)
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    args.func(args)


if __name__ == "__main__":
    main()
