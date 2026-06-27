---
tags: [concept, theory, neural-collapse, geometry]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Layer-Peeled Model (LPM)

## Definition
The **Layer-Peeled Model (LPM)** is a tractable surrogate for the last layer of a deep neural network: it "peels off" the top layer and treats all lower layers as a universal feature extractor that can produce *any* features subject to a norm budget. What remains to be analysed is just **(last-layer features, last-layer classifier)** — a problem small enough to solve analytically. Introduced by Fang et al. (2021) alongside the unconstrained features model ([[Mixon - Neural Collapse with Unconstrained Features]]).

## In Plain Words
A real deep network has dozens of layers tangled together — too complex to analyse mathematically. The Layer-Peeled trick: assume the lower layers are powerful enough to produce *any* features they like (up to a size limit), and focus on just the final features and final classifier. That two-component problem is solvable, and — surprisingly — its answers match real networks quantitatively.

## The Model Formally

Let:
- $H \in \mathbb{R}^{n \times d}$: the last-layer features (one row per training example).
- $W \in \mathbb{R}^{K \times d}$: the last-layer classifier (one row per class).
- Constraints: $\|h_i\|^2 \le \rho$ for all $i$, $\|w_k\|^2 \le \rho_W$ for all $k$.
- Objective: minimise cross-entropy or square loss + weight norm penalty.

Because the "lower layers" are unconstrained (they can produce any $H$), the optimal $H$ is determined entirely by minimising the loss given $W$, and vice versa. This alternating optimisation has a clean, analytic solution.

**Key result**: on balanced data, the unique global optimiser of this problem has class means arranged in a **[[Simplex ETF]]** — proving that [[Neural Collapse]] is the attractor of training, not a coincidence.

## What It Explains

The Layer-Peeled Model gives analytic explanations for:

1. **[[Neural Collapse]]** — balanced data → Simplex ETF geometry. The features collapse to one point per class, and those points form the most symmetric configuration possible.
2. **[[Minority Collapse]]** — imbalanced data → past a critical imbalance ratio, minority class representations merge. The LPM predicts the exact tipping-point ratio ([[Class Imbalance]]).
3. **Loss function invariance** — the Simplex ETF emerges under cross-entropy, square loss, and general softmax-like losses ([[Cross-Entropy Loss]]). The geometry is a property of the regularised classification problem, not the specific loss.

## Relationship to the Unconstrained Features Model

The **unconstrained features model** ([[Mixon - Neural Collapse with Unconstrained Features]]) is a sibling approach: instead of a norm budget on features, features are truly unconstrained (no upper bound). Both models give the same qualitative result (Simplex ETF) but via slightly different proofs. The LPM is tighter on the minority-collapse predictions; the unconstrained model is simpler to analyse.

## A Template for Grokking Theory

The LPM's strategy — replace a messy deep network with a tractable two-parameter model that still captures the key phase transition — is a template applicable to the grokking transition. Can a "grokking surrogate model" be written that treats the transformer's learned representations as free parameters and proves the Fourier circuit is the global optimiser? This would give an analytic grokking predictor — currently an open question.

## Key Insights
- Keep only **(last-layer features, last-layer classifier)** plus a norm budget; the lower layers don't appear.
- On **balanced** data: every optimal solution forms a [[Simplex ETF]] — a proof of [[Neural Collapse]].
- On **imbalanced** data: predicts [[Minority Collapse]] with an exact tipping-point threshold ([[Phase Transition]]).
- Loss function doesn't change the conclusion — ETF geometry is robust across cross-entropy, square loss, etc.

## Evidence
- [[Fang - Layer-Peeled Model and Minority Collapse]] — defines the model; confirms ETF on balanced data and minority collapse on VGG13/CIFAR-10.
- [[Mixon - Neural Collapse with Unconstrained Features]] — sibling "unconstrained features" proof.
- [[Xu - Dynamics in Deep Classifiers with the Square Loss]] — training dynamics view of the same terminal-phase geometry.

## Relationship to Other Concepts
- Proves [[Neural Collapse]] analytically; predicts [[Minority Collapse]].
- Same family as [[Mixon - Neural Collapse with Unconstrained Features|unconstrained features model]].
- Relies on [[Simplex ETF]] geometry being the global optimiser.
- A template for analytic grokking theory (open question).

## Open Questions
Can a Layer-Peeled-style surrogate be written for the *grokking* transition on algorithmic tasks, giving an analytic order parameter and threshold? Would it predict grokking timing from initial conditions?

---
## Related Notes
- [[Fang - Layer-Peeled Model and Minority Collapse]] · [[Minority Collapse]] · [[Simplex ETF]]
- [[Neural Collapse]] · [[Mixon - Neural Collapse with Unconstrained Features]]
- [[Class Imbalance]] · [[Phase Transition]] · [[Cross-Entropy Loss]] · [[Weight Decay]]
