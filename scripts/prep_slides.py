"""Prepare a lecture PDF for note-writing.

  prep  PDF OUT [--pages A-B]          text with page markers + overview sheets + page stats
  shot  PDF OUT PAGE [PAGE ...] [--clip x0,y0,x1,y1] [--dpi 160]
                                        render chosen slides (1-based) to OUT/sNN.png

Page numbers are always 1-based PDF page numbers (index = page - 1).
"""
import argparse
import json
import sys
from pathlib import Path

import pymupdf


def page_range(spec, count):
    if not spec:
        return list(range(1, count + 1))
    start, _, stop = spec.partition("-")
    return list(range(int(start), int(stop or start) + 1))


def prep(args):
    doc = pymupdf.open(args.pdf)
    out = Path(args.out)
    (out / "sheets").mkdir(parents=True, exist_ok=True)
    pages = page_range(args.pages, doc.page_count)

    stats = []
    with open(out / "text.txt", "w", encoding="utf-8") as fh:
        for number in pages:
            page = doc[number - 1]
            text = page.get_text("text").strip()
            fh.write(f"\n===== page {number} =====\n{text}\n")
            stats.append({
                "page": number,
                "chars": len(text),
                "images": len(page.get_images()),
                "drawings": len(page.get_drawings()),
            })

    # 12 slides per sheet (3 columns x 4 rows) so every page can be skimmed visually.
    cols, rows = 3, 4
    width = 640
    for start in range(0, len(pages), cols * rows):
        chunk = pages[start:start + cols * rows]
        first = doc[chunk[0] - 1].rect
        height = width * first.height / first.width
        sheet_doc = pymupdf.open()
        sheet = sheet_doc.new_page(width=cols * width, height=rows * (height + 24))
        for offset, number in enumerate(chunk):
            col, row = offset % cols, offset // cols
            top = row * (height + 24)
            sheet.insert_text((col * width + 6, top + 16), f"p{number}", fontsize=14, color=(0.8, 0, 0))
            rect = pymupdf.Rect(col * width, top + 22, (col + 1) * width, top + 22 + height)
            sheet.show_pdf_page(rect, doc, number - 1)
        name = f"sheet-{chunk[0]:02d}-{chunk[-1]:02d}.png"
        sheet.get_pixmap().save(out / "sheets" / name)

    summary = {
        "pdf": str(Path(args.pdf).resolve()),
        "pdf_page_count": doc.page_count,
        "pages": f"{pages[0]}-{pages[-1]}",
        "last_page_tail": doc[pages[-1] - 1].get_text().strip()[-80:],  # shows the slide footer number
        "empty_text_pages": [s["page"] for s in stats if s["chars"] < 20],
        "text": str(out / "text.txt"),
        "sheets": sorted(p.name for p in (out / "sheets").glob("*.png")),
    }
    (out / "stats.json").write_text(json.dumps(stats, indent=1), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))


def shot(args):
    doc = pymupdf.open(args.pdf)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    zoom = pymupdf.Matrix(args.dpi / 72, args.dpi / 72)
    for number in args.page:
        page = doc[number - 1]
        clip = pymupdf.Rect(*map(float, args.clip.split(","))) if args.clip else page.rect
        target = out / f"s{number:02d}.png"
        page.get_pixmap(matrix=zoom, clip=clip).save(target)
        print(f"{target}  (page rect {tuple(round(v) for v in page.rect)})")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prep")
    p.add_argument("pdf")
    p.add_argument("out")
    p.add_argument("--pages")
    p.set_defaults(func=prep)
    s = sub.add_parser("shot")
    s.add_argument("pdf")
    s.add_argument("out")
    s.add_argument("page", nargs="+", type=int)
    s.add_argument("--clip")
    s.add_argument("--dpi", type=int, default=160)
    s.set_defaults(func=shot)
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    args.func(args)


if __name__ == "__main__":
    main()
