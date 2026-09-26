# lecture-note — Claude Code skill

A Claude Code skill that turns one week's lecture slides (PDF) into a detailed, step-by-step **teaching** note in an Obsidian vault. The notes are written in Chinese with English technical terms; this README describes how the skill works.

## What the notes look like

- **Taught, not summarized.** Each lesson introduces at most one or two new terms and follows the same rhythm: a concrete problem → an everyday analogy → a tiny worked example with small numbers → the formula, with every symbol mapped back to those numbers → a one-sentence takeaway.
- **Easy to hard.** Before writing, the skill plans a learning ladder so every concept only relies on concepts explained above it. No term is used before it is explained.
- **Analogies and small calculations** accompany every abstract idea (gradients, curvature, variance, momentum, …).
- **Simple main line, depth on demand.** Full derivations, proofs, edge cases and material beyond the slides go into collapsible "deep dive (optional)" callouts, so a reader who skips them still follows the lecture.
- **Check-in questions** after each part and at least 10 practice questions with folded answers.
- **Slide screenshots** where a picture carries meaning the text can't.
- **Animated SVGs** for processes that unfold over time (optimizer steps, sliding kernels, forward/backward passes). They are generated from code and play inside Obsidian's `![[file.svg]]` embeds.
- **Every number is verified** by a generated `verify.py` script using exact arithmetic, including the numbers shown in animations.

## Layout

| Path | Purpose |
|---|---|
| `SKILL.md` | The workflow and writing rules Claude follows |
| `references/note-template.md` | Frontmatter and section skeleton of a note |
| `scripts/prep_slides.py` | PDF → text with page markers, overview contact sheets, and slide screenshots (PyMuPDF) |
| `scripts/svg_anim.py` | `Scene` helper that builds animated SVGs from computed data; `lint` checks them for Obsidian compatibility; `frames` renders chosen moments with headless Chrome/Edge into a strip for visual review |
| `scripts/publish_note.py` | Writes the note and its attachments into the vault through `cli-anything-obsidian`, refuses to overwrite edits made in Obsidian, and checks that every embed resolves |

## How animations stay accurate

1. Positions are computed by a generator script from the same numbers used in the note, never typed by hand.
2. `svg_anim.py lint` enforces SMIL-only animation on one shared looping timeline (no scripts, click triggers or CSS keyframes, which do not run when Obsidian embeds an SVG as an image), an opaque background for dark themes, and a CJK font stack.
3. `svg_anim.py frames` pauses the timeline at chosen times and screenshots each frame, so every key moment can be checked against the text before publishing.
4. Every animation is followed by a static table of the same numbers, so the note still works if the animation does not play.

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Python 3 with `pymupdf`
- [`cli-anything-obsidian`](https://github.com/HKUDS/CLI-Anything) for reading and writing the vault
- Google Chrome or Microsoft Edge (only for previewing animation frames)

## Installation

1. Copy this folder to `~/.claude/skills/lecture-note/`.
2. Edit the **Fixed facts** section of `SKILL.md`: the vault path, the course folders and the slide locations are specific to the author's machine.
3. In Claude Code, run `/lecture-note <course> <week> [pdf path] [pages A-B]`.

## License

MIT — see [LICENSE](LICENSE).
