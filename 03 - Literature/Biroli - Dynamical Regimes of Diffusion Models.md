---
tags: [literature, diffusion, phase-transition, physics, generative]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Phase Transition]]

# Biroli — Dynamical Regimes of Diffusion Models

# Citation
Biroli, G., Bonnaire, T., de Bortoli, V., & Mézard, M. (2024). *Dynamical regimes of diffusion models.* Nature Communications 15 (s41467-024-54281-3).

# The Gist (Plain Words)
Image-generating "diffusion" models pass through sudden switches as they remove noise — first deciding the broad category, later the fine details — and these switches can be read off from the data's structure.

# Research Question
What **distinct dynamical regimes** govern the generative (backward) process of diffusion models in the high-dimensional, large-dataset limit, and what controls the transitions between them?

# Methodology
Statistical-physics analysis with both data dimension and sample size large and an optimally-trained score. Analytic solutions for Gaussian mixtures + numerical experiments on real data.

# Key Findings
- Three regimes: (1) **pure Brownian** noise; (2) a **speciation transition** where broad class structure emerges (like symmetry breaking); (3) a **collapse** phase attracted to a specific training point (glass-like condensation).
- **Speciation time** is read from the **spectrum of the data correlation matrix**; **collapse time** from an **excess-entropy** measure → a "curse of dimensionality" for diffusion.

# Strengths
- Maps modern generative AI onto sharp, computable phase transitions.
- Demonstrates the same spectral/entropy toolkit used for grokking order parameters.

# Limitations
- Diffusion generation, not classification/grokking; optimal-score idealisation.
- Gaussian-mixture analytics; real-data results numerical.

# Relation to Other Papers
- Extends the [[Phase Transition]] programme of [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]] and [[Spigler - A Jamming Transition Affects Generalization]] to generative models.
- Spectral-of-correlation-matrix method parallels [[Random Matrix Theory]] usage in [[Advani - High-dimensional Dynamics of Generalization Error]].

# Relevance to Thesis
Lower (analogical). Shows transitions and order parameters are pervasive in deep learning and how to compute them — useful framing and potential methodology transfer, but not grokking-specific.

# Key Quotes
> "the generative dynamics ... first encounters a speciation transition, where the broad structure of the data emerges ... followed by a collapse phase ... similar to condensation in a glass phase."

# Tags
#diffusion #phase-transition #physics #generative #spectral

---
## Related Notes
- [[Phase Transition]] · [[Random Matrix Theory]] · [[Phase Transitions Across Models]] · [[12 - Modern Developments]]
