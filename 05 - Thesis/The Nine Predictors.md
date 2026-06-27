---
tags: [thesis, predictors, catalogue, core]
---
↑ Parent: [[00 - Start Here]] · Concept: [[Grokking Predictors]]

# The Nine Predictors

> [!summary]
> The catalogue benchmarked by [[Thesis Proposal Summary|the thesis]]. Each is a candidate **order parameter** for the grokking [[Phase Transition]], grouped by signal family.

> [!tip] In plain words
> The nine early-warning signals for grokking, each explained simply — what it measures and where it came from.

## Catalogue

| # | Predictor | Signal type | Source | Expected role (thesis) |
|---|-----------|-------------|--------|------------------------|
| 1 | **Commutator Defect** | gradient curvature | Xu (2026) | Top accuracy (H1) |
| 2 | **HTSR Alpha** | spectral (heavy-tail) | Prakash & Martin (2025) | Strong lead time; anti-grokking-relevant |
| 3 | **Correlation Traps** | spectral (shuffled) | Prakash & Martin (2025) | Unique [[Anti-Grokking]] detector (H7) |
| 4 | **Weight-Space PCA** | spectral (PCA conc.) | Xu (2026) | Expected to fail cross-task transfer |
| 5 | **L2 Weight Norm** | weight magnitude | Tan & Huang (2023) | Baseline; likely bottom third |
| 6 | **Spectral Signature** | early-epoch spectrum | Notsawo et al. (2023) | Early lead; moderate accuracy |
| 7 | **AGE (Absolute Gradient Entropy)** | gradient entropy | Zhou et al. (2025) | Strong lead time (H2) |
| 8 | **Higher-Order MI** | activation mutual info | Clauw et al. (2024) | Wildcard; transfer potential |
| 9 | **Dropout Robustness** | test-time perturbation | Salah & Yevick (2025) | Easy; competitive accuracy |

## How each connects to the vault's theory

- **HTSR Alpha & Correlation Traps** ← [[Heavy-Tailed Self-Regularization]] ([[Martin - Predicting Trends in Neural Network Quality]]). α tracks self-regularisation; correlation traps flag rank-one collapse.
- **Weight-Space PCA / L2 norm** ← [[Weight Decay]] (norm-driven solution selection; [[Xu - Dynamics in Deep Classifiers with the Square Loss]]).
- **Commutator Defect** ← gradient/Hessian curvature; mechanistic [[Circuit Formation]].
- **Higher-Order MI** ← [[Information-Theoretic Measures]] ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]).
- **Spectral Signature** ← early-spectrum [[Phase Transition]] precursors; precedent in early-prediction work ([[Jiang - Network Properties Determine Neural Network Performance]]).
- **AGE / Dropout Robustness** ← gradient-entropy and robustness proxies for solution sharpness.

## The fair-comparison design

> [!important]
> Each predictor = **signal** (varies, the only thing tested) + **threshold** (standardised) + **calibration** (standardised to 10% FPR). This isolates signal quality from threshold tricks. See [[Methodological Considerations]].

## Anti-grokking subset
Only **Correlation Traps** is claimed to detect [[Anti-Grokking]]; the thesis tests this against the other eight (H7/H8).

---
## Related Notes
- [[Grokking Predictors]] · [[Common Evaluation Metrics]] · [[Anti-Grokking]] · [[Thesis Proposal Summary]]
