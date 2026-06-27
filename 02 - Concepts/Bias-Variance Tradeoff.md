---
tags: [concept, theory, statistics]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[07 - Double Descent]]

# Bias-Variance Tradeoff

## What Is It?

The **bias-variance tradeoff** is a classic idea in statistics and machine learning that describes two different ways a model can be wrong.

For decades, it provided the main guidance for how to choose the right model size. Modern deep learning has dramatically complicated (and in some ways broken) this classical picture.

---

## Why Does It Exist?

When a model makes predictions, there are two main sources of error (beyond unavoidable noise in the data):

**Bias:** The model is systematically wrong — it makes the same mistake regardless of which training data you use.

**Variance:** The model is inconsistently right — it gives very different answers depending on which training data happens to be used.

The classical insight was: these two errors pull in opposite directions, and you have to balance them.

---

## A Simple Explanation

**High bias (too simple):**
Imagine you are trying to predict house prices using only one factor: the number of bedrooms. This ignores location, size, condition, etc. No matter how much data you have, your predictions will systematically miss houses that are expensive for other reasons. You have high bias — a systematic, baked-in error.

**High variance (too complex):**
Imagine you use every tiny detail of every house in your training set to make predictions. You have learned that "the house at 42 Maple Street with exactly 7 bushes out front sold for $350,000." But this overfitting means your model behaves erratically on new houses — give it a different training set and it would make completely different predictions. You have high variance — inconsistent, data-dependent behaviour.

**The classical "sweet spot":**
Classical theory says: find a model complex enough to capture the real pattern, but not so complex that it memorises training data quirks. This sweet spot minimises total error.

---

## The Classical U-Curve

When you plot error on new data against model complexity, classical theory predicts a U-shape:

- Start simple (high bias, low variance) → error is high
- Increase complexity (bias falls, variance rises) → error decreases to a minimum
- Increase complexity further (bias near zero, variance high) → error rises again

The bottom of the U is the "sweet spot" — the optimal model complexity.

For decades, finding and staying at this sweet spot was the central challenge of machine learning.

---

## How Modern Deep Learning Breaks This Picture

The classical U-curve assumes that making a model more complex always eventually makes things worse. But researchers discovered this is wrong for very large neural networks.

When you make a model large enough to fit all the training data perfectly, and then keep making it larger, the error **falls again** — below even the classical sweet spot. This is called **double descent** (described in full in [[Double Descent]]).

Why does the classical prediction fail?

At the exact size where the model just barely fits all the training data (the "interpolation threshold"):
- The model has no spare flexibility
- It is forced to fit every data point, including noisy, unusual cases
- This tight fitting makes it extremely sensitive to which data it sees
- Variance peaks

But when the model is made even larger (overparameterised):
- The model has spare flexibility
- Among all the ways to fit the training data, the training process tends to find the simplest, smoothest solution
- This "minimum complexity" solution has lower variance than the constrained solution at the threshold
- Error falls again

The key insight: **the training process itself acts as a regulariser for very large models**, preferring simple solutions even without being explicitly told to.

---

## How This Connects to Grokking

Grokking can be understood as the bias-variance story played out over **training time** instead of **model size**.

| Bias-variance concept | Grokking equivalent |
|----------------------|---------------------|
| Simple model (high bias) | Very early training — the model cannot even fit training data yet |
| Classical sweet spot | Does not apply — grokking requires overparameterisation |
| Interpolation threshold (variance peak) | The memorisation phase — the model fits training data perfectly but fails on new data |
| Second descent (variance falls) | The grokking transition — the model finds the simple, generalising solution |

The memorisation phase in grokking corresponds exactly to being stuck at the interpolation threshold — the most dangerous spot on the bias-variance curve. Weight decay is what pushes the network off this dangerous spot toward the second-descent region.

> [!TIP]
> The classical bias-variance tradeoff says: "bigger is worse past a certain point." Double descent and grokking show: "bigger (or longer training) can be better, far past what classical theory predicts." The key is that the training process naturally finds simpler solutions when given enough room.

---

## Variance During Grokking

During the memorisation phase, the network is in a high-variance state:
- Its answers to new questions are essentially random
- This randomness is not because the network is simple — it is because the network is making highly specific, training-data-dependent predictions that do not transfer

After grokking, the network is in a low-variance state:
- It applies a consistent, simple rule to every question
- This rule happens to generalise correctly

Weight decay is what drives the transition from high-variance memorisation to low-variance generalisation.

---

## Important Terms

**Bias:** Systematic, consistent error in a model's predictions. Not affected by which specific training data was used. Caused by model being too simple.

**Variance:** Inconsistent error — how much predictions would change if you used a different training set. Caused by model being too sensitive to training data quirks.

**Noise:** Irreducible error — randomness in the data itself that no model can predict perfectly.

**Bias-variance tradeoff:** The classical idea that reducing bias requires increasing variance, and vice versa. True in the classical regime; breaks down in the overparameterised regime.

**Interpolation threshold:** The model size where the model just barely fits all training data perfectly. Classical theory says this should be near the sweet spot; modern research shows error actually peaks here.

**Double descent:** The phenomenon where error goes down, up, then down again as model size increases. Breaks the classical U-curve. See [[Double Descent]].

**Overparameterised:** Having more parameters than training examples. Classical theory predicted this would cause high variance and poor performance. Modern research shows it can be beneficial.

**Minimum-norm solution:** Among all the ways to fit training data perfectly, the one with the smallest total weight values. The training process tends to find this solution in overparameterised models.

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "The bias-variance tradeoff is always the right way to think about model performance."
> It is the right framework in the classical (underparameterised) regime, but breaks down for very large models. The bias-variance tradeoff describes the left side of the double descent curve correctly, but not the right side.

> [!WARNING]
> **Misconception:** "A model that fits the training data perfectly must be overfitting."
> In the classical regime, this is true. In the overparameterised regime, it is often false. A very large model can fit training data perfectly and still generalise well — this is what grokking demonstrates.

---

## Key Takeaways

- Bias (systematic error from being too simple) and variance (inconsistent error from being too sensitive) are two sources of error in model predictions.
- Classical theory predicted a sweet spot at intermediate model complexity — neither too simple nor too complex.
- Modern deep learning breaks this picture: very large models can achieve lower error than the classical sweet spot.
- The training process itself tends to find simple, generalising solutions when given enough flexibility (overparameterisation).
- Grokking is the time-domain version of this story: the network starts in a high-variance memorisation state and transitions to a low-variance generalisation state.

---

## Related Notes
- [[Double Descent]] · [[Overparameterization]] · [[Interpolation Threshold]]
- [[Random Matrix Theory]] · [[Jamming Transition]] · [[Weight Decay]]
- [[07 - Double Descent]] · [[Memorization]] · [[Generalization]]
