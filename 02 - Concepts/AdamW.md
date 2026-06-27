---
tags: [concept, optimization, foundations]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# AdamW

## What Is It?

**AdamW** is the training algorithm used in almost all grokking experiments.

**AdamW** is the tool that adjusts a neural network's weights during training. It's the engine that makes the network learn.

The name stands for "**Adam** with decoupled **W**eight decay."

It's an improved version of a basic algorithm called gradient descent.

## Why Does It Exist?

Training a neural network requires solving two problems.

### Problem 1: Finding the Right Direction

Imagine you're hiking in thick fog and can only feel the slope under your feet.

You want to reach the lowest valley, but you can't see it.

The basic approach: feel which way is downhill, take a step, feel again, repeat.

This basic approach is called **gradient descent**. The slope you feel is the **gradient**.

But here's the issue: different slopes require different step sizes.

Some directions are steep (you should take big steps). Some are gentle (small steps make more sense).

Basic gradient descent ignores this. It uses the same step size everywhere.

**AdamW solves this:** it uses different step sizes for different weights.

### Problem 2: Weight Decay Becomes Unpredictable

Once you have adaptive step sizes, a new problem appears.

You want to apply [[Weight Decay]] — the rule that shrinks all weights toward zero.

In the basic algorithm (called plain "Adam"), weight decay was tangled into the gradient calculation.

This caused a strange side effect: weights that were frequently updated got less shrinking than weights that were rarely updated.

Weight decay became unpredictable.

**AdamW solves this:** it applies weight decay separately, completely independent from the gradient update.

This makes weight decay clean, consistent, and predictable.

## Intuition: The Blindfolded Hiker

Imagine learning to navigate a city while blindfolded, using only the feeling of slope under your feet.

**Basic gradient descent:** Take the same size step every direction, downhill.

**AdamW:** 
- Takes bigger steps in directions you haven't explored much lately (some roads are steep, some are flat — adjust accordingly)
- Keeps a "memory" of recent slopes to build momentum (like a rolling ball)
- Separately applies a gentle shrinking rule: every step, your stride shortens slightly ([[Weight Decay]])

This makes training faster and more reliable.

## How It Works: Step by Step

At each training step, AdamW follows this process:

### Step 1 — Calculate the Gradient

First, figure out which direction each weight should move to reduce the error.

This is the gradient. It's like feeling the slope under your feet.

If you're on a steep slope, the gradient is large. On a gentle slope, it's small.

### Step 2 — Build Momentum

Remember recent gradients.

AdamW keeps a running average of recent gradient values.

If the gradients have been consistently pointing one direction, momentum builds up — you take bigger steps in that direction.

This is like a ball rolling downhill. The longer it rolls, the faster it goes.

**Technical note:** This is a weighted average. Recent gradients count more than old ones.

### Step 3 — Measure Gradient Variability

Also track how much variation there's been in each weight's gradients.

- Weights with **high variability** (gradients jump around a lot) → take **small steps**
- Weights with **low variability** (gradients are consistent) → take **big steps**

Why? If a gradient is jumping around, you're probably near the optimal value. Small steps help you land precisely. If a gradient is steady, you still have a ways to go. Bigger steps speed things up.

### Step 4 — Update the Weights

Combine the momentum and the per-weight step sizes.

Update each weight accordingly.

### Step 5 — Apply Weight Decay Separately

After all the above, apply [[Weight Decay]].

Multiply all weights by a number slightly less than 1 (like 0.99).

This shrinks every weight toward zero by a fixed percentage.

**This is the "decoupled" part:** weight decay is completely separate from Steps 1-4.

Nothing about Steps 1-4 affects how much weight decay is applied.

Weight decay always has exactly the same effect, regardless of gradient magnitudes.

> [!NOTE]
> **Technical detail:** Steps 2 and 3 use exponential moving averages. Imagine keeping a grade-school style running average, but recent values matter more. Also, these averages start at zero, which would cause initial steps to be too small. AdamW corrects for this automatically.

## Decoupled vs Coupled: Why It Matters

In the older algorithm (plain "Adam"), weight decay was **coupled** (mixed together) with the gradient update.

This caused a problem:

Imagine two weights:
- Weight A: gradients jump around a lot (high variability)
- Weight B: gradients are consistent (low variability)

In coupled weight decay:
- Weight A gets **small adaptive steps** (remember Step 3?)
- This also means Weight A's weight decay is effectively **weaker** (the small steps interact with decay)
- Weight B gets **big adaptive steps**
- Weight B's weight decay is effectively **stronger**

Result: The weight decay effect depends on the gradient variability. This is unpredictable.

### How AdamW Fixes This

AdamW applies weight decay **decoupled** (completely separated) from Steps 1-4.

All weights get the same shrinking rate, regardless of:
- How variable their gradients are
- How large their updates are
- How recently they were changed

Weight decay is always $(1 - \lambda)$ for every weight.

This predictability is crucial for grokking.

## Why This Matters for Grokking

[[Weight Decay]] is the main switch that controls grokking.

The weight decay rate ($\lambda$, pronounced "lambda") determines how fast grokking happens.

If weight decay is messy and unpredictable (as in coupled Adam), grokking timing is unreliable.

If weight decay is clean and predictable (as in AdamW), grokking happens at the same reproducible time, across many experiments.

This consistency is why AdamW is used in grokking research.

## The Hyperparameters

AdamW has several adjustable settings (called hyperparameters):

| Setting | Name | Typical Value | What It Does |
|---------|------|---|---|
| **η** | Learning rate | 0.001 | Step size: how much to move weights each step. Too big = overshoot. Too small = slow training. |
| **β₁** | Momentum rate | 0.9 | How much to remember recent gradients (0.9 means: remember 90%, forget 10% each step) |
| **β₂** | Variance rate | 0.98 | How much to track gradient variability (0.98 means: remember 98%, forget 2% each step) |
| **λ** | Weight decay | 0, 0.01, or 1.0 | Shrinking rate: how aggressively to shrink weights. **The main knob for controlling grokking.** |

### Which One Matters Most for Grokking?

**Weight decay (λ) is the most important.**

Grokking experiments change λ to show:
- λ = 0: No weight decay → grokking doesn't happen
- λ = 0.01: Light decay → grokking happens, but slowly
- λ = 1.0: Standard decay → grokking happens quickly (this is typical)

The other hyperparameters matter less for grokking timing.

## How AdamW Helps Predict Grokking

AdamW keeps track of useful internal numbers:

1. **Running average of gradients** (from Step 2)
2. **Running average of squared gradients** (tracking variability from Step 3)

These numbers are prediction signals.

Different grokking predictors use these differently:

- **[[Grokking Predictors|AGE predictor]]:** Measures randomness in gradient patterns
- **Commutator Defect predictor:** Measures curvature properties

So AdamW isn't just the training algorithm. Its internal statistics also tell us when grokking is coming.

## AdamW vs Other Algorithms

### Why Not Just Use Basic Gradient Descent?

Basic gradient descent is:
- ✓ Simple to understand
- ✗ Slow (same step size everywhere)
- ✗ Unreliable (doesn't adapt)

### Why Not Use Plain Adam (Without the W)?

Plain Adam is:
- ✓ Faster than basic gradient descent
- ✓ Adaptive step sizes
- ✗ Weight decay is unpredictable

### Why Use AdamW?

AdamW is:
- ✓ Fast training
- ✓ Adaptive step sizes
- ✓ Predictable weight decay
- ✓ Makes grokking reliable and reproducible

### What About Muon?

Recently, researchers discovered **Muon**, a different optimization algorithm that causes grokking to happen **much faster** than AdamW.

This raises important questions: Do grokking predictors still work with Muon? Do they rank differently?

These are questions the thesis investigates.

## Important Terms

**Gradient:** The direction to move weights to reduce error. Like the slope of a hill.

**Learning rate (η):** How big each training step is. Large = fast but risky. Small = slow but safe.

**Momentum (β₁):** How much to remember recent gradient directions. Builds up speed like a rolling ball.

**Variance (β₂):** How much to track changes in gradient size. Weights with big changes get smaller steps.

**Weight decay (λ):** The "keep weights small" shrinking rule. The main control for grokking speed.

**Decoupled:** Separated. AdamW applies weight decay independently from the gradient calculation.

**Coupled:** Mixed together. The older plain Adam mixed weight decay into gradients, making it unpredictable.

**Loss:** A number measuring how wrong the network is. Training minimizes this.

**Hyperparameter:** A setting you choose before training (not learned during training).

## Common Mistakes

### Mistake 1: "AdamW is just Adam with weight decay"

They're different in important ways.

Plain Adam **couples** weight decay into the gradient. This makes the effect unpredictable.

AdamW **decouples** weight decay. This makes it clean and predictable.

For grokking research, this difference is critical.

### Mistake 2: "The learning rate is the main control for grokking"

It's not. Weight decay is.

You can change the learning rate a lot and grokking still happens at similar times.

But if you change weight decay, grokking timing changes dramatically.

### Mistake 3: "All the hyperparameters matter equally"

They don't.

- **Weight decay:** Controls grokking timing (very important)
- **Learning rate:** Affects training stability (important)
- **Momentum and variance:** Mostly fine with typical values (less important)

## Key Takeaways

- **AdamW is the training engine** for grokking experiments. It's what makes the network learn.
- **It solves two problems:** (1) Different weights need different step sizes, (2) Weight decay needs to be predictable.
- **Decoupled weight decay is crucial:** Weight decay works the same way regardless of gradient properties. This makes grokking timing reproducible.
- **Weight decay is the main grokking knob:** Increasing λ speeds up grokking. Decreasing it slows it down.
- **AdamW's internal numbers are prediction signals:** The gradient statistics it tracks are used by grokking predictors.
- **Other algorithms exist:** Muon is faster, which raises new research questions about whether predictors still work.

---

## Related Notes

- [[Weight Decay]] — the "keep weights small" rule that enables grokking
- [[Gradient Descent]] — the basic algorithm that AdamW improves on
- [[Grokking Predictors]] — use AdamW's internal statistics
- [[04 - Core Experimental Setup]] — standard grokking setup
- [[Experimental Designs Used in Literature]] — how researchers use AdamW
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] — research using AdamW
