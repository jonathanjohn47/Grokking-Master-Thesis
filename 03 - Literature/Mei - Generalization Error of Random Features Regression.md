---
tags: [literature, double-descent, theory, rmt, interpolation]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Double Descent]]

# Mei — Generalization Error of Random Features Regression

# Citation
Mei, S., & Montanari, A. (2019/2020). *The generalization error of random features regression: Precise asymptotics and the double descent curve.* arXiv:1908.05355 [math.ST].

# The Gist (Plain Words)
The first exactly-solvable model that reproduces the whole double-descent curve, proving it is a general feature of high-dimensional fitting, not a deep-learning quirk.

# Research Question
Can a **fully tractable** model reproduce the entire **[[Double Descent]]** curve, proving it is a general high-dimensional phenomenon rather than a deep-learning quirk?

# Methodology
Ridge regression on **N random features** $\sigma(w_a^\top x)$ over the sphere — equivalently a two-layer net with random first layer. Computed **precise asymptotics** of test error in the limit $N, n, d \to \infty$ with $N/d, n/d$ fixed.

# Key Findings
- Derived exact test-error asymptotics capturing **all** features of double descent **without ad-hoc misspecification**.
- Above a critical SNR, the **minimum test error is achieved by extreme overparameterized interpolators** (parameters ≫ samples, zero training error).
- Double descent appears even in this simple random-features/linear setting.

# Strengths
- First analytically exact, end-to-end model of the curve — a theoretical landmark.
- Cleanly separates the interpolation peak from the second descent.

# Limitations
- Random (fixed) first layer → **no [[Feature Learning]]**; cannot model grokking's representation change.
- Asymptotic, Gaussian-style assumptions.

# Relation to Other Papers
- Rigorous core of the [[Double Descent]] story; complements bias/variance view of [[Rocks - Memorizing Without Overfitting]] and RMT dynamics of [[Advani - High-dimensional Dynamics of Generalization Error]].
- Physical-transition counterpart: [[Spigler - A Jamming Transition Affects Generalization]].

# Relevance to Thesis
Moderate–high (foundational). Establishes the static phenomenon grokking mirrors over training time; grounds the "interpolators can generalise best" premise.

# Key Quotes
> "minimum test error is achieved by extremely overparametrized interpolators, i.e., networks that have a number of parameters much larger than the sample size, and vanishing training error."

# Tags
#double-descent #theory #random-features #rmt #interpolation

---
## Related Notes
- [[Double Descent]] · [[Interpolation Threshold]] · [[Rocks - Memorizing Without Overfitting]] · [[07 - Double Descent]]
