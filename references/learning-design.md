# Learning design: why the notes teach the way they do

This file explains the teaching approach behind the lesson arc in `SKILL.md` and the research each
rule rests on. `SKILL.md` says *what* to do; this file says *why*, so the rules are not changed by
accident. It grew out of live study sessions with the skill's user. The dated notes below record
what went wrong and what fixed it.

## The approach in one paragraph

A topic is taught through **one running scenario** that stays the same from the first lesson to the
last. An example is a cat classifier whose layer 1 outputs 2, 4, 6, 8 on four training images and
whose layer 2 has learned "above 5 means cat". Each new lesson moves that scenario into a new
situation: layer 1 is updated, the GPU fits only 2 images, the model is deployed and receives one
photo. The reader first **applies what they already learned**, watches it **fail inside the
story**, and is then **guided, one small question at a time**, to the fix. Only after that does the
slides' name and formula appear, mapped onto the reader's own answers. The chain ends with
result → consequence → conclusion, and the topic's last lesson calls back to its first.

## Principles and the evidence behind them

### 1. One running scenario per topic (anchored instruction)
- **Rule:** reuse one story across all lessons of a topic. Never bring in free-floating toy data,
  and never give an existing number a new role without saying so.
- **Why:** the Cognition and Technology Group at Vanderbilt (CTGV, led by John Bransford) built
  whole curricula around one "anchor" story, the *Jasper Woodbury* series. All later sub-problems
  live inside that story. Their target was **inert knowledge**, knowledge that can be recited but is
  not used when a real situation calls for it.
- **Session note (2026-09-30):** the same numbers {2, 4, 6, 8} meant "one batch" in one lesson and
  "the whole dataset" in the next, and the switch was never stated. The learner was lost. A
  separate "purpose / mapping" box bolted onto each example was then judged too rigid. What worked
  was letting the story carry the purpose.

### 2. Apply old knowledge → see it fail → introduce the new idea (productive failure)
- **Rule:** in step 2 of the arc, the reader tries what they already know on the new situation
  before the new concept is named.
- **Why:** Kapur's *Productive Failure* has two phases. In the first, students attempt problems with
  their prior knowledge and usually fail. In the second, the teacher consolidates the canonical
  concept on top of those attempts. A meta-analysis of 166 comparisons found better conceptual
  understanding and transfer than instruction-first, with no loss in procedural skill (Sinha &
  Kapur, 2021; Hedges' g = 0.36). The effect was larger when the productive-failure principles were
  followed closely, and it reversed for young children (grades 2–5). Adult university learners, the
  audience of this skill, are in the favourable range. This fits Piaget's account of learning through **cognitive conflict**: an existing
  scheme fails, and the learner restructures it. It also fits Bjork's **desirable difficulties**.

### 3. Build on what the learner already knows; chain lessons (meaningful learning)
- **Rule:** every lesson's problem grows out of the previous lesson's weakness (step 5 → step 1).
  Link back to earlier weeks, and remind the reader of every term where it is used.
- **Why:** Ausubel held that the most important single factor in learning is what the learner
  already knows. New ideas stick when they are anchored to existing ones rather than memorised in
  isolation, which is the "banking" (rote-filling) model that Freire criticised.

### 4. Guided, not minimal-guidance discovery
- **Rule:** discovery is always scaffolded. Use a 3–5 question chain, Q1 is pure observation, each
  question changes one thing, and small integers keep the arithmetic easy. The slides' concept is
  always stated explicitly at the end.
- **Why:** Kirschner, Sweller & Clark (2006) showed that minimally guided discovery overloads
  novices' working memory and underperforms. Productive failure itself depends on a designed
  problem and a teacher-led consolidation phase.

### 5. In live tutoring, never hand over the answer first
- **Rule (Mode B):** ask one question per turn and wait. On a wrong answer, diagnose where the
  learner's number came from rather than re-teaching. The learner does the conceptual step and the
  tutor does the tedious arithmetic.
- **Why:** in a randomised trial with about 1,000 high-school students, unrestricted GPT-4 help
  raised practice scores but lowered unassisted exam scores by 17%. A tutor limited to hints removed
  the harm (Bastani et al., 2025). An AI tutor built on active-learning principles more than doubled
  learning gains, in less time than an active-learning class (Kestin et al., 2025). One-to-one
  tutoring has long been known to beat class teaching (Bloom, 1984, "2 sigma"; see VanLehn, 2011,
  for more modest effect sizes). An AI tutor makes one-to-one cheap, but only if it tutors.

### 6. Expect discomfort; don't mistake fluency for learning
- **Rule:** keep the struggle, and don't collapse a question chain into a finished explanation just
  because the learner hesitates. Do stop adding new content when the learner is lost on basic terms,
  and ground those terms first.
- **Why:** students in active-learning classes learned more but *felt* they learned less than
  students in polished lectures (Deslauriers et al., 2019). Across 225 STEM studies, lecturing had
  1.5× the failure rate of active learning (Freeman et al., 2014).

### 7. Every number checked, every beyond-slides claim sourced
- **Rule:** use `verify.py` for all numbers (step 6), online grounding for anything beyond the
  slides (step 6b), and report errors honestly.
- **Why:** AI tutors make mistakes. In these sessions a count was wrong (12 vs 9 surface forms), and
  a tutorial's cosine answer silently used unnormalised vectors. A learner who trusts wrong numbers
  learns the wrong thing.

### 8. Plain words as a bridge, professional terms as the destination
- **Rule:** tell the story in plain language and land every point on the professional term, stated
  in the note language and in English ("In professional terms").
- **Why:** this is the learner's stated preference. They find the English wording clearer and need
  to talk to practitioners. It is a user requirement, not a research claim.

## References

- Ausubel, D. P. (1968). *Educational Psychology: A Cognitive View*. Holt, Rinehart & Winston.
- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI
  without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26),
  e2422633122. https://doi.org/10.1073/pnas.2422633122
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J.
  Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.
- Bloom, B. S. (1984). The 2 sigma problem: The search for methods of group instruction as effective
  as one-to-one tutoring. *Educational Researcher*, 13(6), 4–16.
- Cognition and Technology Group at Vanderbilt (1990). Anchored instruction and its relationship to
  situated cognition. *Educational Researcher*, 19(6), 2–10.
- Cognition and Technology Group at Vanderbilt (1992). The Jasper series as an example of anchored
  instruction: Theory, program description, and assessment data. *Educational Psychologist*,
  27(3), 291–315. https://doi.org/10.1207/s15326985ep2703_3
- Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). Measuring actual
  learning versus feeling of learning in response to being actively engaged in the classroom.
  *PNAS*, 116(39), 19251–19257. https://doi.org/10.1073/pnas.1821936116
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P.
  (2014). Active learning increases student performance in science, engineering, and mathematics.
  *PNAS*, 111(23), 8410–8415. https://doi.org/10.1073/pnas.1319030111
- Freire, P. (1970). *Pedagogy of the Oppressed*. Herder and Herder.
- Kapur, M. (2008). Productive failure. *Cognition and Instruction*, 26(3), 379–424.
- Kapur, M., & Bielaczyc, K. (2012). Designing for productive failure. *Journal of the Learning
  Sciences*, 21(1), 45–83.
- Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms
  in-class active learning: An RCT introducing a novel research-based design in an authentic
  educational setting. *Scientific Reports*, 15, 17458. https://doi.org/10.1038/s41598-025-97652-6
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does
  not work. *Educational Psychologist*, 41(2), 75–86.
- Piaget, J. (1985). *The Equilibration of Cognitive Structures*. University of Chicago Press.
- Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction works: Evidence for
  productive failure. *Review of Educational Research*, 91(5), 761–798.
  https://doi.org/10.3102/00346543211019105
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems,
  and other tutoring systems. *Educational Psychologist*, 46(4), 197–221.
