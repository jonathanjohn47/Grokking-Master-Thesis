---
tags: [concept, data, generalization]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# Class Imbalance

## Definition
**Class imbalance** occurs when the training set has substantially different numbers of examples per class. The **imbalance ratio R** measures the severity: $R = N_{\text{majority}} / N_{\text{minority}}$. Class imbalance can silently distort what a network learns, biasing it toward majority classes and, past a critical threshold, causing [[Minority Collapse]] for minority classes.

## In Plain Words
If 95% of your images are "cat" and 5% are split among nine other animals, the network can score 95% accuracy just by always predicting "cat." The rare classes get little gradient signal and are learned poorly — or, past a tipping point, lumped together in a phenomenon called minority collapse.

## Why It Matters for This Vault

Class imbalance matters in two ways:
1. **Directly**: it is the trigger for [[Minority Collapse]] — the failure mode in which rare-class representations merge toward a single point, losing discriminative power.
2. **For grokking**: modular arithmetic tasks with $p = 97$ have 97 classes ($\{0, 1, \ldots, 96\}$) and by default are *balanced* — each output class appears equally often. This is one of the clean properties of the canonical grokking setup. However, other algorithmic tasks or practical deployments may be imbalanced, and understanding whether this changes grokking dynamics is an open question.

## The Phase Transition at a Critical Imbalance

[[Fang - Layer-Peeled Model and Minority Collapse]] showed, via the [[Layer-Peeled Model]], that class imbalance does **not** gradually harm minority classes — it is benign below a threshold and catastrophic above:

```
Minority class          
separability            
  │                     
  │ ████████████████    ← stays OK (Simplex ETF holds approximately)
  │                 \   
  │                  \  ← tipping point at critical R*
  │                   \_________________
  │                       ← minority collapse (classes merge)
  └────────────────────────────────────>  imbalance ratio R
```

This is a [[Phase Transition]] in representation geometry: the order parameter (minority class separability) drops sharply at a critical ratio $R^*$.

## The Tipping Point

The critical imbalance ratio $R^* = K_{\text{majority}} / K_{\text{minority}}$ (where $K$ is class count) depends on architecture and depth, but the [[Layer-Peeled Model]] gives a closed-form prediction that matches empirical data on VGG13 / CIFAR-10 subsets ([[Fang - Layer-Peeled Model and Minority Collapse]]). This predictive power is what makes the layer-peeled approach valuable: it converts an observation into a testable quantitative prediction.

## Common Fixes and Their Limitations

| Fix | Mechanism | Limitation |
|---|---|---|
| **Class re-weighting** | Up-weight minority class loss | Pushes tipping point to higher $R$, doesn't remove it |
| **Oversampling** (repeat minority examples) | Effectively increases minority class count | Creates overfitting pressure on duplicated examples |
| **Undersampling** (remove majority examples) | Reduces $R$ directly | Wastes data |
| **Data augmentation** | Creates new minority class variants | Task-dependent; rarely applicable to algorithmic tasks |

No fix completely eliminates the imbalance geometry problem — they all just push back the tipping point.

## Class Imbalance in the Canonical Grokking Setup

For $(a + b) \bmod 97$:
- 97 output classes, each appearing equally in the full dataset (all $97^2 = 9409$ pairs produce each output class exactly 97 times).
- With a 30% train split ($\approx 2794$ pairs), each output class has $\approx 28$ training examples.
- This is approximately balanced — no class is strongly disadvantaged.

Imbalance *could* arise if a non-uniform split is used or if certain operations produce skewed output distributions. For the multiplication operation $(a \times b) \bmod p$, certain residue classes (e.g., 0) are produced more often, creating mild imbalance — worth controlling in multi-task benchmarks.

## Key Insights
- The harm is **non-linear**: it stays mild until a [[Phase Transition|tipping point]] where rare classes merge ([[Fang - Layer-Peeled Model and Minority Collapse]]).
- Common fixes push the tipping point back but don't eliminate the underlying geometry problem.
- Balanced data is what enables [[Neural Collapse]] to form the clean [[Simplex ETF]] shape.
- The canonical grokking task (modular addition) is balanced — this is a design property, not a coincidence.

## Evidence
[[Fang - Layer-Peeled Model and Minority Collapse]] — shows exactly how imbalance drives the collapse and predicts the threshold in advance.

## Relationship to Other Concepts
- Direct cause of [[Minority Collapse]]; the opposite condition (balance) enables [[Neural Collapse]].
- A property of the dataset alongside split size — see [[Common Datasets]].
- The phase-transition structure (sharp threshold) is shared with many other transitions in this vault ([[Phase Transition]]).

## Open Questions
How does class imbalance change grokking timing and predictor reliability on algorithmic tasks? Does mild imbalance (e.g., from multiplicative tasks) affect which [[Grokking Predictors|predictor]] fires first?

---
## Related Notes
- [[Minority Collapse]] · [[Fang - Layer-Peeled Model and Minority Collapse]]
- [[Neural Collapse]] · [[Simplex ETF]] · [[Common Datasets]]
- [[Phase Transition]] · [[Layer-Peeled Model]] · [[Grokking Predictors]]
