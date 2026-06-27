---
tags: [literature, dynamics, rmt, double-descent, theory]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Random Matrix Theory]] · [[Double Descent]]

# Advani — High-dimensional Dynamics of Generalization Error

# Citation
Advani, M. S., & Saxe, A. M. (2017). *High-dimensional dynamics of generalization error in neural networks.* arXiv:1710.03667 [stat.ML].

# The Gist (Plain Words)
Using math for large random systems, the authors show that training with gradient descent already guards against overfitting on its own, and that overtraining hurts most exactly at the point where the model can just barely fit the data.

# Research Question
How does generalisation error **evolve during gradient-descent training** in the high-dimensional regime (parameters ≳ samples), and what protects large networks from overfitting?

# Methodology
Average-case analysis using **[[Random Matrix Theory]]** and exact solutions in linear models; extended qualitatively to nonlinear nets. Derived train/test error **dynamics** as functions of dimensionality and SNR.

# Key Findings
- Gradient-descent dynamics **naturally protect against overfitting**; overtraining is **worst at the interpolation point** (effective params = samples) and reduced by making the net smaller *or larger*.
- Low generalisation error requires **small initial weights**.
- In overcomplete nets: a **frozen subspace** where no learning occurs, plus better-conditioned input correlations, protect against overtraining.
- Worst-case bounds (Rademacher) are **inaccurate**; offers an alternative bound.

# Strengths
- Among the earliest **dynamical** (training-time) treatments of double descent — directly relevant to grokking's time axis.
- The frozen-subspace / slow-mode picture prefigures the plateau dynamics.

# Limitations
- Mostly linear/average-case; nonlinear claims qualitative.
- No explicit grokking or feature learning.

# Relation to Other Papers
- Dynamical complement to the static [[Mei - Generalization Error of Random Features Regression]] and [[Rocks - Memorizing Without Overfitting]].
- Frozen-subspace/slow-mode idea resonates with the memorising/generalising mode competition in [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]].

# Relevance to Thesis
High (conceptual). The **time-domain** view of generalisation error and the slow-mode/frozen-subspace picture are the closest classical analogue to the grokking plateau.

# Key Quotes
> "the dynamics of gradient descent learning naturally protect against overtraining and overfitting in large networks. Overtraining is worst at intermediate network sizes, when the effective number of free parameters equals the number of samples."

# Tags
#dynamics #rmt #double-descent #generalization #small-init

---
## Related Notes
- [[Random Matrix Theory]] · [[Double Descent]] · [[02 - The Grokking Training Dynamics]] · [[Weight Decay]]
