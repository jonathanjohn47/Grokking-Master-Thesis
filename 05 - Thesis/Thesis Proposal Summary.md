---
tags: [thesis, proposal, core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[11 - Predicting Grokking]]

# Thesis Proposal Summary

> [!summary]
> **A Unified Benchmark of Grokking Predictors** (Jonathan John, M.Sc. AI, IU; supervisor Prof. Dr.-Ing. Sheikh Faisal Rashid; June 2026, 2nd refined proposal). The thesis does **not** propose a new predictor — it provides the **first fair, head-to-head comparison** of all nine published [[Grokking Predictors|grokking predictors]] under one controlled protocol.

> [!tip] In plain words
> The project this whole vault supports: building the first fair, head-to-head test of all the grokking early-warning signals.

## Core contribution
> [!important]
> *Consolidation science.* Nine predictors exist; none have been compared fairly. The thesis re-implements all nine, evaluates them on the same models/tasks/scoring, and produces the **first unified leaderboard** — plus a learned ensemble and an [[Anti-Grokking]] side-experiment. Fully reproducible on a 16 GB Apple Silicon laptop.

## Five research questions
- **RQ1 — Accuracy:** which predictor has the highest predictive AUC for grokking within 5,000 steps?
- **RQ2 — Earliness:** which gives the longest lead time at fixed 10% false-positive rate?
- **RQ3 — Transfer:** does any predictor survive calibration on one task/architecture applied to another?
- **RQ4 — Robustness:** does the ranking hold across depth/width/heads and AdamW↔Muon?
- **RQ5 — Ensemble:** can a logistic meta-predictor beat the best single predictor (and does it hold out-of-distribution)?

## Eight hypotheses (pre-registered)
H1 Commutator Defect most accurate; H2 accuracy≠earliness (HTSR Alpha/AGE earliest); H3 Commutator Defect transfers best; H4 top-3 stable under architecture; H5 ensemble wins in-distribution; H6 ensemble fails out-of-distribution; H7 Correlation Traps uniquely detect [[Anti-Grokking]]; H8 grokking and anti-grokking need different signals. See [[Potential Thesis Questions]].

## Method in one line
Decompose every predictor into **signal / threshold / calibration** layers; standardise threshold and calibration (10% FPR) so only **signal quality** differs — the definition of a fair comparison. See [[Methodological Considerations]].

## Five deliverables
C1 open-source 9-predictor library; C2 unified leaderboard; C3 9×4 transfer matrix; C4 learned meta-predictor; C5 anti-grokking benchmark. Four canonical plots: leaderboard bar chart, accuracy-vs-lead-time Pareto scatter, transfer heatmap, ensemble-vs-best line. See [[The Nine Predictors]] and [[Common Evaluation Metrics]].

## Scope limits
Small (1–2 layer) transformers, algorithmic tasks, PyTorch/MPS. **Descriptive** rankings, not causal claims. No LLM/vision generalisation claimed. Null results are publishable.

---
## Related Notes
- [[The Nine Predictors]] · [[Research Gaps]] · [[Methodological Considerations]] · [[Experimental Designs Used in Literature]] · [[11 - Predicting Grokking]]
