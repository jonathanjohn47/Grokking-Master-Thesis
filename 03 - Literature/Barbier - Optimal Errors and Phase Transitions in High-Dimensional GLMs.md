---
tags: [literature, phase-transition, information-theory, theory, glm]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Phase Transition]]

# Barbier — Optimal Errors and Phase Transitions in High-Dimensional GLMs

# Citation
Barbier, J., Krzakala, F., Macris, N., Miolane, L., & Zdeborová, L. (2017). *Optimal errors and phase transitions in high-dimensional generalized linear models.* PNAS / arXiv.

# The Gist (Plain Words)
For a clean family of models, the authors pin down the exact tipping point where a problem flips from unlearnable to learnable — a sharp phase transition.

# Research Question
What are the **information-theoretically optimal** estimation and generalisation errors for high-dimensional **generalized linear models** (the building blocks of neural-net layers), and where are the **sharp phase transitions** between learnable and non-learnable regimes?

# Methodology
Rigorously evaluated the **mutual information / free entropy** of random GLMs in the high-dimensional limit (samples and dimension large, ratio fixed). Proved decades-old **replica-method** conjectures; connected optimal errors to the **approximate message-passing (AMP)** algorithm.

# Key Findings
- Established **Bayes-optimal** estimation/generalisation errors for a class of GLMs.
- Located **sharp phase transitions** separating learnable from non-learnable regions, and where AMP achieves optimality.
- Rigorous foundation for "learning as a phase transition."

# Strengths
- Mathematical rigor for transitions previously only conjectured.
- Provides the **information-theoretic** notion of a sharp learnability threshold.

# Limitations
- GLMs / single-layer; deep nonlinear nets out of scope.
- Random-data assumptions; not training dynamics.

# Relation to Other Papers
- Rigorous backbone of the [[Phase Transition]] framing shared with [[Spigler - A Jamming Transition Affects Generalization]], [[Biroli - Dynamical Regimes of Diffusion Models]], [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]].
- Mutual-information optimality connects to [[Information-Theoretic Measures]].

# Relevance to Thesis
Moderate (foundational). Supplies the rigorous concept of a sharp learnable/non-learnable transition — the formal ancestor of grokking's sudden jump.

# Key Quotes
> "we ... locate the associated sharp phase transitions separating learnable and nonlearnable regions."

# Tags
#phase-transition #information-theory #glm #theory #replica-method

---
## Related Notes
- [[Phase Transition]] · [[Information-Theoretic Measures]] · [[08 - Phase Transitions in Learning]]
