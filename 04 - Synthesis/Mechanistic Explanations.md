---
tags: [synthesis, mechanistic, circuits]
---
↑ Parent: [[00 - Start Here]] · Concept: [[Mechanistic Interpretability]]

# Mechanistic Explanations

> [!summary]
> The mechanistic line answers "what does the grokked network compute, and how does that structure assemble during the plateau?" For modular arithmetic the answer is **Fourier/trig circuits**; the broader principle is that **interpretable structure forms after zero training error**.

> [!tip] In plain words
> What is the grokked network actually doing inside, and how did that machinery get built during the quiet plateau? For clock-math, it builds gear-like circuits that add angles.

## What is computed

For $(a+b)\bmod p$, Nanda et al. (2023) reverse-engineered **discrete-Fourier-transform + trig-identity** circuits: inputs become rotations, the circuit adds angles and reads off the modular sum. **Progress measures** built from these circuits rise during the plateau before test accuracy — the prototype of a mechanistic [[Grokking Predictors|predictor]].

## How structure forms (cross-paper view)

| Lens | Observable | Paper |
|------|-----------|-------|
| Circuit efficiency | generalising circuit uses less norm | Varma et al. 2023 (see [[Role of Weight Decay]]) |
| Terminal-phase geometry | within-class variability → 0; Simplex ETF | [[Papyan - Prevalence of Neural Collapse]] |
| Landscape | collapsed config is the global minimiser | [[Mixon - Neural Collapse with Unconstrained Features]] |
| Dynamics | low-rank emergence under square loss | [[Xu - Dynamics in Deep Classifiers with the Square Loss]] |
| Information | synergy → redundancy; entanglement jump | [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] |
| Representation geometry | manifold dimension/radius shrink | [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] |

## The unifying claim

> [!important]
> Across substrates (transformers, tensor networks, generic classifiers), grokking is a **genuine internal reorganisation** — not a metric artefact. The network *cleans up* a redundant memorising representation into a compact, structured, generalising one. Different fields measure different shadows of the same event.

## Why this matters for prediction

If structure formation is real and measurable, the **best predictor is whatever most directly tracks circuit completeness**. The open question is whether any single mechanistic probe transfers across tasks, or whether mechanism is too task-specific and spectral/geometric proxies generalise better. See [[11 - Predicting Grokking]].

---
## Related Notes
- [[Mechanistic Interpretability]] · [[Circuit Formation]] · [[Neural Collapse]] · [[Information-Theoretic Measures]]
