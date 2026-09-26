"""Course mind map (optional step): outline.md -> '<course> 知识导图.md' with one ```markmap block.

  python mindmap.py OUTLINE.md OUT.md --course-dir "D:/obsidian/repo/NTULEARN/Lecture Notes/<course>"
                    [--expand 6] [--height 1000]

OUTLINE.md is plain markmap markdown (# root, ## themes, ### knowledge points, - details) in which
links to lecture notes are written as  @<week>|<exact heading text>@  , e.g.
    ### 条件数 @7|3.3 细长的碗：条件数与“之字形”（第 32–35 页）@
The script turns them into [[WEEK 7#heading|↗W7]], checks every heading exists in that week's note
(exits with the list of broken ones otherwise), and wraps the outline in a ```markmap block so the
Mindmap NextGen plugin renders it inline as soon as the note is opened. If OUT.md already exists
(e.g. the plugin saved a new height after the user resized the map), its height is kept.
"""
import argparse
import re
import sys
from pathlib import Path


def week_note(course_dir, week):
    hits = sorted(Path(course_dir).glob(f"WEEK {week}*.md"))
    if not hits:
        sys.exit(f"no note for WEEK {week} in {course_dir}")
    return hits[0]


def headings(path):
    return set(h.strip() for h in re.findall(r"^#{1,6} (.+)$", path.read_text(encoding="utf-8"), re.M))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("outline")
    ap.add_argument("out")
    ap.add_argument("--course-dir", required=True)
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
            "> [!tip] 点节点旁的圆点展开 / 收起；每个知识点下有 是什么 · 为什么 · 公式 · 例 · 注意 · ↔ 跨周联系；"
            "点 ↗ 跳到笔记小节。\n\n"
            f"```markmap\n---\nmarkmap:\n  colorFreezeLevel: 2\n  initialExpandLevel: {a.expand}\n"
            f"  maxWidth: 380\n  height: {height}\n---\n{outline}\n```\n")
    out.write_text(note, encoding="utf-8", newline="\n")
    print(f"{out}: {count} links ok, height {height}")


if __name__ == "__main__":
    main()
