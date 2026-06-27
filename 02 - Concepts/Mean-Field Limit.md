---
tags: [concept, mean-field, dynamics, feature-learning, theory]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Mean-Field Limit

## Definition
The **mean-field limit** is a mathematical regime for studying wide two-layer neural networks: instead of tracking each neuron individually, the entire population of neurons is described by a **probability distribution** over weights. In this limit, stochastic gradient descent becomes a deterministic **Wasserstein gradient flow** — a partial differential equation (PDE) on the distribution. This is the **rich (feature-learning)** regime, as opposed to the **lazy** [[Neural Tangent Kernel|NTK regime]] where representations stay fixed.

## In Plain Words
Tracking thousands of individual neurons is intractable. The mean-field trick: describe them as a crowd, characterised by a single distribution. The crowd's evolution under training becomes a smooth, solvable equation — like how we describe gas molecules not individually but by their pressure and temperature. And crucially, this description captures *feature learning* — the crowd changes its distribution during training — unlike the NTK which assumes the crowd never moves.

## The Mathematical Object

Consider a two-layer network:
$$f(x) = \int \sigma(w^T x) \, \mu(dw)$$

where $\mu$ is the distribution over neurons (weights $w$). Under mean-field scaling (overparameterized regime with width → ∞), gradient descent on each neuron becomes:

$$\frac{\partial \mu_t}{\partial t} = \nabla \cdot \left(\mu_t \nabla \frac{\delta \mathcal{F}[\mu_t]}{\delta \mu}\right)$$

where $\mathcal{F}[\mu]$ is the mean-field free energy (loss + entropy regularisation). This is a **Wasserstein gradient flow**: the distribution moves in the direction that most efficiently reduces the free energy, measured in the Wasserstein-2 metric (Earth Mover's distance).

## Why This Captures Feature Learning

In the NTK limit, neurons barely move from initialisation — the kernel $K(x, x')$ stays fixed. In the mean-field limit, neurons move significantly, reshaping the distribution $\mu$ — this is feature learning. The NTK approximates the network as if each neuron is frozen; the mean-field limit describes how neurons collectively reorganise.

For grokking: the memorising-to-generalising transition requires neurons to reshape their representations (from lookup-table patterns to Fourier angle patterns). This is precisely what the mean-field limit describes — a collective rearrangement of the neuron distribution.

## Key Result (Mei et al. 2018)

[[Mei - A Mean Field View of Two-Layer Neural Networks]] proved:
1. The mean-field PDE has a unique stationary measure under mild conditions.
2. The stationary measure corresponds to the **global optimum** of the regularised empirical loss.
3. SGD (with small step size, wide network) converges to this stationary measure.

**Implication**: a sufficiently wide two-layer network trained with SGD will, in the mean-field limit, converge to the globally optimal solution — including learning the best possible features. There are **no spurious local minima** in this regime (the PDE's gradient flow is globally convergent).

This gives theoretical grounding for why overparameterized networks trained with gradient descent eventually generalise well — and why grokking (the eventual discovery of the optimal Fourier representation) should happen given enough training.

## Why Mean-Field Predicts Smooth Convergence (but Grokking Is Abrupt)

The mean-field PDE predicts smooth convergence to the global optimum — no abrupt jump. But grokking involves a sudden jump. The resolution:
- Mean-field is the **infinite-width limit**: at finite width, there are fluctuations and metastability.
- The grokking plateau is a metastable state (the memorising solution is locally stable at finite width).
- The jump at grokking is a finite-width fluctuation that eventually escapes the metastable basin.
- As width → ∞ (mean-field limit), the plateau length diverges — the system gets stuck longer and longer.

Grokking is thus a **finite-width effect**, invisible in the strict mean-field limit but predicted by corrections to it.

## Contrast: Mean-Field vs NTK

| | NTK (lazy) | Mean-Field (rich) |
|---|---|---|
| Width | Infinite, but different scaling | Infinite, mean-field scaling |
| Representations | Fixed at initialisation | Change during training |
| Training dynamics | Kernel regression | Wasserstein gradient flow (PDE) |
| Feature learning | None | Yes — full redistribution |
| Local minima | None (convex kernel regression) | None (PDE converges globally) |
| Captures grokking? | No | Qualitatively yes (globally optimises); grokking jump is a finite-width correction |

## Key Insights
- SGD on two-layer nets in the mean-field limit → a PDE on the neuron distribution; can converge to **near-ideal generalisation** ([[Mei - A Mean Field View of Two-Layer Neural Networks]]).
- This is the **rich regime**: representations change, unlike the NTK/lazy regime.
- Grokking requires leaving the NTK regime — the mean-field limit is the right theoretical home.
- The abruptness of the grokking jump is a **finite-width correction** to the smooth mean-field dynamics.

## Evidence
[[Mei - A Mean Field View of Two-Layer Neural Networks]] (foundational); [[Advani - High-dimensional Dynamics of Generalization Error]] (complementary training-dynamics view via RMT).

## Relationship to Other Concepts
- Rich-regime counterpart to the [[Neural Tangent Kernel]] / [[Spectral Bias]].
- Mathematical engine for [[Feature Learning]] and [[Circuit Formation]].
- Explains *why* gradient descent converges to good representations — the theoretical foundation for grokking eventually happening.
- The smooth convergence of the mean-field limit contrasts with the abrupt grokking jump, which is a finite-width effect.

## Open Questions
Can mean-field / distributional dynamics be extended to reproduce a **plateau followed by an abrupt transition** (grokking) from first principles? What finite-width correction creates the metastable memorising state? Does the mean-field limit predict the plateau length as a function of width and weight decay?

---
## Related Notes
- [[Mei - A Mean Field View of Two-Layer Neural Networks]] · [[Feature Learning]] · [[Neural Tangent Kernel]]
- [[Circuit Formation]] · [[Fourier Features]] · [[Weight Decay]]
- [[Loss Landscape]] · [[Phase Transition]] · [[Overparameterization]]
