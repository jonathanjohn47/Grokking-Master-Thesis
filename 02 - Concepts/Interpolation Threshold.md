---
tags: [concept, theory, double-descent]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[06 - Overparameterization and Interpolation]]

# Interpolation Threshold

## Definition
The **interpolation threshold** is the model capacity (or equivalently, the sample size) at which training error first reaches zero — the exact boundary between under- and over-parameterization. It is the point where the model has *just enough* capacity to fit the training data exactly (to **interpolate**). In the [[Double Descent]] curve, it is where test error peaks. In the [[Jamming Transition]] analogy, it is where the system "jams" — degrees of freedom equal constraints.

## In Plain Words
The exact point where a model becomes *just* big enough to fit every training example perfectly. Counterintuitively, this is the **worst** place to be: test error usually peaks right here. Make the model any bigger and test error starts falling again. The threshold is simultaneously an interpolation point, a critical point of a [[Phase Transition]], and a point of maximum instability.

## The Threshold as a Phase Boundary

Three equivalent ways to describe the threshold:

| Perspective | Threshold condition | What happens at threshold |
|---|---|---|
| **Capacity** | $\text{params} = N_{\text{train}}$ | Model can first achieve zero training error |
| **Sample ratio** | $N_{\text{train}} / \text{params} = 1$ | System has exactly one degree of freedom per constraint |
| **Jamming** | $\phi = \phi_c$ | System transitions from fluid (underdetermined) to jammed (overdetermined) |

## Why Test Error Peaks Here

At the threshold, the model is **maximally constrained**:
- Every parameter is committed to fitting exactly the training set — no slack.
- The fit is unique (exactly determined system): tiny changes in training data → wildly different fits.
- **Variance explodes** (proven analytically in [[Rocks - Memorizing Without Overfitting]] and [[Mei - Generalization Error of Random Features Regression]]).
- The model achieves the worst generalisation of any capacity regime.

Moving past the threshold into the overparameterized regime immediately alleviates the constraint: there are infinitely many zero-loss solutions, and gradient descent finds the minimum-norm one — which generalises well.

## The Jamming Analogy

[[Spigler - A Jamming Transition Affects Generalization]] drew an explicit analogy to jamming in granular physics:
- Below the jamming threshold ($\phi < \phi_c$): particles can rearrange freely — the system is fluid. Analogously, underparameterized models have freedom to choose the right solution.
- At jamming ($\phi = \phi_c$): particles are exactly touching — the system becomes rigid. Analogously, the model is maximally constrained.
- Above jamming ($\phi > \phi_c$): particles overlap — the system has internal stress but can redistribute. Analogously, overparameterized models find minimum-norm solutions that generalise.

The test error *cusp* at the jamming point disappears when [[Early Stopping]] is applied — an analogy to annealing in physics.

## Quantitative Example (Grokking Setup)

For the canonical grokking experiment on $(a + b) \bmod 97$:
- Total pairs: $97 \times 97 = 9409$.
- Training set (30%): $\approx 2794$ pairs.
- A small 1-layer transformer: $\approx 128K$ parameters.
- Parameter-to-sample ratio: $128000 / 2794 \approx 46:1$ — **far past** the threshold.

The grokking model is deeply in the overparameterized regime — not near the threshold. This is why the first descent (from random to memorisation) happens quickly, and why there is a huge manifold of zero-loss solutions available for weight decay to navigate.

## Connection to Grokking

| Double descent (static) | Grokking (dynamic) |
|---|---|
| Below threshold (underfit) | Early training |
| At threshold (max variance) | Not directly applicable — grokking models operate far past the threshold |
| Above threshold (second descent) | Memorisation → grokking transition |

Grokking's dynamics happen entirely in the overparameterized regime. The relevant threshold in grokking is not the interpolation threshold per se, but the conceptual analogue: the moment the memorising solution is sufficiently eroded by weight decay that the generalising solution takes over. The **plateau** is the time during which the system navigates the manifold of zero-loss solutions.

## Key Insights
- At the threshold the fit is maximally constrained, so **variance diverges** ([[Rocks - Memorizing Without Overfitting]]).
- It coincides with the **[[Jamming Transition]]**, complete with a test-error cusp ([[Spigler - A Jamming Transition Affects Generalization]]).
- The effective number of parameters equals the number of samples here ([[Advani - High-dimensional Dynamics of Generalization Error]]).
- [[Early Stopping]] removes the cusp ([[Spigler - A Jamming Transition Affects Generalization]]).
- Grokking models operate far *past* this threshold — the relevant dynamics are about navigating the overparameterized manifold, not crossing the threshold.

## Evidence
[[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]], [[Spigler - A Jamming Transition Affects Generalization]], [[Advani - High-dimensional Dynamics of Generalization Error]].

## Relationship to Other Concepts
- The peak of [[Double Descent]]; a [[Jamming Transition]]; a [[Phase Transition]] critical point.
- Separates [[Overparameterization]] from underparameterization.
- The static analogue of the memorisation-to-grokking transition boundary in [[Grokking]].
- [[Bias-Variance Tradeoff]] breaks down here — variance diverges in the classical picture.

## Open Questions
Is there a *time-domain* analogue of the interpolation threshold during grokking — a moment of maximal variance just before the test accuracy jumps? Can it be detected from internal signals?

---
## Related Notes
- [[Double Descent]] · [[Jamming Transition]] · [[Overparameterization]]
- [[Bias-Variance Tradeoff]] · [[Phase Transition]] · [[Early Stopping]]
- [[Spigler - A Jamming Transition Affects Generalization]] · [[Rocks - Memorizing Without Overfitting]]
- [[06 - Overparameterization and Interpolation]]
