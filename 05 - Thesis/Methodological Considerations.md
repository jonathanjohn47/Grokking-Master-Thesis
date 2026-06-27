---
tags: [thesis, methodology, rigor]
---
↑ Parent: [[00 - Start Here]]

# Methodological Considerations

> [!summary]
> What makes a grokking-predictor comparison *fair* and *trustworthy*, and the pitfalls the literature and thesis must manage.

> [!tip] In plain words
> The easy-to-miss pitfalls that can make a predictor look better than it really is, and how a fair comparison avoids them.

## The fairness problem
Nine predictors measure nine different quantities. Comparing them under different thresholds/calibration conflates **signal quality** with **threshold choice**.

> [!important] The three-layer fix
> - **Signal layer** (varies) — the raw quantity; the only thing tested.
> - **Threshold layer** (standardised) — fire when the signal crosses τ.
> - **Calibration layer** (standardised) — τ chosen on held-out data for exactly **10% false-positive rate**.
> Any leaderboard difference then reflects the signal, not the rule.

## Statistical rigor
- Bootstrap **95% CIs**; **DeLong test** for comparing AUCs; paired tests for lead time.
- Report at **multiple FPR levels** (5/10/20%) — ranking changes are themselves findings.
- 10 seeds canonical, 5 for variation cells.

## Pitfalls to manage

| Pitfall | Consequence | Mitigation |
|---------|-------------|-----------|
| **Implementation infidelity** | a bug deflates one predictor (a scientific error, not a finding) | reproduce each predictor's original reported behaviour first |
| **Survivor bias** | dropping non-grokking seeds inflates AUC | report grokking-success rate per config; evaluate on no-grok subset |
| **Calibration sensitivity** | 10% FPR may favour well-behaved signals | multi-FPR reporting |
| **Hardware precision (MPS)** | silent CPU fallback alters dynamics | reproduce canonical baseline first; log versions |
| **Ill-defined "grokking event"** | inconsistent lead-time measurement | fixed operational definition of the event + horizon |

## Definitions to fix up front
- **Grokking event:** first step test accuracy crosses a set threshold (and stays).
- **Lead time:** steps between predictor firing (at 10% FPR) and the event.
- **Prediction horizon:** ΔT = 5,000 steps for the AUC label.

## Validation gate
> [!warning]
> Reproduce the **canonical Nanda et al. grokking** on $(a+b)\bmod 97$ **before** implementing any predictor. Without this baseline, nothing downstream is trustworthy.

---
## Related Notes
- [[Common Evaluation Metrics]] · [[Experimental Designs Used in Literature]] · [[Research Gaps]] · [[The Nine Predictors]]
