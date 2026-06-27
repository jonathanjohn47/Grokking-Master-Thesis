---
tags: [thesis, metrics, evaluation, reference]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[11 - Predicting Grokking]]

# Common Evaluation Metrics

> [!summary]
> The metrics for scoring grokking predictors (the thesis's evaluation axes) and the internal signals used as predictors, plus the generalisation metrics from foundational papers.

> [!tip] In plain words
> The yardsticks used to judge both the network (did it grok?) and the predictors (did they warn us early, accurately, and cheaply?).

## Predictor-scoring metrics (thesis)

| Metric | Definition | Answers |
|--------|-----------|---------|
| **Predictive AUC** | area under ROC for predicting grokking within ΔT = 5,000 steps (1.0 perfect, 0.5 chance) | accuracy (RQ1) |
| **Lead time** | steps between firing (at 10% FPR) and the grokking event, median across seeds | earliness (RQ2) |
| **Cross-task transfer AUC** | AUC retained when calibrated on task A, applied to task B | transfer (RQ3) |
| **Compute cost** | wall-clock ms + peak MB per signal evaluation | usability |
| **Anti-grokking AUC** | AUC for predicting test-accuracy collapse | side-experiment (H7/H8) |

> [!important]
> **Accuracy and earliness are distinct axes** — the best AUC predictor need not give the longest warning (H2). The thesis reports a **Pareto frontier** of accuracy vs lead time.

## Internal signals used AS predictors
Gradient curvature (Commutator Defect), spectral α and correlation traps ([[Heavy-Tailed Self-Regularization]]), weight-space PCA, L2 norm, early-epoch spectrum, gradient entropy (AGE), activation mutual information ([[Information-Theoretic Measures]]), dropout robustness. Full table: [[The Nine Predictors]].

## Generalisation metrics in foundational papers

| Metric | Source | Idea |
|--------|--------|------|
| Power-law exponent **α** | [[Martin - Predicting Trends in Neural Network Quality]] | data-free quality proxy |
| Neural capacitance | [[Jiang - Network Properties Determine Neural Network Performance]] | graph metric from SGD edge dynamics |
| NC1–NC4 collapse metrics | [[Papyan - Prevalence of Neural Collapse]] | terminal-phase geometry |
| Normalised margin / rank | [[Xu - Dynamics in Deep Classifiers with the Square Loss]] | which interpolant generalises |
| Manifold dimension / radius | [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] | geometric capacity |
| Bias / variance (analytic) | [[Rocks - Memorizing Without Overfitting]] | double-descent decomposition |

## Caveats
Metric choice interacts with calibration; report at multiple FPRs and guard against survivor bias ([[Methodological Considerations]]).

---
## Related Notes
- [[The Nine Predictors]] · [[Common Datasets]] · [[Methodological Considerations]] · [[Grokking Predictors]]
