---
tags: [concept, optimization, foundations]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# AdamW

## What Is It?

**AdamW** is the training algorithm used in almost all grokking experiments. It is the tool that adjusts a neural network's weights during training to make the network better at its task.

The name stands for "**Adam** with decoupled **W**eight decay."

---

## Why Does It Exist?

Training a neural network is like trying to find the lowest point in a very complex, hilly landscape — while blindfolded.

The "landscape" represents how wrong the network is (the "loss"). The hills are combinations of weights that give wrong answers. The valleys are combinations that give right answers. You want to find the lowest valley.

The basic approach is: feel the slope under your feet, take a step downhill, repeat millions of times. This is called **gradient descent** (the gradient is the slope; you descend it).

AdamW is a smarter version of this basic approach. It solves two problems:

**Problem 1:** Basic gradient descent uses the same step size for every weight. But some weights need big steps (they haven't been updated much recently) and others need tiny steps (they are already close to the right value). AdamW adapts the step size separately for each weight.

**Problem 2:** Basic gradient descent with standard weight decay applies the weight-shrinking pressure in a way that gets tangled up with the adaptive step sizes, making it unpredictable. AdamW separates the weight-shrinking from the adaptive step — making weight decay clean and reliable.

---

## How It Works (Step by Step)

At each training step, AdamW does five things:

**Step 1 — Compute the gradient:**
The algorithm figures out which direction each weight should move to reduce the error.

**Step 2 — Track the recent history of gradients:**
AdamW remembers a running average of recent gradients (momentum). If the gradients have been consistently pointing in one direction, the step in that direction is bigger. This is like a ball rolling downhill — it builds up speed.

**Step 3 — Track how much each weight is changing:**
AdamW also tracks how much variation there has been in each weight's gradient. Weights that have been changing a lot get smaller steps; weights that have been changing little get bigger steps. This is the "adaptive" part.

**Step 4 — Update the weights:**
Using the momentum and the per-weight step sizes, each weight is updated.

**Step 5 — Apply weight decay separately:**
After the update, all weights are multiplied by a number slightly less than 1. This shrinks every weight toward zero by a small amount. This step is completely separate from the gradient update — this is the "decoupled" part.

> [!NOTE]
> Steps 2 and 3 use two running averages — one for the gradient itself, and one for the squared gradient. These are corrected for the fact that they start at zero, which would cause the initial steps to be too small.

---

## Why "Decoupled" Matters for Grokking

An earlier version of this algorithm (called plain "Adam") applied weight decay in a different, messier way: it mixed the weight-shrinking pressure into the gradient before the adaptive step-size calculation.

This caused problems: weights that were frequently updated got proportionally less shrinking than weights that were rarely updated. The weight decay became unpredictable.

AdamW fixes this by applying weight decay after the adaptive update, separately. The result: the "keep weights small" pressure is clean, predictable, and consistent across all weights.

**Why does this matter for grokking?**

Weight decay is the main switch for grokking. The rate of weight decay (λ, pronounced "lambda") controls how fast grokking happens. If weight decay is messy and unpredictable (as in plain Adam), grokking timing becomes unreliable. With AdamW's clean, decoupled weight decay, grokking happens at predictable, reproducible times.

---

## The Important Settings

In grokking experiments, these settings are typically used:

| Setting | Typical Value | What It Does |
|---------|--------------|--------------|
| Learning rate (η) | 0.001 | How large each training step is |
| Momentum rate (β₁) | 0.9 | How much recent gradients are remembered |
| Variance rate (β₂) | 0.98 | How much recent squared-gradients are tracked |
| Weight decay (λ) | 0, 0.01, or 1.0 | How aggressively weights are shrunk each step |

The most important setting is weight decay (λ). Grokking experiments sweep through these values to show how weight decay controls grokking.

---

## Why It Matters for Grokking Prediction

AdamW is also important because it keeps track of useful internal statistics:
- The running average of recent gradients
- The running average of how much each gradient has been varying

These statistics are used by some grokking predictors. For example:
- The **AGE predictor** measures the randomness (entropy) of gradient patterns
- The **Commutator Defect predictor** measures curvature properties of the gradients

So AdamW is not just the training tool — its internal statistics are also prediction signals.

---

## AdamW vs Muon: A New Development

Recently, researchers discovered that a different training algorithm called **Muon** causes grokking to happen much faster than AdamW.

This raises an important question: if we switch from AdamW to Muon, do the grokking predictors still work? Do they rank the same way?

This is one of the questions the thesis investigates.

---

## An Analogy

Imagine learning to navigate a city blindfolded, using only the feeling of slope under your feet.

**Basic gradient descent:** You take the same size step every time, in whichever direction feels downhill.

**AdamW:** You take bigger steps in directions you haven't explored much lately (adaptive step sizes), and you keep a "map" of recent slopes to build momentum. Plus, there's a gentle rule: every step, your stride also shortens slightly (weight decay) — this pressure keeps you from running too far from the origin.

---

## Important Terms

**Gradient:** The direction in which you should move the weights to reduce the error. Like the slope of a hill.

**Learning rate (η):** How large each training step is. Too large: you overshoot and miss the valley. Too small: training is extremely slow.

**Momentum:** Remembering recent gradient directions to build up speed in consistent directions.

**Weight decay (λ):** The "keep weights small" pressure applied at every step. The main switch for grokking.

**Adaptive step sizes:** Different step sizes for different weights, based on how much those weights have been changing recently.

**Decoupled:** Applied separately. AdamW applies weight decay separately from the gradient update.

**Loss:** A number measuring how wrong the network is. Training tries to minimise this.

---

## Key Takeaways

- AdamW is the training algorithm that adjusts weights during grokking experiments.
- It uses adaptive step sizes (different steps for different weights) and clean, decoupled weight decay.
- The clean weight decay is crucial: it makes grokking timing reliable and reproducible.
- Weight decay rate (λ) is the primary knob for grokking — higher λ means faster grokking.
- AdamW's internal statistics (gradient averages) are used by some grokking predictors.
- A newer algorithm called Muon may cause faster grokking, which the thesis investigates.

---

## Related Notes
- [[Weight Decay]] · [[Gradient Descent]] · [[Grokking Predictors]]
- [[04 - Core Experimental Setup]] · [[Experimental Designs Used in Literature]]
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]
