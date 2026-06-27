---
tags: [concept, theory, kernel]
---
↑ Parent: [[00 - Start Here]] · Related: [[Neural Tangent Kernel]]

# Spectral Bias (Frequency Principle)

## Definition
**Spectral bias** (also called the *frequency principle*) is the tendency of neural networks to learn **low-complexity (low-frequency) components of the target function first** during training, and high-frequency components only much later. Formalised for kernel regression by [[Canatar - Spectral Bias and Task-Model Alignment]] via the kernel's eigenvalues and eigenfunctions, and empirically demonstrated for neural networks by Rahaman et al. (2019) via Fourier analysis of learned functions.

## In Plain Words
Networks learn the smooth, simple shape of a pattern first and the fine, wiggly details much later — like a painter who lays down broad colour blocking before adding fine lines. This has two implications:
1. Tasks with "smooth" solutions (low-frequency targets) are easy to learn and generalise well.
2. Tasks requiring sharp, wiggly decision boundaries (high-frequency targets) require much more data or training.

For grokking: the [[Fourier Features|Fourier circuit]] that a grokked network discovers encodes a low-frequency, algebraically structured solution. [[Inductive Bias|Spectral bias is one reason]] this solution is eventually preferred over the high-frequency memorisation lookup table.

## The Formal Account (Kernel Regime)

In the [[Neural Tangent Kernel|NTK regime]], the network computes a function $f(\cdot) = K(\cdot, x_{\text{train}})^T (K_{\text{train}})^{-1} y_{\text{train}}$. The generalisation error depends on three quantities:

1. **Sample count** $N$
2. **Kernel eigenvalues** $\lambda_k$ (the inductive bias: small $\lambda_k$ = low learning priority for mode $k$)
3. **Target alignment** $a_k^2$ (how much of the target function lies in mode $k$)

Generalisation error for mode $k$:
$$\mathcal{E}_k \propto \frac{a_k^2}{(1 + N\lambda_k/\sigma^2)^2}$$

Modes with large $\lambda_k$ (top eigenfunctions = simple, smooth functions) are learned quickly. Modes with small $\lambda_k$ (high-frequency modes) require much more data to learn. This is spectral bias.

## Task-Model Alignment

A key insight from [[Canatar - Spectral Bias and Task-Model Alignment]]: the generalisation error is *not just* about frequency — it depends on **alignment** between the target function and the kernel's top eigenfunctions.

| Alignment | Effect |
|---|---|
| High (target aligns with top eigenfunctions) | Good generalisation even with little data |
| Low (target is in low-eigenvalue modes) | Poor generalisation; requires much more data |
| Misaligned + noisy | Non-monotonic learning curves — *more data can hurt* |

The non-monotonic learning curve (a kernel analogue of [[Double Descent]]) emerges when the target partially aligns and the added noise aligns better with high-eigenvalue modes.

## Spectral Bias and Grokking

Spectral bias offers one perspective on *why* grokking happens eventually:
1. The memorising solution (lookup table) is extremely high-frequency — it responds sharply to each specific $(a, b)$ pair, with no smooth structure between neighbouring pairs.
2. The generalising [[Fourier Features|Fourier circuit]] is relatively low-frequency — it encodes a smooth algebraic structure.
3. Spectral bias says the network is biased toward learning the low-frequency structure.
4. But the memorising solution is *also* easy for a different reason: each training pair can be memorised independently, without any cross-pair structure. This makes memorisation fast even though it's high-frequency.
5. The resolution: weight decay pressure eventually makes the low-frequency Fourier circuit cheaper (lower norm), and spectral bias ensures this circuit is the "natural direction" the network drifts toward.

## Beyond the NTK Regime: Feature Learning Reshapes the Kernel

Spectral bias as described above applies strictly in the lazy/NTK regime, where representations stay fixed. When **[[Feature Learning]]** occurs (the rich regime), the effective kernel changes during training — the network can re-align toward the task structure. Grokking happens in the rich regime, so spectral bias is a background bias, not the complete story; the emergence of the Fourier circuit is a feature-learning event that goes beyond what fixed-kernel spectral bias predicts.

## Key Insights
- Neural networks learn low-frequency components first — a systematic, predictable bias.
- An analytic formula for kernel generalisation error depends on sample count, kernel eigenvalues, and **alignment** of target with eigenfunctions ([[Canatar - Spectral Bias and Task-Model Alignment]]).
- More data can **hurt** when the target is misaligned/noisy, giving non-monotonic learning curves — a kernel-world echo of [[Double Descent]].
- In grokking: the generalising circuit is lower-frequency than the memorising solution, consistent with spectral bias favouring it eventually.

## Evidence
[[Canatar - Spectral Bias and Task-Model Alignment]]; Rahaman et al. (2019) "On the spectral bias of neural networks" (empirical demonstration via Fourier analysis of learned functions).

## Relationship to Other Concepts
- A property of the [[Neural Tangent Kernel]] regime; analysed via [[Random Matrix Theory]].
- Related to [[Feature Learning]] (which can *re-shape* the effective kernel into a better-aligned one).
- One component of [[Inductive Bias]] — the architecture's built-in preference for smooth solutions.
- Connects to [[Double Descent]]: non-monotonic learning curves arise from misalignment.

## Open Questions
Does grokking correspond to the network re-aligning its effective kernel toward the task's low-frequency Fourier structure (a feature-learning event that overrides static spectral bias)? Can the kernel alignment score be measured during training as a grokking predictor?

---
## Related Notes
- [[Neural Tangent Kernel]] · [[Feature Learning]] · [[Canatar - Spectral Bias and Task-Model Alignment]]
- [[Inductive Bias]] · [[Double Descent]] · [[Fourier Features]] · [[Random Matrix Theory]]
