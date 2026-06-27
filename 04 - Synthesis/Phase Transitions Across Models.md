---
tags: [synthesis, phase-transition, comparison]
---
↑ Parent: [[00 - Start Here]] · Concept: [[Phase Transition]]

# Phase Transitions Across Models

> [!summary]
> "Sudden change at a critical point" recurs across this literature under many names. Collecting them shows grokking is one instance of a **universal pattern**, and points to which order parameters might transfer.

> [!tip] In plain words
> "Sudden change at a tipping point" shows up again and again under different names. Lining them up shows grokking is just one example of a single, universal pattern.

## Catalogue of transitions

| System | Control parameter | Transition | Order parameter | Paper |
|--------|-------------------|-----------|-----------------|-------|
| Deep net (width) | params vs data | [[Jamming Transition]] / double-descent cusp | generalisation-error cusp | [[Spigler - A Jamming Transition Affects Generalization]] |
| Random GLM | samples/dimension α | learnable ↔ non-learnable | optimal error / mutual info | [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]] |
| Random features | N/d, n/d | [[Double Descent]] | test error peak | [[Mei - Generalization Error of Random Features Regression]] |
| Classifier (training time) | epochs past zero error | [[Neural Collapse]] | within-class variability → 0 | [[Papyan - Prevalence of Neural Collapse]] |
| Diffusion model | denoising time | speciation, then collapse | data-correlation spectrum, excess entropy | [[Biroli - Dynamical Regimes of Diffusion Models]] |
| Tensor network (training) | sweeps | **grokking** / entanglement jump | entanglement entropy, O-information | [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] |
| Transformer (training) | steps | **grokking** | (sought) predictor signals | [[Thesis Proposal Summary]] |

## The shared structure

> [!important]
> Each row has (1) a control parameter, (2) a critical point, (3) an **order parameter** that jumps. **Every [[Grokking Predictors|grokking predictor]] is an attempt to find row-7's order parameter.** Rows 1–6 suggest candidates: spectral (jamming, diffusion, RMT), geometric (neural collapse, manifolds), and information-theoretic (GLM mutual info, O-information).

## Implications for the thesis

- **Spectral order parameters** ([[Heavy-Tailed Self-Regularization]]) are attractive because they recur across rows 1, 3, 5.
- **Geometric** ones ([[Neural Collapse]], [[Neural Manifolds]]) recur in rows 4 and the brain.
- **Information** ones recur in rows 2 and 6.
- The benchmark effectively tests **which family of order parameter best marks the grokking transition**. See [[Common Evaluation Metrics]].

---
## Related Notes
- [[Phase Transition]] · [[Double Descent]] · [[Empirical Evidence Across Studies]] · [[08 - Phase Transitions in Learning]]
