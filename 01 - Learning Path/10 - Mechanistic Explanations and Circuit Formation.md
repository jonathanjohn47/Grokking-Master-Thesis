---
tags: [learning-path, mechanistic, circuits]
---
← Previous: [[09 - Weight Decay and Regularization]]  ↑ Parent: [[00 - Start Here]]  → Next: [[11 - Predicting Grokking]]

# 10 - Mechanistic Explanations and Circuit Formation

## What Is This Note About?

So far we have described grokking from the outside: what the accuracy curves look like, what weight decay does, why the competition between memorisation and generalisation produces a long plateau.

But a deeper question remains: **what is the network actually doing inside?**

When a network finally groks clock math, what has it built? Is there an actual algorithm running inside the weights? Can we look at the weights and see it?

This note answers those questions.

---

## What Is Mechanistic Interpretability?

**Mechanistic interpretability** is the scientific project of reverse-engineering what algorithm a neural network is running.

It is like opening up a black box and figuring out what is inside.

A neural network is trained by adjusting millions of numbers (weights). The training process never explicitly programs any rule — it just adjusts weights based on what produces correct answers. Yet somehow, the network learns to do things that look like following a rule.

Mechanistic interpretability asks: **what is that rule, and where is it encoded in the weights?**

---

## What the Grokked Network Actually Builds

For the clock-math task (addition mod 97), researchers (Nanda et al., 2023) reverse-engineered the grokked transformer and made a stunning discovery:

The network implements a specific, elegant mathematical algorithm using patterns related to **waves and rotations**.

Here is the basic idea in plain terms:

1. The network embeds each input number (let's call them A and B) as a rotation on a circle. Think of A and B as compass directions — A might be "37 degrees" and B might be "61 degrees."

2. The network then adds these rotations together: 37 + 61 = 98 degrees.

3. Since the clock wraps around at 97, the network computes what "98 degrees on a 97-position clock" corresponds to — which is 1.

4. It "reads off" this answer from the final rotation.

This is elegant, efficient, and compact. The entire clock-math operation is implemented as a rotation-addition-and-read-off algorithm.

> [!NOTE]
> The formal name for this algorithm involves "Fourier transforms" and "trigonometric identities" — mathematical tools for working with waves and rotations. But you do not need to understand the formal math to grasp the key point: the grokked network implements an actual algorithm, not a lookup table.

---

## Why This Algorithm Wins Over Memorisation

This brings us back to the key question: why does generalisation eventually win?

The answer from mechanistic interpretability is **circuit efficiency**:

- The **memorised solution** is like a filing cabinet. It stores a separate answer for every training question. This requires a lot of "space" — a lot of weight.

- The **generalised solution** (the rotation algorithm) is like a formula. It computes any answer from scratch using the same compact procedure. This requires much less "space" — much less weight.

When weight decay is pressing all weights toward zero, the generalised solution (using less weight) survives better. Eventually, it wins.

> [!TIP]
> Imagine two calculators. One has every possible addition result stored as a table: "1+1=2, 1+2=3, ..." — a huge lookup table. The other has a single addition algorithm that computes any result. The second calculator is smaller, lighter, and more efficient. Under pressure to keep things compact, you would prefer the second one.

---

## What Happens During the Plateau

During the long plateau, both solutions coexist inside the network. The weights contain a mix of:
- The large, bulky memorised solution (actively producing correct outputs for training questions)
- The small, compact rotation algorithm (being quietly assembled in the background)

As weight decay erodes the memorised solution, the rotation algorithm builds up relative strength. Eventually, the rotation algorithm starts producing larger, more confident outputs — and it takes over.

The grokking moment is the exact moment when the rotation algorithm's outputs become dominant.

Researchers can watch this process unfold by tracking specific internal measurements. For example:
- The structure of the embedding layer (the part that converts input numbers to internal representations) gradually shifts from random to showing clear wave-like patterns.
- Specific attention head patterns shift from being scattered to forming a clear, structured arrangement.

These internal changes happen during the plateau — **before** the test accuracy jumps. This is why internal measurements can predict grokking: they show the rotation algorithm being assembled.

---

## Structure Keeps Forming After Zero Error

A crucial insight from mechanistic research: **the network keeps changing internally after training accuracy hits 100%**.

This might seem paradoxical. Why would the network keep changing if it already gets every training question right?

The answer: weight decay is still active, and it is still pressing weights toward smaller values. This pressure reorganises the internal structure of the network even when the accuracy scores are flat.

Researchers found a beautiful version of this in a phenomenon called **neural collapse**:

- After training accuracy hits 100%, the network's hidden representations of different categories (different numbers, in clock math) keep changing.
- They gradually converge to a very specific geometric arrangement: the most symmetric, balanced arrangement possible.
- This is called "neural collapse" because the representations collapse into this symmetric structure.

Neural collapse happens during the "silent" plateau. It is a sign of internal reorganisation even when the external scores look frozen.

---

## Evidence From Non-Neural-Network Systems

To confirm that these internal changes are not just a quirk of how transformers work, researchers studied grokking in a completely different type of system — a tensor network.

A tensor network is a mathematical model from physics. It is not a neural network at all.

In a tensor network trained on image classification, grokking was observed. At the grokking moment, a specific internal quantity called "entanglement entropy" changed sharply.

This confirms that grokking is a genuine internal reorganisation — not an accident of the specific architecture.

---

## What This Means for Predicting Grokking

If you know what internal structure is being assembled (the rotation algorithm), you can design measurements that detect its formation.

This is the basis for several grokking predictors:
- Watching for wave-like patterns in the embedding layer
- Tracking specific attention head behaviors
- Measuring the gradient patterns that indicate the rotation algorithm is taking shape

These mechanistically-motivated predictors are among the most principled approaches to grokking prediction — because they measure the actual phenomenon (circuit formation), not just correlates of it.

---

## An Analogy: Building a Bridge

Imagine you are watching a bridge being built from above, but you can only see the top surface.

For a long time, nothing seems to happen on the top surface — the bridge deck has not been laid yet.

But underneath, engineers are assembling the support structure: laying foundations, installing girders, pouring concrete. This invisible work is essential. When it is complete, the bridge deck goes on very quickly.

The plateau in grokking is the underground construction phase. The grokking moment is when the bridge deck suddenly appears.

Mechanistic interpretability is the ability to look underground and watch the girders being assembled — giving you advance warning that the deck is about to appear.

---

## Important Terms

**Mechanistic interpretability:** The scientific project of reverse-engineering what algorithm a neural network is running. Opening the "black box" to see what is inside.

**Circuit:** A specific computational pattern implemented by a group of weights and neurons. In grokking, the generalised solution is called a "circuit" because it implements a specific algorithm.

**Fourier features:** Mathematical patterns related to waves and rotations. The grokked network uses these patterns to implement clock arithmetic efficiently.

**Neural collapse:** A phenomenon where a network's internal representations of different categories converge to a maximally symmetric geometric arrangement during the terminal training phase.

**Embedding layer:** The part of a transformer that converts input tokens (numbers or words) into internal numerical representations. In the grokked clock-math network, the embedding layer encodes numbers as rotation angles.

**Attention heads:** Components of a transformer that look at relationships between different parts of the input. In the grokked network, specific attention heads implement specific parts of the rotation algorithm.

**Entanglement entropy:** A measure from physics that describes how correlated different parts of a system are. Used as an order parameter for grokking in tensor-network experiments.

**Terminal phase:** The period after training accuracy hits 100% but before the network has fully settled into its final structure. Neural collapse and circuit formation happen during the terminal phase.

---

## Key Takeaways

- The grokked network implements an actual algorithm — a rotation-based computation — not a lookup table.
- This algorithm is more weight-efficient than memorisation, which is why weight decay causes it to eventually win.
- During the plateau, both the memorised solution and the rotation algorithm coexist inside the network. The rotation algorithm is being assembled while the memorised solution is being eroded.
- The grokking moment is when the rotation algorithm becomes dominant.
- Internal structure keeps forming after training accuracy hits 100% — this is the "silent" phase that mechanistic interpretability can observe.
- Mechanistically-motivated predictors measure the formation of the rotation algorithm directly, giving the earliest possible warning of approaching grokking.

---

## Related Notes
- [[Mechanistic Interpretability]] · [[Circuit Formation]] · [[Feature Learning]]
- [[Neural Collapse]] · [[Information-Theoretic Measures]]
- [[Mechanistic Explanations]] (synthesis)
- [[11 - Predicting Grokking]]
