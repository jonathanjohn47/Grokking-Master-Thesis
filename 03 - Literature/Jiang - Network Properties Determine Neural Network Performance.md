---
tags: [literature, network-science, early-prediction, model-selection]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Generalization]]

# Jiang — Network Properties Determine Neural Network Performance

# Citation
Jiang, C., Huang, Z., Pedapati, T., Chen, P.-Y., Sun, Y., & Gao, J. (2024). *Network properties determine neural network performance.* Nature Communications 15:5718.

# The Gist (Plain Words)
Treat a training network as a graph and you can predict its final performance from just the early part of training — no need to wait for the run to finish.

# Research Question
Can a **network-science** view of the weights — modelling SGD as edge dynamics on a graph — yield a metric that predicts a model's downstream generalisation from **early training only**?

# Methodology
Mapped performance to the **network characteristics of the line graph** governed by the edge dynamics of SGD differential equations; derived a **neural capacitance** metric. Used network-reduction to make it tractable. Evaluated on **17 pretrained ImageNet models × 5 datasets** and a NAS benchmark.

# Key Findings
- Neural capacitance predicts generalisation and supports **model selection using only early training results**.
- More efficient than state-of-the-art model-selection methods.
- Microscopic (edge-level) dynamics carry predictive structure that macroscopic metrics miss.

# Strengths
- Establishes the **early-training-predicts-final-performance** paradigm — the same logic as grokking early-warning signals.
- Principled link between optimisation dynamics and a computable graph metric.

# Limitations
- Transfer-learning / fine-tuning model-selection setting, not grokking dynamics.
- Vision models; algorithmic-task grokking untested.
- Line-graph computation can be heavy without reduction.

# Relation to Other Papers
- Conceptual sibling of [[Martin - Predicting Trends in Neural Network Quality]] (predict quality cheaply) and of [[The Nine Predictors|early grokking predictors]].
- Dynamics-from-SGD framing relates to [[Advani - High-dimensional Dynamics of Generalization Error]].

# Relevance to Thesis
Moderate. Methodological precedent for early prediction and for using a single derived scalar as a generalisation forecaster; a candidate idea for novel predictors.

# Key Quotes
> "a neural capacitance metric to universally capture a model’s generalization capability ... and predict model performance using only early training results."

# Tags
#network-science #early-prediction #model-selection #generalization

---
## Related Notes
- [[Generalization]] · [[Grokking Predictors]] · [[Martin - Predicting Trends in Neural Network Quality]] · [[12 - Modern Developments]]
