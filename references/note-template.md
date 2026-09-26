# Note template

Copy this skeleton. Replace `<…>`; drop optional lines marked `(可选)` when not applicable.

````markdown
---
course: <vault folder name, e.g. AI6103-DeepLearning>
week: <n>
part: <p>                      # (可选) only for WEEK n.p notes
topic: <中文主题，含英文关键词>
lecturer: <name>               # (可选) if on the title slide
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

# WEEK <n>[ · Part <p>] · <中文标题>

> [!info] 课程与范围
> **<course>** · `<pdf file name>` · **PDF 第 A–B 页**
> 讲解式教学笔记：从易到难，一次只讲一个新概念。每节的节奏是 **问题 → 打个比方 → 小算例 → 公式 → 一句话记住**。
> 折叠的「深入」块可以先跳过，跳过也能看懂主线。
> 上一讲：[[WEEK <n-1>]] · 下一讲：[[WEEK <n+1>]]   ← only link notes that exist

| 阅读路线（从易到难） | 课件页 | 学完能回答 |
| --- | --- | --- |
| [[#第一部分 · <…>]] | p.A–p.X | <一个问题> |
| … | … | … |

## 开始之前：这一讲要解决什么问题

<用一个贯穿全讲的小场景（2–3 个数）讲清楚：我们卡在哪里、这一讲给了什么办法。讲故事，不列清单。>

## 第一部分 · <主题>

### 1.1 <概念>（<English term>）

<一个问题 / 失败场景：1–3 句，给出具体数字。>

> [!example] 打个比方
> <日常类比。> 这个比方不完全对的地方：<一句话>。

**小算例：** <2–3 个数，逐步计算，每个中间值都写出来；有多步时用表格。>

| 步 | … | … |
| --- | --- | --- |

**写成公式：** 
$$<公式>$$
<每个符号对应刚才哪个数。>

**一句话记住：** <一句能说出口的话。>

![[Lecture Notes/<course>/attachments/week<n>[.<p>]-<topic>-s<NN>.png]]
<这张图要看哪里、说明了什么。>

![[Lecture Notes/<course>/attachments/week<n>[.<p>]-<topic>-anim-<slug>.svg]]
**看动画时注意：** <盯住哪个元素、它的变化说明了什么>。（动画不动时看上面的表，数值相同。）

> [!note]- 深入：<完整推导 / 证明 / 边界情况>（可跳过）
> <主线不需要、但想弄透时再看的内容。超出课件的标（补充）。>

> [!warning] 易错点
> <只写真实常见的误解 + 正确理解>

### 1.2 <下一个概念> …（同样节奏；每个 ### 最多引入 1–2 个新术语）

> [!question]- 停一下：<检查本部分核心概念的一个小问题>
> <答案 + 一两句解释>

…（按课件顺序继续各部分）…

## 第 N 部分 · 复习与练习

### 本讲一页总结
| 概念 | 一句话 | 关键公式 |
| --- | --- | --- |

### 练习题

#### 题 1 · <标题>
<题目>

> [!success]- 展开答案
> <答案 + 推理过程>

…（≥ 10 题）…

### 术语中英对照
| 中文 | English | 一句话解释 |
| --- | --- | --- |

> [!tip] 学完后的检查标准
> **会算：** …
> **会解释：** …
> **会串联：** …
````

## Callouts used in this vault
- `> [!info]` scope · `> [!warning] 易错点` pitfalls · `> [!important]` exam-critical
- `> [!example] 打个比方` analogy · `> [!note]- 深入：…（可跳过）` folded hard extras (mark （补充） if beyond slides)
- `> [!question]- 停一下：…` end-of-part check (answer inside the fold)
- `> [!success]- 展开答案` folded answers · `> [!quote] 原笔记` user text preserved from an old stub
- `> [!tip] 学完后的检查标准` closing checklist
