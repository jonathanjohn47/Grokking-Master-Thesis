---
tags: [concept, regularization, weight-decay]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[09 - Weight Decay and Regularization]]

# Weight Decay

## What Is It?

**Weight decay** is a simple rule applied during training that makes weights smaller.

Every time the network updates its weights, we apply weight decay to gently nudge the weights toward zero.

Think of it as a "shrinking rule" applied on every training step.

## Why Does It Exist?

Neural networks can learn in two ways:

**Memorization**: The network memorizes the training data exactly. It uses large, complex weights to remember every single example.

**Generalization**: The network learns the underlying pattern. It uses simpler, smaller weights.

Weight decay pushes the network away from memorization and toward generalization.

Without weight decay, once the network memorizes everything, it gets stuck there. Weight decay is like a gentle hand that keeps pushing the network to find simpler solutions.

## Intuition: A Simple Analogy

Imagine you are solving a puzzle:

- You could use a gigantic, complicated machine with thousands of moving parts (memorization).
- Or you could use a simple, elegant mechanism with just a few parts (generalization).

Both solve the puzzle perfectly in training.

But the simple mechanism works on new puzzles too.

Weight decay is like a cost that penalizes the gigantic machine. So the network naturally prefers the simple mechanism.

The simpler the solution, the better it generalizes.

## Formal Definition

**Weight decay** is a regularization technique that adds a penalty for large weights.

The penalty is applied directly to the weights themselves:

$$\theta \leftarrow \theta \cdot (1 - \eta\lambda)$$

Where:
- $\theta$ = the network's weights
- $\eta$ = the learning rate (how big each step is)
- $\lambda$ = the weight decay coefficient (how strong the shrinking is)
- $(1 - \eta\lambda)$ = a number slightly less than 1 (like 0.99)

This means: on every training step, multiply the weights by 0.99 (or whatever value you choose).

Weights shrink slightly with every step.

In [[AdamW]] (a common optimizer used for grokking), this decay is **decoupled** from the gradient update.

**Decoupled** means: the weight shrinking happens independently from the gradient calculation. The shrinking always has the same effect, regardless of how large the gradients are.

## How Does It Work?

Here's the step-by-step process:

### Step 1: The Network Memorizes

At the start, the network memorizes the training data.

It creates a large, complex solution with big weights (like the gigantic machine with thousands of parts).

Training loss reaches zero.

Gradients become nearly zero (there's nothing left to improve).

### Step 2: The Network Gets Stuck

Without weight decay, the network would stop improving. The gradients are basically zero, so nothing changes.

The network is frozen in the memorizing solution.

### Step 3: Weight Decay Continues Anyway

But weight decay doesn't care about gradients.

It always shrinks all weights, every single step.

The memorizing solution has large weights (it needs a big lookup table).

Under weight decay, it shrinks faster and faster.

### Step 4: The Generalizing Solution Emerges

The generalizing solution uses smaller, more efficient weights.

It shrinks more slowly under weight decay (because it's already small).

Over time, the generalizing solution becomes relatively larger compared to the memorizing solution.

### Step 5: The Grokking Jump

Eventually, the generalizing solution produces stronger outputs than the memorizing solution.

The network's predictions shift to use the generalizing solution.

This sudden shift is called **grokking**.

This story is explained by the [[Varma - Explaining Grokking Through Circuit Efficiency|circuit efficiency theory]]: the generalizing circuit wins because it uses weights more efficiently.

## Example: Numbers Getting Smaller

Let's use a concrete example:

Imagine a weight starts at 100.

We apply weight decay with $\lambda = 0.01$ and learning rate $\eta = 0.1$.

The shrinking factor is $(1 - 0.01 \times 0.1) = 0.999$.

Step 1: $100 \times 0.999 = 99.9$
Step 2: $99.9 \times 0.999 = 99.8$
Step 3: $99.8 \times 0.999 = 99.7$
...
Step 1000: The weight is much smaller.

Small weights shrink too, but less noticeably:

If a weight starts at 10:
Step 1: $10 \times 0.999 = 9.99$
Step 2: $9.99 \times 0.999 = 9.98$

Both shrink by the same factor (0.999).

But the large weight (100) shrinks much more in absolute terms than the small weight (10).

This is the key insight: large memorizing solutions shrink away faster than small generalizing solutions.

## Real-World Impact in Grokking

Research from [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] shows:

- **No weight decay** ($\lambda = 0$): Grokking doesn't happen. The network stays memorized forever.
- **Light weight decay** ($\lambda = 0.01$): Grokking happens, but slowly (takes many more training steps).
- **Standard weight decay** ($\lambda = 1.0$): Grokking happens quickly (this is what researchers usually use).
- **Too much weight decay**: The network becomes too weak to learn anything useful. This is called [[Anti-Grokking]].

Weight decay is the dial that controls grokking speed.

## Important Terms

**Regularization**: A technique that penalizes certain properties of the model (like large weights) to improve generalization.

**Weight norm**: The total "size" of all the weights in the network. Calculated as the sum of all weights squared (approximately).

**Decoupled**: Applied independently. In AdamW, weight decay is not affected by gradient magnitudes.

**Coupled**: Applied together. In standard Adam, weight decay is affected by gradient magnitudes, making it less predictable.

**Generalization**: The ability to predict correctly on new, unseen data.

**Memorization**: Storing exact training examples instead of learning underlying patterns.

## Common Mistakes

### Mistake 1: "Weight decay is just L2 regularization"

They're related but not identical.

Weight decay (in AdamW) shrinks weights directly: $\theta \leftarrow \theta \cdot (1 - \lambda)$.

L2 regularization adds a penalty to the loss: add $\lambda \|\theta\|^2$ to the total loss.

In standard Adam, these are similar. But in AdamW, they're different, and this difference matters for grokking.

### Mistake 2: "More weight decay is always better"

Higher weight decay values don't always lead to better generalization.

Too much weight decay can prevent the network from learning anything useful ([[Anti-Grokking]]).

There's an optimal range, and finding it requires experimentation.

### Mistake 3: "Weight decay only matters early in training"

Weight decay matters throughout training.

Even after memorization, it continues pushing the network toward simpler solutions.

This is what enables the grokking jump.

## Key Takeaways

- **Weight decay is a shrinking rule**: On every step, multiply weights by a factor slightly less than 1.
- **It enables grokking**: Without weight decay, memorization solutions never get replaced. Weight decay slowly shrinks them away.
- **Large weights shrink faster**: Memorizing solutions need large weights and shrink quickly. Generalizing solutions are small and shrink slowly.
- **It's about efficiency**: The network learns that efficient, compact solutions (with small weights) generalize better than bloated, memorizing solutions.
- **The tuning matters**: Too little weight decay is slow, too much breaks learning. The right amount enables fast grokking.

## Decoupled vs Coupled Weight Decay

There are two ways to apply weight decay.

### Coupled Weight Decay (Standard Adam)

In standard Adam, weight decay is applied through the gradient:

$$g' = g + \lambda\theta$$

This means: the decay penalty is added to the gradient before the adaptive step.

**Problem**: Adaptive learning rates can reduce the decay effect.

When a gradient is very large, Adam reduces the step size for that weight.

But this also reduces the weight decay effect on that weight.

Large-gradient weights get less effective decay.

This makes the decay unpredictable.

### Decoupled Weight Decay (AdamW)

In [[AdamW]], weight decay is applied directly to weights, completely separate from the gradient:

$$\theta \leftarrow \theta \cdot (1 - \eta\lambda)$$

**Advantage**: The decay effect is constant and predictable.

All weights shrink at the same rate, regardless of gradient size.

Large-gradient weights don't get special treatment.

This consistency matters for grokking: AdamW makes grokking timing more reliable and reproducible.

## Mathematical Details

Weight decay shrinks weights geometrically.

If we start with weight $\theta_0 = 100$ and apply decay factor $(1 - \eta\lambda) = 0.999$ for $n$ steps:

$$\theta_n = \theta_0 \cdot (0.999)^n$$

After 1000 steps: $\theta_{1000} = 100 \cdot (0.999)^{1000} \approx 36.8$

The weight doesn't go to zero linearly. It shrinks exponentially, then levels off.

Small weights shrink too, by the same factor. But they remain small.

This is why large memorizing solutions shrink away, while small generalizing solutions persist.

## More Advanced Insights

**Selection by weight norm**: Among all solutions that reach zero training loss, weight decay biases the network toward the smallest-norm solution. The [[Role of Weight Decay|smallest-norm solution]] happens to generalize better.

**[[Neural Collapse|Neural collapse]] under square loss**: Research shows weight decay encourages weights to become low-rank and collapse to simple patterns under square loss ([[Xu - Dynamics in Deep Classifiers with the Square Loss]]).

**Implicit regularization**: Even without explicit weight decay, the natural dynamics of gradient descent can cause slow grokking ([[Advani - High-dimensional Dynamics of Generalization Error]]). Weight decay just accelerates this process.

**Heavy-tailed weight spectra**: As weight decay strengthens, the pattern of weight magnitudes becomes heavy-tailed ([[Heavy-Tailed Self-Regularization]]). This means: some weights are medium-sized, but many are very large, and the tail follows a power law.

## Research Evidence

This understanding comes from multiple papers:

- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]: Demonstrated the quantitative effect of weight decay on grokking timing.
- [[Varma - Explaining Grokking Through Circuit Efficiency]]: Explained grokking through circuit efficiency and weight norm.
- [[Xu - Dynamics in Deep Classifiers with the Square Loss]]: Studied how weight decay affects weight structure.
- [[Li - Representations and Generalization in Artificial and Brain Neural Networks]]: Examined weight decay's role in generalization.
- [[Martin - Predicting Trends in Neural Network Quality]]: Related weight properties to generalization.

## How This Connects to Other Concepts

**Broader picture**: Weight decay is one type of [[Regularization]]. Regularization is any technique that improves generalization by limiting model complexity.

**The handover mechanism**: Weight decay is the key mechanism that enables the shift from [[Memorization]] to [[Generalization]].

**Implementation**: In grokking experiments, weight decay is applied via the [[AdamW]] optimizer.

**Tracking progress**: The [[Grokking Predictors|L2-norm predictor]] monitors total weight norm to predict grokking. As weight norm drops, grokking is approaching.

**Side effects**: Weight decay produces [[Heavy-Tailed Self-Regularization]] (unusual weight distributions) and [[Neural Collapse]] (weights collapsing to simple patterns).

**The failure case**: Too much weight decay causes [[Anti-Grokking|anti-grokking]] — the network becomes so constrained that generalization fails.

**Other influences**: Even [[Neural Collapse|without explicit weight decay]], implicit regularization from small initialization and gradient descent trajectory can enable slow grokking.

## Open Questions

Researchers are still exploring:

- **Is weight decay necessary?** Could grokking happen naturally without it, just more slowly?
- **What's optimal?** What weight decay value produces fastest grokking for a given task?
- **Can we predict it?** Looking at early training signals, can we predict the optimal weight decay without guessing?
- **How does it interact with other factors?** How does weight decay interact with learning rate, batch size, network width, and [[Curriculum Learning|curriculum learning]]?

---

## Related Notes

- [[Regularization]] — the broader concept
- [[AdamW]] — the optimizer that uses decoupled weight decay
- [[Role of Weight Decay]] — detailed analysis of weight decay's role
- [[Varma - Explaining Grokking Through Circuit Efficiency]] — the circuit efficiency story
- [[Neural Collapse]] — what weights look like after weight decay
- [[Heavy-Tailed Self-Regularization]] — weight distribution patterns
- [[Anti-Grokking]] — when weight decay goes wrong
- [[Memorization]] — what weight decay replaces
- [[Generalization]] — what weight decay enables
- [[09 - Weight Decay and Regularization]] — learning path for this concept
