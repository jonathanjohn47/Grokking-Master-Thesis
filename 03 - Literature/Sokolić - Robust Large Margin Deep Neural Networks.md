---
tags: [literature, margin, robustness, generalization-bounds, theory]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Margin and Robustness]]

# Sokolić — Robust Large Margin Deep Neural Networks

# Citation
Sokolić, J., Giryes, R., Sapiro, G., & Rodrigues, M. R. D. (2016/2017). *Robust Large Margin Deep Neural Networks.* IEEE Transactions on Signal Processing; arXiv:1605.08254.

# The Gist (Plain Words)
Networks that keep a wide margin and don't overreact to small input changes come with solid guarantees that they will generalise — no matter how deep they are.

# Research Question
Can the **generalization error** of a deep network be bounded through its **classification margin**, in a way that does **not** blow up with width or depth?

# Methodology
Bounded generalization error via the **classification margin** combined with the **spectral norm of the network's Jacobian** near the training samples. Architecture-agnostic (feedforward, residual; arbitrary nonlinearities/pooling). Validated on MNIST, CIFAR-10, LaRED, ImageNet.

# Key Findings
- **A bounded Jacobian spectral norm around the training points is crucial** for good generalization at arbitrary depth/width — improving on bounds that grow with width or depth.
- **Batch/weight normalization** are shown to enjoy good generalization properties through this lens.
- Yields a **novel Jacobian-based regularizer**.

# Strengths
- Ties generalization to a **computable, local geometric quantity** (margin + input-Jacobian sensitivity).
- Depth/width-independent bound — a genuine theoretical advance.

# Limitations
- Bound, not exact dynamics; not about training-time onset.
- Vision-classification focus; no grokking/algorithmic tasks.

# Relation to Other Papers
- Margin viewpoint complements [[Xu - Dynamics in Deep Classifiers with the Square Loss]] ("which interpolant has large margin generalizes") and the symmetric-margin geometry of [[Papyan - Prevalence of Neural Collapse]].
- Input-perturbation robustness underlies the **Dropout-Robustness** predictor in [[The Nine Predictors]].
- Sensitivity/Jacobian-norm idea connects to sharpness/curvature signals (Commutator Defect).

# Relevance to Thesis
Moderate–high. Provides the **margin/robustness** theory behind a predictor family (robustness to perturbation) and a geometric order-parameter candidate; motivates [[Margin and Robustness]].

# Key Quotes
> "a bounded spectral norm of the network's Jacobian matrix in the neighbourhood of the training samples is crucial for a deep neural network of arbitrary depth and width to generalize well."

# Tags
#margin #robustness #generalization-bounds #jacobian #theory

---
## Related Notes
- [[Margin and Robustness]] · [[Xu - Dynamics in Deep Classifiers with the Square Loss]] · [[The Nine Predictors]] · [[Neural Collapse]]
