---
tags: [concept, neural-collapse, class-imbalance, phase-transition, geometry]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Minority Collapse

## Definition
**Minority collapse** is a failure mode in [[Neural Collapse]]-type training where, under sufficient class imbalance, the network's last-layer representations (and classifiers) for the minority classes collapse to a **single shared direction** — making those classes indistinguishable. Discovered by Fang et al. (2021) via the [[Layer-Peeled Model]].

## In Plain Words
Imagine training to recognise 10 animals, where 7 breeds are common (many training examples) and 3 are rare. Past a certain imbalance level, the network's internal representation for the 3 rare animals becomes a single blurry point — it can no longer tell them apart at all, even if they are objectively very different. Adding more imbalance doesn't gradually hurt; it crosses a line and then the rare classes *merge completely*.

## The Mechanism

Under the [[Layer-Peeled Model]], the optimal last-layer geometry balances two forces:
1. **Separation pressure** (from the loss): push class means apart so they're easier to classify.
2. **Compression pressure** (from [[Weight Decay]]): pull all class means toward the origin.

For majority classes (many training examples), the separation pressure is strong — they stay separated. For minority classes (few training examples), the separation pressure is weak — and once the imbalance is severe enough, the compression pressure wins, collapsing minority classes together.

**The tipping point**: there is a critical imbalance ratio $R^*$ below which the geometry is approximately healthy (slightly unequal but separated), and above which minority classes merge completely. This is a [[Phase Transition]] — the order parameter (minority class separation) drops sharply at $R^*$.

## Schematic

```
Class means in representation space:

Balanced (R ≈ 1):            Minority collapse (R > R*):
    Majority                     Majority
    *   *   *                    *   *   *   
      ↑ ETF                            
    *                          Minority: * ≈ * ≈ *  ← merged
    *   *   *                      (all point same direction)
   Minority
```

## The Exact Threshold

The [[Layer-Peeled Model]] gives a closed-form prediction for $R^*$:
$$R^* = \frac{K_\text{maj}}{K_\text{min}} \cdot \frac{\rho_W}{\rho_H}$$
where $K_\text{maj}$ and $K_\text{min}$ are class counts per group, and $\rho_W$, $\rho_H$ are the norm budgets for classifier and feature vectors respectively. [[Fang - Layer-Peeled Model and Minority Collapse]] confirmed this threshold matches empirical observations on VGG13 / CIFAR-10.

## Why It Matters for Grokking

1. **Warning for benchmarking**: if a grokking task is class-imbalanced, minority collapse could make test accuracy misleading — the model might "grok" majority classes while never learning minority ones. The test accuracy would reflect majority performance, not true generalisation.

2. **An analogy for the plateau**: grokking's memorising state is a kind of "collapse under pressure" — the network produces undifferentiated representations for test inputs (it has no rule for them). Minority collapse is the analogous failure in representation geometry. Studying minority collapse dynamics may give insight into grokking dynamics.

3. **A measurable phase transition**: like grokking, minority collapse has a sharp threshold and a measurable order parameter (minority class cosine similarity) — a template for understanding transitions in representation space.

## Canonical Grokking Setup: Not Affected

The canonical modular arithmetic task ($p = 97$, uniform split) is **balanced** by construction: every output class appears equally often. Minority collapse is not a concern for this setup. However, for:
- Multiplication tasks (some residues appear more often as products)
- Concatenated tasks
- Real-world deployments

imbalance may appear and minority collapse may distort the grokking signal.

## Key Insights
- Driven by **[[Class Imbalance]]** past a critical threshold — a sharp [[Phase Transition]] in representation geometry.
- The healthy counterpart is [[Neural Collapse]] on balanced data, where classes spread into a symmetric [[Simplex ETF]] instead of merging.
- Predicted by theory ([[Layer-Peeled Model]]) before being observed empirically — a successful quantitative prediction.
- The mechanism is a competition between loss-driven separation and weight-decay-driven compression.

## Evidence
[[Fang - Layer-Peeled Model and Minority Collapse]] — predicts minority collapse in the layer-peeled model; confirms on VGG13 / CIFAR-10 subsets.

## Relationship to Other Concepts
- The imbalanced-data breakdown of [[Neural Collapse]]; the opposite of [[Simplex ETF]] formation.
- Predicted via the [[Layer-Peeled Model]]; an instance of a sharp [[Phase Transition]].
- Caused by [[Class Imbalance]].
- Can distort [[Grokking Predictors]] on imbalanced algorithmic tasks.

## Open Questions
Could a minority-collapse-style metric detect when a grokking model is *partially* generalising (some classes grokked, others not)? Does the transition from "some classes grokked" to "all classes grokked" resemble minority collapse in reverse?

---
## Related Notes
- [[Fang - Layer-Peeled Model and Minority Collapse]] · [[Layer-Peeled Model]] · [[Class Imbalance]]
- [[Neural Collapse]] · [[Simplex ETF]] · [[Phase Transition]] · [[Weight Decay]]
