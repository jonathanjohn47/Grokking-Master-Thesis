---
tags: [concept, phase-transition, modern]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[08 - Phase Transitions in Learning]]

# Emergence

## What Is It?

**Emergence** in AI and machine learning refers to when a capability appears **suddenly** rather than gradually.

Instead of improving little by little, the system goes from near-zero ability to high ability in a short jump — almost as if a switch was flipped.

Grokking is one of the clearest examples of emergence: a network goes from near-zero test accuracy to near-100% accuracy in just a few hundred training steps, after tens of thousands of steps of no progress.

---

## Why Does It Matter?

Emergence matters because it breaks the assumption that learning is always smooth and gradual.

If you plot a learning system's performance against some control variable (like size or training time), you expect to see smooth, continuous improvement. Emergent abilities break this: there is a threshold, and crossing it causes an abrupt jump.

This has important practical implications:
- You cannot predict emergent abilities by extrapolating from small-scale tests.
- The performance before the threshold gives no indication that the threshold is approaching.
- Crossing the threshold can happen very fast.

---

## The Physics Connection

In physics, the same phenomenon is called a **phase transition**. Water does not gradually become more "ice-like" as it cools. At exactly 0°C, it suddenly freezes.

Emergence in learning systems follows the same pattern. The physics vocabulary provides useful concepts:

**Control parameter:** The thing you are changing that eventually triggers the transition (training steps, model size, weight decay).

**Order parameter:** A measurable quantity that is near zero in one phase and clearly nonzero in the other — the signal that tells you which phase you are in.

**Critical point:** The exact threshold where the transition occurs.

When researchers look for grokking predictors, they are essentially searching for the right **order parameter** for the grokking phase transition — a measurement that changes before test accuracy does.

---

## Examples of Emergence in This Vault

Emergence appears in many forms across the research in this vault:

| Phenomenon | What changes (control parameter) | What jumps (order parameter) |
|------------|----------------------------------|------------------------------|
| Grokking | Training steps | Test accuracy |
| Double descent | Model size | Test error (falls again) |
| Neural collapse | Training steps past perfect accuracy | Internal structure/symmetry |
| Anti-grokking | Training steps past grokking | Test accuracy (collapses) |
| Jamming transition | Parameter count | Generalisation error |

---

## Grokking as the Cleanest Example of Emergence

Grokking is particularly valuable as a case study of emergence for two reasons:

**1. It is measurable with certainty.**
The test set in grokking (the clock-math questions not used in training) provides a genuine generalisation check. Success on the test set requires truly computing the rule — there is no luck involved. The jump in test accuracy is unambiguous.

**2. It appears in both accuracy and loss simultaneously.**
Some researchers argued that apparent "emergent abilities" in large language models are not real — they are just artefacts of how you measure performance. Change the measurement scale, and the jump smooths out.

Grokking does not have this problem. The jump appears whether you measure accuracy or loss. It is a real discontinuous change, not a measurement artefact.

---

## Static vs Dynamic Emergence

There are two types of emergence in learning systems:

**Static emergence (over model size or data):**
- The control variable is model size or training data size.
- Example: large language models suddenly become capable at reasoning tasks once they pass a certain size.
- Example: double descent — test error suddenly improves past the interpolation threshold.

**Dynamic emergence (over training time):**
- The control variable is training steps.
- Example: grokking — test accuracy suddenly jumps after a long plateau.
- Example: neural collapse — internal structure suddenly becomes highly symmetric after training accuracy hits 100%.

Grokking is the clearest example of **dynamic** emergence. It is valuable precisely because it is small enough to study in detail — you can watch every weight change, trace every attention head, measure every gradient.

---

## Why Emergence Is Hard to Predict

The frustrating property of emergent abilities: the system shows almost no progress before the threshold, then suddenly jumps. This makes it impossible to predict the threshold by looking at current performance.

This is exactly why grokking predictors are needed. The external signals (training accuracy, test accuracy) give no information about whether the threshold is near. Only internal signals — changes in weight patterns, gradient structure, information flow — can reveal that the threshold is approaching.

> [!TIP]
> Imagine you are watching a pot of water heat up. The temperature (an internal measurement) tells you clearly whether it is close to boiling. But if you could only measure whether the water was bubbling (an external, binary measurement), you would have no warning — it would go from "not boiling" to "boiling" with no intermediate signal. Grokking predictors are like measuring the temperature, not just watching for bubbles.

---

## Important Terms

**Emergence:** When a capability appears suddenly rather than gradually, as a threshold is crossed.

**Phase transition:** The physics term for the same phenomenon. Water freezing is a phase transition — emergence in a physical system.

**Control parameter:** The variable you change that eventually causes the emergent jump (training steps, model size, weight decay).

**Order parameter:** A measurement that distinguishes the two phases. Jumps at the threshold. Used to detect and predict transitions.

**Critical point:** The exact threshold value of the control parameter where the transition occurs.

**Dynamic emergence:** Emergence over training time (grokking).

**Static emergence:** Emergence over model or data size (scaling abilities in language models, double descent).

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "All apparent emergent abilities in AI are real phase transitions."
> Not necessarily. Some apparent emergent abilities in large language models may be measurement artefacts — they appear to jump only because of how performance is measured. Grokking is more robust: the jump appears in multiple measurement scales simultaneously.

> [!WARNING]
> **Misconception:** "Emergence means the network suddenly learned something new at the transition."
> Not exactly. In grokking, the generalising circuit was being built throughout the plateau. The transition happens when the circuit becomes strong enough to dominate the output — not when the learning starts. The "emergence" is the threshold being crossed, not the moment learning began.

---

## Key Takeaways

- Emergence in AI means a capability appears suddenly, as a threshold is crossed, rather than improving gradually.
- Grokking is one of the clearest and most robust examples of emergence in machine learning.
- The physics concept of phase transitions provides the right framework: control parameter, order parameter, critical point.
- Grokking predictors are searches for the right order parameter — the measurement that changes before the visible threshold is crossed.
- Static emergence (over model size) and dynamic emergence (over training time) both exist; grokking is the cleanest example of dynamic emergence.

---

## Related Notes
- [[Phase Transition]] · [[Double Descent]] · [[Neural Scaling Laws]]
- [[Grokking Predictors]] · [[Anti-Grokking]] · [[Grokking]]
- [[Biroli - Dynamical Regimes of Diffusion Models]] · [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]
- [[08 - Phase Transitions in Learning]]
