---
name: lecture-note
description: >
  Turn one week's lecture slides (PDF) into a step-by-step teaching note built for learning, not
  exam drilling: every knowledge point goes problem → reader discovers the fix through guided
  questions → the slides' concept → what it solves and is for → pros/cons leading to the next point;
  hard extras folded; animated SVG where motion helps; in the user's Obsidian vault at
  `Lecture Notes/<course>/WEEK n.md`, with slide screenshots in the course `attachments/` folder,
  hand-worked examples verified by script, and fold-answer practice questions. The note language is
  chosen per note: Chinese, English, Chinese with English key points, English with Chinese terms,
  or custom. Use when the user says "/lecture-note", asks to write / rewrite / complete the notes
  for WEEK n or for a lecture PDF (in any language, e.g. Chinese requests), or names a lecture PDF of
  one of their courses. Also use to teach a section of an existing WEEK note interactively by
  exercises ("teach me WEEK n section x", "you ask, I answer", "what is this section for").
  Not for whole-course exam-prep vaults or mastery-tracked quizzing — that is /tutor-setup and /tutor.
argument-hint: "<course> <week[.part]> [pdf path] [pages A-B] [--lang zh|en|zh+en|en+zh]"
---

# Lecture Note — one week of slides → one step-by-step teaching note

## Where this fits (the three note skills are complementary)

| Skill | Unit | Output | Use for |
|---|---|---|---|
| **lecture-note** (this) | one week / one PDF | `Lecture Notes/<course>/WEEK n.md` in the vault | learning each lecture in depth, week by week |
| obsidian-markdown | syntax | — | callouts, embeds, properties, wikilinks: follow it when writing |
| tutor-setup → tutor | whole course | `StudyVault/` in the course folder (CWD) | exam prep: concept notes, MOC, quizzes with mastery tracking |

The other two are separate skills and may not be installed; this skill works without them (the
template, label table and callout list in `references/note-template.md` are enough).
Do not build a StudyVault here, and do not touch other weeks' notes except to add links.
If `tutor-setup` is installed, point the user to it at the end (run from the course folder) when
the course has several weeks of notes and an exam is coming.

## Who the reader is (read this first — it drives every writing decision)

The reader's attention for new material is **very limited**. A wall of unexplained terms at the
start of a section loses them at once, and summary-style notes (dense bullet lists, "X is …; Y is
…; Z is …") do not teach them. They learn when a **patient teacher lets them discover each idea
themselves**, one idea at a time, easy → hard. The notes are **for learning, not for exam drilling**:
the goal is to understand what each idea solves and what it is for, so that exam answers follow.

Everything below serves one method, the lesson arc. Labels such as "Deep dive", "Pause" or
"(beyond slides)" are written in the note's language: see the label table in
`references/note-template.md`.

## The lesson arc — how every knowledge point is taught (notes and live explanations alike)

Every knowledge point (each `###` lesson in a note, each topic in a live explanation) walks the same
five steps. The steps flow into each other in ordinary sentences ("so we are stuck here… let's try
to fix it ourselves… what we just built has a name on the slides…"), never as a jump from one
heading to an unrelated one.

1. **The problem.** Before anything is named: what goes wrong without this idea, and which problem
   this knowledge point exists to solve. Use plain everyday language and a concrete, picturable
   failure ("layer 2 had learned 'above 5 means cat'; after one training step every image is above
   5"). Say where every number comes from and what it means. Never open with the term, a
   definition, a formula or bare numbers.
2. **Discover it yourself.** Set up one small scenario and guide the reader, step by step, to design
   the fix on their own. Use a question chain of 3–5 small questions: Q1 is pure counting or
   observation on a tiny case with no formula; each next question changes **one** thing; the reader
   does the conceptual step (which number goes where, which way it moves) while arithmetic stays at
   small integers. By the end the reader has built the idea without knowing its name.
3. **Name it: the slides' concept.** Only now introduce the concept exactly as the slides present
   it: its name, definition and formula, with every symbol mapped onto the numbers the reader just
   produced ("this is exactly your answer to Q2: 7 = 3 + 2×2"). Include every point the slide makes
   about it.
4. **Understand it fully.** Analyse the concept and connect it to earlier knowledge points (and
   earlier weeks), then extend it: what exactly it solves, what it is used for in real networks and
   tasks (ResNet stem, a VGG block, the homework setup…), and how it changes the earlier picture.
   An everyday analogy helps here if the idea is still abstract (say where the analogy breaks).
5. **Pros and cons, and what comes next.** Weigh what it costs against what it buys. The remaining
   weakness is the bridge to the next knowledge point ("ReLU's zero slope kills units → Leaky
   ReLU"), so the next lesson's step 1 grows out of this lesson's step 5.

**Language inside the arc.** Narrative, questions and transitions use plain everyday language.
Technical language is reserved for the technical points themselves (terms, definitions, formulas,
key statements), and each such point is stated **once in the note language and once in English**,
because the English wording is often the clearer of the two. The exact mix per note is the
`lang` option (step 1.4).

**Engineering vs pure math.** For engineering topics (networks, training, systems) steps 1–2 are
always a practical scenario. For pure math (linear algebra, probability, proofs) more abstraction
is acceptable, but step 2 still starts from something computable by hand (a 2×2 matrix, one fair
die) before the general statement.

**Coverage.** The arc is how the slides are taught, not a replacement for them: every knowledge
point and every piece of content on the slides must appear (steps 3–4 carry it), in slide order
unless a prerequisite has to come first.

When the reader asks "what is this for?", answer with step 1 and step 4 (the problem it solves and
what it is used for), not with a restatement of the formula.

**Mode A: while writing a note.** Each `###` lesson follows the arc (see the lesson unit in step 5
and the template). Step 2's questions are `> [!question]-` "Question k" folds, each holding the
answer plus a one-line takeaway, and the prose between them carries the reader forward.

**Mode B: explaining an existing note interactively** (the user wants to learn or review a section,
or says "you ask, I answer"). Read the section first. No slide prep and no publishing are needed.
Talk in the user's language, whatever the note's language is. Walk the arc live:
- Step 1 in a few plain sentences, then the roadmap of step 2 ("4 small questions, one at a time").
- Ask **one question per turn** and wait for the answer.
- Right answer → confirm in one line, add the one insight it reveals, then ask the next question.
  Wrong answer → reconstruct where their number came from, say which step is wrong and why, and
  give a one-line self-check ("4×2 = 8, but only 4 pixels were added"). Do not re-teach the section.
- After the chain, do steps 3–5 in prose, then offer the next knowledge point.
- Do long arithmetic yourself (run it); never ask them to multiply decimals.
- If they drift to another topic and come back, re-post the open question verbatim.
- At the end, say what they can now do, and record progress (questions done, questions still open)
  so a later session can resume.

## Setup (nothing machine-specific lives in this file)

- `<skill>` below = this skill's base directory (shown when the skill loads; normally
  `~/.claude/skills/lecture-note`). Fill it in literally, including inside generator scripts.
- Vault: the environment variable `$OBSIDIAN_VAULT` (absolute path of the vault folder). If it is
  unset, stop and ask the user to set it. Read/write notes **only** through `cli-anything-obsidian`
  (the publish script does this); it talks to the vault open in Obsidian, and the publish script
  checks that this is the same folder as `$OBSIDIAN_VAULT`.
- Courses: the vault folders under `Lecture Notes/` (`cli-anything-obsidian --json vault list
  "Lecture Notes"`). Where each course's slides live on this machine is in `<skill>/local.md`
  (git-ignored). If that file or the course's row is missing, ask the user for the slide folder,
  then create/extend `local.md` from `local.example.md`.
- **Lecture number ≠ week number** (e.g. AI6103 "Lecture 3 ML Foundations" is WEEK 4). Never pick
  the PDF from its filename alone: check `source_pdf` in existing WEEK notes, then open the PDF's
  first pages. `source_pdf` may be a path from another machine: match on the file name only.
  If the user named both the PDF and the target note, use what they named.
  If still ambiguous, ask the user with AskUserQuestion.
- Scripts (run with `python`, or `python3` where that is the name; needs `pymupdf`): `<skill>/scripts/`
  - `prep_slides.py` — slide text, overview sheets, screenshots
  - `svg_anim.py` — build / lint / preview animated SVGs (needs Chrome or Edge for `frames`)
  - `publish_note.py` — safe write into the vault + embed check
  - `mindmap.py` — optional course mind map
- Work files go in the session scratchpad, e.g. `<scratchpad>/lecture-note/<course>-week<n>/`.

## Workflow

### 1. Resolve target and note language
1. Parse course, week, optional part (`4.1` → week 4 part 1), PDF, page range, and `--lang`.
2. `cli-anything-obsidian --json vault read "Lecture Notes/<course>/WEEK n"` (also try
   `WEEK n.P`, and `vault list` on the course folder, since titles vary: `WEEK 2 - Linear Algebra`).
3. If the note exists: save its exact `content` to `<work>/baseline.md`, and look at what it already
   has. Empty or stub notes (a few lines, often `source: joplin`) → replace fully, but keep any text
   the user wrote themselves in an Original note `> [!quote]` block. Substantial notes → ask whether
   to rewrite, extend with missing pages, or fix specific parts; never silently discard content.
4. **Note language.** Use `--lang` or a language stated in the request. When extending or fixing an
   existing note, keep its `lang` frontmatter (or the language it is visibly written in) unless the
   user asks to switch. Otherwise ask with AskUserQuestion:
   | Option | What the note looks like |
   |---|---|
   | `zh+en` (recommended default) | Plain Chinese narrative; every technical point (term, definition, formula explanation, key statement) is stated in Chinese and then in English |
   | `zh` | Chinese only; English term in parentheses on first use |
   | `en` | English throughout |
   | `en+zh` | Plain English narrative; every technical point is stated in English and then in Chinese |
   "Other" in the question lets the user describe a custom mix; record it in `lang` as `custom:
   <their description>`. Labels follow the label table in `references/note-template.md`.
5. Read 1–2 recent substantial notes of the **same course** for terminology and link targets
   (their style may predate the rules below; the rules below win).

### 2. Read the slides
```bash
python <skill>/scripts/prep_slides.py prep "<pdf>" "<work>" [--pages A-B]
```
- Read `<work>/text.txt` fully (it has `===== page N =====` markers).
- Look at **every** overview sheet in `<work>/sheets/` (Read the PNGs): text extraction misses
  diagrams, formulas drawn as images, and tables. `empty_text_pages` are image-only slides
  (scanned or pure figures): read those from the sheets or `shot` them at full size.
- Build a page → topic outline. Every page must land in some section; note pages that are pure
  title/agenda/references.

### 3. Plan the teaching path (before writing a single paragraph)
Write `<work>/plan.md`:
1. **Learning ladder** — list the lecture's concepts and order them so each one needs only
   the ones above it. Follow the lecture order, except when the slides use an idea before
   explaining it: then teach the prerequisite first (a short step) and say so.
2. For each knowledge point, plan its arc:
   - **Problem** — what goes wrong without it, as a picturable failure with numbers whose meaning
     is stated.
   - **Discovery scenario** — the small setting and its 3–5 questions (Q1 counting only; each
     next question changes one thing).
   - **Slide concept** — the slides' name, definition, formula and every point the slides make.
   - **Connections and uses** — which earlier points it builds on, what it is used for in practice;
     an everyday analogy if it stays abstract (and where the analogy breaks).
   - **Pros, cons and bridge** — the weakness that motivates the next knowledge point.
   - **Main line vs fold** — what a beginner needs goes in the main line; everything else goes in a
     Deep dive fold.
   - **Visual** — slide screenshot, static figure, animated SVG, or none (see 4b).
3. **New-term budget** — mark the lessons that introduce several new terms and split them so each
   `###` lesson introduces **at most 1–2 new terms**.

### 4. Pick and cut screenshots
Pick slides whose picture carries meaning the text can't (architectures, plots, worked tables,
geometry). Typically 8–20 per lecture; do not screenshot text-only slides.
```bash
python <skill>/scripts/prep_slides.py shot "<pdf>" "<work>/shots" 11 20 28
python <skill>/scripts/prep_slides.py shot "<pdf>" "<work>/shots" 38 --clip 0,170,940,420
```
Read each cut PNG to confirm it is legible and cropped correctly.
Attachment name: `week<N>[.<P>]-<topic-kebab>-s<NN>.png` (e.g. `week4.1-fuzzy-s02.png`,
`week5-mlp-cnn-s17.png`); NN = PDF page number, 2 digits.
Embed: `![[Lecture Notes/<course>/attachments/<name>.png]]`, always followed by 1–3 sentences
saying what to look at in the picture.

### 4b. SVG figures: animations for anything dynamic, diagrams for structure
**Rule: anything dynamic gets an SVG animation.** Anything that happens in steps, flows, or
changes over time gets an animated SVG; anything that is a structure or a pipeline gets at least a
static SVG diagram (same helpers, no tokens). Examples, not a closed list:
- **Iterative math:** optimizer steps (GD / momentum / Adam), a value updated step by step, a
  distribution shifting, a curve being traced, EMA filling up.
- **Computation flow:** a forward pass (numbers flowing layer by layer through a tiny MLP), a
  backward pass (gradients flowing back and being multiplied), a kernel sliding over an image,
  attention weights being computed and mixed.
- **Systems & workflows:** an LLM agent loop (User → LLM ⇄ Tools, Memory), a RAG pipeline, a
  training loop (batch → forward → loss → backward → update), data moving between GPUs.
- **Tokens:** text → tokens → embeddings → layers → next-token probabilities → sampled token
  appended and fed back (autoregressive loop).

Budget: typically **3–6 per lecture**; when the slides draw a workflow as boxes and arrows, redraw it as
an animated SVG rather than only screenshotting it. Not for: static facts, a formula alone, anything a
screenshot already shows well.

**Show the whole process when the reader needs to see it.** A sliding kernel should visit every
position (draw the zero-padding ring when there is padding), and a stack of layers should show each
layer being computed from the one below, not just the final receptive field. A shortcut that shows
one row or one step reads as "it only happens in the middle". If that makes the cycle longer than
12 s, that is fine; use finer keyTimes (`sc._kt = lambda t: f"{t / sc.cycle:.5f}"`) for steps
shorter than 1% of the cycle.

**How (the accuracy recipe — never hand-type coordinates):**
1. Write `<work>/anim/<slug>.py` that **computes** every position from the same numbers the note
   uses (the update rule, the toy function, the table values), then draws with the `Scene` helper.
   Captions and titles are in the note's language:
   ```python
   import sys; sys.path.insert(0, r"<skill>/scripts")
   from svg_anim import Scene
   sc = Scene(640, 360, cycle=8, title="Gradient descent: learning rate 0.2")
   ax = sc.axes(x=(-3.5, 3.5), y=(0, 10), box=(60, 45, 600, 300), xlabel="w", ylabel="L(w)=w²")
   sc.curve(ax, lambda w: w * w)
   ws = [3.0]
   for _ in range(3): ws.append(ws[-1] - 0.2 * 2 * ws[-1])   # same rule as in the note
   pts, ts = [(w, w * w) for w in ws], [1, 3, 5, 7]
   sc.mover(ax, pts, ts); sc.trail(ax, pts, ts)
   sc.captions([(0, "start w=3"), (3, "step 1: w = 3 − 0.2×6 = 1.8"), (5, "step 2 …"), (7, "step 3 …")])
   sc.save("<work>/anim/gd-steps.svg")
   ```
   Helpers: `axes`, `curve`, `mover` (dot moving through points at given times), `trail` (arrows
   appearing), `captions` (step-by-step caption line), `text`/`line`/`rect`/`dot` with
   `show=(t0, t1)` to make things appear/disappear, and `raw()` for anything else (still SMIL,
   still on the shared timeline). Put shared numbers in `verify.py` or import them, so the
   animation and the text can never disagree.

   **Diagram helpers** (workflows, pipelines, networks):
   ```python
   llm = sc.box(260, 190, 220, 90, "LLM", color="blue", sub="reasoning & planning")   # returns a Box
   tools = sc.box(600, 190, 150, 90, "Tools", color="green", sub="search · code execution")
   act = sc.arrow(llm.at(1, 0.3), tools.at(0, 0.3), color="orange", bend=-28, label="Action")
   sc.token(act, 3.0, 4.0, label="search", color="orange")   # a pill travels along the arrow 3s→4s
   sc.pulse(tools, [4.0])                                      # the box lights up: "working now"
   ```
   `Box` gives anchor points `.left/.right/.top/.bottom/.center` and `.at(fx, fy)`; `arrow` returns
   its path so `token` can follow it (`both=True` for ↔, `bend` to curve, `dash` for optional
   paths). Box labels shrink automatically to fit. For a static diagram, draw boxes and arrows
   only. For a numeric flow (forward pass), put the actual numbers in the tokens / box labels with
   `show=(t0, t1)`, computed by the same code as `verify.py`.
2. Lint and look:
   ```bash
   python <skill>/scripts/svg_anim.py lint "<work>/anim/gd-steps.svg"
   python <skill>/scripts/svg_anim.py frames "<work>/anim/gd-steps.svg" "<work>/anim/frames" --times 0.5,3.5,5.5,7.5
   ```
   **Read the `-strip.png`** and check each frame against the note: the dot is where the numbers
   say, captions match, nothing overlaps or is cut off, text is readable. Fix and repeat.
   Pick `--times` just after each key moment, not mid-glide.
3. Rules the lint enforces (Obsidian shows `![[x.svg]]` as an `<img>`: no scripts, no clicks,
   no external files, the theme cannot restyle it):
   - SMIL `<animate>` only (no CSS `@keyframes`, no JS, no `begin="click"` / chained `.end`);
     every animation uses `dur = cycle`, `repeatCount="indefinite"`, scheduled with `keyTimes`,
     so the whole picture loops in sync.
   - `viewBox` + width ≤ 900, opaque background rect (readable in dark theme), CJK font stack.
   - Cycle 6–12 s unless the whole process must be shown (see above); hold the final state ≥ 1.5 s
     before the loop restarts.
4. Design: one idea per animation; ≤ 4 colours with fixed meaning (the helper palette: blue =
   main object, orange = moving/updated thing, green = target/optimum, red = error/overshoot);
   caption line says in words what the current step is, numbered ①②③ to match the prose;
   show the numbers being computed. Workflows: at most ~6 boxes, left→right or top→bottom main
   flow, loops drawn as curved arrows, one token moving at a time.
5. Name: `week<N>[.<P>]-<topic-kebab>-anim-<slug>.svg`. **Never overwrite an embedded SVG under the
   same name**: Obsidian caches images by name and keeps showing the old one. Give a changed
   animation a new name and update the embed. Embed exactly like an image, then **always** write
   what to watch and a static fallback (the key numbers in a small table or list), so the note
   still teaches if the animation does not play:
   ```markdown
   ![[Lecture Notes/<course>/attachments/week7-optimization-anim-gd-steps.svg]]
   **What to watch:** where the orange dot lands at each step, and how the steps get shorter. (If the animation does not play, the table below has the same numbers.)
   ```

### 5. Write the note → `<work>/note.md`
Follow `references/note-template.md` for frontmatter, skeleton and labels, and the
`obsidian-markdown` skill for syntax. Write in the chosen note language (step 1.4).

#### The lesson unit (every `###` knowledge point follows the arc)
1. **The problem** — what goes wrong without it; plain words; numbers explained before use.
2. **Discover it yourself** — the scenario and its Question k folds; short prose between them.
3. **The concept from the slides** — name (note language + English), definition, formula with
   every symbol mapped to the numbers from step 2; then **In one sentence**.
4. **Understand it fully** — connections to earlier points, what it solves, what it is used for;
   optional Analogy callout; slide screenshots / animations with their "what to watch" lines.
5. **Pros and cons → next** — the trade-off, ending in the question the next lesson answers.
6. (optional) Deep dive fold — derivations, proofs, edge cases, extra variants.
7. (optional) `> [!warning]` Common pitfall — only real, common confusions.

A very small point (one slide bullet that refines the previous lesson) may shrink to steps 1, 3
and 5 in a few sentences, but it still starts from the problem, never from the term.

#### Writing rules
- **Explain, do not summarise.** Write connected explanatory prose — "first…, then…, so…" — as a
  teacher speaking. Bullet lists are for enumerating steps or options *after* they have been
  explained, never as the way to introduce new ideas. No paragraphs that list 3+ new terms.
- **Easy to hard.** Inside the note, inside each part, and inside each lesson: intuition → numbers →
  formula → subtleties. The first sentence of each lesson must be understandable by someone who
  has read only the lessons above it.
- **One new concept at a time.** Each `###` lesson introduces 1–2 new terms at most. When a lesson
  must mention a later concept, give a one-line plain explanation and point forward ("Softmax
  (section 3 explains it): exponentiate each number, then divide by the total"). Never use a term
  before it is explained.
- **Small steps + pause.** After each part (and after any lesson that was hard), add a short
  `> [!question]-` Pause fold with one question and the answer inside, so the reader checks one
  idea before the next arrives.
- **Analogy or tiny example, never neither, for abstract ideas.** If a sentence contains an
  abstract word (gradient, curvature, variance, regularisation, momentum, eigenvalue…) and neither
  an analogy nor numbers are nearby, add one.
- **Show a property by contrast.** One instance can't show which part is the property. Pair it
  with something that lacks it and a concrete test that tells them apart (e.g. ReLU vs Softmax:
  change one input, see which outputs move).
- **Keep it simple with folds.** Main line: what's needed to understand the slides. Put in a Deep
  dive fold: full algebra of a derivation (keep the one-line result in the main line), proofs, "it
  can be shown" gaps, rare edge cases, historical notes, alternative variants. Content beyond the
  slides is marked (beyond slides) (in the fold title if it's in a fold).
- **Fill slide jumps** — where a slide skips steps, fill them in (in a fold if long).
- Language per step 1.4 and "Language inside the arc": plain words for the story, technical
  language only for technical points, each stated in the note language and in English.
- Follow the lecture's order and cover every page (plan.md ticks it off).
- Math in `$...$` / `$$...$$`. Tables for step-by-step numbers and comparisons.
  No invented slide content, no fake citations.

### 6. Verify every number
Write `<work>/verify.py` that recomputes **every** worked example, question-chain answer,
dimension, parameter count, practice answer **and animation key position/caption number** with
exact arithmetic (`fractions.Fraction`, integers; floats only where inherent), using `assert`. Run
it; fix the note until it passes. Mention in the reply that the calculations were checked by script.

### 6b. Ground every claim (default, always)
The slides are the ground truth (treat them as ~99.9% right). What can be wrong is what the note
adds beyond them. So, while writing:
1. **Slide content:** state it as the slides do; when you paraphrase or fill in a skipped step,
   re-read the slide page to confirm you did not change its meaning.
2. **Anything beyond the slides** — every (beyond slides) block, every Deep dive fold that is not on
   a slide, paper attributions ("proposed by…", "original paper uses…"), and non-obvious "X because
   Y" explanations of your own — must be checked online *before* it goes in: WebSearch/WebFetch the
   original paper, official docs, or a standard textbook (d2l.ai, Goodfellow et al., Bishop, the
   lecture notes the slides credit). No blogs, forums or AI-generated pages as evidence.
3. Put the source inside the fold: `> Source: Kingma & Ba 2015, Alg. 1 — https://arxiv.org/abs/1412.6980`.
4. If you cannot confirm it, drop it or mark it `(to verify: …)`; never state it as fact from memory.

### 6c. Independent review loop (optional — only when the user asks)
Run this only when the user asks for a strict review ("strict check", "review it", "evaluator",
"check it again" — in any language), or offers it for a high-stakes note (e.g. right before an
exam). It is expensive: a fresh subagent re-reads the note, the slides and many web sources,
typically hundreds of thousands of tokens per round. When it runs, it is an **evaluator-optimizer
loop** with `references/evaluator.md`:

1. **Evaluate:** launch a *fresh* evaluator subagent with the Agent tool (`subagent_type:
   "general-purpose"`), passing the prompt from `references/evaluator.md` with the paths filled in.
   To save tokens, tell it to check slide content only for faithful transcription and to spend web
   lookups on the beyond-slides claims; rounds 2+ re-check only the changed sections.
   It reads only the artifacts (note, slide text/images, verify.py, refs). It checks every claim
   against the slides → course reference PDFs → primary papers / standard textbooks (with URLs),
   and checks the teaching rules. It writes `<work>/eval/round-<k>.json`.
2. **Optimize:** for every blocker/major finding, fix the note or rebut it with evidence in
   `<work>/eval/response-<k>.md`. Rerun `verify.py` (and animation frames if numbers changed).
3. **Repeat** with a new evaluator (never reuse the previous one's context) until the verdict is
   `pass`, max 3 rounds. Anything still open is marked in the note as `(to verify: …)` and reported
   to the user; it is never published silently as fact.
Keep the round files; the reply states how many rounds ran and what was fixed. When the loop is
not run, the reply offers it in one line.

### 7. Publish
```bash
python <skill>/scripts/publish_note.py "<work>/note.md" \
  "Lecture Notes/<course>/WEEK n.md" \
  --image "<work>/shots/s11.png=week4-ml-foundations-s11.png" \
  --image "<work>/anim/gd-steps.svg=week4-ml-foundations-anim-gd-steps.svg" ... \
  --new            # or: --baseline "<work>/baseline.md"
```
`--image` accepts any attachment (png or svg). It refuses to overwrite a note edited in Obsidian
since the baseline was saved, or a different attachment with the same name, then reads the note
back and checks every embed resolves. If it fails, fix the cause; never bypass by writing files
directly.

### 8. Reply
Short summary in the user's language: note path, note language, pages covered, sections, number of
screenshots, animations, question chains and practice questions, "calculations checked by script",
how many beyond-slides claims were checked online, any `(to verify)` items, and — only if 6c ran —
rounds run and findings fixed; otherwise offer 6c in one line. Mention `/tutor-setup` → `/tutor`
for quizzing (only if installed) when relevant.

**Then ask (AskUserQuestion) whether to generate / update the course mind map** (step 9). Never
build it without a yes — it is a supplement, not the core note.

### 9. Course mind map (optional — only when the user says yes)
One mind map per course, `Lecture Notes/<course>/<COURSE> Mind Map.md` (the Chinese name from the
label table for `zh` / `zh+en` courses; keep the name the course already uses), covering all weeks
written so far. It is a ```` ```markmap ```` block, rendered inline by the Obsidian plugin
**Mindmap NextGen** (tell the user to install it once if the map shows as plain code). Layout is
automatic, so there is no manual positioning; do **not** build Canvas maps (tried: cramped,
overlapping, duplicated content).

1. Keep the outline in `<work>/../<course>-mindmap/outline.md` (read the current map note first and
   extend it; never drop earlier weeks). Structure: `#` course · weeks → `##` themes (by topic, not by
   week) → `###` knowledge points → `-` details.
2. **Each knowledge point is explained, not summarised** — as child items, in this order when they
   apply (item labels from the label table):
   - `What:` one or two full sentences a beginner understands
   - `Why needed:` the problem it solves / what fails without it
   - the formula, with what the symbols are
   - `Example:` a tiny worked example with real numbers (taken from the notes' verified examples)
   - `Pitfall:` the common pitfall
   - `↔ Wk …:` how it connects to another week (this is where cross-week links live)
   Put `@<week>|<exact heading>@` after a point or item to link it to that note section.
3. Every number in the map goes into a small `verify_map.py` with `assert`s (reuse the notes'
   `verify.py` results); run it.
4. Build and check links, then publish:
   ```bash
   python <skill>/scripts/mindmap.py outline.md map.md --lang <zh|en> \
     --course-dir "$OBSIDIAN_VAULT/Lecture Notes/<course>"     # exits on any broken heading link
   python <skill>/scripts/publish_note.py map.md \
     "Lecture Notes/<course>/<map note name>.md" --baseline <saved current map>   # or --new
   ```
   `--lang zh` for `zh` / `zh+en` courses, `--lang en` otherwise. `mindmap.py` keeps a height the
   user set by resizing the map in Obsidian.
5. Add the mind map frontmatter key (label table: `mindmap` / its Chinese form) pointing to
   `"[[<map note name>]]"` to the new week note (and to earlier weeks that lack it), via
   `publish_note.py --baseline`.

## Checklist before publishing
- [ ] Frontmatter complete, including `lang`; `source_pdf` is the real file; `pages` / `pdf_page_count` correct
- [ ] The note is in the chosen language and uses that language's labels throughout
- [ ] Every PDF page in range is covered (plan.md outline ticks off)
- [ ] Easy → hard: every lesson's first sentence is readable using only earlier lessons
- [ ] Every abstract concept has an analogy and/or tiny calculation next to it
- [ ] Every lesson walks the arc: problem → self-discovery questions → slide concept → analysis,
      connections and uses → pros/cons that lead into the next lesson; transitions read smoothly
- [ ] No section opens with a term, definition, formula or bare numbers
- [ ] Technical points are stated in the note language and in English (per `lang`)
- [ ] Every knowledge point and piece of content on the slides appears somewhere
- [ ] No summary-style lesson (a bullet list introducing several new terms); ≤ 2 new terms per `###`
- [ ] Hard extras are in Deep dive folds; skipping all folds still leaves a complete explanation
- [ ] A Pause check after each part
- [ ] Every screenshot / animation embed has a "what to look at" line and the file exists;
      every animation passed `svg_anim.py lint`, its frame strip was looked at, and it has a
      static fallback (table/list of the same numbers)
- [ ] Every numeric claim, answer and animation number checked by `verify.py`
- [ ] Every beyond-slides claim ((beyond slides) marks, non-slide Deep dive folds, paper
      attributions) was checked online and cites its source, or is marked `(to verify)`
- [ ] (only if the user asked for 6c) evaluator loop ended with `pass` or ≤ 3 rounds
- [ ] ≥ 10 practice questions that check understanding, not exam tricks (≥ 60% "what does it
      solve / why", ≥ 20% calculation, ≥ 2 connecting two ideas), answers in Show answer folds
- [ ] Glossary table and the Self-check-after-studying tip at the end
- [ ] Links to previous/next week notes if they exist (`[[WEEK 4]]`)
- [ ] LaTeX renders: every multi-row `bmatrix`/`cases` separates rows with `\\` (a lone `\`
      before a digit, `-` or a variable renders red in Obsidian). Write any fixing script with
      the Write tool, not a bash heredoc (heredocs here eat backslashes), and in `re.sub` pass
      a function as the replacement (`lambda _: '\\\\'`), since a replacement string escape-
      processes `\\` down to a single `\`.
- [ ] Links into other notes' headings (`[[WEEK 4#...]]`) still resolve — rewriting a note
      renames its headings and silently breaks other weeks' links to it
