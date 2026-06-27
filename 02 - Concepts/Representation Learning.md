---
tags: [concept, representation, feature-learning]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Representation Learning

## Definition
**Representation learning** is the process by which a network builds internal features — transforming raw inputs (tokens, pixels) into abstract, task-relevant vectors — such that solving the task from those features becomes easy. The quality of these learned representations largely determines generalisation. Grokking is, at heart, a story about representation learning: the network fails to generalise during memorisation because it has the *wrong* internal representation, and succeeds only when it discovers the *right* one.

## In Plain Words
A network doesn't classify inputs directly. It first transforms them into "hidden" features — a new language in which the task is simple. Bad features make generalisation impossible; good features make it trivial. Grokking is the moment the network finally builds the right features for the rule it's meant to learn: embedding each residue class as a point on a circle (the [[Fourier Features|Fourier representation]]) rather than as an arbitrary lookup-table entry.

## Representations in Grokking: Before vs After

| Phase | What the representation looks like | Can it generalise? |
|---|---|---|
| **Pre-grok (memorisation)** | Arbitrary, scattered high-dimensional embeddings for each training input | No — test inputs fall between training examples with no structure to interpolate |
| **Post-grok (generalisation)** | Each residue $k$ embedded as angles $(\cos(2\pi\omega k/p), \sin(2\pi\omega k/p), \ldots)$ across $K$ frequencies | Yes — every input pair maps to a well-defined circular representation; addition = angle addition |

The grokking transition *is* the moment the network switches from the first type to the second — a complete rebuilding of the internal representation.

## How to Measure Representation Quality

Several complementary measurement approaches are used in this vault:

### 1. Neural Manifold Geometry ([[Neural Manifolds]])
For each class, the set of representation vectors forms a manifold. Quality is measured by:
- **Manifold dimension** (lower = more structured, more useful).
- **Manifold radius** (lower = less within-class variability).
- **Margin between manifolds** (higher = better separability).

### 2. Neural Collapse Metrics ([[Neural Collapse]])
In the terminal phase, a well-trained network's class representations collapse to points in a [[Simplex ETF]] geometry. Measuring NC1 (within-class variability → 0) and NC2 (class means → ETF) quantifies how close the representation is to the optimal geometry.

### 3. Weight Spectra ([[Heavy-Tailed Self-Regularization]])
The power-law exponent $\alpha$ of a layer's weight matrix eigenvalues: smaller $\alpha$ indicates better-structured representations. This is data-free — you only need the weights.

### 4. Probing Tasks ([[Mechanistic Interpretability]])
Train a linear probe (a small classifier) on the internal representation of a specific layer. If the probe achieves high accuracy on the task's structure (e.g., "is this the right residue class?"), the representation has encoded the relevant structure.

## Representation Learning vs Feature Learning

[[Feature Learning]] and representation learning are closely related but have different emphases:
- **Feature learning** emphasises the *change* in representations over training — the network is not just using fixed features but inventing new ones (contrasted with the lazy/NTK regime).
- **Representation learning** emphasises the *quality* and *geometry* of the final features — where did the network end up?

Grokking involves both: the network changes its representations (feature learning event) *and* builds high-quality structured representations (good representation learning outcome).

## Representation Learning as a Predictor

The thesis hypothesis is that **grokking predictors are measures of representation quality** that change *before* test accuracy. Specifically:
- The network begins building the correct representation (Fourier angles) during the plateau.
- Predictor signals fire when this new representation reaches a threshold quality.
- Test accuracy only jumps when the representation is complete enough to surpass the memorising solution.

The question is: which representation-quality metric fires earliest? (Thesis RQ1, RQ2.)

## Key Insights
- Networks that **learn representations** beat fixed-feature ("kernel") models when the task structure must be discovered ([[Feature Learning]], [[Neural Tangent Kernel]]).
- Representation quality can be read from **geometry** (manifold dimension/radius — [[Li - Representations and Generalization in Artificial and Brain Neural Networks]]) or **spectra** (heavy-tailed weights — [[Heavy-Tailed Self-Regularization]]).
- The same geometric principles appear in biological neural representations, suggesting they capture something fundamental ([[Neural Manifolds]]).
- Grokking *is* a representation-learning event: the network re-learns its internal representation at the generalisation transition.

## Evidence
- [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] — links representation geometry to generalisation.
- [[Papyan - Prevalence of Neural Collapse]] — terminal-phase representations take a fixed, simple geometric shape.
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — tracks the forming Fourier representation directly.

## Relationship to Other Concepts
- Built on [[Feature Learning]] (the change in representations); measured via [[Neural Manifolds]], [[Neural Collapse]], [[Simplex ETF]].
- Failure mode: [[Shortcut Learning]] (bad representation that works on training data only).
- Drives [[Circuit Formation]] (the generalising representation implements a specific algorithm).
- Measured by the [[Grokking Predictors]] during training.

## Open Questions
Which representation-geometry metric moves earliest at the grokking transition? Can manifold dimension or radius serve as a lead-time predictor? When exactly (in terms of training step) does the Fourier representation begin to form?

---
## Related Notes
- [[Feature Learning]] · [[Neural Manifolds]] · [[Neural Collapse]] · [[Simplex ETF]]
- [[Fourier Features]] · [[Circuit Formation]] · [[Shortcut Learning]]
- [[Grokking Predictors]] · [[Heavy-Tailed Self-Regularization]]
- [[Li - Representations and Generalization in Artificial and Brain Neural Networks]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
