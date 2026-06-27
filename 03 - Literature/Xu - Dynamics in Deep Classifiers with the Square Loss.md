---
tags: [literature, neural-collapse, dynamics, square-loss, generalization-bounds]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Neural Collapse]] · [[Weight Decay]]

# Xu — Dynamics in Deep Classifiers with the Square Loss

# Citation
Xu, M., Rangamani, A., Liao, Q., Galanti, T., & Poggio, T. (2023). *Dynamics in Deep Classifiers Trained with the Square Loss: Normalization, Low Rank, Neural Collapse, and Generalization Bounds.* Research (AAAS), 0024.

# The Gist (Plain Words)
With square-loss training plus normalisation and weight decay, networks provably squeeze their representations into a low-rank, collapsed shape that generalises well.

# Research Question
When and why does **square-loss** training generalise for classification, and what dynamics (normalisation, low rank, **[[Neural Collapse]]**) does gradient descent induce?

# Methodology
Theoretical analysis of GD dynamics under square loss with normalisation and **[[Weight Decay]]**; derive emergence of low-rank, collapsed solutions and **generalisation bounds** tied to normalised margin.

# Key Findings
- Normalisation + weight decay drive **low-rank** weight matrices and **neural collapse**.
- **"Zero square loss does not by itself imply large margin or good classification"** — among interpolating solutions, only some generalise.
- Provides generalisation bounds linking margin/geometry to test performance.

# Strengths
- Bridges loss choice → dynamics → geometry → generalisation in one framework.
- Makes the **"many zero-loss solutions differ"** point precise — central to grokking.

# Limitations
- Square-loss / specific normalisation assumptions; idealised.
- Not a grokking experiment; transformer/algorithmic case is by analogy.

# Relation to Other Papers
- Dynamic extension of [[Papyan - Prevalence of Neural Collapse]] and [[Mixon - Neural Collapse with Unconstrained Features]].
- The author "Xu" lineage connects to the thesis's **Commutator Defect** and **Weight-Space PCA** predictors ([[The Nine Predictors]]).
- Margin/low-rank view complements [[Li - Representations and Generalization in Artificial and Brain Neural Networks]].

# Relevance to Thesis
High. Justifies *why* a generalising solution is selected from the zero-loss manifold (low norm, low rank, large margin) — the mechanism grokking exploits; ties to weight-decay-driven predictors.

# Key Quotes
> "zero square loss does not imply by itself neither large margin nor good classification on a test set."

# Tags
#neural-collapse #square-loss #low-rank #weight-decay #generalization-bounds

---
## Related Notes
- [[Neural Collapse]] · [[Weight Decay]] · [[05 - Memorization vs Generalization]] · [[The Nine Predictors]]
