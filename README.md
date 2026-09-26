# lecture-note — Claude Code skill

A Claude Code skill that turns one week's lecture slides (PDF) into a detailed, step-by-step **teaching** note in an Obsidian vault. The notes are written in Chinese with English technical terms; this README describes how the skill works.

## What the notes look like

- **Taught, not summarized.** Each lesson introduces at most one or two new terms and follows the same rhythm: a concrete problem → an everyday analogy → a tiny worked example with small numbers → the formula, with every symbol mapped back to those numbers → a one-sentence takeaway.
- **Easy to hard.** Before writing, the skill plans a learning ladder so every concept only relies on concepts explained above it. No term is used before it is explained.
- **Analogies and small calculations** accompany every abstract idea (gradients, curvature, variance, momentum, …).
- **Simple main line, depth on demand.** Full derivations, proofs, edge cases and material beyond the slides go into collapsible "deep dive (optional)" callouts, so a reader who skips them still follows the lecture.
- **Check-in questions** after each part and at least 10 practice questions with folded answers.
- **Slide screenshots** where a picture carries meaning the text can't.
- **Animated SVGs for anything dynamic**: optimizer steps, forward/backward passes, sliding kernels, token flow through an LLM, agent and training loops. Workflow diagrams are built from boxes, arrows and "tokens" that travel along the arrows; static structure diagrams use the same helpers. Everything is generated from code and plays inside Obsidian's `![[file.svg]]` embeds.
- **Every number is verified** by a generated `verify.py` script using exact arithmetic, including the numbers shown in animations.
- **Grounded content**: the slides are the ground truth; anything the note adds beyond them (supplements, deep-dive folds, paper attributions) is checked online against primary papers or standard textbooks while writing and cites its source, or is marked as unverified.
- **Optional course mind map**: after a note is written, the user is asked whether to update one course-wide mind map; each knowledge point carries what / why / formula / worked example / pitfall / cross-week links, with links back into the notes.
- **Optional strict review**: on request, an evaluator-optimizer loop runs a fresh evaluator subagent that checks each claim and the teaching rules; the writer fixes or rebuts each finding with evidence, for up to 3 rounds (`references/evaluator.md`). It is optional because it costs hundreds of thousands of tokens per round.

## Layout

| Path | Purpose |
|---|---|
| `SKILL.md` | The workflow and writing rules Claude follows |
| `references/note-template.md` | Frontmatter and section skeleton of a note |
| `scripts/prep_slides.py` | PDF → text with page markers, overview contact sheets, and slide screenshots (PyMuPDF) |
| `scripts/svg_anim.py` | `Scene` helper that builds animated SVGs from computed data; `lint` checks them for Obsidian compatibility; `frames` renders chosen moments with headless Chrome/Edge into a strip for visual review |
| `scripts/mindmap.py` | Optional course mind map: an outline with `@week|heading@` link tokens becomes an inline `markmap` note (rendered by the Obsidian plugin Mindmap NextGen); every heading link is checked |
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
