# Note template

Copy this skeleton. Replace `<…>`; drop optional lines marked `(optional)` when not applicable.
The skeleton uses the **English labels**; for `zh` / `zh+en` notes, swap in the Chinese label for
each one from the [label table](#labels-per-note-language) below. SKILL.md refers to the labels by
their English names (e.g. "the Deep dive fold").

````markdown
---
course: <vault folder name, e.g. AI6103-DeepLearning>
week: <n>
part: <p>                      # (optional) only for WEEK n.p notes
topic: <topic in the note language, with English keywords>
lang: <zh | en | zh+en | en+zh | custom>
lecturer: <name>               # (optional) if on the title slide
source_pdf: "<absolute path with forward slashes>"
pages: "<A-B>"
pdf_page_count: <total pages of the PDF>
created: <YYYY-MM-DD>          # keep the original date when rewriting
updated: <YYYY-MM-DD>
tags:
  - <COURSE CODE, e.g. AI6103>
  - <kebab-case-topic>
  - <kebab-case-topic>
---

# WEEK <n>[ · Part <p>] · <title>

> [!info] Course & scope
> **<course>** · `<pdf file name>` · **PDF p. A–B**
> A step-by-step teaching note: easy → hard, one new idea at a time. Every lesson follows
> **the problem → work it out yourself → the concept from the slides → what it solves and is for → pros and cons → next**.
> The folded Deep dive blocks can be skipped; the main line still makes sense without them.
> Previous: [[WEEK <n-1>]] · Next: [[WEEK <n+1>]]   ← only link notes that exist

| Reading route (easy → hard) | Slides | After it you can answer |
| --- | --- | --- |
| [[#Part 1 · <…>]] | p.A–p.X | <one real question> |
| … | … | … |

## Before we start: what problem this lecture solves

<One running scenario with 2–3 numbers: where we are stuck and what this lecture gives us.
Tell it as a story, not a list.>

## Part 1 · <topic>

### 1.1 <concept> (<English term>) (p. A–B)

**Why we need it**
<Plain words: what goes wrong without this idea, as a concrete failure. Say where every number
comes from and what it means. No term, definition or formula yet.>

**Work it out yourself**
<Move the topic's running scenario into this lesson's new situation, let the reader apply what
they already learned, show it fail inside the story, then guide them to the fix:>

> [!question]- Question 1: <count / observe something on a tiny case>
> <answer> — <one-line takeaway>

<one or two sentences carrying the reader to the next question>

> [!question]- Question 2: <change one thing>
> <answer> — <one-line takeaway>

**The concept from the slides**
<The slides' name for what the reader just built, in the note language and in English; the slides'
definition and every point they make.>
$$<formula>$$
<which number from the questions each symbol stands for.>

**In professional terms:** <one or two sentences the way a practitioner would say it, with the proper
terms (e.g. "use ReLU as the activation"), in the note language and in English.>

**What it solves and what it is for**
<Connect to earlier knowledge points / weeks; what exactly it fixes; where it is used in practice.>

> [!example] Analogy
> <optional everyday picture if the idea is still abstract.> Where the analogy breaks: <one sentence>.

**Table k · <title>**
| Step | … | … |
| --- | --- | --- |

![[Lecture Notes/<course>/attachments/week<n>[.<p>]-<topic>-s<NN>.png]]
*Figure k · p. N · <short title>: <what to look at in this picture and what it shows>*

![[Lecture Notes/<course>/attachments/week<n>[.<p>]-<topic>-anim-<slug>.svg]]
*Figure k · own diagram · <short title>: <which element to follow and what its change means>* (If the animation does not play, Table k has the same numbers.)

> [!note]- Deep dive: <full derivation / proof / edge cases of slide content> (optional)
> <material the main line does not need. Anything from outside the slides goes in a Supplement fold instead.>

> [!note]- Supplement: <topic> [n]
> <content beyond the slides, checked online (step 6b)>
> Sources: [n]

> [!warning] Common pitfall
> <only real, common misunderstandings + the correct view>

**Pros and cons**
<What it buys vs what it costs. End with the weakness that the next lesson fixes, phrased as the
next lesson's problem.>

### 1.2 <next concept> … (same arc; its "Why we need it" grows out of 1.1's pros and cons)

> [!question]- Pause: <one question checking this part's core idea>
> <answer + one or two sentences of explanation>

… (continue part by part in slide order) …

## Part N · Review and practice

### One-page summary
| Concept | In one sentence | Key formula |
| --- | --- | --- |

### Practice questions

#### Q1 · <title>
<question>

> [!success]- Show answer
> <answer + reasoning>

… (≥ 10 questions) …

### Glossary
| Term | English | Meaning in one sentence |
| --- | --- | --- |

> [!tip] Self-check after studying
> **Can compute:** …
> **Can explain:** …
> **Can connect:** …

## References
[1] Author, A., & Author, B. (Year). Title. *Venue*, vol(issue), pages. https://doi.org/…
````

## Labels per note language

`en` and `en+zh` use the English column; `zh` and `zh+en` use the Chinese column. A `custom`
language follows whichever column is closer, or asks the user.

| Label (English) | Chinese |
| --- | --- |
| Course & scope | 课程与范围 |
| Reading route (easy → hard) · Slides · After it you can answer | 阅读路线（从易到难） · 课件页 · 学完能回答 |
| Before we start: what problem this lecture solves | 开始之前：这一讲要解决什么问题 |
| Part 1 · … / Part N · Review and practice | 第一部分 · … / 第 N 部分 · 复习与练习 |
| Why we need it | 为什么需要它 |
| Work it out yourself | 自己动手推一推 |
| Question k: … | 第 k 题：… |
| The concept from the slides | 课件里的概念 |
| In professional terms | 专业说法 |
| What it solves and what it is for | 它解决了什么、能用来干嘛 |
| Analogy | 打个比方 |
| Pros and cons | 优点与代价 |
| What to watch | 看动画时注意 |
| Deep dive: … (optional) | 深入：…（可跳过） |
| Supplement: … | 补充：… |
| (supplement [n]) | （补充 [n]） |
| (derived here) | （本笔记推导） |
| (to verify: …) | （待核对：…） |
| Sources: | 来源： |
| References | 参考文献 |
| Figure k | 图 k |
| own diagram | 自绘 |
| Table k | 表 k |
| Eq. (k) | 式 (k) |
| Cause and effect | 前因后果 |
| Common pitfall | 易错点 |
| Pause: … | 停一下：… |
| One-page summary | 本讲一页总结 |
| Practice questions · Show answer | 练习题 · 展开答案 |
| Glossary | 术语中英对照 |
| Self-check after studying · Can compute / explain / connect | 学完后的检查标准 · 会算 / 会解释 / 会串联 |
| Original note | 原笔记 |
| Mind map note `<COURSE> Mind Map` · frontmatter key `mindmap` | `<COURSE> 知识导图` · frontmatter key `知识导图` |
| Mind map items: What · Why needed · Example · Pitfall | 是什么 · 为什么需要 · 例 · 注意 |

Glossary columns: in `zh` / `zh+en` it is *Chinese · English · one-line meaning*; in `en` it is
*Term · one-line meaning* (drop the English column); in `en+zh` it is *English · Chinese · meaning*.

## House style (one format per element, like a paper's style guide)

Every note uses exactly these formats. Nothing is improvised: if an element is not listed here, add
it here first. `scripts/lint_note.py` checks the mechanical parts before publishing (step 7).
Examples are given in Chinese; `en` notes use the English labels from the table above.

### Where content comes from: three kinds, three looks
| Kind | Format | Example |
| --- | --- | --- |
| **On the slides** | Plain text; cite the page as `（p.N）` / `(p. N)`, ranges `p.51–52` | 用当前 batch 的统计量代替整个数据集的统计量（p.51）。 |
| **Beyond the slides, one sentence** | Sentence + `（补充 [n]）`; `[n]` points to References | GroupNorm 在 batch = 2 时错误率比 BN 低约 10 个百分点（补充 [2]）。 |
| **Beyond the slides, a paragraph or more** | A fold titled `补充：<topic> [n]`, whose last line is `来源：[n]` (or `[n], [m]`) | see below |
| **Derived here from slide content** (algebra, a worked example, no outside claim) | `（本笔记推导）` after the sentence, or inside a `深入：` fold; covered by `verify.py` | 两个式子相减即得 ρ = 2/‖w‖（本笔记推导）。 |
| **Could not be confirmed** | `（待核对：<what is unsure>）` | |

```markdown
> [!note]- 补充：为什么小 batch 下 GroupNorm 更稳 [2]
> <explanation>
> 来源：[2]
```

A `深入：…（可跳过）` fold holds **deeper treatment of slide content** (a full derivation, edge
cases). If a fold contains anything from outside the slides, it is a `补充：` fold instead. Never
mix the two, and never write a bare `（补充）` without a citation.

### Citations and the reference list
- In text: numbered markers `[n]`, numbered in order of first appearance. The same source keeps
  its number throughout the note.
- The last section of the note is `## 参考文献` / `## References`, one entry per number, in an
  APA-like form:
  `[n] Author, A., & Author, B. (Year). Title. *Venue*, vol(issue), pages. https://doi.org/…`
  Use the DOI when one exists, otherwise a stable URL (arXiv, official docs, textbook page).
- The course slides are not listed; they are cited by page `（p.N）`.
- Every `[n]` in the text has an entry, and every entry is cited at least once.

### Figures, tables, equations
- **Figure:** every embed is followed on the next line by an italic caption
  `*图 k · p.N · <short title>：<what to look at>*` (own diagrams: `*图 k · 自绘 · …*`). Number
  figures in order through the note, and refer to them as 「见图 k」.
- **Table:** a table that carries data or a comparison has a bold caption on the line above,
  `**表 k · <title>**`. Layout tables (reading route, glossary) have none.
- **Equation:** a display equation that is referred to later ends with `\tag{k}` and is cited as
  式 (k). Other equations have no number.

### Text conventions
- Headings: `### 14.3 <中文标题>（<English>）（p.53）`; a lesson's page range goes in its heading only.
- A new term's first definition: **中文（English）** in bold, then the one-line `*EN: …*` statement.
- Bilingual statements: the Chinese sentence, then `*EN: …*` on the next line (`zh+en`).
- Symbols: one letter, one meaning for the whole note (symbol table in `plan.md`), and the slide's
  own notation when it has one.
- Numbers: `×` for multiplication and `−` for minus in prose; en dash for ranges (`3–7`); math in
  `$…$`.

### Callouts (fixed titles)
| Use | Callout |
| --- | --- |
| Scope box | `> [!info] 课程与范围` |
| Question chain | `> [!question]- 第 k 题：…` |
| End-of-part check | `> [!question]- 停一下：…` |
| Practice answer | `> [!success]- 展开答案` under `#### Qk · <title>` |
| Analogy | `> [!example] 打个比方` |
| Common pitfall | `> [!warning] 易错点` |
| Exam-critical | `> [!important] <title>` |
| Chain recap | `> [!tip] 前因后果` |
| Deeper slide content | `> [!note]- 深入：…（可跳过）` |
| Beyond the slides | `> [!note]- 补充：… [n]` |
| Closing checklist | `> [!tip] 学完后的检查标准` |
| Kept user text | `> [!quote] 原笔记` |
