---
tags: [concept, regularization, generalization]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[09 - Weight Decay and Regularization]]

# Regularization

## Definition
**Regularization** is any mechanism that biases a model toward simpler solutions from among the many that fit the training data — making it harder to memorise noise and easier to capture the real pattern. It is the umbrella concept covering [[Weight Decay]], dropout, data augmentation, and implicit biases introduced by the optimiser and architecture.

## In Plain Words
A sufficiently flexible model will twist itself to fit every training point perfectly — noise included. Regularisation is the "keep it simple" pressure that prevents this. Like asking someone to explain an idea in one sentence instead of fifty: the simpler explanation usually [[Generalization|generalises]] better to new data.

## Three Types of Regularization

### 1. Explicit Regularization
Added deliberately to the training objective or procedure:

| Method | Mechanism | Effect in grokking |
|---|---|---|
| **[[Weight Decay]] (L2)** | Penalises $\|\theta\|^2$; shrinks weights toward zero | Main driver of grokking — selects minimum-norm generalising solution |
| **L1 penalty** | Penalises $\|\theta\|_1$; promotes sparsity | Less common in grokking setups |
| **Dropout** | Randomly zeroes activations during training | Prevents over-reliance on any one feature; tied to [[Margin and Robustness]] predictor |
| **Data augmentation** | Adds modified copies of training examples | Effective regulariser but not standard in grokking experiments |

### 2. Implicit Regularization
Not added explicitly, but emerges from the training procedure:
- **Gradient descent** inherently prefers low-norm solutions when operating near the interpolating manifold ([[Advani - High-dimensional Dynamics of Generalization Error]]).
- **Small initialisation** biases the model toward simpler representations early in training.
- **Optimiser choice**: AdamW's decoupled weight decay is more "clean" than Adam's implicit L2 — different implicit biases, different grokking dynamics (thesis RQ4 tests Muon vs AdamW).

### 3. Self-Regularization
Training spontaneously produces heavy-tailed weight spectra — the [[Heavy-Tailed Self-Regularization]] (HTSR) phenomenon. This acts like built-in regularisation without any explicit penalty, measurable as the power-law exponent $\alpha$:
- Smaller $\alpha$ (heavier tail) = more self-regularised = better trained.
- Self-regularisation accumulates over training, even at zero training loss.
- This is *why* [[Anti-Grokking]] can happen: self-regularisation eventually over-erodes the learned circuit.

## Why Regularization Drives Grokking

Grokking is the story of what regularisation does *after* training loss reaches zero:
1. Train loss ≈ 0. Loss gradients ≈ 0. Nothing should be moving.
2. But explicit regularisation ([[Weight Decay]]) keeps going: $\theta \leftarrow \theta(1 - \eta\lambda)$.
3. This erodes the memorising solution (high norm) faster than the generalising circuit (low norm).
4. Implicit regularisation (gradient flow's minimum-norm bias) pushes in the same direction.
5. Eventually the generalising solution wins — grokking.

Remove all regularisation and the network stays in the memorising solution indefinitely. Regularisation is what makes the grokking transition possible.

## The Critical Role of Weight Decay

Among all regularisers, [[Weight Decay]] is the most directly responsible for grokking. The reason:
- It applies *directly to weights*, not through the loss.
- It is continuous and slow — it can erode the memorising solution over thousands of steps.
- It gives the generalising solution (lower norm, [[Fourier Features|Fourier circuit]]) a decisive advantage.
- Sweeping $\lambda$ directly controls how fast grokking happens.

The [[Grokking Predictors|L2-norm predictor]] is simply monitoring the direct output of weight decay: total weight norm decreasing is a sign regularisation is winning.

## Surprising Facts About Regularization

- Explicit regularisation is **not required** to generalise: [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] showed neural networks can memorise random labels (no regularisation needed to fit data), *and* they generalise on real tasks even without explicit regularisation. So regularisation is not *required* for generalisation, but it *accelerates* and *makes reliable* the grokking transition.
- Regularisation can cause **anti-grokking** at extreme levels: too much weight decay erodes the generalising circuit after it forms, causing [[Anti-Grokking]].

## Key Insights
- **Explicit** regularisation: [[Weight Decay]] / L2 penalty, dropout — added intentionally.
- **Implicit** regularisation: gradient descent itself favours lower-norm, smoother solutions.
- **Self-regularisation**: training produces heavy-tailed weight spectra ([[Heavy-Tailed Self-Regularization]]).
- Regularisation is the *only* mechanism operating after train loss → 0 — the whole grokking transition is regularisation at work.
- The distinction between explicit and implicit matters for thesis RQ4: Muon vs AdamW have different implicit biases.

## Evidence
- [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] — generalisation persists even without explicit regularisation.
- [[Martin - Predicting Trends in Neural Network Quality]] — implicit self-regularisation visible in weight spectra.
- [[Advani - High-dimensional Dynamics of Generalization Error]] — implicit bias of gradient descent.

## Relationship to Other Concepts
- Parent concept of [[Weight Decay]]; expressed via [[Inductive Bias]] and [[Heavy-Tailed Self-Regularization]].
- The engine behind the [[Memorization]] → [[Generalization]] handover.
- Drives [[Neural Collapse]] (explicit + implicit regularisation → Simplex ETF).
- Excess regularisation causes [[Anti-Grokking]].

## Open Questions
Which type of regularisation most reliably triggers grokking, and which makes it most predictable? Is there an optimal regularisation-to-capacity ratio that maximises grokking speed while preventing anti-grokking?

---
## Related Notes
- [[Weight Decay]] · [[Weight Decay Necessity]] · [[Implicit Regularization]]
- [[Heavy-Tailed Self-Regularization]] · [[Inductive Bias]]
- [[09 - Weight Decay and Regularization]] · [[Role of Weight Decay]] · [[Anti-Grokking]]
- [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]]
- [[AdamW]] · [[Gradient Descent]] · [[Memorization]]
