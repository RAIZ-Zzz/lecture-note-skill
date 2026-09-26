# lecture-note — Claude Code skill

Turns one week's lecture slides (PDF) into a Chinese, step-by-step **teaching** note in an Obsidian vault:

- 讲解式、从易到难：one new idea per lesson, each following *问题 → 打个比方 → 小算例 → 公式 → 一句话记住*
- analogies and tiny hand calculations for every abstract concept
- main line kept simple; derivations / proofs / edge cases folded as `> [!note]- 深入：…（可跳过）`
- slide screenshots + **animated SVGs** generated from code (SMIL, plays inside Obsidian's `![[x.svg]]`)
- every number re-checked by a `verify.py` script; ≥10 practice questions with folded answers

## Layout

| Path | What |
|---|---|
| `SKILL.md` | the workflow and writing rules Claude follows |
| `references/note-template.md` | frontmatter + section skeleton of a note |
| `scripts/prep_slides.py` | PDF → text with page markers, overview sheets, slide screenshots (pymupdf) |
| `scripts/svg_anim.py` | `Scene` helper to build animated SVGs from computed data; `lint`; `frames` renders chosen moments with headless Chrome/Edge into a strip for checking |
| `scripts/publish_note.py` | writes the note + attachments into the vault via `cli-anything-obsidian`, refuses to clobber edits, checks embeds |

## Install

Copy the folder to `~/.claude/skills/lecture-note/`, then run `/lecture-note <course> <week> [pdf]` in Claude Code.
Requires Python with `pymupdf`, [`cli-anything-obsidian`](https://github.com/HKUDS/CLI-Anything), and Chrome or Edge for animation previews.
Course folders and vault path in `SKILL.md` are specific to the author's machine; edit the *Fixed facts* section for yours.
