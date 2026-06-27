---
tags: [literature, dynamics, generalization, history, foundational]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Generalization]] · [[02 - The Grokking Training Dynamics]]

# Baldi — Temporal Evolution of Generalization in Linear Networks

# Citation
Baldi, P., & Chauvin, Y. (1991). *Temporal evolution of generalization during learning in linear networks.* Neural Computation 3(4), 589–603.

# The Gist (Plain Words)
Even simple linear networks, back in 1991, were shown to learn in fits and starts — long flat plateaus and well-timed stopping points. It is the earliest ancestor of grokking's plateau.

# Research Question
How does **generalization (validation) error evolve over training time** — not just as a function of architecture/sample count — in a tractable model, and what governs **overfitting onset, optimal stopping, and plateaus**?

# Methodology
Analytical study of **feedforward linear networks** trained by gradient descent on quadratic error (learning the identity map with noise). Derived closed-form behaviour of the **validation function** over training time as a function of initial conditions and noise.

# Key Findings
- With **sufficiently small initial weights**, the validation function has a **unique minimum** → a computable **optimal stopping time**.
- For other regimes: **multiple local minima** (up to $n$) and **long but finite plateau effects** in the validation curve.
- The complex temporal generalization phenomena seen in nonlinear simulations are **already present in the linear case**.

# Strengths
- The **earliest** (1991) analytical treatment of *training-time* generalization dynamics — a direct conceptual ancestor of grokking.
- Predicts **plateaus** and non-monotonic validation curves from first principles.
- Highlights the decisive role of **small initialization** (echoed decades later).

# Limitations
- Linear networks / identity task; no feature learning or nonlinearity.
- Quadratic-error, Gaussian-noise idealisation.

# Relation to Other Papers
- The 1991 origin of the **temporal** view later developed by [[Advani - High-dimensional Dynamics of Generalization Error]] (small-init, frozen subspace) and made phenomenological in grokking ([[02 - The Grokking Training Dynamics]]).
- "Plateau then change" prefigures the grokking plateau; small-init importance reappears throughout.

# Relevance to Thesis
High (conceptual/historical). Establishes that **plateaus and delayed generalization are intrinsic to learning dynamics**, even in linear models — grounding grokking as an extreme, nonlinear instance and anchoring the [[Research Timeline]].

# Key Quotes
> "the validation function can have ... multiple local minima (at most n) of variable depth and long but finite plateau effects."

# Tags
#dynamics #generalization #history #linear-networks #optimal-stopping #foundational

---
## Related Notes
- [[02 - The Grokking Training Dynamics]] · [[Advani - High-dimensional Dynamics of Generalization Error]] · [[Generalization]] · [[Research Timeline]]
