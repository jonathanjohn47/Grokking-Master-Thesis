---
tags: [literature, kernel, ntk, spectral-bias, theory]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Spectral Bias]] · [[Neural Tangent Kernel]]

# Canatar — Spectral Bias and Task-Model Alignment

# Citation
Canatar, A., Bordelon, B., & Pehlevan, C. (2021). *Spectral bias and task-model alignment explain generalization in kernel regression and infinitely wide neural networks.* Nature Communications 12:2914.

# The Gist (Plain Words)
A model generalises best when its built-in preferences line up with the task. The paper gives an exact formula for this and shows that more data can even hurt when model and task are misaligned.

# Research Question
What determines generalisation in **kernel regression** (and hence infinitely-wide nets via the **[[Neural Tangent Kernel|NTK/NNGPK]]**), and can a theory predict it on **real** data?

# Methodology
Used the **replica method** of statistical mechanics to derive an analytic generalisation-error formula for any kernel and data distribution, as a function of (1) sample count, (2) kernel **eigenvalues/eigenfunctions** (inductive bias), (3) **alignment** of the target with eigenfunctions.

# Key Findings
- **[[Spectral Bias]]:** kernels learn target components along **top eigenfunctions first** (simple functions before complex).
- **Task-model alignment** governs whether a kernel suits a task.
- More data can **hurt** when noisy/misaligned → **non-monotonic learning curves with multiple peaks** (a kernel-world double descent).

# Strengths
- Analytic, applies to **real datasets** and to NTK kernels.
- Quantitative notion of "which functions generalise easily."

# Limitations
- **Lazy/kernel regime** → **no [[Feature Learning]]**; cannot model grokking's representation change.
- Fixed kernel; assumes the NTK correspondence holds.

# Relation to Other Papers
- Defines the lazy-regime baseline that [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] argues must be exceeded (feature learning) to explain real generalisation.
- Non-monotonic curves echo [[Double Descent]] ([[Mei - Generalization Error of Random Features Regression]]).

# Relevance to Thesis
Moderate (boundary case). Clarifies what the **fixed-kernel** theory can and cannot explain — grokking is precisely a *feature-learning* event beyond NTK, sharpening the thesis's conceptual scope.

# Key Quotes
> "We elucidate an inductive bias of kernel regression to explain data with simple functions ... more data may impair generalization when noisy or not expressible by the kernel, leading to non-monotonic learning curves with possibly many peaks."

# Tags
#kernel #ntk #spectral-bias #theory #alignment

---
## Related Notes
- [[Spectral Bias]] · [[Neural Tangent Kernel]] · [[Feature Learning]] · [[Li - Representations and Generalization in Artificial and Brain Neural Networks]]
