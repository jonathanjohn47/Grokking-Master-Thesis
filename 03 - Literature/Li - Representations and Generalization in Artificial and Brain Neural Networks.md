---
tags: [literature, representations, neural-manifolds, feature-learning, neuroscience]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Neural Manifolds]] · [[Feature Learning]]

# Li — Representations and Generalization in Artificial and Brain Neural Networks

# Citation
Li, Q., Sorscher, B., & Sompolinsky, H. (2024). *Representations and generalization in artificial and brain neural networks.* PNAS (Perspective).

# The Gist (Plain Words)
Links how well a network generalises to the *shape* of its internal representations, and shows the same geometric ideas apply to both artificial networks and real brains.

# Research Question
What links a network's **representational geometry** to its **generalisation**, in both artificial and biological networks, and how does **[[Feature Learning]]** (especially in the thermodynamic limit) produce good representations?

# Methodology
Perspective/synthesis introducing two hypotheses: (1) **[[Neural Manifolds|neural-manifold geometry]]** (dimension, radius) are powerful **order parameters** linking substrate to generalisation; (2) **thermodynamic-limit theory of wide-network learning** gives mechanistic insight into how representations form. Reviews visual-object-recognition geometry and learning dynamics.

# Key Findings
- Manifold **dimension/radius** predict few-shot generalisation capacity.
- **Feature-learning** theory (beyond lazy/NTK) explains how desired geometries arise, including the role of **[[Weight Decay|weight-norm regularisation]]**, architecture, and hyperparameters.
- Connects representational drift and learning dynamics across ML and neuroscience.

# Strengths
- Unifying, cross-disciplinary order-parameter framework.
- Emphasises **feature learning** as the key to real generalisation — exactly what grokking exhibits.

# Limitations
- Perspective, not a single experiment; breadth over depth.
- Geometry-to-grokking link is suggested, not demonstrated.

# Relation to Other Papers
- Argues beyond the lazy-regime limits of [[Canatar - Spectral Bias and Task-Model Alignment]].
- Manifold tightening connects to [[Neural Collapse]] ([[Papyan - Prevalence of Neural Collapse]]).
- Weight-norm/geometry view aligns with [[Xu - Dynamics in Deep Classifiers with the Square Loss]].

# Relevance to Thesis
Moderate–high. Provides **geometric order parameters** (manifold dimension/radius) as candidate grokking predictors and frames grokking as a feature-learning/geometry event.

# Key Quotes
> "the geometric properties of the neural manifolds ... are powerful order parameters. They link the neural substrate to the generalization capabilities."

# Tags
#representations #neural-manifolds #feature-learning #neuroscience #geometry

---
## Related Notes
- [[Neural Manifolds]] · [[Feature Learning]] · [[Neural Collapse]] · [[10 - Mechanistic Explanations and Circuit Formation]]
