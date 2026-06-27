---
tags: [concept, theory, optimization]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[08 - Phase Transitions in Learning]]

# Loss Landscape

## Definition
The **loss landscape** is the hypersurface defined by plotting a network's training loss against all possible weight configurations. Training is navigation on this surface: [[Gradient Descent]] follows the steepest downhill direction at each step. The geometry of the landscape — where the valleys are, how wide, how deep, how connected — determines what solutions the network finds and how well they generalise.

## In Plain Words
Think of a hilly terrain where height = "how wrong the network is" and every geographic location = one setting of the weights. [[Gradient Descent]] is a ball rolling downhill, always moving toward lower error. Valleys are solutions the ball can get stuck in. The key insight for grokking: there are **many** valleys at zero training loss, but they are not equal — some generalise, some don't, and the network rolls into the easy (memorising) one first.

## The Landscape in the Overparameterized Regime

In classical (underparameterized) models, the landscape has a unique low point — the optimal solution is essentially determined. In [[Overparameterization|overparameterized]] networks, something fundamentally different happens:

- There is **no unique minimum** — instead, a *connected manifold* (floor) of zero-loss configurations.
- The memorising and generalising solutions are *both* on this manifold — at zero training loss.
- The question becomes: which zero-loss solution does the ball roll to?

This is the central question of grokking: the network starts at a memorising solution, and [[Weight Decay]] slowly nudges it along the zero-loss manifold toward the generalising one.

## Geometry and Generalisation

**Wide, flat valleys generalise better** — this is an empirical and theoretical observation:
- Wide minima have small second derivatives (small Hessian eigenvalues) — small perturbations to weights barely change the loss.
- Sharp minima are fragile: they fit training data tightly but small weight changes (e.g., from the distribution shift between train and test) cause large loss increases.

The generalising [[Fourier Features|Fourier circuit]] in grokking corresponds to a wider, flatter region of the loss landscape than the memorising solution, which is why it generalises.

## Schematic: Two Zero-Loss Valleys

```
Loss
  │
  │           memorising         generalising
  │           solution           solution
  │             │                    │
  │    _________\/_______________/ \/\___
  │   /                              │
  │  /  zero-loss                    │ ← wider valley
  │ /   manifold                     │   (better generalisation)
  ├────────────────────────────────────> weight space (2D slice)
```

Both valleys have zero training loss. But the generalising valley is wider (lower curvature) and further along the manifold. [[Weight Decay]] is the force that drives the ball from the memorising valley toward the generalising one, because the generalising solution has lower weight norm (lower total distance from the origin).

## Role of Weight Decay in the Landscape

Weight decay modifies the loss landscape from:
$$\mathcal{L}(\theta) \quad \to \quad \mathcal{L}(\theta) + \frac{\lambda}{2} \|\theta\|^2$$

This adds a gentle bowl toward the origin. The effect:
- The memorising solution, which typically needs large weights (a complex lookup table), is penalised more.
- The generalising [[Circuit Formation|Fourier circuit]], which uses structured, lower-norm weights, sits at a lower combined loss.
- Over the course of the plateau, the added bowl slowly tilts the landscape so the generalising valley becomes lower than the memorising one.

This explains why, at the moment of the grokking jump, the change is sudden: the memorising valley effectively disappears (or the barrier between them is crossed) and the network snaps into the generalising configuration.

## Theoretical Analyses

Simplified models let us map the landscape more precisely:
- The **[[Mean-Field Limit]]** turns the loss landscape into a smooth PDE on the neuron distribution, with no spurious local minima ([[Mei - A Mean Field View of Two-Layer Neural Networks]]): SGD converges to the global optimum.
- The **[[Layer-Peeled Model]]** shows the low-loss region has its best points at [[Simplex ETF]] configurations — i.e., neural collapse is at the bottom of the bowl ([[Fang - Layer-Peeled Model and Minority Collapse]]).
- The **unconstrained features model** ([[Mixon - Neural Collapse with Unconstrained Features]]) shows neural collapse is the unique global minimiser: the ball must end up there eventually.

## Key Insights
- **Overparameterised networks have a connected floor** of zero-loss solutions — a manifold, not a point.
- **Wide, flat valleys** → better generalisation; sharp, narrow valleys → worse generalisation.
- [[Weight Decay]] tilts the manifold, making the generalising valley lower over the course of the grokking plateau.
- Simplified models ([[Mean-Field Limit]], [[Layer-Peeled Model]]) can map the landscape exactly and confirm the generalising solution is the global optimum.
- The grokking transition corresponds to the network leaving the memorising valley and falling into the generalising one.

## Evidence
- [[Mei - A Mean Field View of Two-Layer Neural Networks]] — wide-network landscape becomes analysable; often no bad local minima.
- [[Mixon - Neural Collapse with Unconstrained Features]] — the collapsed geometry is the global low point, so dynamics are drawn to it.
- [[Fang - Layer-Peeled Model and Minority Collapse]] — layer-peeled analysis maps the landscape near terminal phase.

## Relationship to Other Concepts
- Explored by [[Gradient Descent]]; reshaped by [[Weight Decay]] and [[Overparameterization]].
- Connects to [[Memorization]] vs [[Generalization]] (different valleys on the same zero-loss manifold).
- [[Phase Transition]] language describes sudden moves between regions of the landscape.
- Simplified by the [[Mean-Field Limit]] and [[Layer-Peeled Model]].

## Open Questions
Can the path from the memorising valley to the generalising one be measured live (e.g., via weight-space PCA trajectory), giving a grokking predictor? Is the barrier between the two zero-loss valleys a saddle point, and does its height predict grokking timing?

---
## Related Notes
- [[Gradient Descent]] · [[Overparameterization]] · [[Weight Decay]] · [[Memorization]] · [[Generalization]]
- [[Mean-Field Limit]] · [[Layer-Peeled Model]] · [[Phase Transition]]
- [[Mei - A Mean Field View of Two-Layer Neural Networks]] · [[Mixon - Neural Collapse with Unconstrained Features]]
