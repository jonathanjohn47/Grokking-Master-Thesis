---
tags: [concept, mechanistic, circuits]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Circuit Formation

## What Is It?

**Circuit formation** is the process by which a specific, efficient algorithm is gradually assembled inside a neural network during the grokking plateau.

The word "circuit" is borrowed from electronics. Just as an electronic circuit is a collection of connected components that together perform a function (like adding numbers or storing memory), a neural network circuit is a collection of connected weights and neurons that together implement a specific computation.

In grokking, the "generalising circuit" is the compact, rule-based algorithm that eventually takes over from the bulky memorised solution.

---

## Why Does It Exist?

When a neural network is trained, it does not receive explicit instructions about what algorithm to build. There is no programmer telling it: "Use this formula." It only receives feedback about whether its outputs are correct or wrong.

Yet researchers discovered that the trained grokking network implements a very specific, elegant mathematical algorithm. This algorithm was not designed — it emerged from training.

Circuit formation is the study of how this algorithm emerges: how it gets built up, piece by piece, during the long plateau phase when the training scores look completely flat.

---

## The Circuit for Clock Math

For the clock-math task (addition mod 97), researchers (Nanda et al., 2023) completely reverse-engineered the circuit that the grokked network builds. They found three main parts:

**Part 1 — The Embedding Layer:**
The network encodes each input number as a rotation angle on a circle. Specifically, each number gets turned into a set of wave patterns (mathematically: combinations of cosines and sines). Think of representing the number 37 as "pointing in a direction that is 37/97 of the way around a circle."

**Part 2 — The Attention Heads:**
The attention heads combine the wave patterns from the two input numbers (A and B) using a mathematical identity. This identity says: "the wave pattern for A+B can be computed from the wave patterns for A and B separately."

In plain terms: the attention heads are computing "if A is at this direction on the circle, and B is at this direction, then A+B must be at this combined direction."

**Part 3 — The Feed-Forward Network:**
The feed-forward network reads the resulting combined direction and figures out which of the 97 answer classes (0 through 96) corresponds to that direction.

Together, these three parts implement a complete algorithm for computing clock math — not by storing answers, but by actually computing them using the geometry of rotations.

> [!NOTE]
> The formal mathematical name for this approach involves "Fourier transforms" and "trigonometric identities." You do not need to know these terms to understand the key point: the grokked network builds a real algorithm, not a lookup table. The algorithm is elegant, efficient, and compact. See [[Fourier Features]] for more detail on the wave-based representation.

---

## How the Circuit Forms: Step by Step

During the plateau, the circuit is being assembled while the memorised solution still dominates. Here is the timeline:

**Early plateau:**
The memorised solution dominates the outputs completely. The circuit components (embedding patterns, attention behaviors, feed-forward readout) are essentially random — not yet organised into the correct structure.

**Middle plateau:**
Weight decay is slowly eroding the large, bulky memorised solution. The circuit components begin to align — the embedding layer starts showing wave-like patterns, and the attention heads begin computing the right combinations. But the circuit is not yet strong enough to produce correct outputs.

**Late plateau:**
The circuit is nearly complete. Its components are well-organised and it produces increasingly correct outputs. But the memorised solution is still dominant — its larger weights still dominate the final answer.

**Grokking moment:**
The circuit becomes strong enough that its correct outputs outweigh the memorised solution's outputs. Test accuracy jumps suddenly. The circuit is now in charge.

> [!TIP]
> Researchers confirmed this timeline using "progress measures" — specific internal measurements that directly track how complete the circuit is. These measures rise consistently during the plateau, proving that assembly is happening invisibly while the accuracy scores look flat.

---

## Why the Circuit Wins

The circuit wins for a simple reason: **it is more efficient**.

- The memorised solution needs large weights — one set for each training question's answer.
- The circuit needs small weights — just enough to encode the rotation-based algorithm.

Under weight decay (which constantly shrinks all weights), the solution requiring less total weight survives better. Eventually, the circuit's smaller weight requirement allows it to stay effective while the memorised solution is eroded away.

This is called "circuit efficiency" — the generalising circuit wins not because it is clever, but because it is compact.

---

## Circuits in Other Neural Networks

The idea of circuits is not unique to grokking. Researchers have found circuits in larger language models too:

**Induction circuit:**
A pair of attention heads that work together to detect and complete repeated patterns. If a sequence "A B ... A" has appeared, the circuit predicts "B" will come next. This circuit is thought to be important for how language models learn from examples provided in their context (called in-context learning).

**Indirect object identification circuit:**
In the sentence "John gave Mary a book to ___", a specific set of attention heads correctly identifies "Mary" as the recipient. Researchers traced exactly which attention heads are responsible and how they cooperate.

These examples show that neural networks learn real algorithms — specific, decomposable computational procedures — not just statistical patterns.

---

## How Researchers Find Circuits

Finding a circuit requires systematic detective work:

**Step 1:** Identify the behavior to explain (e.g., "network can compute A+B mod 97").

**Step 2:** Use "activation patching" — take activations (internal values) from one training run and insert them into another run, then observe what breaks. The components that matter most are the circuit.

**Step 3:** Inspect the weight matrices for interpretable patterns (e.g., wave-like patterns in the embedding layer).

**Step 4:** Write a human-readable description of the algorithm the circuit implements and verify it matches the network's actual behavior.

---

## Why Circuit Formation Matters

Understanding circuit formation matters for three reasons:

**1. It explains why grokking is abrupt:**
The circuit must reach a "tipping point" — a level of completeness where it produces stronger outputs than the memorised solution — before the grokking jump happens. Before this tipping point, nothing visible changes. After it, everything changes at once. This is why grokking looks sudden.

**2. It explains why weight decay is necessary:**
Weight decay erodes the memorised solution (large weights) while leaving the circuit (small weights) relatively intact. Without weight decay, the memorised solution stays dominant indefinitely.

**3. It motivates circuit-based predictors:**
If you know what the circuit looks like and how it forms, you can measure its formation directly. Predictors that track circuit formation — like spectral patterns in the embedding layer — are the most principled approach to predicting grokking.

---

## Important Terms

**Circuit:** A specific sub-network (set of weights and connections) that implements a specific computation. Can be reverse-engineered and described as a human-readable algorithm.

**Circuit formation:** The gradual assembly of the generalising circuit during the grokking plateau.

**Embedding layer:** The part of the network that converts input tokens (numbers, words) into internal representations. In the grokking circuit, this layer encodes numbers as rotation angles.

**Feed-forward network (FFN):** The other main component of a transformer layer (alongside attention). In the grokking circuit, it reads the combined rotation angle and identifies the correct answer.

**Activation patching:** A technique for identifying which components of a network are responsible for a specific behavior by replacing their values with those from a different run.

**Progress measures:** Specific internal measurements that track how complete the grokking circuit is. These rise during the plateau before test accuracy changes.

**Circuit efficiency:** The property of needing less total weight to produce the same correct outputs. The generalising circuit is more efficient than the memorised solution.

**Induction circuit:** A pair of attention heads that together implement pattern-matching and completion. A canonical example of a circuit in language models.

---

## Key Takeaways

- The grokking network secretly builds a specific algorithm (a rotation-based circuit) during the plateau.
- This circuit implements real clock-math computation — not memorisation.
- The circuit forms gradually in three parts: embedding layer, attention heads, feed-forward network.
- The circuit wins over memorisation because it is more efficient (uses less total weight).
- Circuit formation explains why grokking is abrupt and why weight decay is necessary.
- Measuring circuit formation directly is the most principled approach to predicting grokking.

---

## Related Notes
- [[Mechanistic Interpretability]] · [[Feature Learning]] · [[Neural Collapse]]
- [[Fourier Features]] · [[Transformer]] · [[Attention Mechanism]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
- [[Varma - Explaining Grokking Through Circuit Efficiency]] · [[Weight Decay]]
