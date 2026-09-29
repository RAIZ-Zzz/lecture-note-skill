# lecture-note — Claude Code skill

A Claude Code skill that turns lecture slides (PDF) into a detailed, step-by-step **teaching** note in an Obsidian vault, and that can teach an existing note interactively by exercises. This README describes how the skill works.

## Note language

Chosen per note (`--lang`, or the skill asks):

| Option | Result |
|---|---|
| `zh+en` (recommended) | Plain Chinese narrative; every technical point is stated in Chinese and then in English |
| `zh` | Chinese only, English term in parentheses on first use |
| `en` | English throughout |
| `en+zh` | Plain English narrative; every technical point is stated in English and then in Chinese |
| custom | any mix you describe |

Callout labels ("Analogy", "Deep dive", "Pause", …) follow the note language; the label table is in `references/note-template.md`.

## What the notes look like

- **One lesson arc for every knowledge point.** (1) What goes wrong without it, in plain words; (2) a small scenario in which the reader, guided by 3–5 questions, designs the fix themselves; (3) only then the slides' name, definition and formula, mapped onto the reader's own answers; (4) what it really solves, how it connects to earlier material, and what it is used for; (5) its pros and cons, whose remaining weakness leads into the next lesson. No section opens with a term, a formula or bare numbers.
- **Built for learning, not exam drilling.** Every point on the slides is covered, but the aim is to understand what each idea is for. Engineering topics start from practical situations ("can this layer see the whole cat?"); pure-math topics may be more abstract but still start from something computable by hand.
- **Interactive mode.** Ask the skill to teach a section of an existing note and it poses one question per turn, checks each answer, and on a wrong answer shows where the number came from instead of re-teaching the whole section.
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
| `scripts/mindmap.py` | Optional course mind map: an outline with `@week\|heading@` link tokens becomes an inline `markmap` note (rendered by the Obsidian plugin Mindmap NextGen); every heading link is checked |
| `scripts/publish_note.py` | Writes the note and its attachments into the vault through `cli-anything-obsidian`, refuses to overwrite edits made in Obsidian, and checks that every embed resolves |

## How animations stay accurate

1. Positions are computed by a generator script from the same numbers used in the note, never typed by hand.
2. `svg_anim.py lint` enforces SMIL-only animation on one shared looping timeline (no scripts, click triggers or CSS keyframes, which do not run when Obsidian embeds an SVG as an image), an opaque background for dark themes, and a CJK font stack.
3. `svg_anim.py frames` pauses the timeline at chosen times and screenshots each frame, so every key moment can be checked against the text before publishing.
4. Every animation is followed by a static table of the same numbers, so the note still works if the animation does not play.

## Installation on a new machine

The skill itself holds nothing machine-specific: nothing in this repo needs editing. A machine
needs the following before the first run.

### Required

1. [Claude Code](https://claude.com/claude-code).
2. Python 3, then the two packages the scripts use (both on PyPI):
   ```bash
   pip install pymupdf cli-anything-obsidian
   ```
   On macOS / Linux the command may be `python3` / `pip3`.
3. [Obsidian](https://obsidian.md), with your vault open whenever the skill runs:
   - install and enable the community plugin **Local REST API**;
   - copy its API key into the environment variable `OBSIDIAN_API_KEY`.

   Check: `cli-anything-obsidian --json vault list` prints your vault's top-level folders.
4. The environment variable `OBSIDIAN_VAULT` = absolute path of that same vault folder
   (attachments are copied there on disk; the publish script refuses to run if it is not the
   vault Obsidian has open).
5. The skill itself:
   ```bash
   git clone https://github.com/RAIZ-Zzz/lecture-note-skill ~/.claude/skills/lecture-note
   ```
   Update later with `git pull`. Without git, download the zip and unpack it to the same folder.

Notes go to `Lecture Notes/<course>/` inside the vault; create one folder per course there.

### Optional

- Google Chrome or Microsoft Edge: only for previewing animation frames. Set `$CHROME` if it is
  not in a standard location.
- `local.md`: a two-column table (`| Vault folder | Slides |`) listing where each course's slides are on
  this machine. It is git-ignored. Without it, the skill asks for the PDF path and offers to
  create the file.
- The Obsidian plugin **Mindmap NextGen**: only for the optional course mind map.

### Use

In Claude Code, run `/lecture-note <course> <week> [pdf path] [pages A-B] [--lang zh|en|zh+en|en+zh]`, or ask it to teach a section of an existing note ("teach me WEEK 5 section 10.2, you ask and I answer").

## License

MIT — see [LICENSE](LICENSE).
