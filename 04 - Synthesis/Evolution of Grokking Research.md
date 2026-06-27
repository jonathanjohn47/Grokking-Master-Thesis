---
tags: [synthesis, history, timeline]
---
↑ Parent: [[00 - Start Here]] · See also: [[Research Timeline]]

# Evolution of Grokking Research

> [!summary]
> How the field arrived at grokking and where it is going — a narrative companion to the dated [[Research Timeline]].

> [!tip] In plain words
> The story of how the field arrived at grokking and where it's heading, told as three short chapters.

## Three eras

### Era 0 — Seeds (1991–2016)
[[Baldi - Temporal Evolution of Generalization in Linear Networks]] (1991) already showed **plateaus and delayed generalization** in linear nets; [[Sokolić - Robust Large Margin Deep Neural Networks]] (2016) tied generalization to [[Margin and Robustness|margin]]. These are the deep roots.

### Era 1 — The generalisation puzzle (2017–2021)
The puzzle was crystallised by [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] (memorise anything, yet generalise). Physicists and statisticians attacked "why do overparameterized nets generalise?" with exact, high-dimensional methods: dynamics ([[Advani - High-dimensional Dynamics of Generalization Error]]), mean-field feature learning ([[Mei - A Mean Field View of Two-Layer Neural Networks]]), rigorous transitions ([[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]]), jamming ([[Spigler - A Jamming Transition Affects Generalization]]), double descent ([[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]]), scaling laws ([[Bahri - Explaining Neural Scaling Laws]]), and terminal-phase structure ([[Papyan - Prevalence of Neural Collapse]], [[Mixon - Neural Collapse with Unconstrained Features]]). **None used the word "grokking"** — they built its foundations.

### Era 2 — Grokking named and explained (2022–2024)
Power et al. (2022) named the phenomenon; Nanda et al. (2023) reverse-engineered it; Varma et al. (2023) gave the circuit-efficiency account. Spectral/geometric tools matured ([[Martin - Predicting Trends in Neural Network Quality]], [[Xu - Dynamics in Deep Classifiers with the Square Loss]], [[Li - Representations and Generalization in Artificial and Brain Neural Networks]], [[Jiang - Network Properties Determine Neural Network Performance]]). The first **predictors** appeared (Notsawo et al. 2023).

### Era 3 — Detection, generalisation, consolidation (2024–2026)
Predictors proliferated (gradient entropy, mutual information, dropout robustness, commutator defect…); grokking was shown **beyond neural nets** ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]); optimisers were found to change its timescale (Muon, 2025); and the **first unified benchmark** was proposed ([[Thesis Proposal Summary]], 2026).

## The trajectory

> [!important]
> The field has moved **discovery → explanation → prediction → consolidation**. The thesis sits at the consolidation frontier: enough predictors now exist that the bottleneck is no longer inventing another, but **fairly comparing** them. See [[Research Gaps]].

---
## Related Notes
- [[Research Timeline]] · [[03 - Historical Background]] · [[12 - Modern Developments]] · [[Research Gaps]]
