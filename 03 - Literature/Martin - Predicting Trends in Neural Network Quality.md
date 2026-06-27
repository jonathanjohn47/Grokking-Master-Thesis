---
tags: [literature, spectral, rmt, predictors, htsr]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Heavy-Tailed Self-Regularization]]

# Martin — Predicting Trends in Neural Network Quality

# Citation
Martin, C. H., Peng, T. (Serena), & Mahoney, M. W. (2021). *Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data.* Nature Communications 12:4122.

# The Gist (Plain Words)
You can rank how well-trained a network is purely from the statistics of its weights — no test data required — using a heavy-tail measure called alpha.

# Research Question
Can you predict the **quality/generalisation** of a trained network using **only its weights** — no training data, no test data, no labels?

# Methodology
Meta-analysis of **hundreds of publicly available pretrained models**. Compared **norm-based** capacity metrics against **power-law (heavy-tailed) spectral** metrics from the **Theory of Heavy-Tailed Self-Regularization (HTSR)**: fit the eigenvalue spectrum of each weight matrix to a power law and read its exponent **α**. (Basis of the **WeightWatcher** library.)

# Key Findings
- Norm metrics correlate with test accuracy for well-trained models but **cannot distinguish well- vs poorly-trained** models.
- **Power-law/HTSR metrics do much better** — quantitatively among well-trained series, qualitatively for well vs poorly trained.
- Weight spectra carry **data-free** signal about training quality and hidden problems.

# Strengths
- Massive empirical base; practical, data-free diagnostics.
- Provides the theoretical and software foundation (WeightWatcher) for two thesis predictors.

# Limitations
- Vision/standard-architecture focus; not grokking-specific.
- α fitting is sensitive to layer shape and fitting procedure.
- Correlational, not causal.

# Relation to Other Papers
- Foundation of [[Heavy-Tailed Self-Regularization]] → the **HTSR Alpha** and **Correlation Traps** entries in [[The Nine Predictors]].
- Spectral viewpoint shared with [[Advani - High-dimensional Dynamics of Generalization Error]], [[Mei - Generalization Error of Random Features Regression]] via [[Random Matrix Theory]].
- Underpins the [[Anti-Grokking]] detector (Prakash & Martin 2025).

# Relevance to Thesis
Very high. Direct source of HTSR Alpha and Correlation Traps; the WeightWatcher tooling is in the thesis software stack.

# Key Quotes
> "power law based metrics can do much better—quantitatively better at discriminating among series of well-trained models ... and qualitatively better at discriminating well-trained versus poorly trained models."

# Tags
#spectral #rmt #htsr #predictors #weightwatcher

---
## Related Notes
- [[Heavy-Tailed Self-Regularization]] · [[Random Matrix Theory]] · [[Anti-Grokking]] · [[The Nine Predictors]]
