---
tags: [learning-path, history]
---
← Previous: [[02 - The Grokking Training Dynamics]]  ↑ Parent: [[00 - Start Here]]  → Next: [[04 - Core Experimental Setup]]

# 03 - Historical Background

## What Is This Note About?

Grokking was officially named and described in 2022. But the ideas behind it did not appear from nowhere.

For decades before 2022, researchers were puzzling over a related mystery: **why do large neural networks — which have far more capacity than they need — still learn to generalise correctly?** Classical statistics said they should fail. They didn't.

This note traces the history of that puzzle, and shows how grokking is the latest chapter in a long story.

---

## The Central Puzzle That Set the Stage

Here is the classical prediction from statistics:

> If a model has more adjustable parameters than it has training examples, it will simply memorise the training data and fail on anything new.

This seemed reasonable. If you have enough flexibility, you can memorise anything — but memorisation is not the same as understanding.

But in the 2010s, researchers noticed something strange: **huge neural networks were memorising the training data AND still generalising correctly to new examples**.

How could that be?

One famous experiment made this explicit: researchers trained networks on completely **random labels** — where every image was assigned a random, meaningless category. The network memorised these random labels perfectly. But the same type of network, trained on real data with real labels, also generalised correctly.

This seemed contradictory. The same network can memorise nonsense, and yet somehow also learn meaningful structure.

> [!NOTE]
> This paradox — that large networks can memorise anything, yet still generalise on real tasks — is the deep question that grokking research is trying to understand. Grokking is a controlled, small-scale version of this exact puzzle.

---

## Key Milestones in the History

### 1991 — The First Hint: Long Plateaus in Simple Networks

The earliest ancestor of grokking was discovered in 1991 by researchers studying the simplest possible neural networks (called linear networks).

They proved mathematically that even these simple networks can show:
- Long periods where performance looks completely flat
- Multiple moments where the network seems to reach a local best, then suddenly improves
- A specific optimal moment to stop training

This was remarkable: even the simplest networks can have "stuck" phases that are not really stuck — something is building up underneath.

Grokking is the dramatic, extreme version of this same behaviour.

---

### 2017 — Large Networks Do Not Overfit Like They Should

A landmark paper showed that deep neural networks can fit completely random data to perfect accuracy, yet still generalise on real data.

This was the clearest possible demonstration that the classical rule ("too many parameters = overfitting") was wrong for these networks.

The mystery of why big networks generalise — instead of memorising — became a central question in machine learning research.

---

### 2017 — Sharp Transitions in Learning (Statistical Physics)

Researchers from physics brought a new tool: **phase transitions**.

A phase transition is like water freezing — the temperature crosses a threshold, and the system suddenly switches from one state (liquid) to a completely different state (solid).

These researchers found that in learning systems, there are similar sharp thresholds. Below a certain number of training examples, a model completely fails to learn. Above that threshold, it suddenly succeeds. There is no gradual middle ground.

This "all-or-nothing" pattern is closely related to what we see in grokking, where test accuracy jumps suddenly from near 0% to near 100%.

---

### 2018 — Gradient Descent Protects Against Overfitting

Researchers discovered that the training process itself (called gradient descent) acts as a kind of built-in protection against overfitting, even without any explicit rules telling it to.

In a big overparameterised network, gradient descent tends to find solutions that are simpler and more efficient — not just any solution that fits the data, but the **simplest** one.

This is important for grokking: it helps explain why the network eventually drifts from the memorised solution (complex, large) to the generalised solution (simpler, smaller).

---

### 2018 — The Boundary Between "Too Small" and "Too Large"

Researchers from physics found that the critical point where a network goes from too small (cannot memorise the data) to large enough (can memorise the data) behaves like a physical phase transition.

Right at this boundary, something unusual happens: test error peaks sharply before falling again. This is closely related to the "double descent" phenomenon described in the next note.

---

### 2020 — Structure Keeps Forming After Perfect Accuracy

A key discovery: even after a network has reached perfect accuracy on its training data, the network's internal structure **keeps changing and becoming more organised**.

Researchers found that the network's hidden representations of different classes converge to a very specific, geometrically beautiful arrangement. This keeps happening even after training accuracy cannot get any better.

This was crucial for understanding grokking: the "silent" plateau phase is not empty. Structure is forming. The network is reorganising itself, even though the scores are not moving.

---

### 2022 — Grokking Is Named

In 2022, a team at OpenAI (Power et al.) trained small transformer models on simple arithmetic tasks (like clock math) and made the grokking observation explicit for the first time.

They showed:
- Training accuracy hits 100% quickly
- Test accuracy stays near 0% for a very long time
- Then test accuracy jumps to near 100%

They gave this phenomenon the name "grokking" and showed it was reproducible and could be studied scientifically.

---

### 2023 — What Is Happening Inside

After 2022, researchers began asking: **what is the network actually doing during the plateau?**

A team (Nanda et al.) reverse-engineered the grokked network and found it had built a specific, elegant computational structure — like a miniature gear mechanism — that computes the correct answer using mathematical patterns related to waves and rotations.

Another team (Varma et al.) showed why this structure eventually wins: it is more **efficient** than the memorised solution. The rule-based solution can do the same job with fewer resources, so a training process that rewards efficiency will eventually prefer it.

---

## A Simple Timeline

| Year | Discovery |
|------|-----------|
| 1991 | Simple networks can show long plateaus before improving — the first ancestor of grokking |
| 2017 | Large networks memorise random data yet still generalise on real data — the central paradox |
| 2017 | Sharp "all-or-nothing" transitions discovered in learning — connected to grokking's sudden jump |
| 2018 | Training process itself provides built-in protection against overfitting |
| 2018 | Critical boundary between "too small" and "too large" networks behaves like a physical transition |
| 2020 | Structure keeps forming after perfect accuracy — the plateau is not empty |
| 2022 | Grokking officially named and studied on clock-math tasks |
| 2023 | The mechanism inside a grokked network is reverse-engineered |
| 2024–2025 | New early-warning signals proliferate; grokking found in non-neural-network systems |
| 2026 | The thesis proposes the first fair comparison of all early-warning signals |

---

## Why This History Matters

Understanding this history helps you see grokking not as a strange isolated quirk, but as a **clear, small-scale example of questions that have occupied researchers for decades**:

- Why do large networks generalise?
- When does learning happen in jumps rather than gradually?
- What is a network secretly doing during a "stuck" phase?
- What is the simplest possible controlled setting to study these questions?

Grokking answers all four: it is a **clean, reproducible, fully observable case** of generalisation emerging after apparent stagnation, in a system small enough to inspect completely.

---

## Important Terms

**Overfitting:** When a network memorises the training data so closely that it fails on any new data. Like a student who memorises past exams but cannot answer new questions.

**Generalisation:** When a network learns the underlying rule and can correctly answer new questions it has never seen.

**Parameters:** The adjustable numbers inside a neural network. More parameters means more flexibility — and historically, the fear was that too many parameters would lead to overfitting.

**Gradient descent:** The training process. At each step, it adjusts all the network's parameters slightly to improve performance. Think of it as slowly rolling downhill to find the lowest point in a landscape.

**Phase transition:** A sudden shift in the behaviour of a system as a threshold is crossed. Examples: water freezing, a magnet losing its magnetism. In learning, it refers to the sudden jump from "cannot generalise" to "can generalise."

**Linear network:** The simplest possible neural network. It has no non-linear parts, making it mathematically tractable — you can prove things about it rigorously.

---

## Key Takeaways

- Grokking did not come from nowhere. It is the latest chapter in a 30+ year story about why large networks generalise at all.
- The central paradox is: networks that can memorise anything still learn meaningful structure on real tasks.
- Key discoveries — long plateaus in simple networks, sharp learning transitions, structure forming after accuracy peaks — all set the stage for grokking.
- Grokking is valuable because it makes this complex phenomenon small and observable.

---

## Related Notes
- [[Research Timeline]] · [[Evolution of Grokking Research]]
- [[The Generalization Puzzle]]
- [[Double Descent]] · [[Phase Transition]]
