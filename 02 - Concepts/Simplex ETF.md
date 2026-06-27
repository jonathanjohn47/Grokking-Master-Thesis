---
tags: [concept, geometry, neural-collapse, terminal-phase]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Simplex Equiangular Tight Frame (Simplex ETF)

## Definition
A **Simplex Equiangular Tight Frame (Simplex ETF)** is the unique geometry in which $K$ unit vectors in $\mathbb{R}^d$ are arranged with equal angles between every pair and equal norms — the most symmetric, maximally separable arrangement possible. It is the geometry that the last-layer class representations of a well-trained neural network converge to, as described by [[Neural Collapse]] (NC2).

## The Formal Definition

A set of class mean vectors $\{\mu_1, \ldots, \mu_K\} \subset \mathbb{R}^d$ (with $d \ge K-1$) forms a Simplex ETF when:

$$\frac{\mu_i^T \mu_j}{\|\mu_i\| \|\mu_j\|} = \begin{cases} 1 & i = j \\ -\frac{1}{K-1} & i \ne j \end{cases}$$

In words: every pair of class means has the same inner product $-1/(K-1)$, i.e., all pairwise angles are equal to $\arccos(-1/(K-1))$. For $K$ classes:
- $K = 2$: two vectors pointing in opposite directions (angle = 180°).
- $K = 3$: three vectors at equal 120° angles — a triangle.
- $K = 4$: four vectors forming a tetrahedron (equal angles of ~109.5°).
- $K = 97$ (grokking): 97 vectors at equal angles in $\mathbb{R}^{96}$.

The "tight frame" property ensures the vectors form a complete, uniform covering of the relevant subspace.

## In Plain Words
Place $K$ arrows from the origin, spread as evenly as possible so no two crowd each other — like the corners of a perfectly balanced shape in $K-1$ dimensions. "Equiangular" = every pair sits at the same angle. "Tight frame" = they cover the space evenly. This is geometry's definition of **maximally fair class separation**: no class is favoured or crowded by others.

## Why Training Converges to This Geometry

The Simplex ETF is the **global optimiser** of a simplified neural collapse model. [[Mixon - Neural Collapse with Unconstrained Features]] proved:

Given $K$ classes with equal numbers of training examples and a loss of the form $\mathcal{L} = \text{cross-entropy} + \frac{\lambda}{2}\|\theta\|^2$, treating last-layer features as free variables, the unique global minimiser assigns class means to a Simplex ETF configuration.

The intuition: [[Weight Decay]] pushes class means toward the origin. [[Cross-Entropy Loss]] pushes class means apart (for better classification). The unique balance point that minimises the total objective is the most symmetric arrangement: a Simplex ETF.

Training dynamics are therefore *drawn toward* this configuration under any reasonable initialisation — it is not a coincidence or an approximation, but the theoretical attractor.

## The Geometry in Grokking

For the grokking task with $p = 97$ classes, the [[Fourier Features|Fourier circuit]] naturally produces a different geometry: class representations form a **circular Fourier basis** rather than a Simplex ETF. However, the principles are related:

- Both are highly structured, low-dimensional representations.
- Both maximise separation given their respective constraints.
- The Simplex ETF is the terminal-phase attractor for classification tasks; the Fourier circle is the task-specific structure for modular addition.

Whether the representations in a grokked [[Transformer]] converge toward a Simplex ETF *or* a Fourier circle structure (or both) is a research question related to the thesis.

## Failure Mode: Minority Collapse

When training data is class-imbalanced, the Simplex ETF breaks:
- Majority class means remain separated.
- Minority class means collapse toward each other or toward the majority means.
- This is **[[Minority Collapse]]**, studied in [[Fang - Layer-Peeled Model and Minority Collapse]].

For grokking on balanced tasks (equal number of examples for each residue class), the ETF should form cleanly.

## Measurement

The Simplex ETF structure can be measured directly:
1. Compute per-class mean representations $\mu_k$ from the final layer.
2. Compute the Gram matrix $G_{ij} = \mu_i^T \mu_j / (\|\mu_i\|\|\mu_j\|)$.
3. Compare to the ideal ETF Gram matrix $G^*_{ij} = \delta_{ij} - 1/(K-1)(1 - \delta_{ij})$.
4. The **ETF deviation** $\|G - G^*\|_F / \|G^*\|_F$ is a continuous measure of how close the geometry is to ideal.

This deviation is a candidate [[Grokking Predictors|order parameter]] for the grokking transition: does it drop sharply at the moment test accuracy jumps?

## Key Insights
- The angle between any two class means in a Simplex ETF is exactly $\arccos(-1/(K-1))$ — a clean, checkable signature.
- It is the **global optimiser** of simplified last-layer models, so training dynamics are *drawn* toward it ([[Mixon - Neural Collapse with Unconstrained Features]]).
- Balanced data → clean ETF; severe class imbalance → the ETF breaks ([[Minority Collapse]]).
- It maximises the minimum margin between classes — the most robust geometry for classification.

## Evidence
- [[Papyan - Prevalence of Neural Collapse]] — measures the ETF forming empirically across 3 architectures × 7 datasets.
- [[Mixon - Neural Collapse with Unconstrained Features]] and [[Fang - Layer-Peeled Model and Minority Collapse]] — prove it is the optimal and attractor geometry.

## Relationship to Other Concepts
- The geometric core of [[Neural Collapse]] (NC2 specifically).
- Its failure is [[Minority Collapse]].
- A candidate [[Grokking Predictors|order parameter]] for grokking structure formation.
- Driven by [[Cross-Entropy Loss]] + [[Weight Decay]] together.
- The [[Layer-Peeled Model]] is the simplified model that admits an exact ETF proof.

## Open Questions
Does a Simplex ETF form in the embedding layer of a grokked transformer at the generalisation transition? Or does the Fourier circle structure take the ETF's role in this task? Can ETF deviation serve as a grokking predictor?

---
## Related Notes
- [[Neural Collapse]] · [[Minority Collapse]] · [[Layer-Peeled Model]]
- [[Papyan - Prevalence of Neural Collapse]] · [[Mixon - Neural Collapse with Unconstrained Features]]
- [[Fang - Layer-Peeled Model and Minority Collapse]]
- [[Cross-Entropy Loss]] · [[Weight Decay]] · [[Grokking Predictors]]
