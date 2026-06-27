---
tags: [concept, theory, phase-transition]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[08 - Phase Transitions in Learning]]

# Phase Transition

## Definition
A **phase transition** is an abrupt, qualitative change in a system's macroscopic behaviour as a **control parameter** crosses a critical value, marked by an **order parameter** that is zero in one phase and nonzero in the other. The term is borrowed from statistical physics. In the context of learning, grokking *is* a phase transition in training time.

## In Plain Words
Like water turning to ice: nudge the temperature past 0°C and the whole system flips its behaviour at once — not gradually, but as a sharp switch. Many learning effects work this way: a quiet build-up inside the system, then a sudden external switch when some hidden quantity crosses a threshold. Grokking is this: a quiet circuit-building period, then a sudden jump in test accuracy when the circuit crosses the "good enough" threshold.

## The Two Key Concepts

**Control parameter:** the variable you change to drive the transition.
- In water freezing: temperature.
- In grokking: training steps (or equivalently, how much [[Weight Decay|regularisation]] pressure has accumulated).
- In [[Double Descent]]: model capacity.
- In [[Jamming Transition]]: ratio of parameters to constraints.

**Order parameter:** a measurable quantity that distinguishes the two phases.
- In water freezing: density (liquid ≠ solid).
- In grokking: test accuracy — but we want to find something that moves *earlier* (see [[Grokking Predictors]]).
- Candidates from this vault: weight-norm (drops at grokking), entanglement entropy (spikes at grokking, [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]), spectral exponent α ([[Heavy-Tailed Self-Regularization]]).

> [!important]
> **Every [[Grokking Predictors|grokking predictor]] is, at its core, a proposed order parameter for the grokking phase transition.** The thesis benchmarks which order parameter fires earliest and most reliably.

## Why It Matters
Grokking is a phase transition in training time. The statistical-physics papers in this vault supply the rigorous machinery — replica method, message passing, [[Random Matrix Theory]] — to locate transitions and identify order parameters. This is exactly what [[Grokking Predictors]] try to measure: the moment just before the transition, visible in an internal quantity that moves before test accuracy.

## Key Instances in This Vault

| System | Control parameter | Transition | Order parameter | Paper |
|--------|-------------------|-----------|-----------------|-------|
| Learning (general) | samples/params | learnable ↔ not | optimal error / mutual info | [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]] |
| Deep nets (width) | params vs constraints | under ↔ over-parameterized | gen-error cusp | [[Spigler - A Jamming Transition Affects Generalization]] |
| Classifier (time) | epochs | memorise → collapse | within-class variability | [[Papyan - Prevalence of Neural Collapse]] |
| Diffusion model | denoising time | speciation → collapse | data-correlation spectrum | [[Biroli - Dynamical Regimes of Diffusion Models]] |
| Tensor network (sweeps) | training sweeps | memorise → grok | entanglement entropy | [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] |
| Transformer (steps) | training steps | memorise → **grok** | (the nine predictors) | [[Thesis Proposal Summary]] |

## First-Order vs Second-Order Transitions

- **Second-order (continuous):** order parameter grows smoothly from zero (e.g., magnetisation near a magnetic transition). The transition is gradual.
- **First-order (discontinuous):** order parameter jumps suddenly (e.g., water-ice). The system can get "stuck" in a metastable state before the jump — a **nucleation** event.

Grokking's sharp plateau followed by an abrupt jump is consistent with a **first-order-like** transition: the network is in a metastable memorising state, then nucleates a generalising circuit. This interpretation aligns with the "circuit-formation nucleation" view of [[Circuit Formation]].

## Evidence
[[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]], [[Spigler - A Jamming Transition Affects Generalization]], [[Biroli - Dynamical Regimes of Diffusion Models]], [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]].

## Relationship to Other Concepts
- Special cases: [[Jamming Transition]], [[Double Descent]] peak, [[Neural Collapse]].
- Each [[Grokking Predictors|predictor]] is a candidate order parameter.
- The [[Emergence]] concept is the plain-language name for the same phenomenon.
- [[Phase Transitions Across Models]] synthesises the cross-system view.

## Open Questions
Is grokking a first-order or second-order (continuous) transition? Is there a single universal order parameter that fires before the grokking transition across all tasks and architectures?

---
## Related Notes
- [[Jamming Transition]] · [[Double Descent]] · [[Emergence]]
- [[Phase Transitions Across Models]] · [[08 - Phase Transitions in Learning]]
- [[Grokking Predictors]] · [[Grokking]]
