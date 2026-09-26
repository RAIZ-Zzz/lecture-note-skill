---
name: lecture-note
description: >
  Turn one week's lecture slides (PDF) into a Chinese step-by-step teaching note (讲解式、从易到难、
  类比 + 小算例, hard extras folded, animated SVG where motion helps) in the user's Obsidian vault at
  `Lecture Notes/<course>/WEEK n.md`, with slide screenshots in the course `attachments/` folder,
  hand-worked examples verified by script, and fold-answer practice questions. Use when the
  user says "/lecture-note", "整理 WEEK n 笔记", "把这周课件做成笔记", "写/重写/补全 WEEK n", or asks for
  notes on a specific lecture PDF of AI6103 / AI6104 / AI6124 / AI6127 / AI6130. Not for whole-course
  exam-prep vaults or quizzing — that is /tutor-setup and /tutor.
argument-hint: "<course> <week[.part]> [pdf path] [pages A-B]"
---

# Lecture Note — 一周课件 → 一篇讲解式教学笔记

## Where this fits (the three note skills are complementary)

| Skill | Unit | Output | Use for |
|---|---|---|---|
| **lecture-note** (this) | one week / one PDF | `Lecture Notes/<course>/WEEK n.md` in the vault | learning each lecture in depth, week by week |
| obsidian-markdown | syntax | — | callouts, embeds, properties, wikilinks: follow it when writing |
| tutor-setup → tutor | whole course | `StudyVault/` in the course folder (CWD) | exam prep: concept notes, MOC, quizzes with mastery tracking |

Do not build a StudyVault here, and do not touch other weeks' notes except to add links.
At the end, point the user to `/tutor-setup` (run from the course folder) when the course has
several weeks of notes and an exam is coming.

## Who the reader is (read this first — it drives every writing decision)

The user's attention for new material is **very limited**. They cannot absorb a pile of new terms
at once, and summary-style notes (dense bullet lists, "X 是 …；Y 是 …；Z 是 …") do not teach them.
They learn from a **patient teacher talking them through one idea at a time**, easy → hard, with an
everyday analogy or a tiny calculation whenever something is abstract. They asked for five things:

1. **能看懂、学会** — the note must teach the lecture without the slides, **from easy to hard**.
2. **类比很重要** — every abstract concept gets an everyday analogy *or* a tiny hand calculation
   (usually both: analogy for the feeling, numbers for the substance).
3. **尽量从简** — the main line explains only what is needed to understand the lecture. Harder
   extras (full derivations, proofs, edge cases, "why exactly 0.9", history) are **not dropped but
   folded**: `> [!note]- 深入：<标题>（可跳过）`. A reader who skips every fold still understands the lecture.
4. **讲解式、教学式，不是总结式** — prose that explains, in small steps, like a lesson.
5. **会动的图** — where a process unfolds over steps or time, add an animated SVG made by code
   (section 4b). Motion must show something the text would otherwise need many words for.

## Fixed facts

- Vault: `$OBSIDIAN_VAULT` = `D:\obsidian\repo\NTULEARN`. Read/write notes **only** through
  `cli-anything-obsidian` (the publish script does this).
- Courses (vault folder ← slide folder):

  | Vault folder | Slides |
  |---|---|
  | `AI6103-DeepLearning` | `D:\Study\AI6103-DeepLearning\*.pdf` |
  | `AI6104-MATH FOR AI` | `D:\Study\AI6104-Math\PPT\` |
  | `AI6124-FUZZY` | `D:\Study\AI124-Fuzzy\PPT\` and `...\MSAI 2026 dropbox link\` |
  | `AI6127-NLP` | `D:\Study\AI127-NLP\` |
  | `AI6130-LLM` | `D:\Study\AI6130-LLM\` |

- **Lecture number ≠ week number** (e.g. AI6103 "Lecture 3 ML Foundations" is WEEK 4). Never pick
  the PDF from its filename alone: check `source_pdf` in existing WEEK notes, then open the PDF's
  first pages. If the user named both the PDF and the target note, use what they named.
  If still ambiguous, ask the user with AskUserQuestion.
- Scripts (run with `python`, pymupdf is installed): `~/.claude/skills/lecture-note/scripts/`
  - `prep_slides.py` — slide text, overview sheets, screenshots
  - `svg_anim.py` — build / lint / preview animated SVGs (needs Chrome or Edge for `frames`)
  - `publish_note.py` — safe write into the vault + embed check
- Work files go in the session scratchpad, e.g. `<scratchpad>/lecture-note/<course>-week<n>/`.

## Workflow

### 1. Resolve target
1. Parse course, week, optional part (`4.1` → week 4 part 1), PDF, page range.
2. `cli-anything-obsidian --json vault read "Lecture Notes/<course>/WEEK n"` (also try
   `WEEK n.P`, and `vault list` on the course folder, since titles vary: `WEEK 2 - Linear Algebra`).
3. If the note exists: save its exact `content` to `<work>/baseline.md`, and look at what it already
   has. Empty or stub notes (a few lines, often `source: joplin`) → replace fully, but keep any text
   the user wrote themselves as a `> [!quote] 原笔记` block. Substantial notes → ask whether to
   rewrite, extend with missing pages, or fix specific parts; never silently discard content.
4. Read 1–2 recent substantial notes of the **same course** for terminology and link targets
   (their style may predate the rules below; the rules below win).

### 2. Read the slides
```bash
python ~/.claude/skills/lecture-note/scripts/prep_slides.py prep "<pdf>" "<work>" [--pages A-B]
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
2. For each concept, decide:
   - **Analogy** — one everyday picture (下山、找零钱、平均成绩、开车刹车…). Also note where the
     analogy stops working, so the note can say it in one line.
   - **Tiny example** — the 2–3 numbers you will compute by hand.
   - **Main line vs fold** — what a beginner needs to follow the lecture goes in the main line;
     everything else goes in a `深入` fold (see rule 3).
   - **Visual** — slide screenshot, static figure, animated SVG, or none (see 4b).
3. **New-term budget** — mark the lessons that introduce several new terms and split them so each
   `###` lesson introduces **at most 1–2 new terms**.

### 4. Pick and cut screenshots
Pick slides whose picture carries meaning the text can't (architectures, plots, worked tables,
geometry). Typically 8–20 per lecture; do not screenshot text-only slides.
```bash
python ~/.claude/skills/lecture-note/scripts/prep_slides.py shot "<pdf>" "<work>/shots" 11 20 28
python ~/.claude/skills/lecture-note/scripts/prep_slides.py shot "<pdf>" "<work>/shots" 38 --clip 0,170,940,420
```
Read each cut PNG to confirm it is legible and cropped correctly.
Attachment name: `week<N>[.<P>]-<topic-kebab>-s<NN>.png` (e.g. `week4.1-fuzzy-s02.png`,
`week5-mlp-cnn-s17.png`); NN = PDF page number, 2 digits.
Embed: `![[Lecture Notes/<course>/attachments/<name>.png]]`, always followed by 1–3 sentences
saying what to look at in the picture.

### 4b. Animated SVGs (会动的图)
**When:** the idea is a *process* — iterations of an optimizer, a kernel sliding over an image, a
value being updated step by step, a distribution shifting, a curve being traced, a forward/backward
pass flowing through a network. Typically **2–5 per lecture**; zero is fine if nothing moves.
Not for: static facts, formulas, anything a screenshot already shows.

**How (the accuracy recipe — never hand-type coordinates):**
1. Write `<work>/anim/<slug>.py` that **computes** every position from the same numbers the note
   uses (the update rule, the toy function, the table values), then draws with the `Scene` helper:
   ```python
   import sys; sys.path.insert(0, r"C:/Users/32454/.claude/skills/lecture-note/scripts")
   from svg_anim import Scene
   sc = Scene(640, 360, cycle=8, title="梯度下降：学习率 0.2")
   ax = sc.axes(x=(-3.5, 3.5), y=(0, 10), box=(60, 45, 600, 300), xlabel="w", ylabel="L(w)=w²")
   sc.curve(ax, lambda w: w * w)
   ws = [3.0]
   for _ in range(3): ws.append(ws[-1] - 0.2 * 2 * ws[-1])   # same rule as in the note
   pts, ts = [(w, w * w) for w in ws], [1, 3, 5, 7]
   sc.mover(ax, pts, ts); sc.trail(ax, pts, ts)
   sc.captions([(0, "起点 w=3"), (3, "第 1 步：w = 3 − 0.2×6 = 1.8"), (5, "第 2 步 …"), (7, "第 3 步 …")])
   sc.save("<work>/anim/gd-steps.svg")
   ```
   Helpers: `axes`, `curve`, `mover` (dot moving through points at given times), `trail` (arrows
   appearing), `captions` (step-by-step caption line), `text`/`line`/`rect`/`dot` with
   `show=(t0, t1)` to make things appear/disappear, and `raw()` for anything else (still SMIL,
   still on the shared timeline). Put shared numbers in `verify.py` or import them, so the
   animation and the text can never disagree.
2. Lint and look:
   ```bash
   python ~/.claude/skills/lecture-note/scripts/svg_anim.py lint "<work>/anim/gd-steps.svg"
   python ~/.claude/skills/lecture-note/scripts/svg_anim.py frames "<work>/anim/gd-steps.svg" "<work>/anim/frames" --times 0.5,3.5,5.5,7.5
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
   - Cycle 6–12 s; hold the final state ≥ 1.5 s before the loop restarts.
4. Design: one idea per animation; ≤ 4 colours with fixed meaning (the helper palette: blue =
   main object, orange = moving/updated thing, green = target/optimum, red = error/overshoot);
   caption line says in words what the current step is; show the numbers being computed.
5. Name: `week<N>[.<P>]-<topic-kebab>-anim-<slug>.svg`. Embed exactly like an image, then
   **always** write what to watch and a static fallback (the key numbers in a small table or
   list), so the note still teaches if the animation does not play:
   ```markdown
   ![[Lecture Notes/<course>/attachments/week7-optimization-anim-gd-steps.svg]]
   **看动画时注意：** 每一步橙点落在哪里、步长怎样越来越小。（动画不动时看下表，数值相同。）
   ```

### 5. Write the note → `<work>/note.md`
Follow `references/note-template.md` for frontmatter and skeleton, and the `obsidian-markdown`
skill for syntax.

#### The lesson unit (every `###` concept follows this rhythm)
1. **一个问题 / 失败场景** — start from something concrete the reader can picture
   ("学习率太大时会发生什么？看这 3 个数…"). 1–3 sentences.
2. **类比** — `> [!example] 打个比方` with the everyday picture; one line on where it breaks.
3. **小算例** — 2–3 numbers, every intermediate value shown, in a small table if there are steps.
4. **再写成公式** — only now the formula; map every symbol back to the numbers just used.
5. **一句话记住** — one sentence the reader could say out loud.
6. (optional) `> [!note]- 深入：…（可跳过）` — derivations, proofs, edge cases, extra variants.
7. (optional) `> [!warning] 易错点` — only real, common confusions.

Sometimes a lesson needs just 1+3+5; keep it short when the idea is simple (rule 3).

#### Writing rules
- **讲解，不要总结.** Write connected explanatory prose — "先…，然后…，所以…" — as a teacher
  speaking. Bullet lists are for enumerating steps or options *after* they have been explained,
  never as the way to introduce new ideas. No paragraphs that list 3+ new terms.
- **从易到难.** Inside the note, inside each part, and inside each lesson: intuition → numbers →
  formula → subtleties. The first sentence of each lesson must be understandable by someone who
  has read only the lessons above it.
- **一次一个新概念.** Each `###` lesson introduces 1–2 new terms at most. When a lesson must mention
  a later concept, give a one-line plain explanation and point forward
  ("Softmax（第 3 节细讲）：把每个数取指数再除以总和"). Never use a term before it is explained.
- **小步 + 停一下.** After each part (and after any lesson that was hard), add a short
  `> [!question]- 停一下：<一个问题>` with the answer inside, so the reader checks one idea before
  the next arrives.
- **类比或小算例, 缺一不可 for abstract ideas.** If a sentence contains an abstract word (梯度、
  曲率、方差、正则、动量、特征值…) and neither an analogy nor numbers are nearby, add one.
- **Show a property by contrast.** One instance can't show which part is the property. Pair it
  with something that lacks it and a concrete test that tells them apart (e.g. ReLU vs Softmax:
  change one input, see which outputs move).
- **从简 with folds.** Main line: what's needed to understand the slides. Put in a `深入` fold:
  full algebra of a derivation (keep the one-line result in the main line), proofs, "it can be
  shown" gaps, rare edge cases, historical notes, alternative variants. Content beyond the slides
  is marked `（补充）` (in the fold title if it's in a fold).
- **Fill slide jumps** — where a slide skips steps, fill them in (in a fold if long).
- Chinese prose, English term in parentheses on first use: 感受野（receptive field）.
- Follow the lecture's order and cover every page (plan.md ticks it off).
- Math in `$...$` / `$$...$$`. Tables for step-by-step numbers and comparisons.
  No invented slide content, no fake citations.

### 6. Verify every number
Write `<work>/verify.py` that recomputes **every** worked example, dimension, parameter count,
practice answer **and animation key position/caption number** with exact arithmetic
(`fractions.Fraction`, integers; floats only where inherent), using `assert`. Run it; fix the note
until it passes. Mention in the reply that the calculations were checked by script.

### 7. Publish
```bash
python ~/.claude/skills/lecture-note/scripts/publish_note.py "<work>/note.md" \
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
Short summary: note path, pages covered, sections, number of screenshots, animations and practice
questions, "计算已用脚本核对". Mention `/tutor-setup` → `/tutor` for quizzing when relevant.

## Checklist before publishing
- [ ] Frontmatter complete; `source_pdf` is the real file; `pages` / `pdf_page_count` correct
- [ ] Every PDF page in range is covered (plan.md outline ticks off)
- [ ] Easy → hard: every lesson's first sentence is readable using only earlier lessons
- [ ] Every abstract concept has an analogy and/or tiny calculation next to it
- [ ] No summary-style lesson (a bullet list introducing several new terms); ≤ 2 new terms per `###`
- [ ] Hard extras are in `> [!note]- 深入：…（可跳过）` folds; skipping all folds still leaves a
      complete explanation
- [ ] A `> [!question]- 停一下` check after each part
- [ ] Every screenshot / animation embed has a "what to look at" line and the file exists;
      every animation passed `svg_anim.py lint`, its frame strip was looked at, and it has a
      static fallback (table/list of the same numbers)
- [ ] Every numeric claim, answer and animation number checked by `verify.py`
- [ ] ≥ 10 practice questions (≥ 60% concept recall, ≥ 20% calculation, ≥ 2 “why” analysis),
      answers folded in `> [!success]- 展开答案`
- [ ] 术语中英对照 table and `> [!tip] 学完后的检查标准` at the end
- [ ] Links to previous/next week notes if they exist (`[[WEEK 4]]`)
- [ ] LaTeX renders: every multi-row `bmatrix`/`cases` separates rows with `\\` (a lone `\`
      before a digit, `-` or a variable renders red in Obsidian). Write any fixing script with
      the Write tool, not a bash heredoc (heredocs here eat backslashes), and in `re.sub` pass
      a function as the replacement (`lambda _: '\\\\'`), since a replacement string escape-
      processes `\\` down to a single `\`.
- [ ] Links into other notes' headings (`[[WEEK 4#...]]`) still resolve — rewriting a note
      renames its headings and silently breaks other weeks' links to it
