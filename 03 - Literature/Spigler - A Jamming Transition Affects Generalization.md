---
tags: [literature, phase-transition, jamming, double-descent, physics]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Jamming Transition]]

# Spigler — A Jamming Transition Affects Generalization

# Citation
Spigler, S., Geiger, M., d'Ascoli, S., Sagun, L., Biroli, G., & Wyart, M. (2018/2019). *A jamming transition from under- to over-parametrization affects generalization in deep learning.* arXiv:1810.09665 [cs.LG].

# The Gist (Plain Words)
The boundary between too-small and too-big networks behaves like sand "jamming" into a rigid pile, and test error is worst right at that boundary.

# Research Question
Does the under- to over-parameterized boundary behave like a physical **jamming transition**, and how does crossing it shape generalisation?

# Methodology
Studied generalisation vs network width across the transition; analysed loss-landscape constraints (jamming analogy from granular media), with and without **early stopping**.

# Key Findings
- The transition is a **[[Jamming Transition]]**: below it, constraints create stable poor minima; above it, abundant flat directions make fitting easy.
- Generalisation error shows **three phases** vs width: decay → **cusp at the transition** → slow decay to an asymptote.
- The cusp is the [[Double Descent]] peak; **early stopping removes the cusp**, localising overfitting to the transition's neighbourhood.

# Strengths
- Physical, intuitive account of *why* overparameterized training avoids bad minima.
- Directly ties the interpolation peak to a known physics transition.

# Limitations
- Empirical/physical analogy; not fully rigorous for deep nets.
- Width-axis (static), not training-time dynamics.

# Relation to Other Papers
- Physics realisation of the [[Interpolation Threshold]] peak from [[Mei - Generalization Error of Random Features Regression]] / [[Rocks - Memorizing Without Overfitting]].
- Shares authors/lineage with [[Biroli - Dynamical Regimes of Diffusion Models]] (statistical-physics of learning).

# Relevance to Thesis
Moderate. Provides the jamming/landscape intuition for a metastable plateau that "un-jams" at grokking; reinforces the phase-transition framing.

# Key Quotes
> "a phase transition, analogous to the jamming transition of granular media, delimits the over- and under-parametrized regimes ... the generalization error displays three phases ... where it displays a cusp."

# Tags
#phase-transition #jamming #double-descent #physics #landscape

---
## Related Notes
- [[Jamming Transition]] · [[Interpolation Threshold]] · [[Double Descent]] · [[08 - Phase Transitions in Learning]]
