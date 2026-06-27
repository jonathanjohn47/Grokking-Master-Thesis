---
tags: [learning-path, grokking, dynamics]
---
← Previous: [[01 - What Is Grokking]]  ↑ Parent: [[00 - Start Here]]  → Next: [[03 - Historical Background]]

# 02 - The Grokking Training Dynamics

## What Is This?

Grokking is not a single moment. It is a journey with three distinct chapters.

When a neural network is training, you can watch three completely different phases unfold — one after another — like a story with a beginning, a middle, and a dramatic ending.

This note explains what happens in each phase, and more importantly, what is changing *inside* the network even when the outside appears completely frozen.

---

## Why Does Grokking Have These Phases?

Before we explain what happens, let's understand *why* there are phases at all.

A neural network faces a strange puzzle during training:
- There is a **fast solution**: memorise everything you have seen. This works immediately.
- There is a **slow solution**: learn the underlying rule. This takes much longer to build.

The network starts by taking the fast path (memorisation). But there is a force quietly pushing it toward the slow path (generalisation) — and this force is called [[Weight Decay]].

This creates a competition inside the network. The slow, correct solution has to build up its strength while the fast, wrong solution gradually weakens. This competition unfolds in three stages.

---

## The Three Phases of Grokking

### Phase 1 — Memorisation (This Happens Fast)

This is the first chapter. The network learns to remember.

**What you observe:**
- **Training score:** Jumps from nearly 0% to around 100% within the first few training steps.
- **Test score:** Stays at random guessing level (about 50% for a two-choice problem, for example).
- **Graph appearance:** Training loss drops like a stone. Test loss barely moves.

**What is actually happening inside:**

The network is building a **giant lookup table** — like a filing cabinet with millions of tiny drawers. Each drawer stores one answer.

For example, if the network is learning modular arithmetic (like "what is 7 + 5 in mod 11?"), it stores:
- Drawer 1: "7 + 5 → 1"
- Drawer 2: "3 + 9 → 1"  
- Drawer 3: "4 + 8 → 1"
- ...and so on for every training example

The network can now answer every single training question perfectly. But it has not learned the underlying rule ("add the numbers, then find the remainder when divided by 11").

> [!ANALOGY]
> Imagine a student who photocopies the answers to every past exam question. When the same questions appear on the real exam, they score 100%. But if the exam has any new question — even a slight variation — they fail completely.

**This is memorisation, not understanding.**

---

### Phase 2 — The Plateau (Long, Silent, and Deceptive)

This is the most mysterious phase. From the outside, it looks like nothing is happening.

**What you observe:**
- **Training score:** Stays stuck at around 100%. Completely flat.
- **Test score:** Stays at random guessing level. Completely flat.
- **Graph appearance:** Both curves are horizontal lines. No movement whatsoever.
- **Time duration:** This can last for thousands of training steps. Sometimes tens of thousands.

**What it looks like:**

The network appears completely frozen. A researcher looking at the performance graph would think training has stalled. Perhaps there is a bug. Perhaps this task is impossible.

> [!WARNING]
> This is where many experiments fail. Researchers see flat performance and stop training, thinking "nothing is happening." They never discover grokking because they quit too early.

**What is actually happening inside (the invisible drama):**

While the performance scores stay flat, something profound is changing inside the network.

Remember the "filing cabinet" lookup table from Phase 1? That solution uses enormous, bulky weights — like a massive library storing every answer on separate shelves.

There is now a **competing solution building in the shadows**: a small, elegant circuit that actually understands the rule.

This new circuit is being constructed piece by piece, while [[Weight Decay]] is slowly **squeezing the network** to abandon the bulky memorisation solution.

**Weight Decay** works like this:
- At every training step, the network is gently encouraged to make all its internal numbers slightly smaller.
- This pressure is constant and relentless.
- It is not enough to destroy the memorisation solution immediately. But it slowly, steadily weakens it.

Think of it as a slow erosion. Drop by drop, the memorisation solution loses its strength. Meanwhile, the generalisation solution builds up its strength.

> [!TIP]
> Weight decay is not random pressure. It is specifically designed to favor compact solutions over bulky solutions. A solution that memorises requires large weights (a fat filing cabinet). A solution that understands rules requires fewer, more efficient weights (a concise algorithm).

**Why is this phase so long?**

The memorised solution got a huge head start. It was fully formed by the end of Phase 1. The generalisation solution is being built from scratch.

Under weight decay's slow pressure, the generalisation solution gradually gains strength. But it takes a very long time to build up enough strength to compete with the solution that already dominated the network.

This is the core reason for the long plateau: **two solutions are competing, and the slower-but-better solution needs time to mature**.

> [!QUESTION]
> How do researchers know that something is actually happening during the plateau? They look *inside* the network at the weights, gradients, and activations — not at the external performance scores. This is what [[Grokking Predictors]] try to do.

---

### Phase 3 — Grokking (The Breakthrough Moment)

After the long, silent plateau, something dramatic happens.

**What you observe:**
- **Training score:** Stays at around 100%. (No change — it was already perfect from Phase 1.)
- **Test score:** Explodes upward from random guessing (~50%) to near-perfect (~99%) in just a few hundred training steps.
- **Graph appearance:** The test curve, which was flat and useless, suddenly shoots upward like a rocket.
- **Duration of the jump:** Very fast — perhaps 500 to 1000 training steps.

**What happened:**

The generalisation solution — the one that was quietly building during the plateau — finally became strong enough to take over.

The [[Weight Decay]] pressure has done its job. The memorisation solution is now so weak that the network's outputs are dominated by the generalisation solution.

**The network has now truly learned the rule.** It can answer questions it has never seen before.

> [!NOTE]
> This jump is *abrupt*. There is no gradual learning curve. The test performance stays flat, then suddenly explodes upward. This explosive, sudden transition is the defining characteristic of grokking. It is not a normal learning curve.

**A concrete example:**

Imagine a network learning "modular arithmetic mod 11". During Phase 1, it memorises patterns like:
- 7 + 5 = 1 (because 12 mod 11 = 1)
- 3 + 9 = 1 (because 12 mod 11 = 1)
- 6 + 6 = 1 (because 12 mod 11 = 1)

It looks like the network is learning random facts.

During Phase 2, the network is building a circuit that computes the actual rule: "add the numbers, divide by 11, take the remainder."

At the grokking moment (Phase 3), this circuit takes over completely. Now the network can compute:
- 2 + 4 = 6 ✓ (correct, never seen before)
- 8 + 7 = 4 ✓ (correct, never seen before)  
- 10 + 10 = 9 ✓ (correct, never seen before)

The rule is now active. The memorisation is now dormant.

> [!TIP]
> Grokking is dramatic because it feels like a sudden understanding. But in reality, the understanding was being built all along, during the seemingly-frozen plateau. Grokking is the moment when that understanding finally becomes strong enough to matter.

---

## Quick Reference: The Three Phases at a Glance

| Phase | Duration | Training Score | Test Score | Internal Event |
|-------|----------|----------------|------------|-----------------|
| **1 — Memorisation** | Fast (seconds to minutes) | Rises to ~100% | Stays near 0% | Lookup table being constructed |
| **2 — Plateau** | Slow (thousands of steps) | Stays at ~100% | Stays near 0% | Weight decay erodes memorisation; rule circuit builds silently |
| **3 — Grokking** | Rapid (hundreds of steps) | Stays at ~100% | Shoots to ~100% | Rule circuit becomes dominant and takes control |

---

## The Fundamental Question: Why Is There a Plateau?

This is worth asking directly: **Why doesn't the network just learn the rule from the beginning?**

The answer is about **complexity and efficiency**:

- **The memorisation solution is easy to find.** It requires no insight into the problem. Just store every answer.
- **The generalisation solution is hard to find.** It requires discovering the underlying pattern, which demands both internal computation and understanding.

During training, the network takes the path of least resistance: memorisation.

But memorisation is expensive (it requires many large weights). [[Weight Decay]] penalizes this expense, slowly making the network abandon the bulky solution and adopt the lean, efficient rule.

The plateau is simply the time it takes for this competition to unfold:
- The **memorisation solution** (lookup table) is a fast runner who gets out ahead immediately.
- The **generalisation solution** (the actual rule) is a slow but efficient runner.
- Under weight decay pressure, the slow runner gradually gains ground during the plateau.
- Eventually, the efficient runner overtakes the fast runner — and that is the grokking moment.

> [!TIP]
> Researchers discovered that this kind of "long but finite plateau" is not unique to grokking. Even in the simplest possible networks (called linear networks), mathematicians proved in 1991 that you can have very long plateaus followed by sudden improvement. Grokking is an extreme version of something that has always been possible.

The plateau is not a failure of learning. It is a reflection of the **difficulty of finding a good general rule** versus the **ease of memorising specific answers**.

---

## The Plateau Is Invisible From the Outside

Here is the core problem: **nothing you can measure from outside tells you that something is changing.**

If you only look at training and test scores (the standard way researchers monitor neural networks), the plateau looks like complete stagnation.

A normal training curve looks like this:
- Error gets smaller over time (smooth downward curve).
- You can predict when training is done (error stops improving).

But grokking looks like this:
- Error drops fast (Phase 1).
- Error stays flat for a very long time (Phase 2).
- Error suddenly drops again (Phase 3).

**The plateau breaks normal intuition.** If you train a network for 10,000 steps and it shows no improvement after step 2,000, you would normally say "training is done, stop." But grokking says "wait another 8,000 steps and something dramatic will happen."

**How do researchers know grokking is coming?**

They must look *inside* the network at measurements that are invisible from the outside:
- **Weights:** The internal numbers are changing during the plateau, slowly shifting from the memorisation solution toward the generalisation solution.
- **Gradients:** The direction and magnitude of change is shifting.
- **Activations:** The patterns of internal computation are reorganizing.

This is the entire purpose of [[Grokking Predictors]] research — to find internal signals that change during the plateau, giving advance warning that grokking is approaching.

> [!QUESTION]
> Could we have predicted the grokking moment if we had looked at the right internal signals?
> 
> That is the research question. The answer appears to be **yes** — multiple predictor methods have found success in detecting pre-grokking signals.

---

## The Dark Twin: Anti-Grokking

There is a disturbing phenomenon called **[[Anti-Grokking]]** that can happen after grokking.

**What is it?**

After a network has grokked and learned to generalise, if you keep training long enough, something tragic can happen:

- The test score suddenly **collapses**.
- The network goes back to failing on new questions.
- It has *forgotten* the rule it just learned.
- The memorisation solution reactivates.

This is the reverse of grokking. It is learning followed by unlearning.

**Why does anti-grokking happen?**

This is an active area of research. One theory is that extreme [[Weight Decay]] can eventually damage even the generalisation solution, pushing the network to find some other way to fit the training data.

Or the winner could change. If conditions during training shift enough — maybe the learning rate changes, or the data pattern changes — memorisation might suddenly become the better solution again. Even though generalisation was winning just moments before.

**Why does this matter?**

Anti-grokking makes the prediction problem *much harder*:
- We need to find signals that predict when grokking is approaching.
- We also need to find signals that predict when anti-grokking is approaching.
- These might require completely different detection methods.

This adds another layer of complexity to understanding neural network training dynamics.

> [!WARNING]
> Not all [[Grokking Predictors]] account for anti-grokking. Many assume that once grokking happens, generalisation is stable. But the presence of anti-grokking challenges this assumption.

---

## Important Terms

**Memorisation:**
The act of storing individual facts without understanding the underlying pattern. A memorised solution requires the network to store many large internal numbers (weights) — like a filing cabinet with a drawer for every answer.

**Generalisation:**
The act of discovering and applying a general rule that works for any input. A generalised solution is compact and efficient — like an algorithm.

**[[Weight Decay]]:**
A technique that gently penalizes large weights at every training step. Think of it as a constant pressure pushing the network toward simpler, more efficient solutions. It is the force that makes memorisation increasingly expensive over time.

**Weights (or parameters):**
The millions (or billions) of small numbers inside a neural network. Training adjusts these numbers so the network performs better. A weight can be thought of as a connection strength between neurons.

**Gradients:**
Measurements of how much each weight should change to reduce the network's error. Gradients point in the direction of improvement.

**Activations:**
The values produced inside the network as it processes an input. By examining activations, researchers can see what internal computations are happening and which parts of the network are "active" for different tasks.

**Loss or Loss Curve:**
A measurement of how wrong the network is on average. A loss curve is a graph of this error over training time. During the plateau, the loss curve appears flat because performance is not changing, even though the internal structure is.

**[[Anti-Grokking]]:**
The reverse of grokking. A network that has learned to generalise can suddenly regress, going back to memorisation or failing entirely. The test score collapses after it had recovered.

---

## Key Takeaways

- **Grokking has three distinct phases:** fast memorisation (Phase 1), a long silent plateau (Phase 2), and a sudden breakthrough to generalisation (Phase 3).

- **Two solutions compete inside the network:** a bulky memorisation solution (a filing cabinet) and a compact generalisation solution (an algorithm).

- **The plateau is not stagnation — it is hidden progress.** Both solutions are changing during the plateau, even though external scores are frozen.

- **[[Weight Decay]] is the mechanism.** It slowly squeezes the network to abandon bulky solutions and adopt efficient ones. This pressure tips the balance from memorisation toward generalisation.

- **The plateau is a measurement blind spot.** Standard training graphs (loss curves) tell you nothing during Phase 2. You must look inside the network at weights, gradients, or activations to detect pre-grokking signals.

- **Grokking feels sudden because it is sudden.** But the sudden transition is only the visible moment when internal changes finally become strong enough to show up in test performance.

- **[[Anti-Grokking]] adds complexity.** After grokking, training can reverse course. The network can forget its learned rule and regress to memorisation or complete failure.

---

## Related Notes
- [[Grokking]] · [[Anti-Grokking]]
- [[09 - Weight Decay and Regularization]]
- [[10 - Mechanistic Explanations and Circuit Formation]]
- [[What Causes Grokking]] · [[Role of Weight Decay]]
