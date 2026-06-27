---
tags: [synthesis, causation, grokking]
---
↑ Parent: [[00 - Start Here]] · Related: [[Competing Theories of Grokking]]

# What Causes Grokking?

> [!summary]
> A working causal story, assembled from the vault: grokking is the **delayed, regularisation-driven selection of a low-norm generalising solution from the manifold of zero-loss solutions**, made visible because the selection is slow and leaves no loss signature.

> [!tip] In plain words
> The best current story in one breath: once a network can fit the training data in many ways, slow "keep it simple" pressure quietly steers it from the memorised answer to the real rule — and the switch looks sudden because nothing in the loss curve hints at it.

## The causal chain

1. **[[Overparameterization]]** creates a large manifold of zero-training-loss solutions ([[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]]).
2. **[[Memorization]] is reached first** because it is locally easy and high-norm ([[05 - Memorization vs Generalization]]).
3. **Not all zero-loss solutions are equal** — only some have large margin / low rank / good geometry ([[Xu - Dynamics in Deep Classifiers with the Square Loss]]).
4. **[[Weight Decay]] applies slow pressure** toward the low-norm, more efficient generalising [[Circuit Formation|circuit]] ([[Role of Weight Decay]]).
5. **A structured circuit forms silently** during the plateau (mechanistic + [[Neural Collapse|terminal-phase]] structure formation).
6. **The transition is abrupt** because it is a **[[Phase Transition]]** — once the circuit is efficient enough, it takes over the output ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] entanglement transition).

## What is necessary vs sufficient

| Ingredient | Role | Evidence |
|-----------|------|----------|
| Overparameterization | **Necessary** — provides the solution manifold | [[Mei - Generalization Error of Random Features Regression]] |
| Small train fraction | **Necessary** — creates the memorise/generalise gap | [[04 - Core Experimental Setup]] |
| Regularisation (explicit or implicit) | **Drives** the transition (explicit accelerates) | [[Advani - High-dimensional Dynamics of Generalization Error]], [[Xu - Dynamics in Deep Classifiers with the Square Loss]] |
| Long training budget | **Necessary** — the selection is slow | [[02 - The Grokking Training Dynamics]] |
| A learnable structured rule | **Necessary** — there must be a generalising solution to find | [[Mechanistic Explanations]] |

## Caveats

> [!warning]
> This is a *synthesised* account, not a settled consensus. The relative weight of regularisation vs dynamics vs geometry is unresolved, and most evidence is from tiny algorithmic models. See [[Competing Theories of Grokking]] and [[13 - Open Problems and Research Gaps]].

---
## Related Notes
- [[Competing Theories of Grokking]] · [[Role of Weight Decay]] · [[The Generalization Puzzle]] · [[Grokking]]
