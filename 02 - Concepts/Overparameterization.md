---
tags: [concept, theory]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[06 - Overparameterization and Interpolation]]

# Overparameterization

## Definition
A model is **overparameterized** when it has more free parameters than training examples — enough capacity to **interpolate** (fit the training data exactly, achieving zero training error), often by orders of magnitude.

## In Plain Words
Having far more dials than data points to fit — much more capacity than seems "needed." Classic intuition says this should produce catastrophic [[Overfitting]]. In practice these oversized networks often generalise best, and they're the only place grokking happens, because there's room to hold both a memorised answer and the real rule at once.

## A Concrete Example

A small [[Transformer]] for $(a+b)\bmod 97$ might have ~128K parameters. The training set (30% of all pairs) has ~2,794 examples. The model has **~46 parameters per training example** — wildly overparameterized by classical standards. Yet it eventually groks.

## The Manifold of Solutions

In the overparameterized regime, there are **infinitely many** weight configurations that achieve exactly zero training error. This set forms a manifold (a connected surface of solutions) in the space of all possible weights. This is crucial for grokking:

- The memorising solution is one point on this manifold.
- The generalising [[Fourier Features|Fourier circuit]] is another point on the same manifold — further away, reachable only under [[Weight Decay]] pressure.
- Training *wanders along* the manifold, slowly finding the generalising solution.

Without overparameterization (if the model just barely fits the data), there is no wandering possible — the solution is unique.

## Why Generalisation Improves Past the Threshold

Classical theory (the [[Bias-Variance Tradeoff]]) predicted the worst case at high overparameterization. Modern theory ([[Double Descent]]) shows the opposite. Several explanations:

1. **Variance collapse.** Past the threshold, gradient descent finds the **minimum-norm** interpolant — which has lower variance than constrained solutions ([[Mei - Generalization Error of Random Features Regression]]).
2. **Frozen subspace.** Large nets have eigenvalues of the feature/kernel matrix near zero — these weights barely move, providing implicit protection ([[Advani - High-dimensional Dynamics of Generalization Error]]).
3. **Benign overfitting.** The model can memorise noise *and* generalise on the signal — the noise fits into the "null space" of the prediction (low-variance directions) ([[Rocks - Memorizing Without Overfitting]]).

## Why It Matters for Grokking
Grokking only occurs in this regime: the network has spare capacity to both [[Memorization|memorise]] and [[Generalization|generalise]], so the question becomes *which* zero-loss solution it dynamically selects. Overparameterization is what makes the long plateau possible — there is a whole manifold to wander across.

## Key Insights
- Counter to classical intuition, test error often **decreases** with capacity past the [[Interpolation Threshold]] — the second descent of [[Double Descent]].
- A **frozen subspace** of weights does no learning in large nets, which protects against [[Overfitting]] ([[Advani - High-dimensional Dynamics of Generalization Error]]).
- Overparameterized interpolation can be benign: zero training error with good test error.
- [[Weight Decay]] navigates the manifold of zero-loss solutions toward the generalising minimum.

## Evidence
[[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]], [[Spigler - A Jamming Transition Affects Generalization]], [[Advani - High-dimensional Dynamics of Generalization Error]].

## Relationship to Other Concepts
- Enables [[Memorization]] and benign interpolation on the same manifold.
- Boundary with underparameterization: the [[Interpolation Threshold]] / [[Jamming Transition]].
- Sets the stage for [[Double Descent]] (static) and grokking (dynamic).
- [[Weight Decay]] navigates the manifold of solutions.
- Without it, [[Early Stopping]] would be optimal — with it, grokking is possible.

## Open Questions
How much overparameterization is *needed* for grokking? Is there an upper limit past which grokking disappears (too many parameters, too flat a loss landscape to navigate)?

---
## Related Notes
- [[Interpolation Threshold]] · [[Double Descent]] · [[Jamming Transition]]
- [[Memorization]] · [[Overfitting]] · [[Weight Decay]]
- [[06 - Overparameterization and Interpolation]] · [[Bias-Variance Tradeoff]]
