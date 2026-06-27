---
tags: [concept, theory, kernel]
---
↑ Parent: [[00 - Start Here]] · Related: [[Feature Learning]]

# Neural Tangent Kernel (NTK)

## Definition
The **Neural Tangent Kernel (NTK)** is the kernel that emerges when a neural network is in the infinite-width, small-initialisation limit: in this regime, training all layers with gradient descent is equivalent to **kernel regression** with a fixed kernel $K_{\text{NTK}}(x, x')$. The network parameters barely move from initialisation (the **lazy** regime), and learning is entirely captured by the kernel's structure. The NTK is important because it makes deep learning analytically tractable — but grokking lives *outside* the NTK regime.

## In Plain Words
One way to understand a complicated neural network: pretend it barely changes during training. If the network is wide enough and initialised with small weights, this approximation becomes exact. Then "training the network" is mathematically identical to "doing kernel regression" — a well-understood classical method. All the NTK's predictions come from the kernel's eigenvalues and eigenfunctions ([[Spectral Bias]]). But grokking *requires* the network to change significantly — so grokking happens precisely where the NTK approximation breaks down.

## How the NTK Emerges

Consider a neural network $f(x; \theta)$ with parameters $\theta \in \mathbb{R}^P$. For a small learning rate, the parameter update is:
$$\theta_{t+1} - \theta_t \approx -\eta \nabla_\theta \mathcal{L} = -\eta J^T \nabla_f \mathcal{L}$$

where $J_{ni} = \partial f(x_n; \theta) / \partial \theta_i$ is the Jacobian. In the infinite-width limit, $J$ concentrates and the function $f$ evolves as:
$$\frac{df(x)}{dt} = -K_{\text{NTK}}(x, X_{\text{train}}) \nabla_f \mathcal{L}$$

where $K_{\text{NTK}}(x, x') = J(x) J(x')^T$ is the NTK. Crucially, $K_{\text{NTK}}$ stays *constant during training* (in the limit) — so the dynamics are linear and equivalent to kernel regression.

## Properties of the NTK Regime

| Property | NTK regime | Rich regime (mean-field) |
|---|---|---|
| Representations | Fixed at initialisation | Change during training |
| Training dynamics | Linear (kernel regression) | Nonlinear PDE on neuron distribution |
| Feature learning | None | Yes |
| Local minima | None (convex kernel regression) | None (mean-field converges globally) |
| Grokking | Not possible (no feature change) | Possible (representations reorganise) |
| Analysis | Exact (kernel eigenspectrum) | Approximate (mean-field theory) |

## The NTK's Inductive Bias: Spectral Bias

In the NTK regime, the learning dynamics are governed by the kernel's eigendecomposition. Target function modes aligned with large kernel eigenvalues are learned quickly; modes aligned with small eigenvalues require much more data/training. This is **[[Spectral Bias]]**:
- Low-frequency, smooth components of the target → large NTK eigenvalues → learned fast.
- High-frequency, sharp components → small NTK eigenvalues → learned slowly.

For grokking on modular arithmetic:
- The memorising solution (lookup table) is high-frequency → small NTK eigenvalues → NTK theory predicts it should be learned slowly. Yet it's learned fast because memorisation doesn't require learning the smooth structure — it learns individual training pairs as isolated objects.
- The generalising Fourier circuit is low-frequency → large NTK eigenvalues → NTK theory says this should be preferred eventually.

But neither the fast memorisation nor the eventual grokking is well-described by the NTK: memorisation requires fitting isolated points (which the NTK handles), but grokking requires *changing* the internal representations to discover the Fourier structure — which the NTK (frozen representations) cannot describe.

## Where Grokking Falls on the NTK/Rich Spectrum

The NTK regime is approached by: large width + small initialisation + small learning rate. Grokking experiments typically use:
- Small networks (~1-2 layers, 128 dimensions) — not infinitely wide.
- Standard initialisation scale.
- Standard learning rates.

These are finite-width, finite-init settings — far from the NTK limit. Grokking is a **finite-width, rich-regime phenomenon**:
- During the memorisation phase, the network is partially in a lazy regime (just fitting training points).
- During the plateau and grokking transition, representations reorganise significantly — this is feature learning, entirely outside the NTK picture.
- The [[Mean-Field Limit]] (not the NTK) is the appropriate theoretical framework.

## NTK as a Diagnostic Tool

Despite not describing grokking directly, NTK-inspired analysis is useful as a baseline:
- Computing the NTK eigenspectrum at initialisation tells you the network's "default" inductive bias.
- Tracking how much the NTK *changes* during training measures the degree of feature learning.
- A large change in the NTK (the network leaving the lazy regime) could serve as a grokking predictor: the moment representations begin to reorganise.

## Key Insights
- Infinite-width networks → kernel regression with NTK; training behaves linearly with fixed representations.
- The NTK regime has **no feature learning**; grokking requires leaving it for the **rich / [[Mean-Field Limit|mean-field]]** regime.
- Grokking experiments are firmly in the finite-width, rich regime — the NTK provides a useful contrast but not a description.
- The NTK's [[Spectral Bias]] does predict the eventual preference for the Fourier circuit (low-frequency), but not the dynamics.

## Evidence
Jacot et al. (2018) "Neural Tangent Kernel: Convergence and Generalization in Neural Networks" (foundational NTK paper); [[Canatar - Spectral Bias and Task-Model Alignment]] (kernel-regime generalisation analysis); [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] (rich-regime comparison).

## Relationship to Other Concepts
- Contrast with [[Feature Learning]] (rich regime) and [[Mean-Field Limit]] (the right theory for grokking).
- Analysed with [[Random Matrix Theory]]; exhibits [[Spectral Bias]].
- The exit from the NTK regime (representations start changing) may be a grokking predictor.

## Open Questions
Exactly where does the network leave the lazy/NTK regime during grokking, and can that exit be detected as a predictor? Does the NTK-to-rich-regime transition coincide with the grokking jump or precede it (lead time)?

---
## Related Notes
- [[Spectral Bias]] · [[Feature Learning]] · [[Mean-Field Limit]]
- [[Canatar - Spectral Bias and Task-Model Alignment]] · [[Li - Representations and Generalization in Artificial and Brain Neural Networks]]
- [[Inductive Bias]] · [[Grokking Predictors]] · [[Circuit Formation]]
