---
tags: [learning-path, grokking, dynamics]
---
← Previous: [[01 - What Is Grokking]]  ↑ Parent: [[00 - Start Here]]  → Next: [[03 - Historical Background]]

# 02 - The Grokking Training Dynamics

## What Is This Note About?

When a neural network groks, it does not happen all at once. The process unfolds in **three distinct phases**, like acts in a play.

This note explains what happens in each phase — and crucially, what is happening *inside* the network even when nothing seems to be changing from the outside.

---

## The Three Phases of Grokking

### Phase 1 — Memorisation (Fast)

In this first phase, the network rapidly learns to get every training example right.

- **Training score:** Goes from 0% to nearly 100% very quickly.
- **Test score:** Stays at chance level — basically random guessing.
- **What is happening inside:** The network has built something like a giant lookup table. For every question it has seen, it has stored the answer. But it has not discovered the underlying rule. It cannot answer new questions.

Think of a student who photocopied all the past exam answers. They can get 100% on those exact questions, but will fail entirely if asked anything slightly different.

---

### Phase 2 — The Plateau (Long and Silent)

This is the most confusing phase. Everything looks frozen.

- **Training score:** Stays at ~100%. No change.
- **Test score:** Stays at chance level. No change.
- **What it looks like from the outside:** Nothing is happening. The network appears stuck.
- **What is actually happening inside:** Something important is changing, but it is invisible from the outside.

> [!WARNING]
> Many researchers would stop training here. The scores are flat, so why continue? But stopping here would mean missing the grokking event. The plateau is deceptive.

**What is secretly happening during the plateau?**

The network is under a slow, constant pressure to keep its internal values (called weights) small. This pressure is applied by a technique called **weight decay**.

The memorised lookup-table solution requires large internal values — it is like a bulky filing cabinet storing every answer separately. The network is slowly being squeezed to abandon this bulky solution.

At the same time, a more efficient solution — one that actually understands the rule — is being quietly assembled. This solution is smaller and more compact.

The competition between these two solutions is what makes the plateau last so long. The memorised solution is hard to dislodge. But weight decay keeps pressing.

---

### Phase 3 — Grokking (Abrupt)

After the long plateau, the efficient solution suddenly takes over.

- **Training score:** Stays at ~100%. (No change — it was already perfect.)
- **Test score:** Jumps from near 0% to near 100% in just a few hundred training steps.
- **What happened:** The efficient, rule-understanding solution finally became strong enough to dominate the network's outputs. The network can now compute the correct answer for any question, including ones it has never seen.

> [!NOTE]
> This jump happens very suddenly. It is not a gradual improvement. One moment the network is failing on new questions; a few hundred steps later, it is getting almost all of them right. This abruptness is one of the reasons grokking is so striking and interesting.

---

## A Table Summary

| Phase | Training Score | Test Score | What Is Happening Inside |
|-------|---------------|------------|--------------------------|
| 1 — Memorisation | Goes to ~100% quickly | Stays near 0% (random) | Network builds a lookup table of all training answers |
| 2 — Plateau | Stays ~100% | Stays near 0% | Weight decay slowly erodes the lookup table; a rule-understanding circuit builds up quietly |
| 3 — Grokking | Stays ~100% | Jumps to ~100% suddenly | The rule-understanding circuit takes over and the network can now answer any question |

---

## Why Does the Plateau Exist?

This is one of the most important questions in grokking research.

The short answer is: **there are two competing solutions, and one takes a long time to overtake the other**.

Think of it like a race:
- The **memorisation solution** (lookup table) is a fast runner who gets out ahead immediately.
- The **generalisation solution** (the actual rule) is a slow but efficient runner.
- Under weight decay pressure, the slow runner gradually gains ground during the plateau.
- Eventually, the efficient runner overtakes the fast runner — and that is the grokking moment.

The plateau is simply the time it takes for the efficient solution to build up enough strength to win.

> [!TIP]
> Researchers discovered that this kind of "long but finite plateau" is not unique to grokking. Even in the simplest possible networks (called linear networks), mathematicians proved in 1991 that you can have very long plateaus followed by sudden improvement. Grokking is an extreme version of something that has always been possible.

---

## Why the Plateau Is a Measurement Problem

Because both training and test scores are flat during Phase 2, the usual tools researchers use to monitor training are **useless** during this phase.

Looking at the loss curve (a graph of how wrong the network is) tells you nothing. Everything looks frozen.

The only way to tell if grokking is coming is to look **inside** the network — at the actual values (weights), the patterns of change (gradients), or the information in the network's hidden layers (activations).

This is exactly what grokking predictor research tries to do: find internal signals that change *before* the test score changes, giving researchers advance warning that grokking is approaching.

---

## The Dark Twin: Anti-Grokking

There is a disturbing counterpart to grokking called **[[Anti-Grokking]]**.

In some situations, if you keep training even after grokking has happened, the test score can **collapse again**. The network goes back to failing on new questions, even though it had already learned to generalise.

This makes the prediction problem even harder: you need signals not just to detect approaching grokking, but also to detect when **anti-grokking** is approaching — which may require completely different kinds of signals.

---

## Important Terms

**Weight decay:** A technique that gently pushes all the network's internal values (weights) toward zero at every training step. Think of it as a constant pressure to keep the network small and efficient.

**Weights:** The millions of small numbers inside a neural network. Training adjusts these numbers so the network gets better at its task.

**Gradients:** Measurements of how much each weight should change to improve the network's performance.

**Activations:** The values produced inside the network as it processes an input. Analysing activations can reveal what the network is "thinking."

**Loss curve:** A graph showing how wrong the network is over time. During the plateau, this curve looks flat — even though something is changing inside.

**Anti-Grokking:** The reverse of grokking — when a network that had learned to generalise suddenly starts failing on new questions again.

---

## Key Takeaways

- Grokking has three phases: fast memorisation, a long plateau, and a sudden jump to generalisation.
- The plateau looks like nothing is happening, but two solutions are competing inside the network.
- Weight decay is the force that slowly tips the balance toward the generalising solution.
- The plateau is a measurement problem: you cannot see what is coming by looking at the usual training graphs.
- After grokking, anti-grokking can undo the progress — adding another layer of complexity to the prediction problem.

---

## Related Notes
- [[Grokking]] · [[Anti-Grokking]]
- [[09 - Weight Decay and Regularization]]
- [[10 - Mechanistic Explanations and Circuit Formation]]
- [[What Causes Grokking]] · [[Role of Weight Decay]]
