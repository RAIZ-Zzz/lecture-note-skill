"""Course mind map (optional step): outline.md -> the course mind map note with one ```markmap block.

  python mindmap.py OUTLINE.md OUT.md --course-dir "$OBSIDIAN_VAULT/Lecture Notes/<course>"
                    [--lang zh|en] [--expand 6] [--height 1000]

OUTLINE.md is plain markmap markdown (# root, ## themes, ### knowledge points, - details) in which
links to lecture notes are written as  @<week>|<exact heading text>@  , e.g.
    ### Condition number @7|3.3 A long narrow bowl: condition number and zig-zagging (pp. 32-35)@
The script turns them into [[WEEK 7#heading|↗W7]], checks every heading exists in that week's note
(exits with the list of broken ones otherwise), and wraps the outline in a ```markmap block so the
Mindmap NextGen plugin renders it inline as soon as the note is opened. --lang picks the language of
the one-line usage tip at the top (zh for zh / zh+en notes, en for en / en+zh). If OUT.md already exists
(e.g. the plugin saved a new height after the user resized the map), its height is kept.
"""
import argparse
import re
import sys
from pathlib import Path


TIPS = {
    "zh": "> [!tip] \u70b9\u8282\u70b9\u65c1\u7684\u5706\u70b9\u5c55\u5f00 / \u6536\u8d77\uff1b"
          "\u6bcf\u4e2a\u77e5\u8bc6\u70b9\u4e0b\u6709 \u662f\u4ec0\u4e48 \u00b7 \u4e3a\u4ec0\u4e48 \u00b7 "
          "\u516c\u5f0f \u00b7 \u4f8b \u00b7 \u6ce8\u610f \u00b7 \u2194 \u8de8\u5468\u8054\u7cfb\uff1b"
          "\u70b9 \u2197 \u8df3\u5230\u7b14\u8bb0\u5c0f\u8282\u3002",
    "en": "> [!tip] Click the dot next to a node to expand / collapse. Each knowledge point has what \u00b7 "
          "why \u00b7 formula \u00b7 example \u00b7 pitfall \u00b7 \u2194 cross-week links; "
          "click \u2197 to jump to the note section.",
}


def week_note(course_dir, week):
    # "WEEK 1" or "WEEK 1 - Title", never WEEK 10 or WEEK 1.1
    hits = [p for p in Path(course_dir).glob("WEEK *.md")
            if re.fullmatch(rf"WEEK {re.escape(week)}( .*)?", p.stem)]
    if len(hits) != 1:
        sys.exit(f"WEEK {week} in {course_dir}: expected one note, found {[p.name for p in hits]}")
    return hits[0]


def headings(path):
    return set(h.strip() for h in re.findall(r"^#{1,6} (.+)$", path.read_text(encoding="utf-8"), re.M))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("outline")
    ap.add_argument("out")
    ap.add_argument("--course-dir", required=True)
    ap.add_argument("--lang", choices=sorted(TIPS), default="zh", help="language of the usage tip line")
    ap.add_argument("--expand", type=int, default=6, help="initialExpandLevel (levels shown when opened)")
    ap.add_argument("--height", type=int, default=1000)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    src = Path(a.outline).read_text(encoding="utf-8").strip("\n")
    bad, count = [], 0

    def link(m):
        nonlocal count
        week, head = m.group(1), m.group(2).strip()
        note = week_note(a.course_dir, week)
        if head not in headings(note):
            bad.append(f"WEEK {week}: {head}")
        count += 1
        return f"[[{note.stem}#{head}|↗W{week}]]"

    outline = re.sub(r"@(\d+(?:\.\d+)?)\|([^@]+)@", link, src)
    if bad:
        sys.exit("headings not found:\n" + "\n".join(bad))
    if "@" in re.sub(r"\$[^$]*\$", "", outline):
        sys.exit("an @week|heading@ token was not closed")

    height = a.height
    out = Path(a.out)
    if out.exists():  # keep a height the user set by resizing the map in Obsidian
        m = re.search(r"^\s*height:\s*(\d+)", out.read_text(encoding="utf-8"), re.M)
        if m:
            height = int(m.group(1))

    note = ("---\ntags:\n  - mindmap\n---\n\n"
            f"{TIPS[a.lang]}\n\n"
            f"```markmap\n---\nmarkmap:\n  colorFreezeLevel: 2\n  initialExpandLevel: {a.expand}\n"
            f"  maxWidth: 380\n  height: {height}\n---\n{outline}\n```\n")
    out.write_text(note, encoding="utf-8", newline="\n")
    print(f"{out}: {count} links ok, height {height}")


if __name__ == "__main__":
    main()
