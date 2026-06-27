---
tags: [concept, geometry, representations]
---
↑ Parent: [[00 - Start Here]] · Related: [[Feature Learning]]

# Neural Manifolds

## Definition
A **neural manifold** is the geometric object traced in activation space by all inputs belonging to one category or class. For each class, the set of internal representations $\{h(x) : x \in \text{class } k\}$ forms a cloud in the high-dimensional activation space — this cloud has geometric properties (shape, size, dimension) that determine how separable the classes are and how well the network will generalise.

## In Plain Words
All the internal activity a network produces for one category — say, every possible way to write "the number 5 in modular arithmetic" — forms a blob in a high-dimensional space. The shape of this blob matters:
- **Small, tight blob** (low radius) = all category inputs look the same inside the network → easy to classify.
- **Low-dimensional blob** = the category lives on a simple manifold, not scattered randomly → efficient representation.
- **Well-separated blobs** = different categories are far apart → low classification error.

## Geometric Measures of Manifold Quality

Three key geometric properties, introduced in [[Li - Representations and Generalization in Artificial and Brain Neural Networks]]:

| Measure | Definition | What it means |
|---|---|---|
| **Dimension** | Effective number of dimensions of the manifold | Lower = more structured, more efficient |
| **Radius** | Average distance from class mean to class examples | Lower = less within-class variability (NC1 is the limit: radius → 0) |
| **Margin** | Minimum distance between different class manifolds | Higher = more separable, better generalisation |

These three together determine the **manifold capacity** — roughly, how many classes can be linearly decoded from this representation:
$$\text{capacity} \propto \frac{1}{R^2 \cdot D}$$
where $R$ = radius and $D$ = dimension. High capacity = many classes can be decoded → good representation.

## The Grokking Connection

In grokking, the manifold geometry evolves dramatically:

| Phase | Dimension | Radius | Margin |
|---|---|---|---|
| **Pre-grok (memorisation)** | High (representations scattered) | High (no within-class compression) | Low (overlapping manifolds) |
| **Plateau** | Slowly decreasing (circuit forming) | Slowly decreasing | Slowly increasing |
| **Post-grok** | Low (Fourier representation is 2D per frequency) | Near zero (each class = a point on the circle) | High (ETF-like separation) |

The grokking transition is a sudden decrease in manifold radius and dimension, combined with a sudden increase in margin. Measuring these during the plateau could detect grokking early — a geometric predictor.

## Neural Manifolds and Neural Collapse

[[Neural Collapse]] (NC1) is the terminal limit of the radius → 0 trajectory: the manifold collapses to a single point per class. This is the most extreme version of manifold tightening. The steps are:

1. High-dimensional, high-radius scattered manifold (random initialisation).
2. Manifold compresses: dimension decreases as the network discovers relevant features.
3. Radius decreases: within-class variability collapses as the rule is learned.
4. Final state: point-like manifolds (NC1) arranged in a [[Simplex ETF]] (NC2).

Step 4 is neural collapse; steps 2–3 are the intermediate manifold dynamics that could serve as grokking predictors.

## Manifolds in the Fourier Circuit

For the grokking task with $p = 97$ classes, the grokked representation places each class on a circle (the Fourier embedding). This means:
- Each class's manifold has **radius ≈ 0** (each class is a single point on the circle).
- The manifold **dimension ≈ 2K** (where $K$ is the number of Fourier frequencies used), independent of input diversity.
- Class manifolds are **equidistant** (equal spacing on the circle → Simplex ETF-like separation).

This is a highly structured, highly compressed representation — exactly what "good manifold geometry" looks like.

## Biological Connection

The same manifold geometry principles appear in **biological neural representations** — [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] shows that mammalian visual cortex representations have manifold properties that predict generalisation in the same way they do for artificial networks. This suggests manifold geometry captures something fundamental about how learning systems organise information, across biological and artificial implementations.

## Key Insights
- Manifold **dimension and radius** govern few-shot generalisation capacity ([[Li - Representations and Generalization in Artificial and Brain Neural Networks]]).
- The extreme case of manifold tightening is **[[Neural Collapse]]** (radius → 0, NC1).
- Manifold geometry during the plateau should change before test accuracy — a potential predictor family.
- The grokked Fourier circuit produces point-like manifolds on a circle — the task-specific version of optimal manifold geometry.
- Biological neural representations obey the same geometric principles as artificial ones.

## Evidence
[[Li - Representations and Generalization in Artificial and Brain Neural Networks]] (manifold geometry framework + biological validation); [[Papyan - Prevalence of Neural Collapse]] (terminal-phase limit of manifold tightening).

## Relationship to Other Concepts
- Quantifies [[Feature Learning]] (better features = better manifold geometry).
- Extreme limit: [[Neural Collapse]] (NC1 = radius → 0, NC2 = Simplex ETF).
- Candidate geometric grokking order parameter ([[Phase Transition]]).
- Connects to [[Margin and Robustness]] (inter-manifold distance = classification margin).

## Open Questions
Does manifold dimension or radius drop sharply at the grokking transition, providing lead time? Which manifold metric fires earliest? Can manifold-based measures serve as transferable grokking predictors (thesis RQ3)?

---
## Related Notes
- [[Feature Learning]] · [[Neural Collapse]] · [[Simplex ETF]] · [[Margin and Robustness]]
- [[Li - Representations and Generalization in Artificial and Brain Neural Networks]]
- [[Papyan - Prevalence of Neural Collapse]] · [[Phase Transition]] · [[Grokking Predictors]]
