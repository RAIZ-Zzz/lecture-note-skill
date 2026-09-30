"""Check a note against the house style in references/note-template.md.

    python lint_note.py NOTE.md

Checks the mechanical parts only:
  1. slide pages are cited as (p.N) / (p. N), not "第 N 页" / "pp."
  2. beyond-slides content carries a citation: "(补充 [n])", or a "补充：… [n]" / "Supplement: … [n]"
     fold that ends with a "来源：[n]" / "Sources: [n]" line; no bare "（补充）", "(beyond slides)"
  3. every [n] cited in the text has a References entry, and every entry is cited
  4. every image / SVG embed is followed by a "*图 k · …*" / "*Figure k · …*" caption
Exits 1 and lists line numbers if anything fails.
"""
import re
import sys
from pathlib import Path

REF_HEAD = re.compile(r"^##\s+(参考文献|References)\s*$")
EMBED = re.compile(r"!\[\[[^\]]+\.(png|jpe?g|svg|gif)(\|[^\]]*)?\]\]", re.I)
CAPTION = re.compile(r"^\*(图|Figure) \d+ · ")
OLD_PAGE = re.compile(r"第\s*\d+(\s*[–-]\s*\d+)?\s*页|\bpp\.\s*\d")
BARE_SUPP = re.compile(r"（补充）|（补充[，,]|\(beyond slides\)|补充推理|（补充(?! \[\d+\]）)")
SUPP_FOLD = re.compile(r"^>\s*\[!note\]-\s*(补充：|Supplement: )(.*)$")
SOURCE_LINE = re.compile(r"^>\s*(来源：|Sources?: )(.*)$")
CITE = re.compile(r"(?<!\[)\[(\d+)\](?!\])")


def strip_code_math(line):
    line = re.sub(r"`[^`]*`", "", line)
    return re.sub(r"\$[^$]*\$", "", line)


def main():
    path = Path(sys.argv[1])
    lines = path.read_text(encoding="utf-8").splitlines()
    issues, cited, entries = [], set(), set()
    in_refs = in_fence = False
    open_supp = None  # line number of a supplement fold waiting for its source line

    for i, raw in enumerate(lines, 1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if REF_HEAD.match(raw):
            in_refs = True
            continue
        if in_refs:
            m = re.match(r"^\[(\d+)\]\s+\S", raw)
            if m:
                entries.add(int(m.group(1)))
            continue
        line = strip_code_math(raw)

        if open_supp and not raw.startswith(">"):
            issues.append(f"{open_supp}: supplement fold has no '来源：[n]' / 'Sources: [n]' line")
            open_supp = None
        m = SUPP_FOLD.match(raw)
        if m:
            if not CITE.search(m.group(2)):
                issues.append(f"{i}: supplement fold title needs a citation [n]")
            open_supp = i
        m = SOURCE_LINE.match(raw)
        if m:
            if not CITE.search(m.group(2)):
                issues.append(f"{i}: source line must cite numbered references, e.g. '来源：[2]'")
            open_supp = None

        if OLD_PAGE.search(line):
            issues.append(f"{i}: cite slide pages as （p.N） / (p. N)")
        if BARE_SUPP.search(line):
            issues.append(f"{i}: beyond-slides content needs '（补充 [n]）' or a '补充：… [n]' fold")
        cited.update(int(n) for n in CITE.findall(line))

        if EMBED.search(raw):
            nxt = next((l for l in lines[i:] if l.strip()), "")
            if not CAPTION.match(nxt):
                issues.append(f"{i}: embed needs a caption line '*图 k · p.N · …*' / '*Figure k · …*'")

    if open_supp:
        issues.append(f"{open_supp}: supplement fold has no '来源：[n]' / 'Sources: [n]' line")
    for n in sorted(cited - entries):
        issues.append(f"[{n}] is cited but has no References entry")
    for n in sorted(entries - cited):
        issues.append(f"References entry [{n}] is never cited")
    if cited and not entries:
        issues.append("citations used but no '## 参考文献' / '## References' section")

    sys.stdout.reconfigure(encoding="utf-8")
    if issues:
        print(f"{path.name}: {len(issues)} house-style issue(s)")
        print("\n".join(issues))
        sys.exit(1)
    print(f"{path.name}: house style ok")


if __name__ == "__main__":
    main()
