---
tags: [concept, regularization, weight-decay]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[09 - Weight Decay and Regularization]]

# Weight Decay

## Definition
**Weight decay** is an L2 regularisation penalty that shrinks all weights toward zero at every training step. In [[AdamW]] (the canonical grokking optimiser), this is **decoupled** from the gradient update — the weights are simply multiplied by a factor slightly less than 1 each step. It penalises large weight norm, biasing optimisation toward low-norm solutions.

## In Plain Words
A gentle rule applied every training step: keep the weights small. Among all the ways to ace the training set, this nudge steers the network toward the simplest, smallest-weight solution — which happens to be the one that truly generalises. It's the main reason grokking eventually happens.

## The Mechanism, Step by Step

Without weight decay, once training loss reaches zero, the gradient is (approximately) zero and **nothing moves** — the network is stuck wherever it landed. Weight decay breaks this stalemate:

1. After memorisation, train loss ≈ 0. Gradient from the loss ≈ 0.
2. But weight decay continues: every step, $\theta \leftarrow \theta \cdot (1 - \eta\lambda)$ — weights shrink slightly.
3. The **memorising solution** has large weight norm (it needs a big lookup table). It shrinks faster under absolute weight decay.
4. The **generalising [[Fourier Features|Fourier circuit]]** has smaller weight norm. It shrinks less.
5. Eventually the generalising circuit produces larger logits *relative to the memorising solution* and takes over the output — the grokking jump.

This is the **circuit efficiency** story of [[Varma - Explaining Grokking Through Circuit Efficiency|Varma et al. (2023)]]: the generalising circuit wins because it is more norm-efficient.

## The Quantitative Effect

Sweeping weight decay $\lambda \in \{0, 0.01, 1.0\}$ ([[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]):
- $\lambda = 0$: grokking absent or extremely delayed (no pressure to move off the memorising solution).
- $\lambda = 0.01$: grokking occurs, but slowly.
- $\lambda = 1.0$: grokking occurs much faster — the standard experimental setting.

Too high a value: risks [[Anti-Grokking]] (generalisation collapses under excessive pressure).

## Key Insights

- Among zero-loss solutions, weight decay selects the **smallest-norm** one — the generalising [[Circuit Formation|circuit]], which is more efficient than memorisation ([[Role of Weight Decay]]).
- Drives **low-rank** and **[[Neural Collapse|collapsed]]** solutions under square loss ([[Xu - Dynamics in Deep Classifiers with the Square Loss]]).
- Even *implicit* regularisation (GD trajectory, small init) can cause grokking slowly without an explicit penalty ([[Advani - High-dimensional Dynamics of Generalization Error]]).
- Its accumulated effect is detectable in **heavy-tailed weight spectra** ([[Heavy-Tailed Self-Regularization]]) — as weight decay strengthens, the spectrum's tail gets heavier and the power-law exponent $\alpha$ drops.

## Decoupled vs Coupled (AdamW vs Adam)

Standard Adam applied L2 regularisation through the gradient: $g' = g + \lambda\theta$. This couples the regularisation strength to the adaptive scaling — large-gradient weights get less effective decay. [[AdamW]] fixes this by applying decay directly to weights, making the effect clean and predictable. This difference matters for grokking: AdamW's decoupled decay gives more reliable grokking timing.

## Evidence
[[Xu - Dynamics in Deep Classifiers with the Square Loss]], [[Li - Representations and Generalization in Artificial and Brain Neural Networks]], [[Martin - Predicting Trends in Neural Network Quality]], [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]], [[Varma - Explaining Grokking Through Circuit Efficiency]].

## Relationship to Other Concepts
- Mechanism for the [[Memorization]]→[[Generalization]] handover.
- Applied via [[AdamW]] in canonical grokking experiments.
- Tracked by the [[Grokking Predictors|L2-norm predictor]] (the simplest predictor: watch total weight norm drop).
- Produces [[Heavy-Tailed Self-Regularization]] and [[Neural Collapse]].
- A specific form of [[Regularization]] — see that note for the broader picture.

## Open Questions
Is weight decay *necessary*, or just an accelerator? What sets the optimal decay for fastest grokking without [[Anti-Grokking|anti-grokking collapse]]? Can the "optimal weight decay" be predicted from early-training signals?

---
## Related Notes
- [[AdamW]] · [[Regularization]] · [[Role of Weight Decay]]
- [[Varma - Explaining Grokking Through Circuit Efficiency]]
- [[Neural Collapse]] · [[Heavy-Tailed Self-Regularization]]
- [[09 - Weight Decay and Regularization]] · [[Anti-Grokking]]
