---
tags: [synthesis, weight-decay, regularization]
---
↑ Parent: [[00 - Start Here]] · Concept: [[Weight Decay]]

# Role of Weight Decay

> [!summary]
> [[Weight Decay]] is the most-cited cause of grokking, but the literature disagrees on whether it is *necessary* or merely an *accelerator*. This note collects the evidence on both sides.

> [!tip] In plain words
> The "keep weights small" rule is the most-blamed cause of grokking — but researchers disagree on whether it's strictly required or just speeds things up. Here's both sides.

## The case that weight decay drives grokking

- **Selection by norm:** among zero-loss solutions, decay prefers the smallest-norm one — the generalising [[Circuit Formation|circuit]] (circuit-efficiency, Varma et al. 2023).
- **Geometry steering:** under square loss, normalisation + decay provably drive **low-rank, [[Neural Collapse|collapsed]]** solutions with generalisation bounds ([[Xu - Dynamics in Deep Classifiers with the Square Loss]]).
- **Empirically:** stronger decay shortens the plateau; the thesis sweeps decay ∈ {0, 0.01, 1.0} as a primary variable ([[Experimental Designs Used in Literature]]).

## The case that it is not strictly necessary

- **Implicit regularisation suffices (slowly):** GD itself provides a frozen subspace and conditioning effects that protect generalisation without an explicit penalty ([[Advani - High-dimensional Dynamics of Generalization Error]]); small initialisation matters.
- **Self-regularisation emerges from training:** heavy-tailed spectra appear as an *induced* regularisation, visible without an explicit term ([[Martin - Predicting Trends in Neural Network Quality]], [[Heavy-Tailed Self-Regularization]]).

## Reconciling the views

> [!important]
> Best current synthesis: **some** regularisation pressure (explicit *or* implicit) is required to move off the memorising solution; **explicit weight decay sets the speed**. Zero explicit decay can still grok via implicit effects, but very slowly. This makes decay the dominant *timescale* knob rather than an on/off switch.

## The dark side

Too much / too long: regularisation can over-shrink and trigger **[[Anti-Grokking]]** (test-accuracy collapse). The optimal-decay window is itself an open question ([[Future Directions]]).

---
## Related Notes
- [[Weight Decay]] · [[Heavy-Tailed Self-Regularization]] · [[Anti-Grokking]] · [[What Causes Grokking]]
