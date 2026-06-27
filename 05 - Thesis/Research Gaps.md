---
tags: [thesis, gaps, core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[13 - Open Problems and Research Gaps]]

# Research Gaps

> [!summary]
> The validated gaps in grokking-predictor research (as of June 2026) — the precise voids the thesis fills, plus broader scientific gaps for future work.

> [!tip] In plain words
> The specific holes in current knowledge that the thesis is built to fill.

## The thesis-target gaps (validated)

> [!important]
> 1. **No unified comparison.** No existing work compares **more than 4** predictors on one benchmark. Every predictor wins only on its author's setup.
> 2. **No open library.** No single codebase implements all nine predictors under one API.
> 3. **No transfer matrix.** Cross-task / cross-architecture transfer has been tested for at most 2 predictors on 3 tasks ([[Xu - Dynamics in Deep Classifiers with the Square Loss|Xu 2026]]).
> 4. **No learned ensemble.** No one has combined predictors into a meta-predictor.
> 5. **One unverified anti-grokking detector.** The Correlation-Traps [[Anti-Grokking]] claim has never been tested against competitors.

## Broader scientific gaps

- **No universal order parameter.** Is there one internal signal marking the transition across all tasks/architectures? ([[Phase Transitions Across Models]])
- **Theory–dynamics bridge unfinished.** Static [[Double Descent]] formulas are not yet connected to the *time-domain* grokking curve. ([[The Generalization Puzzle]])
- **Grokking vs [[Anti-Grokking]] decoupling untested at scale.**
- **Scaling unknown.** Almost all evidence is tiny algorithmic models; relevance to LLMs is open.
- **Lazy vs feature-learning.** Fixed-kernel theory ([[Canatar - Spectral Bias and Task-Model Alignment]]) cannot produce grokking; a feature-learning theory of the transition is missing.

## Methodological gaps
- Inconsistent definitions of "the grokking event" and "lead time."
- No standard calibration (FPR) across studies.
- Survivor bias: non-grokking seeds dropped. See [[Methodological Considerations]].

## Gap → contribution map

| Gap | Thesis contribution |
|-----|---------------------|
| No unified comparison | C2 leaderboard |
| No open library | C1 9-predictor library |
| No transfer study | C3 9×4 transfer matrix |
| No ensemble | C4 meta-predictor |
| Unverified anti-grokking | C5 anti-grokking benchmark |

---
## Related Notes
- [[Future Directions]] · [[Potential Thesis Questions]] · [[Methodological Considerations]] · [[Thesis Proposal Summary]]
