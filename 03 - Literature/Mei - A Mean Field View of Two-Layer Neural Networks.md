---
tags: [literature, mean-field, dynamics, feature-learning, theory, landscape]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Mean-Field Limit]] · [[Feature Learning]]

# Mei — A Mean Field View of the Landscape of Two-Layer Neural Networks

# Citation
Mei, S., Montanari, A., & Nguyen, P.-M. (2018). *A mean field view of the landscape of two-layer neural networks.* PNAS / arXiv:1804.06561.

# The Gist (Plain Words)
For very wide two-layer networks, training can be rewritten as a single clean, flowing equation — and that equation provably reaches near-perfect solutions.

# Research Question
Does **SGD on two-layer networks** converge to a global optimum of the (non-convex) risk, and *why* do the solutions it reaches generalize well?

# Methodology
Took the **mean-field scaling limit** (infinitely many hidden units, weights as a probability distribution). Proved SGD dynamics is captured by a **non-linear PDE — "distributional dynamics" (DD)**. Analysed specific examples; proved convergence of noisy SGD.

# Key Findings
- In the mean-field limit, SGD = **gradient flow on a distribution of neurons** governed by a PDE.
- For several cases, DD proves convergence to **near-ideal generalization error**, "averaging out" landscape complexity.
- A rigorous **feature-learning (rich) regime** — distinct from the lazy/[[Neural Tangent Kernel|NTK]] limit where features are frozen.

# Strengths
- Rigorous global-convergence results for a non-convex problem.
- Provides the mathematical home of the **rich / feature-learning** regime that grokking requires.

# Limitations
- Two-layer, infinite-width idealisation; finite-width corrections nontrivial.
- Describes convergence, not the *delayed* (plateau) phenomenology of grokking.

# Relation to Other Papers
- The **rich-regime counterpart** to the lazy-regime kernel theory of [[Canatar - Spectral Bias and Task-Model Alignment]]; together they frame the **lazy vs feature-learning** dichotomy ([[Feature Learning]]).
- Distributional-dynamics view complements the RMT training dynamics of [[Advani - High-dimensional Dynamics of Generalization Error]] and the geometry of [[Li - Representations and Generalization in Artificial and Brain Neural Networks]].

# Relevance to Thesis
Moderate. Supplies the theory of **how feature-learning solutions form under SGD** — the regime in which grokking lives — and a candidate language (distributional dynamics) for modelling the plateau-to-grok transition.

# Key Quotes
> "in a suitable scaling limit – SGD dynamics is captured by a certain non-linear partial differential equation that we call distributional dynamics ... DD can be used to prove convergence of SGD to networks with nearly-ideal generalization error."

# Tags
#mean-field #dynamics #feature-learning #landscape #sgd #theory

---
## Related Notes
- [[Mean-Field Limit]] · [[Feature Learning]] · [[Neural Tangent Kernel]] · [[Advani - High-dimensional Dynamics of Generalization Error]]
