---
course: Example for skill
topic: Special relativity from the source — Einstein, On the Electrodynamics of Moving Bodies (1905)
lang: en
lecturer: A. Einstein (paper); Fourmilab edition of the 1923 Perrett & Jeffery translation
source_pdf: "https://www.fourmilab.ch/etexts/einstein/specrel/specrel.pdf"
pages: "1-24"
pdf_page_count: 24
created: 2026-09-30
updated: 2026-09-30
tags:
  - example
  - physics
  - special-relativity
  - lorentz-transformation
  - electrodynamics
---

# Special Relativity 1905 · On the Electrodynamics of Moving Bodies

> [!info] Course & scope
> **Example for skill** · `specrel.pdf` · **PDF p. 1–24** (Einstein, 30 June 1905; English translation of 1923, Fourmilab edition)
> A step-by-step teaching note: easy → hard, one new idea at a time. Every lesson follows
> **the problem → work it out yourself → the concept from the paper → what it solves and is for → pros and cons → next**.
> The folded Deep dive blocks can be skipped; the main line still makes sense without them. Every number in this note was checked by a script.

| Reading route (easy → hard) | Pages | After it you can answer |
| --- | --- | --- |
| [[#Part 1 · Kinematics: clocks, rods and light\|Part 1 · Kinematics]] | p. 1–12 | Why can two observers disagree about "at the same time"? |
| [[#Part 2 · Electrodynamics: what moving observers measure\|Part 2 · Electrodynamics]] | p. 12–24 | What does a moving observer measure for fields, light and a fast electron? |
| [[#Part 3 · Review and practice\|Part 3 · Review and practice]] | — | Summary, exercises, glossary |

## Before we start: what problem this lecture solves

Imagine you are a student in Bern in the summer of 1905. You know Newton's mechanics, the Maxwell–Hertz equations of electricity and magnetism, and the widely held idea that light is a wave in a "luminiferous ether" that fills space. You also know railways: the telegraph keeps station clocks in step, and a passenger in a smooth train cannot tell by any mechanical experiment whether the train is moving.

This paper starts from a small crack in that picture and ends with a new idea of time. We will follow it with one running story, **the Bern express**:

- Station A (Bern) and station B lie on a straight line **300 km** apart. Light travels 300,000 km per second, which is **300 km per millisecond**, so a light signal from A to B takes **1 ms**. We measure lengths in km and times in ms throughout.
- An imagined express runs along the line at **v = 0.6c = 180 km per ms**. It is a thought experiment in the paper's own style: no real train is that fast, but the numbers make every effect large enough to see. The train is **300 km long** when measured at rest.
- In Part 2 the express carries a **laboratory car** with a magnet, a coil, a mirror and a cathode-ray tube, and a signal lamp stands on the platform.

The paper numbers its sections §1–§10; this note teaches them as 16 lessons: §1 → lesson 2, §2 → lessons 3–4, §3 → lessons 5–6, §4 → lessons 7–8, §5 → lesson 9, §6 → lessons 10–11, §7 → lesson 12, §8 → lesson 13, §9 → lesson 14, §10 → lessons 15–16 (the introduction is lesson 1). A "§" always means the paper's section.

At v = 0.6c one number appears again and again, the paper's factor $\beta = 1/\sqrt{1 - v^2/c^2}$:
$1 - 0.6^2 = 0.64$, $\sqrt{0.64} = 0.8$, so $\beta = 1/0.8 = 1.25$.

![[Lecture Notes/Example for skill/attachments/specrel-1905-s01.png]]
*Figure 0.1 · p. 1 · The first page of the paper: the title, the date 30 June 1905, and the opening sentence about "asymmetries which do not appear to be inherent in the phenomena" — the crack we start from in lesson 1.*

## Part 1 · Kinematics: clocks, rods and light

Part 1 (the paper's "Kinematical Part", §1–§5) never mentions electricity. It asks only what we mean by time, length and velocity when things move. Lesson 1 shows why that question is forced on us; lessons 2–9 answer it.

### 1. The puzzle: a magnet, a coil, and no absolute rest (p. 1–2)

**Why we need it**

In the laboratory car there is a coil of wire; on the platform next to the track lies a strong magnet. As the train passes, a current flows in the coil. Now swap them: put the magnet on the train and the coil on the platform, with the same relative speed. The same current flows. The experiment cares only about the **relative** motion. Yet the theory of 1905 tells two completely different stories for the two cases, as if it knew which body is "really" moving.

**Work it out yourself**

> [!question]- Question 1: In case (a) the coil moves past a resting magnet; in case (b) the magnet moves past a resting coil, with the same relative speed. Does the measured current differ?
> No. The paper says the currents have "the same path and intensity" in both cases (p. 1). Only the relative motion is observable.

> [!question]- Question 2: The usual theory explains case (b) by an electric field that appears around the moving magnet, carrying energy. What does it say in case (a), where the magnet rests?
> No electric field arises around the magnet. Instead the moving conductor feels an "electromotive force", with no corresponding energy in the field, which happens to push exactly the same current (p. 1).
> — Two different mechanisms for one observable result.

> [!question]- Question 3: If nature really had a state of "absolute rest" (rest relative to the ether), what should experiments on the moving Earth detect?
> A difference depending on the Earth's motion through the ether, for example a change in light's speed along and against that motion. The paper notes that all such attempts to discover the Earth's motion "relatively to the 'light medium'" were unsuccessful (p. 1).

> [!question]- Question 4: Put questions 1 and 3 together. What is the simplest guess about the laws of physics?
> That there is no absolute rest: the laws of electrodynamics and optics are the same in every frame of reference in which Newton's mechanics holds, not only to a first approximation but exactly.

> [!tip] Cause and effect
> Magnet–coil experiments depend only on relative motion, and no experiment detects motion through the ether → the theory's distinction between "moving" and "resting" has nothing to do with observation → guess that the same laws hold in every uniformly moving frame.

**The concept from the paper**

Einstein raises this guess to a postulate, the **principle of relativity**: the same laws of electrodynamics and optics are valid for all frames of reference for which the equations of mechanics hold good (p. 1). He adds a second postulate that "is only apparently irreconcilable with the former": **light is always propagated in empty space with a definite velocity $c$, independent of the state of motion of the emitting body** (p. 1). These two postulates are enough for "a simple and consistent theory of the electrodynamics of moving bodies"; the luminiferous ether becomes superfluous, and no "absolutely stationary space" is needed (p. 1–2).

The paper then says where the trouble lies: every theory of electrodynamics rests on the **kinematics of the rigid body** — on rods, clocks and how they relate to electromagnetic processes — and "insufficient consideration of this circumstance lies at the root of the difficulties" (p. 2). So Part 1 rebuilds kinematics first.

Footnote 1 on p. 1 adds that the preceding memoir by Lorentz (H. A. Lorentz, whose electrodynamics of moving bodies lesson 14 returns to) was not known to the author at the time.

**In professional terms:** Special relativity rests on two postulates: the laws of physics are the same in all inertial frames, and the speed of light in vacuum is the same for all inertial observers, independent of the source's motion.

**What it solves and what it is for**

The two postulates remove the need to say which body "really" moves. The magnet–coil asymmetry will disappear completely in lesson 11, once we know how electric and magnetic forces look from a moving frame.

> [!info]- Supplement: the best-known "unsuccessful attempt"
> The most famous of the experiments the paper alludes to is Michelson and Morley's interferometer experiment on the relative motion of the Earth and the luminiferous ether. They compared the travel time of light along two perpendicular arms and found no effect of the Earth's motion of the size the ether theory predicted. The paper itself does not name any experiment.
> Sources: [Michelson & Morley, 1887]

**Pros and cons**

The postulates are simple and explain the magnet–coil result without two mechanisms. The cost is a direct clash with everyday kinematics: if the train moves at 0.6c and a lamp on the train shines forward, Galileo's rule says the platform sees the light at $c + 0.6c = 1.6c$, while the second postulate says $c$. One of our everyday ideas must be wrong. Einstein finds it in the most innocent word of all: "time". Lesson 2 starts there.

### 2. What "at the same time" means: synchronising two clocks (p. 2–3)

**Why we need it**

"The train arrives at 7 o'clock" means: the small hand of my watch points to 7 and the train arrives, and these two events are **simultaneous** (p. 2). That works when the watch and the train are at the same place. But the stationmaster at Bern wants to know the time of an event at station B, 300 km away. His watch is not there. What does "the time at B" even mean?

**Work it out yourself**

A light signal leaves A when A's clock reads $t_A = 0$ ms, is reflected at B, and arrives back at A when A's clock reads $t'_A = 2$ ms.

> [!question]- Question 1: How long was the whole round trip, measured on A's clock?
> $2 - 0 = 2$ ms.

> [!question]- Question 2: Nothing distinguishes the trip A→B from the trip B→A. If we agree that the two trips take the same time, what should B's clock read at the moment of reflection?
> Halfway: 1 ms. Each trip then takes 1 ms.

> [!question]- Question 3: Suppose B's clock read 1.3 ms at the reflection. How long would the outward and the return trips be, according to the two clocks? How should B's clock be corrected?
> Outward: $1.3 - 0 = 1.3$ ms; back: $2 - 1.3 = 0.7$ ms. They differ, so the clocks are not synchronous; B must set its clock back by 0.3 ms.

> [!question]- Question 4: A third station C lies 600 km from A on the same line. A sends a signal at 0 ms and gets it back at 4 ms. What must C's clock read at the reflection?
> Halfway again: 2 ms.
> — The same rule works for any number of clocks.

> [!tip] Cause and effect
> A distant time cannot be read off a local watch → define it: the light trip out and the trip back take equal times → with this rule every station clock on the line can be set, and "simultaneous at A and B" gets a meaning.

![[Lecture Notes/Example for skill/attachments/specrel-1905-anim-sync.svg]]
*Figure 2.1 · own diagram · Synchronising A and B: follow the orange light pill out to B and back; B's clock must show exactly halfway between sending (0 ms) and return (2 ms).* (If the animation does not play, questions 1–3 contain the same numbers.)

**The concept from the paper**

Einstein first takes a "stationary system", a system of co-ordinates in which Newton's mechanics holds (to a first approximation, footnote 2). A point at rest in it is located with rigid measuring rods and Euclidean geometry (p. 2). Using the position of one watch's hands as "time" is fine for events next to the watch, but fails for events far away; letting one observer at the origin time every event by the light it sends him also fails, because the result depends on where that observer stands (p. 2).

The paper's solution (p. 3): a clock at A gives an "A time", a clock at B a "B time", but a common "time" for A and B is only defined once we **establish by definition** that light needs as long from A to B as from B to A. A ray leaves A at A-time $t_A$, is reflected at B at B-time $t_B$, and returns to A at A-time $t'_A$. The two clocks **synchronize** if

$$t_B - t_A = t'_A - t_B \tag{2.1}$$

With our numbers: $1 - 0 = 2 - 1$. The definition is assumed free of contradictions and to satisfy two rules: (1) if B synchronizes with A, then A synchronizes with B; (2) if A synchronizes with both B and C, then B and C synchronize with each other. The "time" of an event is the reading, simultaneous with the event, of a stationary clock at the event's place that is synchronous with a specified stationary clock. In agreement with experience,

$$\frac{2\,AB}{t'_A - t_A} = c \tag{2.2}$$

is a universal constant, the velocity of light in empty space: $2 \times 300 / 2 = 300$ km per ms. Time defined this way belongs to the stationary system: it is "the time of the stationary system" (p. 3). Footnote 3 sets aside the small inexactitude of simultaneity for two events at *approximately* the same place.

**In professional terms:** Distant clocks are synchronised by the Einstein synchronisation convention: equal one-way light travel times, so that $t_B = (t_A + t'_A)/2$.

**What it solves and what it is for**

"Simultaneous" is no longer an intuition but an operation you can perform with clocks and light. This is how every later lesson measures anything: a length (lesson 4), a moving clock's rate (lesson 8), a velocity (lesson 9). It is also the reason the definition must name a system: the stationary one.

> [!warning] Common pitfall
> The rule does not measure the one-way speed of light and find it equal both ways; it **defines** equal one-way times. That is exactly why, in lesson 4, observers who move can end up with a different definition.

**Pros and cons**

We now have one time for all clocks of the station system. But the rule used "the time light needs", and light's speed enters only as a stationary-system fact. What happens when the train's passengers apply the same rule with clocks that move? Before we can answer, the paper states its two principles precisely.

### 3. Two principles (p. 3–4)

**Why we need it**

Lesson 1 stated the postulates in words. To compute anything with the moving train, we need them in a form that tells us exactly what is the same for the station and for the train, and exactly what light does.

**Work it out yourself**

> [!question]- Question 1: A passenger in the smoothly running express drops a ball. Does it fall differently from a ball dropped on the platform?
> No. In a uniformly moving train every mechanical experiment gives the same result as at rest. That was known since Galileo.

> [!question]- Question 2: The principle of relativity extends this to all laws. Does it say the passenger sees the same *numbers* as the stationmaster for the same event?
> No. It says the same *laws* (the same equations) hold in both systems. The numbers describing one event can differ: that is what the rest of Part 1 computes.

> [!question]- Question 3: A lamp on the platform and a lamp on the train, both flashing forward. With what speed does each light ray move in the station system?
> Both at $c$ = 300 km per ms. The second principle: the velocity of light in the stationary system does not depend on whether the source is at rest or moving.

> [!tip] Cause and effect
> Mechanics already looks the same in uniformly moving systems → the first principle extends that to all physical laws → the second principle fixes the speed of every light ray in the stationary system at $c$, whatever emits it.

**The concept from the paper**

The reflections of the paper's §2 (lessons 3–4) rest on two principles, defined as follows (p. 3–4):

1. **Principle of relativity:** the laws by which the states of physical systems change are not affected, whether these changes are referred to the one or the other of two systems of co-ordinates in uniform translatory motion.
2. **Principle of the constancy of the velocity of light:** any ray of light moves in the "stationary" system with the determined velocity $c$, whether emitted by a stationary or a moving body. Hence

$$\text{velocity} = \frac{\text{light path}}{\text{time interval}} \tag{3.1}$$

where the time interval is taken in the sense of the definition of lesson 2.

**In professional terms:** Postulate 1: physical laws take the same form in all inertial frames. Postulate 2: light moves at $c$ in an inertial frame, independent of the source's velocity.

**What it solves and what it is for**

The principles turn the vague "no absolute rest" of lesson 1 into two checkable statements. The first is a symmetry (station and train are equivalent); the second is a rule for computing where light is at any station time. Lesson 4 uses the second one directly, and lesson 5 uses both to find how station and train co-ordinates are related.

**Pros and cons**

Stated this way, the principles look harmless. Their cost appears as soon as we measure a moving rod with them: the next lesson shows that the train's passengers and the stationmaster cannot agree on which clocks are synchronous.

### 4. Simultaneity is relative (p. 4–5)

**Why we need it**

The stationmaster wants the length of the moving express. He cannot hold a measuring rod against a train rushing by at 180 km per ms. The passengers can measure it easily at rest. Are the two lengths the same? Everyday kinematics assumes they are. To test that, the paper first asks what happens to **clock synchronisation** on the moving train.

**Work it out yourself**

Clocks sit at the rear and the front of the express. They are set to agree with the station clocks wherever they pass, so they are "synchronous in the stationary system". Measured from the platform the train is 240 km long (lesson 7 will explain this number; for now take it as given). A light signal leaves the rear, is reflected at the front and returns to the rear. All times below are station times.

> [!question]- Question 1: Light moves at 300 km per ms; the front runs away from it at 180 km per ms. By how many km per ms does the light gain on the front? How long does it need to catch a front 240 km ahead?
> It gains $300 - 180 = 120$ km per ms, so it needs $240 / 120 = 2$ ms.

> [!question]- Question 2: On the way back the rear runs **towards** the light. At what rate does the gap close, and how long does the return trip take?
> $300 + 180 = 480$ km per ms, so $240 / 480 = 0.5$ ms.

> [!question]- Question 3: Passengers now apply the rule of lesson 2 to their rear and front clocks (which show station time). Are those clocks synchronous by that rule?
> No. The rule needs equal out and back times, but the clocks show 2 ms out and 0.5 ms back. The passengers conclude that their clocks are **not** synchronous, while the stationmaster calls them synchronous.

> [!question]- Question 4: Two flashes happen at the rear and the front at the same station time. Would the passengers call them simultaneous?
> No. The passengers' synchronisation differs from the station's (question 3), so events that are simultaneous for the station are not simultaneous for the train.

> [!tip] Cause and effect
> Light's speed is $c$ in the station system → on a moving train the out and back trips take $2$ ms and $0.5$ ms → the train's own synchronisation rule disagrees with the station's → simultaneity depends on the system.

![[Lecture Notes/Example for skill/attachments/specrel-1905-anim-simul.svg]]
*Figure 4.1 · own diagram · The express as seen from the platform: watch the orange light chase the running front for 2 ms, then meet the approaching rear after only 0.5 ms more.* (If the animation does not play, questions 1 and 2 have the same numbers.)

**The concept from the paper**

The paper imagines a stationary rigid rod of length $\ell$ (the paper writes $l$), then sets it moving along the $x$-axis with velocity $v$, and describes two ways to measure its length (p. 4):

- **(a)** An observer moves with the rod and a measuring rod and measures directly, as if all were at rest. By the principle of relativity this "length of the rod in the moving system" must equal $\ell$.
- **(b)** Using stationary clocks synchronised as in lesson 2, the observer finds at which points of the stationary system the two ends are at a definite time, and measures the distance between those points. This is "the length of the (moving) rod in the stationary system". Einstein announces it **differs** from $\ell$. Current kinematics tacitly assumes (a) and (b) give the same length.

Clocks at the ends A and B of the rod (here A and B are the rod's two ends, in our story the rear and the front of the express, not the two stations) are synchronous in the stationary system (footnote 4: "time" here means the time of the stationary system and also the reading of the moving clock at that place). A ray leaves A at time $t_A$, is reflected at B at $t_B$ and returns at $t'_A$. By the constancy of light's velocity (p. 5):

$$t_B - t_A = \frac{r_{AB}}{c - v}, \qquad t'_A - t_B = \frac{r_{AB}}{c + v} \tag{4.1}$$

where $r_{AB}$ is the length of the moving rod measured in the stationary system: questions 1 and 2 with $r_{AB} = 240$ km give 2 ms and 0.5 ms. Observers moving with the rod find the clocks not synchronous; observers in the stationary system call them synchronous. So **we cannot attach any absolute signification to the concept of simultaneity**: two events simultaneous in one system are not simultaneous when viewed from a system moving relative to it (p. 5).

**In professional terms:** Simultaneity is frame-dependent (relativity of simultaneity): events simultaneous in one inertial frame are generally not simultaneous in another moving relative to it.

**What it solves and what it is for**

This is the hidden assumption behind Galileo's velocity rule: that "now" is the same everywhere for everyone. Once it falls, the clash of lesson 1 ($1.6c$ versus $c$) is no longer a contradiction: velocities are measured with clocks, and the two systems' clocks disagree. Lesson 5 now works out exactly how they disagree.

> [!quote] Analogy
> Two towns that set their clocks by the noon sun disagree on "12 o'clock" because the sun reaches them at different moments; neither is wrong, each follows its own rule. Where the analogy breaks: sun time differs by a fixed offset between two resting towns, while relativistic disagreement depends on the speed of relative motion and on distance.

**Pros and cons**

We gained a consistent notion of time for each system, at the price of losing a universal "now". The station and the train each have their own co-ordinates and their own time. What is still missing is the dictionary between them: given where and when an event happens for the stationmaster, where and when does it happen for the passenger? Lesson 5 derives it.

### 5. From station to train: the Lorentz transformation (p. 5–7)

**Why we need it**

The stationmaster describes an event by $x, y, z, t$ (station co-ordinates and station time); a passenger describes the same event by $\xi, \eta, \zeta, \tau$ (co-ordinates measured with the train's rods, time from train clocks synchronised by the lesson-2 rule on the train). We need the equations that turn one description into the other. The old answer, Galileo's, is $\xi = x - vt$ and $\tau = t$. Let us test it on the express.

**Work it out yourself**

When the rear of the express passes station A, both the station clock and the train clock there read 0, and the rear of the train is the origin of the train's co-ordinates. At that moment a flash leaves the origin forward. In station co-ordinates the light arrives at station B, $x = 300$ km, at $t = 1$ ms.

> [!question]- Question 1: Use Galileo's rule $\xi = x - vt$, $\tau = t$ with $v = 180$ km per ms. Where and when is the light, for the passenger? What speed does the passenger then find for light?
> $\xi = 300 - 180 \times 1 = 120$ km, $\tau = 1$ ms, speed $120/1 = 120$ km per ms $= c - v$. Together, the principle of relativity and the constancy of light demand that the passenger also measure $c$; Galileo gives 120, so Galileo's rule must go.

> [!question]- Question 2: Now use Einstein's rule $\tau = \beta(t - vx/c^2)$, $\xi = \beta(x - vt)$ with $\beta = 1.25$. First compute $vx/c^2$: $v = 180$, $x = 300$, $c^2 = 90{,}000$. What are $\tau$ and $\xi$?
> $vx/c^2 = 180 \times 300 / 90{,}000 = 0.6$ ms. So $\tau = 1.25 \times (1 - 0.6) = 0.5$ ms and $\xi = 1.25 \times (300 - 180) = 150$ km.

> [!question]- Question 3: With Einstein's numbers, what speed does the passenger find for the flash?
> $150 / 0.5 = 300$ km per ms $= c$. The light keeps speed $c$ in the train system as well.

> [!question]- Question 4: The train's own origin clock is at $x = vt$. At station time $t = 1$ ms it is at $x = 180$ km. What do the formulas give for $\xi$ and $\tau$?
> $\xi = 1.25 \times (180 - 180) = 0$ (it stays at the train's origin, as it should); $vx/c^2 = 180 \times 180/90{,}000 = 0.36$, so $\tau = 1.25 \times (1 - 0.36) = 1.25 \times 0.64 = 0.8$ ms. The train clock shows 0.8 ms when the station clock beside it shows 1 ms — lesson 8 returns to this.

> [!tip] Cause and effect
> Galileo's rule gives the passenger light at $c - v$ → it violates the two principles → Einstein's transformation mixes $x$ into the time, $\tau = \beta(t - vx/c^2)$ → light keeps speed $c$ for both observers.

**The concept from the paper**

Einstein takes two systems with parallel axes: the stationary system **K** with co-ordinates $x, y, z$ and time $t$, and the moving system **k** with $\xi, \eta, \zeta$ and time $\tau$, whose origin moves with constant velocity $v$ along the increasing $x$ of K (p. 5). Both have identical rods and clocks; each system's clocks are synchronised by the lesson-2 rule using light signals within that system. To every $x, y, z, t$ there belongs a $\xi, \eta, \zeta, \tau$ of the same event; the task is to find the equations connecting them (p. 5–6).

The derivation (p. 6–7) uses only: the equations must be **linear** (space and time are homogeneous), $\tau$ must summarise the readings of k's clocks synchronised by the lesson-2 rule, and light moves with $c$ in K, so relative to k's origin it moves with $c - v$ forward and $c + v$ back. It yields

$$\tau = s(v)\,\beta\,(t - vx/c^2),\quad \xi = s(v)\,\beta\,(x - vt),\quad \eta = s(v)\,y,\quad \zeta = s(v)\,z \tag{5.1}$$

with

$$\beta = \frac{1}{\sqrt{1 - v^2/c^2}} \tag{5.2}$$

and $s(v)$ a function of $v$ not yet known (the paper writes it $\varphi(v)$; this note calls it $s(v)$ because $\varphi$ is needed for an angle in lesson 12). If nothing is assumed about the initial position of k and the zero of $\tau$, an additive constant goes on the right of each equation (p. 7). Lesson 6 shows $s(v) = 1$; the numbers in questions 2–4 already used $s = 1$.

> [!note]- Deep dive: the derivation on p. 6–7, step by step (optional)
> 1. Put $u = x - vt$ (the paper calls it $x'$). A point at rest in k has constant $u, y, z$. Treat $\tau$ as a function of $u, y, z, t$.
> 2. From k's origin a ray leaves at $\tau_0$ along k's $\xi$ axis to the point at distance $u$, is reflected at $\tau_1$ and returns at $\tau_2$. The lesson-2 rule on the train says $\tfrac12(\tau_0 + \tau_2) = \tau_1$. In K the out trip takes $u/(c - v)$ and the return $u/(c + v)$, so
> $\tfrac12\left[\tau(0,0,0,t) + \tau\left(0,0,0,t + \tfrac{u}{c-v} + \tfrac{u}{c+v}\right)\right] = \tau\left(u,0,0,t + \tfrac{u}{c-v}\right)$.
> 3. Let $u$ be infinitesimally small and expand both sides to first order:
> $\tfrac12\left(\tfrac{1}{c-v} + \tfrac{1}{c+v}\right)\tfrac{\partial\tau}{\partial t} = \tfrac{\partial\tau}{\partial u} + \tfrac{1}{c-v}\tfrac{\partial\tau}{\partial t}$, i.e. $\tfrac{\partial\tau}{\partial u} + \tfrac{v}{c^2 - v^2}\tfrac{\partial\tau}{\partial t} = 0$. Any starting point would do, so this holds for all $u, y, z$.
> 4. Along k's $\eta$ and $\zeta$ axes light, seen from K, moves with $\sqrt{c^2 - v^2}$; the same argument gives $\partial\tau/\partial y = \partial\tau/\partial z = 0$.
> 5. $\tau$ is linear, so $\tau = a\left(t - \tfrac{v}{c^2 - v^2}u\right)$, with $a$ an unknown function of $v$ and $\tau = 0$ at k's origin when $t = 0$.
> 6. Light sent along $\xi$ at $\tau = 0$ has $\xi = c\tau$. In K it moves relative to k's origin with $c - v$, so $u/(c - v) = t$. Substituting: $\xi = a\,\tfrac{c^2}{c^2 - v^2}\,u$. Rays along the other axes (with $y/\sqrt{c^2 - v^2} = t$, $u = 0$) give $\eta = a\,\tfrac{c}{\sqrt{c^2 - v^2}}\,y$ and $\zeta = a\,\tfrac{c}{\sqrt{c^2 - v^2}}\,z$.
> 7. Substituting $u = x - vt$ and writing $s(v) = a\,c/\sqrt{c^2 - v^2}$ gives equations (5.1).
>
> Check with question 2's numbers ($s = 1$): $c^2 - v^2 = 90{,}000 - 32{,}400 = 57{,}600$, and $\beta = 300/\sqrt{57{,}600} = 300/240 = 1.25$.

**In professional terms:** The Lorentz transformation relates the co-ordinates of an event in two inertial frames in standard configuration: $t' = \gamma(t - vx/c^2)$, $x' = \gamma(x - vt)$, $y' = y$, $z' = z$, with the Lorentz factor $\gamma = 1/\sqrt{1 - v^2/c^2}$ (the paper's $\beta$).

**What it solves and what it is for**

This single set of equations contains everything in Part 1: lesson 7 reads length contraction out of the $\xi$ equation, lesson 8 reads the slow moving clock out of the $\tau$ equation, and lesson 9 composes two of them to add velocities. The term $-vx/c^2$ in $\tau$ is lesson 4 in formula form: the train's time at an event depends on where along the line it happens.

> [!warning] Common pitfall
> $\beta$ in this paper is the Lorentz factor, $\ge 1$. Many modern books use $\beta$ for $v/c$ and $\gamma$ for the factor. With $v = 0.6c$: the paper's $\beta = 1.25$, while modern $\beta = 0.6$.

**Pros and cons**

The derivation needs only the two principles, but it leaves one unknown, $s(v)$, and one worry: the principle of constant light speed was assumed in K; is it compatible with the principle of relativity, so that light also moves at $c$ in every direction in k? Lesson 6 checks both.

### 6. Light is still a sphere, and s(v) = 1 (p. 8–9)

**Why we need it**

Lesson 5 built the transformation from light moving along the three axes only. A lamp flashing at the origin sends light in every direction. If in the train system that light did not spread as a sphere at speed $c$, the two principles would contradict each other after all. And the unknown factor $s(v)$ must be pinned down, or every number we compute is uncertain by that factor.

**Work it out yourself**

The flash of lesson 5 leaves the common origin at $t = \tau = 0$. In the station system it is a sphere of radius $ct$.

> [!question]- Question 1: One point of the sphere: the light that went straight along the track, at $x = 300$ km, $y = 0$, $t = 1$ ms. Lesson 5 turned this into $\xi = 150$ km, $\tau = 0.5$ ms. Is $\xi^2 + \eta^2 + \zeta^2 = (c\tau)^2$?
> $150^2 = 22{,}500$ and $(300 \times 0.5)^2 = 150^2 = 22{,}500$. Yes.

> [!question]- Question 2: Another point: light that went sideways, perpendicular to the track, at $x = 0$, $y = 300$ km, $t = 1$ ms (in K, $x^2 + y^2 = 300^2 = (ct)^2$). Transform it with $s = 1$. Is it on a sphere of radius $c\tau$ in k?
> $\xi = 1.25 \times (0 - 180) = -225$ km, $\eta = 300$ km, $\tau = 1.25 \times (1 - 0) = 1.25$ ms. $\xi^2 + \eta^2 = 50{,}625 + 90{,}000 = 140{,}625$ and $(c\tau)^2 = 375^2 = 140{,}625$. Yes: the passenger also sees a sphere spreading at $c$.

> [!question]- Question 3: Transform the event of question 1 from K to k with $v$, then from k to a third system K′ that moves with $-v$ relative to k. Call K′'s co-ordinates and time $\bar x, \bar t$ (the paper writes $x', t'$). Use $\bar x = \beta(\xi + v\tau)$, $\bar t = \beta(\tau + v\xi/c^2)$. Do you get back $x = 300$ km, $t = 1$ ms?
> $\bar x = 1.25 \times (150 + 180 \times 0.5) = 1.25 \times 240 = 300$ km. $v\xi/c^2 = 180 \times 150/90{,}000 = 0.3$, so $\bar t = 1.25 \times (0.5 + 0.3) = 1.25 \times 0.8 = 1$ ms. Yes: going with $v$ and back with $-v$ returns to the start.

> [!tip] Cause and effect
> Points of the light sphere in K land on a sphere of radius $c\tau$ in k → the two principles are compatible → going to k and back must be the identity, which (with a symmetry argument) forces $s(v) = 1$.

**The concept from the paper**

**Compatibility of the principles (p. 8).** A spherical wave emitted at $t = \tau = 0$ from the common origin satisfies in K

$$x^2 + y^2 + z^2 = c^2t^2 \tag{6.1}$$

and after transforming, "after a simple calculation",

$$\xi^2 + \eta^2 + \zeta^2 = c^2\tau^2 \tag{6.2}$$

so it is still a spherical wave with velocity $c$ in the moving system: the two fundamental principles are compatible. Footnote 5 adds that the Lorentz transformation may be deduced more simply directly from the condition that (6.1) implies (6.2).

**Finding $s(v)$ (p. 8–9).** Introduce a third system K′ moving relative to k with velocity $-v$ along k's $\xi$ axis (the paper labels it $\Xi$; the Fourmilab editor's notes, marked †, correct the 1923 translation, which wrote k's axes as $X, Y, Z$, clashing with K's, and wrote "k" for K′). Applying the transformation twice gives
$\bar t = s(v)s(-v)\,t$, $\bar x = s(v)s(-v)\,x$, $\bar y = s(v)s(-v)\,y$, $\bar z = s(v)s(-v)\,z$ (K′'s co-ordinates, written $x', y', z', t'$ in the paper — not the $x' = x - vt$ of lesson 5's deep dive).
The relations between $\bar x, \bar y, \bar z$ and $x, y, z$ do not contain $t$, so K and K′ are at rest relative to each other and the transformation must be the identity: $s(v)\,s(-v) = 1$. Next, a rod along k's $\eta$ axis, from $\eta = 0$ to $\eta = \ell$, moves perpendicular to its own length; in K its ends are at $x_1 = vt,\ y_1 = \ell/s(v)$ and $x_2 = vt,\ y_2 = 0$, so its length in K is $\ell/s(v)$. By symmetry this length can depend only on the speed, not on the direction of motion, so $s(v) = s(-v)$. Together: $s(v) = 1$, and the transformation is

$$\tau = \beta\,(t - vx/c^2),\qquad \xi = \beta\,(x - vt),\qquad \eta = y,\qquad \zeta = z,\qquad \beta = 1/\sqrt{1 - v^2/c^2} \tag{6.3}$$

![[Lecture Notes/Example for skill/attachments/specrel-1905-s09.png]]
*Figure 6.1 · p. 9 · The transformation equations exactly as printed on p. 9, after $\varphi(v) = 1$ has been shown: read them line by line against equation (6.3); the paper's $\varphi$ is this note's $s$.*

**In professional terms:** The Lorentz transformation preserves the light cone ($x^2 + y^2 + z^2 - c^2t^2 = 0$ maps to itself), transverse lengths are unchanged, and the boosts along one axis form a group: a boost by $v$ followed by $-v$ is the identity.

**What it solves and what it is for**

Equation (6.3) is now fixed with no unknowns. Question 3 is the first hint of a deeper structure: transformations can be chained, and the chain of $v$ and $-v$ gives nothing. Lesson 9 chains two transformations in the same direction to get the velocity-addition law.

> [!note]- Deep dive: why "a simple calculation" works (optional)
> Take $s = 1$ and write $\xi = \beta(x - vt)$, $\tau = \beta(t - vx/c^2)$. Then
> $\xi^2 - c^2\tau^2 = \beta^2\left[(x - vt)^2 - (ct - vx/c)^2\right] = \beta^2\left[x^2(1 - v^2/c^2) - c^2t^2(1 - v^2/c^2)\right] = x^2 - c^2t^2$,
> because the cross terms $-2xvt$ and $+2xvt$ cancel and $\beta^2(1 - v^2/c^2) = 1$. With $\eta = y$, $\zeta = z$: $\xi^2 + \eta^2 + \zeta^2 - c^2\tau^2 = x^2 + y^2 + z^2 - c^2t^2$, so (6.1) gives (6.2). Question 2's numbers: $140{,}625 - 140{,}625 = 0$ on both sides.

**Pros and cons**

We now have the finished transformation and the proof that the principles fit together. What we do not yet have is its physical meaning: what does a passenger's rod look like to the stationmaster, and how fast does a passenger's clock tick? Lesson 7 starts with the rod.

### 7. Moving bodies are shorter (p. 9–10)

**Why we need it**

Lesson 4 used the number 240 km for the length of the moving express without explaining it. The train is 300 km long at rest. The stationmaster measures it by method (b): he notes where the rear and the front are at one and the same station time, then measures the distance between those two platform marks. What does he get?

**Work it out yourself**

At station time $t = 0$ the rear of the train is at $x = 0$. In the train's co-ordinates the rear is at $\xi = 0$ and the front at $\xi = 300$ km.

> [!question]- Question 1: Use $\xi = \beta(x - vt)$ with $t = 0$ and $\beta = 1.25$. At what platform position $x$ is the front, where $\xi = 300$?
> $300 = 1.25 \times (x - 0)$, so $x = 300/1.25 = 240$ km.

> [!question]- Question 2: So how long is the moving train, measured from the platform? By what factor is it shorter than at rest?
> 240 km, shorter by the factor $240/300 = 0.8 = \sqrt{1 - v^2/c^2}$.

> [!question]- Question 3: A ball on the train, round when at rest, with radius 1 m. Which of its three diameters change for the stationmaster: along the track, sideways, up?
> Only the one along the track: $\eta = y$ and $\zeta = z$ are unchanged. Along the track it is 0.8 of 2 m, i.e. 1.6 m; the other two stay 2 m.

> [!question]- Question 4: What happens to the factor $\sqrt{1 - v^2/c^2}$ as $v$ approaches $c$?
> It approaches 0: along the direction of motion the body would shrink to nothing.

> [!tip] Cause and effect
> The stationmaster marks both ends at one station time → by the transformation the front's mark is at $300/\beta = 240$ km → a moving body is shortened along its motion by $\sqrt{1 - v^2/c^2}$ and unchanged across it.

**The concept from the paper**

A rigid sphere of radius $R$ is at rest in k with centre at k's origin (footnote 6: a body of spherical form when examined at rest). Its surface is $\xi^2 + \eta^2 + \zeta^2 = R^2$. Expressed in $x, y, z$ at $t = 0$ (p. 9–10):

$$\frac{x^2}{\left(\sqrt{1 - v^2/c^2}\right)^2} + y^2 + z^2 = R^2 \tag{7.1}$$

So, viewed from the stationary system, the moving sphere is an **ellipsoid of revolution** with axes

$$R\sqrt{1 - v^2/c^2},\quad R,\quad R \tag{7.2}$$

The $Y$ and $Z$ dimensions of every rigid body are unchanged by the motion; the $X$ dimension appears shortened in the ratio $1 : \sqrt{1 - v^2/c^2}$ — the greater $v$, the greater the shortening. For $v = c$ all moving objects, viewed from the stationary system, shrivel up into plane figures (editor's note †: the 1923 translation wrote "plain figures"). For velocities greater than that of light the deliberations become meaningless; light's velocity plays, physically, the part of an infinitely great velocity. The same results hold for bodies at rest in the "stationary" system viewed from a system in uniform motion (p. 10).

**In professional terms:** Length contraction: an object of proper length $L_0$ moving with speed $v$ has length $L_0/\gamma = L_0\sqrt{1 - v^2/c^2}$ along its motion in the frame where it moves; transverse dimensions are unchanged.

**What it solves and what it is for**

It explains lesson 4's number: $r_{AB} = 240$ km is method (b)'s length, while method (a) (the passengers' rods) gives 300 km, just as the principle of relativity requires. The effect is **mutual**: to the passengers, the platform and the distance between stations are shortened by the same factor. Nobody's measurement is "the real one"; each is the length in that system.

> [!warning] Common pitfall
> The contraction is not a squeezing caused by some force, and the passengers notice nothing unusual: in the train, their rods, bodies and the train itself are all 300 km long by method (a). The 240 km appears only when the moving train's ends are located simultaneously *in the station's sense*, and lesson 4 showed that sense differs from the train's.

**Pros and cons**

Contraction answers the length question. The same transformation has a second consequence that the paper finds "peculiar": it concerns clocks carried by the train. Question 4 of lesson 5 already showed a train clock reading 0.8 ms while the station clock beside it read 1 ms. Lesson 8 makes that general.

### 8. Moving clocks are slow (p. 10–11)

**Why we need it**

A clock rides at the rear of the express, set to 0 as it passes station A at station time 0. Later it passes other station clocks, all synchronised in the station system. If the train clock always matched the station clock beside it, time would be the same for both. Lesson 5's question 4 suggests it does not.

**Work it out yourself**

> [!question]- Question 1: The train clock is always at $x = vt$. Put $x = vt$ into $\tau = \beta(t - vx/c^2)$. What is left?
> $\tau = \beta\,t\,(1 - v^2/c^2) = t\sqrt{1 - v^2/c^2}$, because $\beta(1 - v^2/c^2) = \sqrt{1 - v^2/c^2}$.

> [!question]- Question 2: At $v = 0.6c$, what does the train clock read when it passes the station clock at 180 km (which reads 1 ms)? And at 360 km (2 ms)?
> $0.8 \times 1 = 0.8$ ms and $0.8 \times 2 = 1.6$ ms.

> [!question]- Question 3: By how much does the train clock fall behind per station millisecond? The paper's approximation for small $v$ is $\tfrac12 v^2/c^2$. What does that give at $v = 0.6c$?
> Exactly $1 - 0.8 = 0.2$ ms per ms. The approximation gives $\tfrac12 \times 0.36 = 0.18$: close, but at this speed the neglected higher-order terms matter.

> [!question]- Question 4: A real express at 30 m/s: $v/c = 10^{-7}$. How much does its clock fall behind per second, using $\tfrac12 v^2/c^2$?
> $\tfrac12 \times (10^{-7})^2 = 5 \times 10^{-15}$ seconds per second (a ratio, so it is the same in ms per ms) — far below anything measurable with clocks of 1905.

> [!tip] Cause and effect
> The train clock stays at $x = vt$ → the transformation gives $\tau = t\sqrt{1 - v^2/c^2}$ → viewed from the station, a moving clock runs slow by the factor 0.8 at 0.6c, by about $\tfrac12 v^2/c^2$ at everyday speeds.

![[Lecture Notes/Example for skill/attachments/specrel-1905-anim-passing.svg]]
*Figure 8.1 · own diagram · The 300-km express at 0.6c seen from the platform: check the train's length on the platform scale (240 km), then compare the orange train clock with each green station clock it passes (0.80 vs 1.0 ms, 1.60 vs 2.0 ms).* (If the animation does not play, questions 2 of lessons 7 and 8 give the same numbers.)

**The concept from the paper**

A clock that marks time $t$ when at rest in K and $\tau$ when at rest in k is placed at k's origin and adjusted to mark $\tau$. What is its rate viewed from K? With $x = vt$ (p. 10):

$$\tau = \frac{1}{\sqrt{1 - v^2/c^2}}\,(t - vx/c^2) = t\sqrt{1 - v^2/c^2} = t - \left(1 - \sqrt{1 - v^2/c^2}\right)t \tag{8.1}$$

So the clock, viewed in the stationary system, is **slow by $1 - \sqrt{1 - v^2/c^2}$ seconds per second**, or, neglecting magnitudes of fourth and higher order, by $\tfrac12 v^2/c^2$.

The "peculiar consequence" (p. 10–11): if clocks at A and B are synchronous in the stationary system and the clock at A is moved with velocity $v$ along AB to B, on arrival it lags the clock at B by $\tfrac12 t v^2/c^2$ (up to fourth order), $t$ being the travel time. This still holds if the clock moves along any polygonal line, and also when A and B coincide. Assuming the result holds for a continuously curved line: a clock moved around a closed curve with constant velocity, returning after $t$ seconds, is $\tfrac12 t v^2/c^2$ second slow compared with the clock that stayed. Hence, Einstein concludes, a balance-clock (a clock regulated by a balance wheel and spring) at the equator must go more slowly, by a very small amount, than a similar clock at one of the poles (footnote 7: not a pendulum clock, which is physically a system to which the Earth belongs).

**In professional terms:** Time dilation: a clock moving with speed $v$ runs slow by the factor $\sqrt{1 - v^2/c^2} = 1/\gamma$ in the frame where it moves; the time it shows is its proper time.

**What it solves and what it is for**

The slow clock is the time-side twin of lesson 7's short rod, and both come straight from equation (6.3). The travelling-clock result is the origin of the "twin" or "clock paradox": after a round trip the travelled clock really shows less time, and the travel is not symmetric, because only one clock changed its motion.

> [!info]- Supplement: the equator clock, and a clock trip that was actually made
> Einstein's equator prediction, as he stated it here, turned out to be wrong once gravity is included. Clocks on the equator and at the poles at sea level run at the same rate, because the gravitational effect on clock rates (unknown in 1905, part of general relativity) exactly cancels the time dilation from the equator clock's motion: sea level is a surface on which gravitational plus centrifugal potential is constant.
> The travelling-clock effect itself has been measured. In October 1971 four caesium clocks were flown around the world on commercial jets, once eastward and once westward. Compared with the clocks of the U.S. Naval Observatory they lost 59 ± 10 ns on the eastward trip and gained 273 ± 7 ns on the westward trip, in good agreement with relativity's predictions.
> Sources: [Harvey & Schucking, 2005]; [Hafele & Keating, 1972]

> [!note]- Deep dive: how small is the equator effect by the paper's own formula? (optional)
> The equator moves at about 465 m/s. Then $\tfrac12 v^2/c^2 = \tfrac12 \times (465/(3 \times 10^8))^2 \approx 1.2 \times 10^{-12}$ seconds per second, about $1.0 \times 10^{-7}$ s ≈ 0.1 microsecond per day (derived here). As the supplement above explains, gravity cancels it at sea level, but the size shows why no 1905 clock could have tested it.

**Pros and cons**

Rods and clocks are now understood. One kinematic question is left, the one that started the trouble in lesson 1: if the train moves at $v$ and something moves inside the train at $w$, how fast does it move for the stationmaster? Galileo said $v + w$. Lesson 9 gives the answer that respects the two principles.

### 9. Adding velocities (p. 11–12)

**Why we need it**

A conductor in the express fires a signal ball forward at $w = 0.6c$ relative to the train (a thought experiment; the numbers are chosen to make the effect visible). The train itself moves at $v = 0.6c$. Galileo's rule gives the ball $1.2c$ on the platform, faster than light, while lesson 7 said speeds above $c$ make the theory meaningless. Something must replace $v + w$.

**Work it out yourself**

> [!question]- Question 1: Galileo's rule: how fast is the ball for the stationmaster?
> $0.6c + 0.6c = 1.2c$.

> [!question]- Question 2: Einstein's rule for motion along the track is $V = (v + w)/(1 + vw/c^2)$. With $v = w = 0.6c$, what is $vw/c^2$, and what is $V$?
> $vw/c^2 = 0.36$, so $V = 1.2c/1.36 = \tfrac{15}{17}c \approx 0.882c$. Below $c$.

> [!question]- Question 3: Instead of the ball, a lamp on the train shines forward: $w = c$. What does the rule give?
> $V = (v + c)/(1 + v/c) = c\,(v + c)/(c + v) = c$. Light from the moving train still moves at exactly $c$ for the station, as the second principle demands.

> [!question]- Question 4: Try $v = w = 0.9c$. What is $V$?
> $1.8c/(1 + 0.81) = 1.8c/1.81 \approx 0.9945c$. Two speeds below $c$ always combine to a speed below $c$.

> [!tip] Cause and effect
> Galileo's rule adds speeds and exceeds $c$ → the Lorentz transformation gives $V = (v + w)/(1 + vw/c^2)$ → speeds below $c$ stay below $c$, and $c$ combined with anything stays $c$.

![[Lecture Notes/Example for skill/attachments/specrel-1905-anim-veladd.svg]]
*Figure 9.1 · own diagram · Three rows, same train at 0.6c: compare where each bar ends relative to the dashed light-speed wall — Galileo's 1.2c crosses it, Einstein's 0.882c stays below, and light in the train stops exactly at c.* (If the animation does not play, questions 1–3 give the same numbers.)

**The concept from the paper**

In k, moving along K's $x$-axis with velocity $v$, a point moves according to $\xi = w_\xi \tau$, $\eta = w_\eta \tau$, $\zeta = 0$. Transforming with (6.3) gives its motion in K (p. 11):

$$x = \frac{w_\xi + v}{1 + vw_\xi/c^2}\,t,\qquad y = \frac{\sqrt{1 - v^2/c^2}}{1 + vw_\xi/c^2}\,w_\eta\,t,\qquad z = 0 \tag{9.1}$$

So the parallelogram law of velocities is valid only to a first approximation. With $V^2 = (dx/dt)^2 + (dy/dt)^2$, $w^2 = w_\xi^2 + w_\eta^2$ and $\alpha = \tan^{-1}(w_\eta/w_\xi)$ the angle between $v$ and $w$ (the paper writes $a$; editor's note †: the original had $w_y/w_x$), "a simple calculation" gives (p. 12)

$$V = \frac{\sqrt{(v^2 + w^2 + 2vw\cos\alpha) - (vw\sin\alpha/c)^2}}{1 + vw\cos\alpha/c^2} \tag{9.2}$$

$v$ and $w$ enter symmetrically. If $w$ is also along $X$:

$$V = \frac{v + w}{1 + vw/c^2} \tag{9.3}$$

From this: two velocities less than $c$ always give a velocity less than $c$ (setting $v = c - \kappa$, $w = c - \lambda$ with $\kappa, \lambda$ positive and less than $c$, $V = c\,\dfrac{2c - \kappa - \lambda}{2c - \kappa - \lambda + \kappa\lambda/c} < c$); and $c$ cannot be altered by composition with a velocity less than $c$: $V = (c + w)/(1 + w/c) = c$. The same formula follows from compounding two transformations (6.3): a system k′ moving parallel to k with velocity $w$ along k's $\xi$ axis (the paper's $\Xi$) is related to K by equations (6.3) with $v$ replaced by $(v + w)/(1 + vw/c^2)$, so such parallel transformations **necessarily form a group** (p. 12).

**In professional terms:** Relativistic velocity addition: collinear velocities combine as $u = (v + w)/(1 + vw/c^2)$; boosts along one axis compose into a boost, i.e. they form a group, and $c$ is invariant.

**What it solves and what it is for**

This closes the clash of lesson 1: the lamp on the train gives light at $c$ for the station (question 3), because velocities are measured with each system's clocks and rods, and those differ as lessons 4, 7 and 8 showed. At everyday speeds $vw/c^2$ is tiny and Galileo's rule is recovered.

> [!note]- Deep dive: getting (9.3) from the transformation (optional)
> The ball has $\xi = w\tau$. Invert (6.3): $x = \beta(\xi + v\tau)$, $t = \beta(\tau + v\xi/c^2)$. Then $x = \beta\tau(w + v)$ and $t = \beta\tau(1 + vw/c^2)$, so $x/t = (v + w)/(1 + vw/c^2)$. With $v = w = 180$ km per ms: $x/t = 360/(1 + 32{,}400/90{,}000) = 360/1.36 \approx 264.7$ km per ms $= \tfrac{15}{17}c$.

**Pros and cons**

With velocity addition the kinematics is complete and self-consistent, and it reduces to Galileo's at low speed. The paper now turns to what it was written for: electrodynamics. If a magnet and a coil in lesson 1 looked different from different systems, the fields themselves must change between K and k. Part 2 starts there.

> [!question]- Pause: A passenger measures the express as 300 km; the stationmaster measures 240 km. The passenger's clock runs slow for the stationmaster. Does the stationmaster's clock run slow for the passenger?
> Yes. The principle of relativity makes the situation symmetric: for the passenger, the platform moves at 0.6c, so platform rods are shortened to 0.8 and platform clocks run at 0.8 of the rate. There is no contradiction because the two compare readings using different definitions of simultaneity (lesson 4). The asymmetry appears only when one clock turns round and returns, as in lesson 8's closed curve.

## Part 2 · Electrodynamics: what moving observers measure

The express now carries a laboratory car. Part 2 (the paper's "Electrodynamical Part", §6–§10) brings one instrument aboard per lesson and asks what a passenger measures, using nothing but the transformation (6.3) and the principle of relativity. The paper uses Gaussian units (the centimetre–gram–second system in which a unit charge is the charge that exerts one dyne on an equal charge 1 cm away): $(X, Y, Z)$ is the electric force and $(L, M, N)$ the magnetic force, i.e. the force on a unit charge and on a unit magnetic pole respectively. From here on a single prime marks a quantity measured in k (lesson 13 adds ″ for reflected light in k and ‴ for reflected light back in K). Axes: $x$ runs along the track, $y$ horizontally across it, $z$ vertically.

### 10. Transforming electric and magnetic forces (p. 12–14)

**Why we need it**

A strong magnet lies on the platform beside the track. Near the track its field is purely magnetic in the station system: the magnetic force points vertically, $N = 1$ unit, and there is no electric force, $X = Y = Z = 0$. A small charged ball of unit charge rides at rest in the laboratory car. Lesson 1 asked what pushes charges in a moving conductor. Now we can ask it precisely: which force does a passenger measure on the ball?

**Work it out yourself**

> [!question]- Question 1: In the station system, a charge **at rest** next to the magnet: what force does it feel?
> None. A charge at rest feels only the electric force, and here $X = Y = Z = 0$.

> [!question]- Question 2: For the passenger, the ball in the car is at rest. By the principle of relativity, the only force a resting unit charge can feel in k is the electric force $(X', Y', Z')$ in k. If the ball is in fact pushed (lesson 1: currents do flow in the moving coil), what must be true of $(X', Y', Z')$?
> It cannot be zero: in the train system there must be an **electric** force at the ball, even though the station sees only a magnetic one.

> [!question]- Question 3: The paper's result is $Y' = \beta\,(Y - \tfrac{v}{c}N)$. With $Y = 0$, $N = 1$, $v/c = 0.6$, $\beta = 1.25$: what is $Y'$?
> $Y' = 1.25 \times (0 - 0.6 \times 1) = -0.75$ units, sideways across the track.

> [!question]- Question 4: A real express at 30 m/s has $v/c = 10^{-7}$. What is $Y'$ then, and does the factor $\beta$ matter?
> $Y' \approx -10^{-7}$ units; $\beta - 1 \approx 5 \times 10^{-15}$, so the factor $\beta$ is invisible and $Y' \approx -\tfrac{v}{c}N$.

> [!tip] Cause and effect
> A pure magnetic field in K pushes a charge only if it moves → in k the charge is at rest, so the push must be an electric force → the principle of relativity forces electric and magnetic forces to mix when we change systems.

**The concept from the paper**

Let the Maxwell–Hertz equations for empty space hold in K (p. 12–13):

$$\frac{1}{c}\frac{\partial X}{\partial t} = \frac{\partial N}{\partial y} - \frac{\partial M}{\partial z},\quad \frac{1}{c}\frac{\partial Y}{\partial t} = \frac{\partial L}{\partial z} - \frac{\partial N}{\partial x},\quad \frac{1}{c}\frac{\partial Z}{\partial t} = \frac{\partial M}{\partial x} - \frac{\partial L}{\partial y}$$
$$\frac{1}{c}\frac{\partial L}{\partial t} = \frac{\partial Y}{\partial z} - \frac{\partial Z}{\partial y},\quad \frac{1}{c}\frac{\partial M}{\partial t} = \frac{\partial Z}{\partial x} - \frac{\partial X}{\partial z},\quad \frac{1}{c}\frac{\partial N}{\partial t} = \frac{\partial X}{\partial y} - \frac{\partial Y}{\partial x}$$

Rewriting them in the co-ordinates $\xi, \eta, \zeta, \tau$ of lesson 6 gives six equations of the same shape in which the combinations $X$, $\beta(Y - \tfrac{v}{c}N)$, $\beta(Z + \tfrac{v}{c}M)$, $L$, $\beta(M + \tfrac{v}{c}Z)$, $\beta(N - \tfrac{v}{c}Y)$ take the places of the six field components (editor's note †: the 1923 translation interchanged $\zeta$ and $\xi$ in the second equation). The principle of relativity requires that the forces measured in k, $(X', Y', Z')$ and $(L', M', N')$, defined by their ponderomotive effects (the mechanical forces they exert) on electric or magnetic masses (charges and magnetic poles), satisfy the Maxwell–Hertz equations in k. Both systems of equations express the same thing, so the functions at corresponding places must agree up to a common factor $\psi(v)$ (p. 13–14). Solving back for the inverse transformation (velocity $-v$) gives $\psi(v)\psi(-v) = 1$, and symmetry (footnote 8: with only $N \neq 0$, reversing $v$ must reverse $Y'$) gives $\psi(v) = 1$:

$$X' = X,\quad Y' = \beta\left(Y - \tfrac{v}{c}N\right),\quad Z' = \beta\left(Z + \tfrac{v}{c}M\right) \tag{10.1}$$
$$L' = L,\quad M' = \beta\left(M + \tfrac{v}{c}Z\right),\quad N' = \beta\left(N - \tfrac{v}{c}Y\right) \tag{10.2}$$

With our magnet: $X' = 0$, $Y' = -0.75$, $Z' = 0$ and $N' = 1.25 \times (1 - 0) = 1.25$: the passenger sees a stronger magnetic force **and** an electric one.

**In professional terms:** Electric and magnetic fields are not separately frame-independent; under a boost along $x$ the field components perpendicular to the boost transform as $E'_\perp = \gamma(\mathbf{E} + \mathbf{v} \times \mathbf{B}/c)_\perp$ and $B'_\perp = \gamma(\mathbf{B} - \mathbf{v} \times \mathbf{E}/c)_\perp$ (Gaussian units), while the parallel components are unchanged.

**What it solves and what it is for**

This is the first use of the kinematics of Part 1 on electricity: the same equation (6.3) that shortens rods and slows clocks also tells us how the fields look from the train. The equations of Maxwell and Hertz keep exactly their form in the moving system: they already satisfy the principle of relativity, provided we use the new transformation instead of Galileo's.

> [!warning] Common pitfall
> "The magnetic field turns into an electric field" is too strong: in our example the passenger sees **both** a magnetic force $N' = 1.25$ and an electric force $Y' = -0.75$. What changes between systems is the split of one electromagnetic field into its electric and magnetic parts.

**Pros and cons**

We have the rule, but not yet its meaning for the "electromotive force" that 1905 textbooks use. Does the old concept survive? And does lesson 1's asymmetry really disappear? Lesson 11 answers both.

### 11. The electromotive force explained; the asymmetry disappears (p. 14–15)

**Why we need it**

Lesson 1's two stories for one experiment used a special concept, the "electromotive force" on a moving conductor. With equation (10.1) in hand we can ask what that force really is, and whether lesson 1's coil-moving and magnet-moving cases now get the same explanation.

**Work it out yourself**

> [!question]- Question 1: In the station system the ball moves at $v$ through a pure magnetic force $N$. The old rule says it feels an electromotive force equal to (velocity × magnetic force)/c. How big is it at $v/c = 0.6$, $N = 1$?
> $0.6 \times 1 = 0.6$ units, perpendicular to both the velocity and the magnetic force.

> [!question]- Question 2: The old rule gives 0.6 (a calculation in the station system); lesson 10 gives $|Y'| = 0.75$ for the electric force in the ball's own system. What is the ratio, and which order in $v/c$ does the old rule drop?
> $0.75/0.6 = 1.25 = \beta$. The old rule neglects terms of second and higher order in $v/c$ (at 30 m/s, a relative difference of about $5 \times 10^{-15}$).

> [!question]- Question 3: Case (a): magnet on the platform, coil on the train. Case (b): magnet on the train, coil on the platform, and the train now runs in the $-x$ direction, so that in the coil's system the magnet moves past with the same velocity as in (a). In the **coil's own system**, what electric and magnetic forces does the coil find near the magnet in the two cases?
> The same: in both cases, in the coil's rest system, the magnet moves past with the same velocity, so (10.1) gives the same forces, $N = 1.25$ and $Y = -0.75$ units in our example. The coil's charges feel the same electric force, and the currents are equal.
> — One explanation for both cases.

> [!tip] Cause and effect
> The force on a moving charge equals the electric force in the charge's own rest system → the "electromotive force" is only the first-order name for that electric force seen from another system → both magnet–coil cases are one situation seen from the coil, and the asymmetry disappears.

**The concept from the paper**

Let a point charge have magnitude "one" in K (at rest it exerts one dyne on an equal charge 1 cm away); by the principle of relativity it is also "one" in k. At rest in K, the force on it is $(X, Y, Z)$; at rest in k (at least at the relevant instant), the force on it measured in k is $(X', Y', Z')$. The first three equations of (10.1) can therefore be put in words in two ways (p. 14–15):

1. **Old manner of expression:** if a unit point charge moves in an electromagnetic field, there acts on it, in addition to the electric force, an "electromotive force" which, neglecting terms multiplied by the second and higher powers of $v/c$, equals the vector product of the charge's velocity and the magnetic force, divided by $c$.
2. **New manner of expression:** the force on a unit point charge moving in an electromagnetic field equals the electric force at the charge's location, found by transforming the field to a system of co-ordinates at rest relative to the charge.

The analogy holds for "magnetomotive forces". The electromotive force plays merely the part of an **auxiliary concept**, needed only because electric and magnetic forces do not exist independently of the state of motion of the system of co-ordinates. The asymmetry of the introduction (magnet versus conductor in motion) now disappears, and questions about the "seat" of electrodynamic electromotive forces (unipolar machines, dynamos in which a conductor turns next to a magnet) lose their point (p. 15).

**In professional terms:** The Lorentz force $q(\mathbf{E} + \mathbf{v} \times \mathbf{B}/c)$ on a moving charge is the electric force in the charge's instantaneous rest frame; "motional EMF" and "transformer EMF" are one phenomenon seen from different frames.

**What it solves and what it is for**

This is the payoff promised on page 1: the observable current depends only on relative motion, and now the theory also depends only on relative motion. The "new manner" is also a general method, which the next lessons use again and again: to find what a moving body experiences, transform everything into the body's rest system, where only the ordinary laws for bodies at rest are needed.

**Pros and cons**

The method works for static fields. Light is a field that changes rapidly in space and time. What does a passenger measure for the colour, direction and brightness of light from a platform lamp? Lesson 12 applies (10.1) and (6.3) to a light wave.

### 12. Doppler's principle and aberration (p. 15–17)

**Why we need it**

A signal lamp stands far behind the express on the platform and shines along the track. The express runs away from it at 0.6c. 1905 physics knows that a moving observer sees a changed frequency (the Doppler effect) and a changed direction of starlight (aberration), but only in approximations tied to the ether. We want the exact answer, valid "for any velocities whatever".

**Work it out yourself**

The lamp sends one wave crest per period $T$ (station time). The crests move at $c$; the train runs ahead of them at $0.6c$.

> [!question]- Question 1: Each crest must catch up with the train. How much station time passes between two successive crests reaching it? (Hint: a crest gains on the train at $c - v = 0.4c$, and crests are $cT$ apart.)
> $cT/(0.4c) = 2.5\,T$ apart.

> [!question]- Question 2: The train's own clock runs at 0.8 of the station rate (lesson 8). How far apart are the crests on the train clock, and what frequency $\nu'$ does the passenger measure, if the lamp's frequency is $\nu = 1/T$?
> $2.5\,T \times 0.8 = 2\,T$ apart, so $\nu' = \nu/2$.

> [!question]- Question 3: The paper's formula for light arriving straight from behind is $\nu' = \nu\sqrt{(1 - v/c)/(1 + v/c)}$. Check it at $v/c = 0.6$.
> $\sqrt{0.4/1.6} = \sqrt{0.25} = 0.5$. It agrees with question 2.

> [!question]- Question 4: Now the train runs **towards** a lamp ahead of it (use $v = -0.6c$ in the same formula). What frequency does the passenger see?
> $\sqrt{1.6/0.4} = \sqrt{4} = 2$, so $\nu' = 2\nu$.

> [!tip] Cause and effect
> Crests reach a receding train every 2.5 periods of station time → the slow train clock counts that as 2 periods → $\nu' = \nu/2$ receding and $2\nu$ approaching; the paper's formula contains both effects at once.

![[Lecture Notes/Example for skill/attachments/specrel-1905-anim-doppler.svg]]
*Figure 12.1 · own diagram · Crests from the platform lamp spreading at c while the train runs away at 0.6c: watch the green markers — a crest reaches the train only every 2.5 T of station time, which the train's slow clock records as every 2 T.* (If the animation does not play, questions 1–3 give the same numbers.)

**The concept from the paper**

Far from the origin of K a source emits electrodynamic waves which near the origin are (p. 15; here $l, m, n$ are the paper's direction cosines, not the rod length $\ell$ or the mass $m$)
$X = X_0 \sin\Phi$, …, $N = N_0 \sin\Phi$ with $\Phi = \omega\left(t - \tfrac{1}{c}(lx + my + nz)\right)$,
where $(X_0, Y_0, Z_0)$ and $(L_0, M_0, N_0)$ are the amplitude vectors and $l, m, n$ the direction cosines of the wave normals. Transforming the fields with lesson 10 and the co-ordinates with lesson 6 gives a wave of the same form in k, with $X' = X_0\sin\Phi'$, $Y' = \beta(Y_0 - vN_0/c)\sin\Phi'$, and so on, where (p. 15–16)

$$\omega' = \omega\beta(1 - lv/c),\quad l' = \frac{l - v/c}{1 - lv/c},\quad m' = \frac{m}{\beta(1 - lv/c)},\quad n' = \frac{n}{\beta(1 - lv/c)} \tag{12.1}$$

**Doppler's principle for any velocities.** If an observer moves with velocity $v$ relative to an infinitely distant source of frequency $\nu$, and the line "source–observer" makes the angle $\varphi$ with the observer's velocity (in the source's rest system), the observed frequency is

$$\nu' = \nu\,\frac{1 - \cos\varphi \cdot v/c}{\sqrt{1 - v^2/c^2}} \tag{12.2}$$

For $\varphi = 0$: $\nu' = \nu\sqrt{\dfrac{1 - v/c}{1 + v/c}}$ (questions 3–4). In contrast with the customary view, for $v = -c$ (approaching at the speed of light) $\nu' = \infty$.

**Aberration.** With $\varphi'$ the angle between the ray direction in k and the source–observer line (editor's note †: an old misprint gave $l'$ here),

$$\cos\varphi' = \frac{\cos\varphi - v/c}{1 - \cos\varphi \cdot v/c} \tag{12.3}$$

the law of aberration in its most general form. For $\varphi = \tfrac12\pi$ (a lamp exactly abeam of the train in the station system) it becomes $\cos\varphi' = -v/c$: at $0.6c$, $\cos\varphi' = -0.6$, $\varphi' \approx 126.9°$.

**Amplitude.** With $\mathcal{A}$ and $\mathcal{A}'$ the amplitude of the electric or magnetic force in K and in k (the paper writes $A$; renamed here because $A$ is a station), $\mathcal{A}'^2 = \mathcal{A}^2\,\dfrac{(1 - \cos\varphi \cdot v/c)^2}{1 - v^2/c^2}$, which for $\varphi = 0$ becomes $\mathcal{A}'^2 = \mathcal{A}^2\,\dfrac{1 - v/c}{1 + v/c}$ (at 0.6c: $\tfrac14$). So to an observer approaching a light source with velocity $c$, the source would appear of infinite intensity (p. 16–17).

**In professional terms:** The relativistic Doppler shift $\nu' = \gamma\nu(1 - \beta_v\cos\varphi)$ with $\beta_v = v/c$ (for head-on recession $\sqrt{(1-\beta_v)/(1+\beta_v)}$), relativistic aberration $\cos\varphi' = (\cos\varphi - \beta_v)/(1 - \beta_v\cos\varphi)$; both follow from the Lorentz transformation of the wave's phase.

**What it solves and what it is for**

The two old effects, Doppler and aberration, now come from one calculation with no ether. Question 2 shows the new ingredient: the familiar "catching up" factor $1/(1 - v/c)$ is multiplied by the slow-clock factor. The same formula also predicts a shift for light arriving from the side ($\varphi = 90°$): $\nu' = \nu\beta = 1.25\,\nu$ at 0.6c, which comes entirely from the slow-clock factor, since the "catching up" factor $1 - \cos\varphi \cdot v/c$ equals 1 there (derived here).

**Pros and cons**

We know the colour and brightness of light in the moving system. The paper next asks about the **energy** carried by a packet of light, and the push light exerts on a moving mirror. For that, amplitude alone is not enough: the volume the light occupies changes too. Lesson 13.

### 13. Energy of light and radiation pressure (p. 17–19)

**Why we need it**

On the rear wall of the laboratory car hangs a perfect mirror facing the platform lamp behind it. Light from the lamp hits the mirror, which runs away at 0.6c. How much energy does a packet of that light carry for the passenger, how hard does it push the mirror, and what colour is the reflected light back on the platform?

**Work it out yourself**

The light arrives from straight behind ($\varphi = 0$), $v = 0.6c$.

> [!question]- Question 1: Lesson 12 gave the energy density ratio (amplitude squared) as $\tfrac14$. The paper shows that the volume occupied by a fixed packet of light is $S'/S = \sqrt{1 - v^2/c^2}/(1 - v/c)$ in k. What is it here, and what energy ratio $E'/E$ follows?
> $S'/S = 0.8/0.4 = 2$. Energy $=$ density × volume, so $E'/E = \tfrac14 \times 2 = \tfrac12$.

> [!question]- Question 2: Compare $E'/E = \tfrac12$ with the frequency ratio of lesson 12. What do you notice?
> They are equal: energy and frequency of a light packet change by the same law, $\nu'/\nu = E'/E = \tfrac12$.

> [!question]- Question 3: In the mirror's own system the light arrives at frequency $\nu/2$ and is reflected with the same frequency. Seen from the platform, the reflected light comes from a source moving away at 0.6c. What frequency does the platform see?
> Another halving: $\tfrac12 \times \tfrac12 = \tfrac14$, so the reflected light has frequency $\nu/4$ on the platform (the paper calls it $\nu'''$: one prime for k, two for reflected in k, three for reflected and back in K). The paper's formula $\nu''' = \nu\,(1 - 2v/c + v^2/c^2)/(1 - v^2/c^2)$ gives $(1 - 1.2 + 0.36)/0.64 = 0.16/0.64 = \tfrac14$.

> [!question]- Question 4: The pressure on a mirror at rest is $2\cdot\tfrac{\mathcal{A}^2}{8\pi}$ for head-on light. The paper's factor for a mirror receding at $v$ is $(1 - v/c)^2/(1 - v^2/c^2)$. How much weaker is the push at 0.6c?
> $0.16/0.64 = \tfrac14$ of the push on a resting mirror.

> [!tip] Cause and effect
> Energy density and volume both change in the moving system → their product changes exactly like the frequency → treating reflection in the mirror's rest system and transforming back gives the reflected colour and, via energy balance, the pressure.

**The concept from the paper**

Since $\mathcal{A}^2/8\pi$ is the energy of light per unit volume, $\mathcal{A}'^2/8\pi$ is by the principle of relativity the energy per unit volume in k. But the volume of a light complex (the paper's name for a bounded packet of light) is not the same in K and k. A spherical surface moving with the velocity of light, $(x - lct)^2 + (y - mct)^2 + (z - nct)^2 = R^2$, permanently encloses the same light complex (no energy crosses it); viewed in k at $\tau = 0$ it is an ellipsoid (p. 17). With $S$ the volume of the sphere and $S'$ that of the ellipsoid, and $E$, $E'$ the enclosed light energy in K and k:

$$\frac{S'}{S} = \frac{\sqrt{1 - v^2/c^2}}{1 - \cos\varphi \cdot v/c},\qquad \frac{E'}{E} = \frac{\mathcal{A}'^2 S'}{\mathcal{A}^2 S} = \frac{1 - \cos\varphi \cdot v/c}{\sqrt{1 - v^2/c^2}} \tag{13.1}$$

which for $\varphi = 0$ simplifies to $E'/E = \sqrt{(1 - v/c)/(1 + v/c)}$. "It is remarkable that the energy and the frequency of a light complex vary with the state of motion of the observer in accordance with the same law" (p. 18).

**Reflection at a moving mirror (p. 18–19).** Let the plane $\xi = 0$ be perfectly reflecting. Incident light has $\mathcal{A}$, $\cos\varphi$, $\nu$ in K; in k these become $\mathcal{A}'$, $\cos\varphi'$, $\nu'$ by lesson 12. In k the reflection is ordinary: $\mathcal{A}'' = \mathcal{A}'$, $\cos\varphi'' = -\cos\varphi'$, $\nu'' = \nu'$. Transforming back to K gives for the reflected light

$$\mathcal{A}''' = \mathcal{A}\,\frac{1 - 2\cos\varphi \cdot v/c + v^2/c^2}{1 - v^2/c^2},\quad \cos\varphi''' = -\frac{(1 + v^2/c^2)\cos\varphi - 2v/c}{1 - 2\cos\varphi \cdot v/c + v^2/c^2},\quad \nu''' = \nu\,\frac{1 - 2\cos\varphi \cdot v/c + v^2/c^2}{1 - v^2/c^2}$$

The energy arriving per unit area of the mirror per unit time is $\mathcal{A}^2(c\cos\varphi - v)/8\pi$; the energy leaving is $\mathcal{A}'''^2(-c\cos\varphi''' + v)/8\pi$. By the energy principle their difference is the work done by the light pressure $P$ per unit time, $Pv$, which gives

$$P = 2\cdot\frac{\mathcal{A}^2}{8\pi}\,\frac{(\cos\varphi - v/c)^2}{1 - v^2/c^2} \tag{13.2}$$

and, to a first approximation, in agreement with experiment and other theories, $P = 2\cdot\frac{\mathcal{A}^2}{8\pi}\cos^2\varphi$. The general lesson: all problems in the optics of moving bodies can be solved by transforming the light's fields into a system at rest relative to the body, which reduces them to problems in the optics of stationary bodies (p. 19).

**In professional terms:** The energy of a light pulse transforms like its frequency ($E'/E = \nu'/\nu$), and radiation pressure on a moving mirror follows from reflecting in the mirror's rest frame and transforming back (double Doppler shift for the reflected light).

**What it solves and what it is for**

Question 2's "remarkable" coincidence, energy proportional to frequency in every system, is a hint of what light is made of; the paper states it without comment. The mirror problem shows the lesson-11 method at work: do the physics where the body is at rest, then transform.

**Pros and cons**

So far every source of fields has been fixed in one system. Real electrodynamics also has moving charges: currents made of charged particles. Do the Maxwell–Lorentz equations with moving charges also keep their form? Lesson 14.

### 14. Moving charges: convection currents (p. 19–20)

**Why we need it**

A small charged ball sits on the platform. In the station system its charge density is $\rho$ (in the paper's units, $4\pi$ times the density of electricity). The passenger sees the ball rush backwards at 0.6c. What charge density does the passenger measure, and is the ball's total charge the same for both?

**Work it out yourself**

The paper's result is $\rho' = \beta\,(1 - u_x v/c^2)\,\rho$, where $u_x$ is the ball's velocity along the track in the station system.

> [!question]- Question 1: The ball rests on the platform: $u_x = 0$. What is $\rho'$?
> $\rho' = 1.25\,\rho$.

> [!question]- Question 2: For the passenger the ball is shortened along the track (lesson 7). By what factor is its volume changed? What happens to its total charge, density × volume?
> Its volume is multiplied by 0.8; the charge becomes $1.25\rho \times 0.8V = \rho V$. The total charge is unchanged.

> [!question]- Question 3: Now take a **different** ball that rides in the laboratory car, so $u_x = v = 0.6c$, and let $\rho$ now denote the density the station measures for this moving ball. What is $\rho'$, and what is its velocity $u_\xi$ in the train, by $u_\xi = (u_x - v)/(1 - u_x v/c^2)$?
> $\rho' = 1.25 \times (1 - 0.36)\,\rho = 0.8\,\rho$, and $u_\xi = 0$: at rest in the train, where its density is its rest density. In the station it moves and is contracted, which is why the station measured the larger $\rho$.

> [!tip] Cause and effect
> Charge density changes with the system because volumes do → the product, total charge, stays the same → the equations with moving charges keep their form, and the charge velocities transform by the velocity-addition law of lesson 9.

**The concept from the paper**

Start from the Maxwell–Hertz equations with convection currents, where $(u_x, u_y, u_z)$ is the velocity of the charge and
$\rho = \dfrac{\partial X}{\partial x} + \dfrac{\partial Y}{\partial y} + \dfrac{\partial Z}{\partial z}$ is $4\pi$ times the density of electricity; for instance $\dfrac{1}{c}\left(\dfrac{\partial X}{\partial t} + u_x\rho\right) = \dfrac{\partial N}{\partial y} - \dfrac{\partial M}{\partial z}$, with $u_y\rho$ and $u_z\rho$ in the next two (p. 19). With charges coupled to small rigid bodies (ions, electrons) these are the electromagnetic basis of Lorentz's electrodynamics and optics of moving bodies. Transforming with lessons 6 and 10 gives equations of the same form in k, with (p. 20)

$$u_\xi = \frac{u_x - v}{1 - u_x v/c^2},\quad u_\eta = \frac{u_y}{\beta(1 - u_x v/c^2)},\quad u_\zeta = \frac{u_z}{\beta(1 - u_x v/c^2)},\quad \rho' = \beta\left(1 - \frac{u_x v}{c^2}\right)\rho \tag{14.1}$$

Since, by the addition theorem of lesson 9, $(u_\xi, u_\eta, u_\zeta)$ is nothing else than the velocity of the charge measured in k, this proves that the electrodynamic foundation of Lorentz's theory agrees with the principle of relativity. Moreover: if a charged body moves anywhere in space without altering its charge when regarded from a system moving with the body, its charge also remains constant when regarded from the stationary system K (p. 20).

**In professional terms:** Electric charge is Lorentz invariant; charge density transforms with the contraction factor and, together with the current density, forms the four-current, so the Maxwell–Lorentz equations with sources are Lorentz covariant.

**What it solves and what it is for**

With lesson 10, this completes the proof that the whole of Lorentz's electrodynamics, fields and moving charges, obeys the principle of relativity. The remaining question is mechanical: a charged particle in a field accelerates. How does a very fast particle respond to a force? Lesson 15 takes the cathode-ray tube aboard.

**Pros and cons**

Charges are fine. But Newton's $m\,\ddot{x} = $ force was written for slow bodies. For an electron moving at 0.6c, which "mass" should appear in it? Lesson 15.

### 15. The moving electron: longitudinal and transverse mass (p. 20–22)

**Why we need it**

In the laboratory car a cathode-ray tube shoots electrons at 0.6c along the track. An electric field then pushes one electron, once along its motion and once across it. For slow electrons Newton says acceleration = force / mass, the same in every direction. Is a fast electron equally easy to push along and across its motion?

**Work it out yourself**

Consider an electron of mass $m$ (its slow-motion mass) and charge $\varepsilon$ moving at $v = 0.6c$ along the $x$-axis. The paper finds, in the station system, $\dfrac{d^2x}{dt^2} = \dfrac{\varepsilon}{m\beta^3}X$ for a push along the motion.

> [!question]- Question 1: For an electron at rest, $\dfrac{d^2x}{dt^2} = \dfrac{\varepsilon}{m}X$. At $v = 0.6c$, what is $\beta^3$, and how does the acceleration compare with the resting one?
> $\beta^3 = 1.25^3 = 1.953125$; the acceleration is $1/1.953 \approx 0.51$ of the resting value.

> [!question]- Question 2: Let both pushes have the same size $F$ in the electron's own system (for the push along the motion $X' = X$, so $\varepsilon X = F$). Across the motion the paper's equation is $m\beta^2\,\dfrac{d^2y}{dt^2} = \varepsilon Y' = F$. Which push gives the larger acceleration in the station system?
> Along: $F/(m\beta^3) = F/(1.953\,m)$. Across: $F/(m\beta^2) = F/(1.5625\,m)$. Since $1.5625 < 1.953$, the sideways push gives the larger acceleration: the fast electron is harder to push along its motion than across it.

> [!question]- Question 3: If we keep "mass × acceleration = force", what "mass" must we assign for the push along the motion, and for the push across?
> Along: $m\beta^3 \approx 1.95\,m$ (the longitudinal mass). Across: $m\beta^2 \approx 1.56\,m$ (the transverse mass).

> [!tip] Cause and effect
> Write the slow-motion law in the electron's momentary rest system → transform to the station system → accelerations along and across the motion are reduced by different factors → with mass × acceleration = force, a fast electron has two different "masses".

**The concept from the paper**

Assume: if the electron is at rest at an instant, its motion in the next instant follows $m\,\dfrac{d^2x}{dt^2} = \varepsilon X$ (and likewise for $y, z$), $m$ being its mass as long as its motion is slow (p. 20–21). Now let it move with velocity $v$ along the $x$-axis at $t = 0$. It is then at rest in k, so, by the principle of relativity, for small $t$ it moves in k according to $m\,\dfrac{d^2\xi}{d\tau^2} = \varepsilon X'$, etc. Transforming with lessons 6 and 10 ($\xi = \beta(x - vt)$, …, $X' = X$, $Y' = \beta(Y - vN/c)$, $Z' = \beta(Z + vM/c)$) gives the paper's equations (A) (p. 21), numbered (15.1) here:

$$\frac{d^2x}{dt^2} = \frac{\varepsilon}{m\beta^3}X,\qquad \frac{d^2y}{dt^2} = \frac{\varepsilon}{m\beta}\left(Y - \tfrac{v}{c}N\right),\qquad \frac{d^2z}{dt^2} = \frac{\varepsilon}{m\beta}\left(Z + \tfrac{v}{c}M\right) \tag{15.1}$$

Written as $m\beta^3\,\ddot{x} = \varepsilon X'$, $m\beta^2\,\ddot{y} = \varepsilon Y'$, $m\beta^2\,\ddot{z} = \varepsilon Z'$: here $\varepsilon X', \varepsilon Y', \varepsilon Z'$ are the components of the force on the electron as viewed in a system moving with it (measurable, for example, by a spring balance at rest in that system). Calling this "the force acting upon the electron", keeping mass × acceleration = force, and measuring accelerations in K (p. 22):

$$\text{Longitudinal mass} = \frac{m}{\left(\sqrt{1 - v^2/c^2}\right)^3},\qquad \text{Transverse mass} = \frac{m}{1 - v^2/c^2} \tag{15.2}$$

With a different definition of force and acceleration one would naturally obtain other values, so different theories of the electron's motion must be compared very cautiously. Footnote 9: this definition of force is not advantageous, as M. Planck first showed; it is better to define force so that the laws of momentum and energy take the simplest form. The results also hold for ponderable material points, since any such point can be made an "electron" by adding an electric charge, no matter how small (p. 22).

**In professional terms:** Under the force measured in the instantaneous rest frame, a particle's acceleration in the lab frame is reduced by $\gamma^3$ along its velocity and by $\gamma^2$ across it; today one avoids "longitudinal/transverse mass" and uses relativistic momentum $\mathbf{p} = \gamma m\mathbf{v}$ with $\mathbf{F} = d\mathbf{p}/dt$.

**What it solves and what it is for**

This gives the first testable prediction for fast electrons, the kind produced in cathode-ray and β-ray experiments. It also shows why the paper is careful with words: "mass" in these formulas depends on how force is defined, as footnote 9 admits.

> [!warning] Common pitfall
> "Mass increases with speed" is a statement about these particular definitions, not a change in the electron itself. The paper says explicitly that other definitions give other values; the modern habit is to keep $m$ fixed and let momentum and energy carry the $\gamma$ factors.

**Pros and cons**

The masses say how hard the electron is to push. The practical question for an experimenter is how much energy the push costs, and what can be measured in a tube. Lesson 16 finishes the paper.

### 16. Kinetic energy and three testable predictions (p. 22–24)

**Why we need it**

The cathode-ray tube accelerates electrons from rest through a voltage. Newton says the kinetic energy is $\tfrac12 mv^2$, so a big enough voltage could push an electron past $c$. Lesson 7 said speeds above $c$ make the theory meaningless. The energy formula must change too.

**Work it out yourself**

The paper's result is $W = mc^2\left(\dfrac{1}{\sqrt{1 - v^2/c^2}} - 1\right) = mc^2(\beta - 1)$.

> [!question]- Question 1: At $v = 0.6c$, what is $W$ in units of $mc^2$, and what does Newton's $\tfrac12 mv^2$ give?
> $W = mc^2(1.25 - 1) = 0.25\,mc^2$; Newton gives $\tfrac12 \times 0.36 = 0.18\,mc^2$.

> [!question]- Question 2: At $v = 0.1c$: $\beta = 1/\sqrt{0.99} \approx 1.00504$. What are the two energies?
> Einstein: $0.00504\,mc^2$; Newton: $0.005\,mc^2$. At everyday and even at rather high speeds the two agree.

> [!question]- Question 3: What happens to $W$ as $v$ approaches $c$?
> $\beta$ grows without bound, so $W$ becomes infinite: no finite energy brings the electron to $c$.

> [!tip] Cause and effect
> Energy = work of the force along the path, with the longitudinal law of lesson 15 → $W = mc^2(\beta - 1)$, which matches Newton at low speed → the energy diverges at $c$, so no body reaches the speed of light.

![[Lecture Notes/Example for skill/attachments/specrel-1905-anim-energy.svg]]
*Figure 16.1 · own diagram · Kinetic energy in units of $mc^2$ against $v/c$: follow the two dots — they stay together at low speed, separate to 0.25 versus 0.18 at 0.6c, and Einstein's curve shoots up at the red line $v = c$.* (If the animation does not play, questions 1–3 give the same numbers.)

**The concept from the paper**

An electron moves from rest at the origin along the $x$-axis under an electrostatic force $X$. Being slowly accelerated, it radiates no energy, so the energy withdrawn from the field, $\int \varepsilon X\,dx$, equals its energy of motion $W$. Using the first equation of (15.1) (p. 22–23):

$$W = \int \varepsilon X\,dx = m\int_0^v \beta^3 v\,dv = mc^2\left(\frac{1}{\sqrt{1 - v^2/c^2}} - 1\right) \tag{16.1}$$

When $v = c$, $W$ becomes infinite: velocities greater than that of light have "no possibility of existence". By the argument of lesson 15, the expression applies to ponderable masses as well.

The paper then lists the properties of the electron's motion that follow from (15.1) and "are accessible to experiment" (p. 23):

1. An electric force $Y$ and a magnetic force $N$ have equally strong deflecting action on an electron moving with velocity $v$ when $Y = Nv/c$. So the velocity follows from the ratio of the magnetic power of deflexion $A_m$ to the electric power of deflexion $A_e$, for any velocity: $A_m/A_e = v/c$. This can be tested, since the electron's velocity can be measured directly (for example with rapidly oscillating electric and magnetic fields).
2. Between the potential difference $U$ traversed (the paper writes $P$) and the velocity acquired: $U = \int X\,dx = \dfrac{m}{\varepsilon}\,c^2\left(\dfrac{1}{\sqrt{1 - v^2/c^2}} - 1\right)$.
3. In a magnetic force $N$ perpendicular to the velocity (the only deflecting force), the radius of curvature $R_\text{curv}$ of the path (the paper writes $R$) follows from $-\dfrac{d^2y}{dt^2} = \dfrac{v^2}{R_\text{curv}} = \dfrac{\varepsilon}{m}\,\dfrac{v}{c}\,N\sqrt{1 - \dfrac{v^2}{c^2}}$, i.e. $R_\text{curv} = \dfrac{mc^2}{\varepsilon}\cdot\dfrac{v/c}{\sqrt{1 - v^2/c^2}}\cdot\dfrac{1}{N}$.

These three relations are a complete expression of the laws by which, according to the theory, the electron must move. The paper closes by thanking "my friend and colleague M. Besso" for loyal assistance and several valuable suggestions (p. 23). Page 24 is the editor's note on this edition: the English translation of 1923 (Methuen), in the public domain; numbered footnotes are from 1923, editor's notes are marked †; the 1923 translation uses $c$ where Einstein in 1905 wrote $V$; the edition was prepared by John Walker (fourmilab.ch).

**In professional terms:** The relativistic kinetic energy is $K = (\gamma - 1)mc^2$, reducing to $\tfrac12 mv^2$ for $v \ll c$ and diverging as $v \to c$; the cyclotron radius is $r = \gamma m v c/(eB)$ in Gaussian units.

**What it solves and what it is for**

This closes the circle opened by lesson 7's remark that $c$ plays the part of an infinite velocity: now we see why, since reaching it would take infinite energy. The three predictions turn the theory into experiments on cathode rays and β-rays. For example, at $0.6c$ prediction 3 gives a radius $(v/c)\beta = 0.75$ in units of $mc^2/(\varepsilon N)$, where Newton's mechanics would give $0.6$: 25 % larger.

> [!info]- Supplement: the sequel, E = mc²
> A few months later Einstein published a three-page follow-up, "Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?" ("Does the inertia of a body depend upon its energy content?"). Using the results of this paper on the energy of light, he concluded: "If a body gives off the energy L in the form of radiation, its mass diminishes by L/c²", and "the mass of a body is a measure of its energy-content." The $mc^2$ in equation (16.1) is the first appearance of that combination.
> Sources: [Einstein, 1905b]

**Pros and cons**

The paper gives a complete, self-consistent kinematics and electrodynamics from two postulates, and its predictions can be tested. Its limits are its own: the force definition behind the two masses is admitted to be awkward (Planck's remark), the argument covers uniform motion only, and gravity is absent — which is exactly where lesson 8's equator-clock prediction needed correcting.

> [!question]- Pause: Lessons 12 and 13 both used the phrase "transform to the rest system of the body". Why is that the key method of the whole electrodynamical part?
> Because in the body's rest system only the laws for bodies at rest are needed, which were already known (reflection at a resting mirror, the slow electron's $m\ddot{x} = \varepsilon X$, a resting charge feeling only electric force). The principle of relativity guarantees those laws hold in that system; the Lorentz transformation (6.3) and the field transformation (10.1) then carry the result back to the station.

## Part 3 · Review and practice

### Summary

| Concept | In one sentence | Key formula |
| --- | --- | --- |
| Two postulates | Same laws in all uniformly moving systems; light at $c$ regardless of its source | lesson 1, 3 |
| Synchronisation | Distant clocks agree if light's out and back trips take equal times | $t_B - t_A = t'_A - t_B$, (2.1) |
| Relativity of simultaneity | Clocks synchronous for the station are not for the train | $r_{AB}/(c - v)$ vs $r_{AB}/(c + v)$, (4.1) |
| Lorentz transformation | The dictionary between station and train co-ordinates | $\tau = \beta(t - vx/c^2)$, $\xi = \beta(x - vt)$, (6.3) |
| Length contraction | Moving bodies are shorter along their motion | $R\sqrt{1 - v^2/c^2}$, (7.2) |
| Time dilation | Moving clocks run slow | $\tau = t\sqrt{1 - v^2/c^2}$, (8.1) |
| Velocity addition | Speeds combine below $c$; $c$ stays $c$ | $(v + w)/(1 + vw/c^2)$, (9.3) |
| Field transformation | Electric and magnetic forces mix between systems | $Y' = \beta(Y - vN/c)$, (10.1) |
| Electromotive force | The electric force in the charge's own rest system | lesson 11 |
| Doppler and aberration | Exact for any speed, from one transformation | (12.2), (12.3) |
| Light energy and pressure | Energy changes like frequency; pressure by energy balance | (13.1), (13.2) |
| Convection currents | Charge is invariant; Lorentz's theory obeys relativity | $\rho' = \beta(1 - u_xv/c^2)\rho$, (14.1) |
| Electron masses | Harder to push along the motion than across it | $m\beta^3$, $m\beta^2$, (15.2) |
| Kinetic energy | Diverges at $c$; matches Newton at low speed | $mc^2(\beta - 1)$, (16.1) |

### Exercises

#### Exercise 1 · Synchronising a third station
Station D lies 150 km from A. A sends a light signal at A-time 5.0 ms. At what A-time does it come back, and what must D's clock read at the reflection?

> [!success]- Show answer
> 150 km takes $150/300 = 0.5$ ms each way. Back at A at $5.0 + 1.0 = 6.0$ ms; D must read the midpoint, $5.5$ ms.

#### Exercise 2 · Why "by definition"?
Why does lesson 2's rule define equal one-way light times instead of measuring them?

> [!success]- Show answer
> To measure a one-way time you need two synchronised clocks at the two ends, and synchronising them is exactly what the rule is for. Without a definition the comparison of an A time with a B time has no meaning (p. 3).

#### Exercise 3 · Simultaneity on a slower train
A different train, 240 km long as measured from the platform, runs at $v = 0.2c = 60$ km per ms. How long does light take from rear to front, and separately from front back to rear, in station time?

> [!success]- Show answer
> Forward: $240/(300 - 60) = 1$ ms. Back: $240/(300 + 60) = 2/3 \approx 0.67$ ms. Still unequal, so simultaneity still differs, just less.

#### Exercise 4 · Transform an event
An event has station co-ordinates $x = 600$ km, $t = 1$ ms. With $v = 0.6c$, find $\xi$ and $\tau$.

> [!success]- Show answer
> $\xi = 1.25 \times (600 - 180) = 525$ km. $vx/c^2 = 180 \times 600/90{,}000 = 1.2$ ms, so $\tau = 1.25 \times (1 - 1.2) = -0.25$ ms: the k-system clock at $\xi = 525$ km (imagine the train's line of synchronised clocks extended beyond its front) reads $-0.25$ ms, i.e. earlier in train time than the moment the rear passed station A ($\tau = 0$).

#### Exercise 5 · Contraction at 0.8c
The express (300 km at rest) runs at $0.8c$. What is $\beta$, and how long is the train for the stationmaster?

> [!success]- Show answer
> $1 - 0.64 = 0.36$, $\sqrt{0.36} = 0.6$, $\beta = 1/0.6 = 5/3$. Length $300 \times 0.6 = 180$ km.

#### Exercise 6 · The travelled clock
A clock travels from A to B (300 km) at 0.6c and is compared with B's clock on arrival. Exactly how far behind is it? What does the paper's approximation $\tfrac12 tv^2/c^2$ give?

> [!success]- Show answer
> Travel time $300/180 = 5/3$ ms. The travelled clock shows $0.8 \times 5/3 = 4/3$ ms, so it lags by $1/3 \approx 0.333$ ms. The approximation gives $\tfrac12 \times \tfrac53 \times 0.36 = 0.3$ ms; the difference is the fourth-order terms the paper neglects, large at this speed.

#### Exercise 7 · Velocity addition backwards
The conductor throws the ball **backwards** at $w = -0.6c$ relative to the train ($v = 0.6c$). What speed does the stationmaster see?

> [!success]- Show answer
> $V = (0.6c - 0.6c)/(1 - 0.36) = 0$: the ball stands still on the platform, as Galileo's rule also says in this case.

#### Exercise 8 · Why not v + w?
Explain in two sentences why $v + w$ fails, using lessons 4 and 7.

> [!success]- Show answer
> The ball's speed relative to the train is measured with the train's rods and clocks, which the station finds shortened, slow and differently synchronised. Converting that measurement into station rods and clocks with the Lorentz transformation gives $(v + w)/(1 + vw/c^2)$, not the plain sum.

#### Exercise 9 · Fields from the train
In the station there is a pure electric force $Y = 1$ (no magnetic force). What magnetic force $N'$ does the passenger measure at 0.6c?

> [!success]- Show answer
> $N' = \beta(N - \tfrac{v}{c}Y) = 1.25 \times (0 - 0.6) = -0.75$ units. A passenger moving through a pure electric field measures a magnetic field too: the mirror image of lesson 10.

#### Exercise 10 · Doppler at 0.8c
The express runs away from the platform lamp at $0.8c$. What frequency does the passenger see?

> [!success]- Show answer
> $\nu' = \nu\sqrt{0.2/1.8} = \nu\sqrt{1/9} = \nu/3$.

#### Exercise 11 · Energy and frequency
A light packet has energy $E$ and frequency $\nu$ on the platform. The train approaches the lamp head-on at 0.6c. What energy does the passenger assign to the packet?

> [!success]- Show answer
> Energy changes like frequency (lesson 13): the frequency doubles (lesson 12), so $E' = 2E$.

#### Exercise 12 · Pushing a fast electron
At $v = 0.8c$ ($\beta = 5/3$), what are the longitudinal and transverse masses in units of $m$?

> [!success]- Show answer
> $\beta^3 = 125/27 \approx 4.63$ and $\beta^2 = 25/9 \approx 2.78$.

#### Exercise 13 · How much energy?
What kinetic energy, in units of $mc^2$, does an electron need to reach $0.8c$? Compare with Newton.

> [!success]- Show answer
> $W = mc^2(5/3 - 1) = \tfrac23\,mc^2 \approx 0.667\,mc^2$; Newton: $\tfrac12 \times 0.64 = 0.32\,mc^2$, less than half.

#### Exercise 14 · Connecting ideas: the magnet and the coil
Use lessons 10 and 11 to explain why lesson 1's two cases (coil moving, or magnet moving) must give the same current.

> [!success]- Show answer
> In both cases, go to the coil's rest system. There the magnet moves past with the same velocity, so the fields at the coil, obtained from the magnet's own field by the same transformation (10.1), are the same, and the charges at rest in the coil feel the same electric force. Same force, same current; the distinction between "moving magnet" and "moving conductor" was never physical.

### Glossary

| Term | Meaning in one sentence |
| --- | --- |
| stationary system (K) | The system of co-ordinates in which Newton's mechanics holds and the station clocks are synchronised; here, the platform |
| moving system (k) | A system in uniform translation relative to K; here, the express |
| synchronous clocks | Clocks for which light's out and back trips take equal times by the lesson-2 rule (the paper's §1) |
| principle of relativity | The laws of physics are the same in all systems in uniform translatory motion |
| constancy of the velocity of light | In the stationary system every light ray moves at $c$, whatever emits it |
| luminiferous ether | The hypothetical light medium at absolute rest, made superfluous by the paper |
| relativity of simultaneity | Events simultaneous in one system are not simultaneous in another moving relative to it |
| Lorentz transformation | The equations (6.3) turning $x, y, z, t$ into $\xi, \eta, \zeta, \tau$ |
| $\beta$ (paper) / Lorentz factor $\gamma$ (modern) | $1/\sqrt{1 - v^2/c^2}$, 1.25 at $0.6c$ |
| length contraction | A moving body is shortened along its motion by $\sqrt{1 - v^2/c^2}$ |
| time dilation | A moving clock runs slow by the factor $\sqrt{1 - v^2/c^2}$ |
| velocity addition | $V = (v + w)/(1 + vw/c^2)$ for parallel velocities |
| group (of transformations) | Composing two transformations of this kind gives another of the same kind |
| electric force / magnetic force | $(X, Y, Z)$ and $(L, M, N)$: force on a unit charge or unit pole |
| electromotive force | The old name for the extra force on a moving charge; really the electric force in its rest system |
| Doppler's principle | The change of observed frequency with the observer's motion |
| aberration | The change of the observed direction of light with the observer's motion |
| radiation pressure | The push of light on a surface, here on a moving mirror |
| convection current | Electric current carried by moving charged bodies |
| longitudinal / transverse mass | The "mass" for a push along / across the motion, $m\beta^3$ and $m\beta^2$ |
| kinetic energy | Energy of motion, $mc^2(\beta - 1)$ |

> [!tip] Self-check after studying
> **Can compute:** synchronise two clocks from three readings; transform an event with (6.3); contract a length and slow a clock at a given speed; add two velocities; transform $Y$ and $N$ to a moving system; Doppler-shift a frequency; the longitudinal and transverse mass; the kinetic energy at a given speed.
> **Can explain:** why simultaneity needs a definition; why it differs between systems; why nothing reaches $c$; what the "electromotive force" really is; why lesson 1's asymmetry disappears.
> **Can connect:** synchronisation → relativity of simultaneity → Lorentz transformation → contraction, dilation, velocity addition → field transformation → Doppler, light energy, electron dynamics.

## References

- [Einstein, 1905b] Einstein, A. (1905). Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig? *Annalen der Physik*, 323(13), 639–641. https://doi.org/10.1002/andp.19053231314 (English translation: https://www.fourmilab.ch/etexts/einstein/E_mc2/www/)
- [Hafele & Keating, 1972] Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: Observed relativistic time gains. *Science*, 177(4044), 168–170. https://doi.org/10.1126/science.177.4044.168
- [Harvey & Schucking, 2005] Harvey, A., & Schucking, E. (2005). A small puzzle from 1905. *Physics Today*, 58(3), 34–36. https://doi.org/10.1063/1.1897562
- [Michelson & Morley, 1887] Michelson, A. A., & Morley, E. W. (1887). On the relative motion of the Earth and the luminiferous ether. *American Journal of Science*, s3-34(203), 333–345. https://doi.org/10.2475/ajs.s3-34.203.333
