---
tags: [synthesis, theories, grokking]
---
↑ Parent: [[00 - Start Here]] · Related: [[What Causes Grokking]]

# Competing Theories of Grokking

> [!summary]
> Several explanations for grokking coexist. They are **not mutually exclusive** — most describe the same memorise→generalise transition from different vantage points (regularisation, mechanism, dynamics, information, geometry). This note lays them side by side.

> [!tip] In plain words
> There are several stories for why grokking happens, and they mostly aren't rivals — they're the same event seen from different angles: the "keep it simple" pressure, the circuit being built, the slow dynamics, the information reshuffle, and the geometry.

## The five main accounts

| Theory | Core claim | Mechanism of the transition | Primary support in vault | Main weakness |
|--------|-----------|------------------------------|--------------------------|---------------|
| **Regularisation / circuit efficiency** | Generalising circuit has lower norm; [[Weight Decay]] selects it once both fit data | Slow norm decay tips balance from memorising to generalising solution | [[Xu - Dynamics in Deep Classifiers with the Square Loss]], Varma et al. 2023 | Why is the efficient circuit slow to form? |
| **Slow-mode / dynamical** | GD has fast (memorising) and slow (generalising) modes; a frozen subspace delays generalisation | Slow modes evolve over the plateau until generalisation dominates | [[Advani - High-dimensional Dynamics of Generalization Error]] | Mostly linear theory |
| **Mechanistic** | Network builds an interpretable algorithm (Fourier circuits) | Gradual [[Circuit Formation]] under the surface | [[Mechanistic Explanations]], Nanda et al. 2023 | Task-specific (modular arithmetic) |
| **Information-theoretic** | Internal information reorganises (synergy→redundancy) | Entanglement/redundancy transition | [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] | Estimator sensitivity; transfer unproven |
| **Geometric / collapse** | Representations tighten to low-rank, collapsed, high-margin geometry | Terminal-phase [[Neural Collapse]] | [[Papyan - Prevalence of Neural Collapse]], [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] | Link to algorithmic grokking not yet shown |

## Where they agree

> [!important]
> All five agree on the **shape**: a metastable memorising state, a silent reorganisation, then an abrupt switch to a special (low-norm / efficient / collapsed / structured) generalising solution. They differ on **what to measure**. This is precisely why there are many [[Grokking Predictors|predictors]] — each operationalises a different theory as an order parameter.

## Where they disagree

- **Is [[Weight Decay]] necessary or just an accelerator?** Regularisation theory leans necessary; dynamical theory says grokking can occur slowly even without explicit decay. See [[Role of Weight Decay]].
- **Single universal order parameter, or task-specific?** Mechanistic/information accounts risk being task-bound; spectral/geometric accounts aim for universality.
- **Grokking vs [[Anti-Grokking]]:** same or different signals? The thesis predicts *different*.

## How the thesis adjudicates

By benchmarking predictors derived from each theory on a shared protocol, the thesis turns this theoretical debate into a **measurable** question: which operationalisation fires earliest and most reliably across tasks. See [[Thesis Proposal Summary]] and [[The Nine Predictors]].

---
## Related Notes
- [[What Causes Grokking]] · [[Role of Weight Decay]] · [[Mechanistic Explanations]] · [[Phase Transitions Across Models]]
