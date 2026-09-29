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
> **<course>** · `<pdf file name>` · **PDF pp. A–B**
> A step-by-step teaching note: easy → hard, one new idea at a time. Every lesson follows
> **problem → analogy → worked example (or question chain) → formula → one-sentence takeaway**.
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

### 1.1 <concept> (<English term>)

<A real problem / failure case: 1–3 sentences with concrete numbers, ending in a number or a decision.>

> [!example] Analogy
> <everyday picture.> Where the analogy breaks: <one sentence>.

**Worked example:** <2–3 numbers, step by step, every intermediate value shown; a table if there are several steps.>

| Step | … | … |
| --- | --- | --- |

<For a key mechanism, use a question chain instead of the worked example:>

> [!question]- Question 1: <count / observe something on a tiny case>
> <answer> — <one-line takeaway>

> [!question]- Question 2: <change one thing>
> <answer> — <one-line takeaway>

**As a formula:**
$$<formula>$$
<which number from the example / questions each symbol stands for.>

**In one sentence:** <one sentence the reader could say out loud.>

![[Lecture Notes/<course>/attachments/week<n>[.<p>]-<topic>-s<NN>.png]]
<what to look at in this picture and what it shows.>

![[Lecture Notes/<course>/attachments/week<n>[.<p>]-<topic>-anim-<slug>.svg]]
**What to watch:** <which element to follow and what its change means>. (If the animation does not play, the table above has the same numbers.)

> [!note]- Deep dive: <full derivation / proof / edge cases> (optional)
> <material the main line does not need. Mark anything beyond the slides as (beyond slides).>

> [!warning] Common pitfall
> <only real, common misunderstandings + the correct view>

### 1.2 <next concept> … (same rhythm; each ### introduces at most 1–2 new terms)

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
| Analogy | 打个比方 |
| Worked example | 小算例 |
| Question k: … | 第 k 题：… |
| As a formula | 写成公式 |
| In one sentence | 一句话记住 |
| What to watch | 看动画时注意 |
| Deep dive: … (optional) | 深入：…（可跳过） |
| (beyond slides) | （补充） |
| (to verify: …) | （待核对：…） |
| Source: | 来源： |
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

## Callouts used in this vault
- `> [!info]` scope · `> [!warning]` Common pitfall · `> [!important]` exam-critical
- `> [!example]` Analogy · `> [!note]- Deep dive: … (optional)` folded hard extras (mark (beyond slides) where it applies)
- `> [!question]-` Question k (question chains) and Pause (end-of-part check), answer inside the fold
- `> [!success]-` Show answer, for folded practice answers · `> [!quote]` Original note, for user text kept from an old stub
- `> [!tip]` Self-check after studying, the closing checklist
