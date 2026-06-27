---
tags: [concept, optimization, foundations]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[02 - The Grokking Training Dynamics]]

# Gradient Descent

## What Is It?

**Gradient descent** is the algorithm that trains neural networks.

It is the process of repeatedly adjusting all the network's internal values (weights) to make the network's answers more correct. It does this by figuring out, for each weight, whether making it slightly larger or slightly smaller would reduce the error — and then moving it in the direction that reduces error.

---

## Why Does It Exist?

A neural network starts with completely random weights. At this point, its answers are random too.

Training is the process of changing these weights so the answers become correct.

But with millions of weights, you cannot manually figure out the right values. You need an automated procedure.

Gradient descent is that procedure. It works by computing — for every single weight — exactly how much making it larger or smaller would improve the answer. Then it makes a small move in the direction that improves things.

It repeats this millions of times, and the network gradually improves.

---

## The Core Intuition: Walking Downhill Blindfolded

Imagine you are blindfolded on a hilly landscape, and you want to find the lowest valley.

You cannot see anything. But you can feel the slope under your feet.

Your strategy:
1. Feel which direction the ground is sloping downward.
2. Take a small step in that direction.
3. Feel the slope again.
4. Take another small step.
5. Repeat until you cannot feel any slope — you are at a valley.

This is gradient descent. The "landscape" is the error surface — the shape of how wrong the network is for every possible combination of weights. The valleys are combinations of weights that produce correct answers.

The "gradient" is the slope. It tells you which direction is downhill from where you currently are.

**Learning rate** controls how large each step is. Too large: you might overshoot the valley. Too small: it takes forever to get there.

---

## How It Works: Step by Step

**Step 1 — Forward pass:**
Show the network an example (e.g., "37 + 61 = ?"). The network processes the input through all its layers and produces a prediction.

**Step 2 — Compute the error:**
Compare the network's prediction to the correct answer. The "loss function" converts this comparison into a single number — the error.

**Step 3 — Backward pass (backpropagation):**
Starting from the error, compute how much each weight contributed to the error. This is done using a mathematical technique called backpropagation, which applies the chain rule of calculus through all the layers.

The result is the "gradient" — a measurement for every single weight saying: "if you increase this weight, does the error go up or down, and by how much?"

**Step 4 — Update the weights:**
Adjust every weight slightly in the direction that reduces the error. The size of the adjustment is controlled by the learning rate.

**Step 5 — Repeat:**
Do this for many examples, many times. The network gradually improves.

---

## Mini-Batch: An Efficiency Shortcut

Computing the exact gradient requires looking at all training examples. For large datasets, this is very slow.

The practical solution: pick a random small group of examples (called a "mini-batch"), compute the gradient for just those examples, and use that as an estimate of the true gradient.

This is called **stochastic gradient descent (SGD)** — "stochastic" means random. The gradient estimate is noisy (based on a random sample), but it is fast, and the noise often helps the network escape bad local valleys.

---

## Why Gradient Descent Matters for Grokking

Grokking is entirely a story about what gradient descent does over time.

**Phase 1 — Memorisation:**
Gradient descent rapidly finds a solution (the memorised lookup table) that reduces the error to near zero on the training data. This solution is easy to reach — it is close by in the weight space.

**Phase 2 — Plateau:**
The error is near zero. The gradient from the error signal is also near zero. Gradient descent has almost nothing to drive it forward.

But weight decay is still active: it applies a constant push toward smaller weights, even when the error gradient is zero.

This weight decay pressure, combined with the very small remaining error gradient, causes the network to slowly drift from the memorised solution toward the generalised solution. This drift is very slow — hence the long plateau.

**Phase 3 — Grokking:**
The slow drift reaches a tipping point. The generalised solution (the rotation algorithm) becomes dominant. Test accuracy jumps.

> [!TIP]
> The plateau is not "nothing happening." It is gradient descent operating in extreme slow motion — almost entirely driven by weight decay rather than the error signal. The slow modes of the landscape (directions where learning is very slow) are where the generalised solution lives.

---

## AdamW: The Enhanced Version

The canonical grokking experiments use an enhanced version of gradient descent called **AdamW**.

Plain gradient descent uses the same step size for every weight. AdamW adapts the step size separately for each weight based on its recent history of gradient changes. Weights that have been changing a lot get smaller steps; weights that have been changing little get bigger steps.

This makes training faster and more reliable. See [[AdamW]] for details.

---

## An Important Property: Gradient Descent Prefers Simple Solutions

When there are many possible solutions that achieve the same training error, gradient descent tends to find the **simplest** one — the one with the smallest total weights.

This is called **implicit regularisation** — the training algorithm itself has a built-in tendency toward simpler solutions, even without being explicitly told to prefer them.

This property is part of why grokking happens even without explicit weight decay, though explicit weight decay makes it happen much faster.

---

## Important Terms

**Gradient descent:** The training algorithm that repeatedly adjusts weights to reduce error.

**Gradient:** The slope of the error surface at the current weight values. Points in the direction that increases error most steeply. Moving opposite to the gradient decreases error.

**Learning rate:** How large each step is in gradient descent. Controls the trade-off between speed and stability.

**Backpropagation:** The algorithm for efficiently computing the gradient for every weight simultaneously, using the chain rule of calculus.

**Loss function:** The mathematical measurement of error. Gradient descent minimises this.

**Mini-batch (SGD):** Using a random subset of examples to estimate the gradient at each step. Faster than using all examples, and the noise can help.

**Implicit regularisation:** The tendency of gradient descent to find simpler solutions among many options that achieve the same error. Exists even without explicit weight decay.

**AdamW:** An enhanced version of gradient descent that adapts step sizes per weight and includes clean weight decay. Standard in grokking experiments.

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "Gradient descent always finds the best solution."
> Gradient descent finds a local minimum — a valley nearby, not necessarily the deepest valley in the whole landscape. In grokking, it finds the memorised solution (a local minimum that happens to be nearby) before finding the generalised solution (a better minimum that requires travelling further through the landscape).

> [!WARNING]
> **Misconception:** "Once gradient descent stops moving, training is done."
> In grokking, the gradient signal from the error is near zero during the plateau. But weight decay continues to push weights smaller, causing slow movement. The network is not "done" — it is moving very slowly.

---

## Key Takeaways

- Gradient descent is the algorithm that trains neural networks by repeatedly adjusting weights to reduce error.
- It works like walking downhill blindfolded: feel the slope (gradient), take a small step, repeat.
- The learning rate controls step size. Mini-batch SGD uses random subsets for efficiency.
- Grokking is a story about what gradient descent does over long timescales: fast memorisation, then slow drift under weight decay, then sudden generalisation.
- Gradient descent implicitly prefers simpler solutions — this is part of why generalisation eventually wins.
- AdamW is the enhanced version used in grokking experiments.

---

## Related Notes
- [[Loss Landscape]] · [[Weight Decay]] · [[Mean-Field Limit]] · [[Inductive Bias]]
- [[AdamW]] · [[Cross-Entropy Loss]]
- [[02 - The Grokking Training Dynamics]] · [[Baldi - Temporal Evolution of Generalization in Linear Networks]]
