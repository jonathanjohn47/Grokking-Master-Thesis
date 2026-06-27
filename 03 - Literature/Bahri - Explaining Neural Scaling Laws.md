---
tags: [literature, scaling-laws, spectral, kernel, theory]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Neural Scaling Laws]]

# Bahri — Explaining Neural Scaling Laws

# Citation
Bahri, Y., Dyer, E., Kaplan, J., Lee, J., & Sharma, U. (2021/2024). *Explaining neural scaling laws.* arXiv:2102.06701 (PNAS).

# The Gist (Plain Words)
Explains why bigger models and bigger datasets give smoothly, predictably lower error — and traces those neat "scaling laws" back to the underlying shape of the data and the kernel.

# Research Question
Why does test loss follow **power-law scaling** with dataset size $D$ and parameter count $P$, and what *mechanisms* set the exponents?

# Methodology
Theory identifying **four scaling regimes**: **variance-limited** and **resolution-limited**, each for $D$ and for $P$. Variance-limited follows from a well-behaved infinite-data/infinite-width limit; resolution-limited from models **resolving a smooth data manifold**, linked to the **spectrum of a kernel**. Tested on random-feature and pretrained models across standard architectures.

# Key Findings
- **Four scaling regimes** with distinct mechanisms; loss-improvement is not one phenomenon.
- Resolution-limited exponents derive from the **kernel/data-manifold spectrum** (power-law eigenvalue decay).
- Evidence for a **duality** relating large-width and large-data resolution-limited exponents.

# Strengths
- A mechanistic **taxonomy** for scaling, connecting exponents to spectral/manifold structure.
- Bridges empirical scaling laws with [[Random Matrix Theory|spectral]] theory.

# Limitations
- Loss-scaling focus, not grokking dynamics or sudden transitions.
- Idealised limits; algorithmic-task grokking not addressed.

# Relation to Other Papers
- Shares the **kernel-spectrum / data-manifold** machinery with [[Canatar - Spectral Bias and Task-Model Alignment]] (eigenvalue decay → generalization) and the geometry of [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] ([[Neural Manifolds]]).
- Spectral mechanism complements [[Mei - Generalization Error of Random Features Regression]] and [[Random Matrix Theory]].

# Relevance to Thesis
Moderate (context). Frames *how* generalization improves with scale and ties it to spectra — useful for situating grokking among smooth scaling phenomena and for the "is grokking a scaling/transition effect?" question. Motivates [[Neural Scaling Laws]].

# Key Quotes
> "We identify variance-limited and resolution-limited scaling behavior for both dataset and model size, for a total of four scaling regimes ... resolution-limited [scaling can be obtained] from the spectrum of certain kernels."

# Tags
#scaling-laws #spectral #kernel #data-manifold #theory

---
## Related Notes
- [[Neural Scaling Laws]] · [[Canatar - Spectral Bias and Task-Model Alignment]] · [[Neural Manifolds]] · [[Random Matrix Theory]]
