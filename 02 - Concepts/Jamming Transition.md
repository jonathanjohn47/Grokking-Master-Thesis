---
tags: [concept, theory, phase-transition, physics]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[08 - Phase Transitions in Learning]]

# Jamming Transition

## Definition
In physics, **jamming** is the transition where a granular system (sand, foam, colloidal suspensions) rigidifies as packing density crosses a critical point $\phi_c$ — the system goes from fluid-like to rigid. Applied to deep learning by [[Spigler - A Jamming Transition Affects Generalization]]: the under-to-over-parameterized boundary behaves like jamming, where the ratio of constraints (data points) to degrees of freedom (parameters) determines the loss landscape's structure and the network's generalisation ability.

## The Physics Analogy in Plain Terms

Pour dry sand into a box and shake it. At low density, grains slide freely — the sand flows. Keep adding grains until they're packed tight enough that each grain is touching others. At the **critical density** $\phi_c$, the system suddenly jams: nothing moves. Add more grains (above critical density) and the system develops **internal stress** but can still redistribute forces through the network of contacts.

In deep learning:
- **Below threshold** (underparameterized): too few degrees of freedom, model is "jammed" into bad solutions — cannot fit training data, stuck in high-error local minima.
- **At threshold** (interpolation threshold): exactly $N_\text{params} = N_\text{data}$. Maximum constraint, maximum instability. The system "jams" at the worst generalisation.
- **Above threshold** (overparameterized): many more degrees of freedom than constraints. The landscape has flat directions; the model can move between solutions freely.

## The Three-Phase Error Curve

[[Spigler - A Jamming Transition Affects Generalization]] observed three phases as model width grows:

```
Test error
  │
  │  \.             
  │   '.            /\   ← cusp (jamming point = interpolation threshold)
  │    '.           / \  
  │     '.         /   '.____________
  │      '._______/
  │
  +────────────────────────────────────> model width / N_params
       under          threshold            over
```

1. **Underparameterized decay**: test error falls as capacity grows — more capacity reduces bias.
2. **Cusp at the threshold**: test error peaks sharply — maximum variance, maximum instability.
3. **Overparameterized asymptote**: test error falls again and flattens — the second descent, minimum-norm solution.

This is exactly the [[Double Descent]] curve in a physics framing.

## How the Cusp Disappears

**[[Early Stopping]]** removes the cusp: if you stop training at a fixed point before convergence (even at the threshold), the variance explosion is never realised. This shows the cusp is a property of *converged solutions* at the threshold, not the training path — and is why early stopping was so successful in the classical era (it implicitly avoided the threshold).

## Connection to Grokking

The jamming framework offers a physical interpretation of the **grokking plateau** as a *time-domain jamming state*:

| Jamming (static) | Grokking (dynamic) |
|---|---|
| Density $\phi < \phi_c$ (fluid) | Early training (underfitting) |
| Density $\phi = \phi_c$ (jammed) | Memorisation plateau |
| Density $\phi > \phi_c$ (stressed but mobile) | Overparameterized overfit → grokking |

The memorisation state can be thought of as a **metastable jammed state**: the network found a valley (zero training loss) that is locally stable but not globally optimal. Weight decay is the force that eventually unjams it — analogous to thermal fluctuations unjamming a dense granular system. The grokking transition is the unjamming event.

This analogy is explicitly explored in [[08 - Phase Transitions in Learning]] and is consistent with the first-order-like behaviour of the grokking transition (metastable plateau + sudden nucleation of the generalising state).

## Key Insights
- Generalisation error shows three phases vs width: decay → cusp at the transition → slow decay ([[Spigler - A Jamming Transition Affects Generalization]]).
- The cusp at the transition is exactly the [[Double Descent]] peak.
- **Early stopping removes the cusp**, identifying the overfitting region as the neighbourhood of the threshold.
- The analogy suggests the grokking plateau is a metastable jammed state, and grokking is an unjamming event — consistent with phase-transition picture.
- The jamming framing imports powerful physical intuitions: correlation length, order-disorder, nucleation.

## Evidence
[[Spigler - A Jamming Transition Affects Generalization]] (original ML jamming paper); [[Advani - High-dimensional Dynamics of Generalization Error]] (related landscape/glass analogies); [[Rocks - Memorizing Without Overfitting]] (bias-variance decomposition of the cusp).

## Relationship to Other Concepts
- A physical realisation of the [[Interpolation Threshold]] and [[Phase Transition]].
- Same critical point as the [[Double Descent]] peak.
- Motivates viewing the grokking plateau as a time-domain jammed state.
- [[Early Stopping]] removes the static cusp; for grokking it would prevent the transition.

## Open Questions
Does a jamming-like rigidity argument apply to the *time-domain* grokking plateau (a metastable jammed state that un-jams at grokking)? Can correlation-length divergence near the threshold be measured inside the network during training?

---
## Related Notes
- [[Phase Transition]] · [[Interpolation Threshold]] · [[Double Descent]]
- [[Early Stopping]] · [[Overparameterization]] · [[Weight Decay]]
- [[Spigler - A Jamming Transition Affects Generalization]] · [[08 - Phase Transitions in Learning]]
