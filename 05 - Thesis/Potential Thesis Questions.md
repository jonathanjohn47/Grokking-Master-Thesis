---
tags: [thesis, questions]
---
↑ Parent: [[00 - Start Here]]

# Potential Thesis Questions

> [!summary]
> Ready-to-run questions — the thesis's five RQs plus spin-offs this vault suggests. Each is phrased to be falsifiable.

> [!tip] In plain words
> A list of concrete, ready-to-run questions the thesis could answer.

## The thesis's core RQs
1. Which predictor has the highest grokking-prediction **AUC**? (RQ1)
2. Which gives the longest **lead time** at 10% FPR? (RQ2)
3. Does any predictor **transfer** across tasks/architectures without recalibration? (RQ3)
4. Is the leaderboard **robust** to architecture and optimiser changes? (RQ4)
5. Can a **learned ensemble** beat the best single predictor, in- and out-of-distribution? (RQ5)

## Spin-off questions from the literature
- Do **[[Neural Collapse]] metrics** (NC1 variability, ETF angle) work as grokking predictors on modular arithmetic? ([[Papyan - Prevalence of Neural Collapse]])
- Does **manifold dimension/radius** drop sharply at grokking? ([[Li - Representations and Generalization in Artificial and Brain Neural Networks]])
- Does **HTSR α** move early enough for useful lead time on algorithmic tasks? ([[Heavy-Tailed Self-Regularization]])
- Is grokking **literally** epoch-wise [[Double Descent]], reproducible in random-features models over training time? ([[Mei - Generalization Error of Random Features Regression]])
- Do **O-information / transfer-entropy** signals from tensor networks transfer to transformers? ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]])
- Does the **Muon** optimiser change predictor rankings, not just grokking time? ([[12 - Modern Developments]])
- Are **grokking and [[Anti-Grokking]] signals** truly uncorrelated (H8)?

## Question selection guidance
> [!tip]
> The thesis is staked on **measurement rigor**, not on any hypothesis confirming. A clean null result (e.g., no predictor transfers, or the ensemble does not beat the best single) is a valid contribution. See [[Methodological Considerations]].

---
## Related Notes
- [[Thesis Proposal Summary]] · [[Research Gaps]] · [[Future Directions]] · [[The Nine Predictors]]
