---
tags: [synthesis, generalization, theory]
---
↑ Parent: [[00 - Start Here]]

# The Generalization Puzzle

> [!summary]
> The single question uniting all 15 papers: **why do overparameterized models that can memorise anything still generalise — and grokking adds: why sometimes only after a long delay?** This note frames grokking as the *time-domain face* of a *model-size* puzzle.

> [!tip] In plain words
> The one big question behind everything here: why do giant networks that could memorise anything still get *new* questions right? Grokking adds a twist — why sometimes only after a long wait?

## The static puzzle

Classical theory (the [[Bias-Variance Tradeoff]]) says huge models overfit. The defining empirical proof of the contradiction is [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]]: networks **memorise random labels yet generalise on real data**, and explicit regularization is neither necessary nor sufficient. Reality: they generalise, and often *better* with more capacity ([[Double Descent]]). Resolutions in this vault:
- **Variance, not bias, drives the interpolation peak; it falls past the threshold** ([[Rocks - Memorizing Without Overfitting]]).
- **Exact asymptotics confirm interpolators can be optimal** ([[Mei - Generalization Error of Random Features Regression]]).
- **A frozen subspace + good conditioning protect large nets** ([[Advani - High-dimensional Dynamics of Generalization Error]]).
- **The threshold is a real phase transition** ([[Spigler - A Jamming Transition Affects Generalization]], [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]]).

## The dynamic puzzle (grokking)

Same contradiction, **over training time**: a model interpolates immediately yet generalises only much later. The mapping:

| Static axis (model size) | Dynamic axis (training time) |
|--------------------------|------------------------------|
| Interpolation threshold | Memorisation point (train loss → 0) |
| Double-descent peak | Plateau (test still poor) |
| Second descent | Grokking transition |
| Benign overparameterization | Benign overtraining |

## Why the bridge is plausible

> [!important]
> The mechanisms are shared: **variance control, margin maximisation, effective-capacity reduction, regularisation selecting a special solution**. Grokking turns the static "more parameters help" into the dynamic "more training helps," with [[Weight Decay]] and slow [[Advani - High-dimensional Dynamics of Generalization Error|GD modes]] as the clock.

## The unfinished part

No paper here *derives* the grokking time-curve from the static double-descent formulas. Closing that gap — an exact theory of epoch-wise double descent with feature learning — is a major open direction ([[Future Directions]]). Note also the **lazy vs feature-learning** divide: [[Canatar - Spectral Bias and Task-Model Alignment]] (fixed kernel) cannot produce grokking; [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] (feature learning) can.

---
## Related Notes
- [[Double Descent]] · [[Phase Transitions Across Models]] · [[What Causes Grokking]] · [[Feature Learning]]
