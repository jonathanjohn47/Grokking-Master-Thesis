---
tags: [concept, geometry, terminal-phase]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Neural Collapse

## Definition
**Neural collapse** (Papyan, Han & Donoho, 2020) is a geometric regularity that emerges in the **terminal phase of training** — *after* training error has already reached zero. It is characterised by four simultaneous properties (NC1–NC4): (NC1) within-class feature variability collapses to zero; (NC2) class means arrange themselves into a **[[Simplex ETF|Simplex Equiangular Tight Frame (ETF)]]**; (NC3) the last-layer classifier aligns with the class means (self-duality); (NC4) classification reduces to a nearest-class-centre rule.

## In Plain Words
After a network has nailed the training set, its internal picture of each class keeps tidying up: every class shrinks toward a single tight point, and those points spread out as evenly and symmetrically as possible — like the corners of a perfectly balanced shape. Structure keeps improving even though the loss and accuracy have stopped changing. This is the same "quiet work" behind grokking's plateau: the network is still reorganising internally even when external metrics are flat.

## The Four Properties (NC1–NC4) in Plain Language

| Property | Technical | Plain language |
|---------|-----------|----------------|
| NC1 | Within-class variability → 0 | All "dog" images produce the same internal representation; "cat" has its own, etc. |
| NC2 | Class means form Simplex ETF | The class representations spread as evenly as possible — all at equal angles |
| NC3 | Classifier = class means (self-duality) | The weights that decide "is it a dog?" point exactly at where "dog" lives in representation space |
| NC4 | Classification = nearest centre | The network simply finds which class centre is closest — no complex decision boundary |

Together these properties produce a **maximally symmetric, maximally separable** set of class representations — the geometry that most cleanly separates the classes.

## Why It Matters

1. **Structure forms after zero loss** — the clearest example, across many architectures and datasets, that a network's internal representations *continue to improve* after training metrics flatten. This is the principle behind grokking's plateau: things are happening inside.
2. **A concrete order parameter candidate.** NC1 (within-class variability) dropping toward zero is a measurable event. If it coincides with the grokking transition on algorithmic tasks, NC metrics become grokking predictors.
3. **Generalisation guarantee.** The Simplex ETF maximises the margin between classes — consistent with the best-known generalisation bounds ([[Xu - Dynamics in Deep Classifiers with the Square Loss]], [[Sokolić - Robust Large Margin Deep Neural Networks]]).

## How It Forms

Under [[Weight Decay]] + continued training:
- Weight decay shrinks all weights, including the last-layer classifier and the feature extractor.
- The geometry that minimises the combined loss + norm-penalty across all classes simultaneously is precisely the Simplex ETF configuration.
- [[Mixon - Neural Collapse with Unconstrained Features]] proved this is the **global minimiser** of a simplified model (treating last-layer features as free variables). This explains why training dynamics are drawn toward it.

## Evidence
[[Papyan - Prevalence of Neural Collapse]] (empirical: 3 architectures × 7 datasets, measured NC1–NC4 over training), [[Mixon - Neural Collapse with Unconstrained Features]] (theory: collapse is the global optimum), [[Xu - Dynamics in Deep Classifiers with the Square Loss]] (dynamics + generalisation bounds).

## Relationship to Other Concepts
- A terminal-phase [[Phase Transition]] in representation geometry.
- Driven by [[Weight Decay]]; a form of [[Circuit Formation|structure formation]] and [[Feature Learning]].
- The extreme case of [[Neural Manifolds|manifold compression]] (NC1 = zero radius).
- Its geometry is the [[Simplex ETF]]; its imbalanced-data failure mode is [[Minority Collapse]].
- A candidate **order parameter** for grokking ([[Grokking Predictors]]).

## Open Questions
Does grokking's generalisation onset coincide with neural collapse in the last layer? Can NC metrics (NC1 variability, ETF angle alignment) serve as grokking predictors on algorithmic tasks?

---
## Related Notes
- [[Papyan - Prevalence of Neural Collapse]] · [[Mixon - Neural Collapse with Unconstrained Features]] · [[Xu - Dynamics in Deep Classifiers with the Square Loss]]
- [[Simplex ETF]] · [[Minority Collapse]] · [[Layer-Peeled Model]]
- [[Feature Learning]] · [[Weight Decay]] · [[Grokking Predictors]]
