---
tags: [literature, double-descent, bias-variance, interpolation, theory]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Bias-Variance Tradeoff]] · [[Double Descent]]

# Rocks — Memorizing Without Overfitting

# Citation
Rocks, J. W., & Mehta, P. (2020/2022). *Memorizing without overfitting: Bias, variance, and interpolation in over-parameterized models.* arXiv:2010.13933 [stat.ML].

# The Gist (Plain Words)
Carefully separates the two sources of error in oversized models and shows they can memorise the training data perfectly yet still not overfit.

# Research Question
How do **bias** and **variance** behave in overparameterized models, and why can a model **memorise** the training data yet still **generalise** ("memorize without overfitting")?

# Methodology
Statistical-physics derivation of **analytic bias and variance** in two minimal models: linear regression and two-layer nets with nonlinear data. Disentangled architecture effects from data-sampling effects; related results to [[Random Matrix Theory]].

# Key Findings
- Increasing parameters drives a **phase transition**: training error → 0 and test error **diverges via variance** at the threshold (bias stays finite).
- **Beyond** the threshold, both bias and variance **decrease** — opposite of classical intuition (the second descent).
- Overparameterized models can **overfit even without noise** and show **bias even when student matches teacher**.

# Strengths
- Precise, interpretable bias/variance decomposition of the [[Double Descent]] peak.
- Clarifies the variance origin of the interpolation spike.

# Limitations
- Minimal models; real deep nets only by analogy.
- No feature-learning / training-time dynamics.

# Relation to Other Papers
- Bias/variance complement to [[Mei - Generalization Error of Random Features Regression]] and RMT dynamics of [[Advani - High-dimensional Dynamics of Generalization Error]].
- "Memorize without overfitting" reframes [[Memorization]] vs [[Generalization]].

# Relevance to Thesis
Moderate. Supplies the conceptual vocabulary (variance spike at interpolation; memorisation ≠ overfitting) that grokking inherits over the time axis.

# Key Quotes
> "increasing the number of fit parameters leads to a phase transition where the training error goes to zero and the test error diverges as a result of the variance (while the bias remains finite)."

# Tags
#double-descent #bias-variance #interpolation #theory

---
## Related Notes
- [[Bias-Variance Tradeoff]] · [[Double Descent]] · [[Memorization]] · [[05 - Memorization vs Generalization]]
