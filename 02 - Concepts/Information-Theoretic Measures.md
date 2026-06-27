---
tags: [concept, information-theory, predictors]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Information-Theoretic Measures

## Definition
Information-theoretic measures quantify how information is shared, transmitted, and structured inside a network. The three key tools in this vault are: **mutual information** (shared information between two variables), **transfer entropy** (directed/causal information flow from one time series to another), and **O-information** (whether a group of variables is dominated by synergy or redundancy). Together they form the **Higher-Order MI** grokking predictor and reveal how the network's internal information architecture changes at the generalisation transition.

## Core Concepts: A Glossary

### Entropy $H(X)$
The average uncertainty in a variable $X$:
$$H(X) = -\sum_x p(x) \log p(x)$$
High entropy = unpredictable; low entropy = structured/predictable.

### Mutual Information $I(X;Y)$
How much knowing $X$ reduces uncertainty about $Y$, and vice versa:
$$I(X;Y) = H(X) + H(Y) - H(X,Y)$$
$I(X;Y) = 0$ if and only if $X$ and $Y$ are independent. It is symmetric (no direction).

### Transfer Entropy $T_{X \to Y}$
The directed version: how much of $Y$'s future is explained by $X$'s past, *beyond* what $Y$'s past already tells us:
$$T_{X \to Y} = I(Y_{t+1}; X_t \mid Y_t)$$
Non-zero $T_{X \to Y}$ implies $X$ is a causal driver of $Y$. ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] uses this to detect causal structure between label-specific quantum masks.)

### O-Information $\Omega$
Generalises MI to $n \geq 3$ variables. Measures whether the group is dominated by:
- **Redundancy** ($\Omega > 0$): multiple variables carry the same information — structured, duplicated representation.
- **Synergy** ($\Omega < 0$): the variables are only informative *together* — disordered, joint representation.
$$\Omega(X_1, \ldots, X_n) = (n-2) H(X_1, \ldots, X_n) + \sum_i H(X_i) - \sum_{i<j} H(X_i, X_j)$$

## What Happens at Grokking

[[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] (using a tensor network, not a transformer, as a proxy) found:

| Phase | O-information | Transfer entropy | Interpretation |
|---|---|---|---|
| Pre-grok (memorising) | Negative (synergistic) | Disordered, no clear causal chain | Features are jointly computed, not structured |
| Grokking transition | Sign flip: synergy → redundancy | Causal structure between label masks emerges | Circuit forms: structured, redundant representation |
| Post-grok (generalised) | Positive (redundant) | Stable causal structure | Fourier circuit encodes rule redundantly across heads |

The non-grokking (overfitting) model retains synergistic behaviour throughout, providing a clean contrast. The sign flip in $\Omega$ is the information-theoretic fingerprint of grokking.

## The Higher-Order MI Predictor

Clauw et al. (2024) translate this into a practical grokking predictor (Predictor #8 in [[The Nine Predictors]]):
- Monitor the sign and magnitude of $\Omega$ for groups of activations across training.
- **The moment $\Omega$ transitions from negative to positive** is the predictor signal — fired before test accuracy moves.
- This is the only predictor grounded in multivariate information theory rather than weight spectral analysis.

## Connections to Cross-Entropy

The training objective, [[Cross-Entropy Loss]], is itself an information-theoretic quantity:
$$\mathcal{L}_{\text{CE}} = H(y, \hat{y}) = H(y) + D_{\text{KL}}(y \| \hat{y})$$
Minimising cross-entropy is equivalent to minimising the KL divergence between the model's predicted distribution and the true label distribution — i.e., compressing the information gap. When the generalising circuit forms, the model's predicted distribution abruptly aligns with the true distribution: this is why test cross-entropy drops sharply at grokking.

## Key Insights
- **Synergy → redundancy** ($\Omega$ flip) at grokking: before generalising, class outputs carry synergistic (disordered) information; after, redundant (structured) information ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]).
- **Transfer entropy** reveals causal dependencies between label-specific activations.
- The overfitted (non-grokking) model **retains** synergistic, disordered behaviour — a clean contrast.
- These measures detect *internal reorganisation* at grokking that loss curves and accuracy curves miss entirely.
- The measures complement spectral ([[Heavy-Tailed Self-Regularization]]) and geometric ([[Neural Collapse]]) predictors — capturing a different facet of the transition.

## Evidence
[[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]; Clauw et al. (2024) Higher-Order MI predictor (see [[The Nine Predictors]]).

## Relationship to Other Concepts
- An order parameter for the grokking [[Phase Transition]].
- Complements spectral ([[Heavy-Tailed Self-Regularization]]) and geometric ([[Neural Collapse]]) probes.
- Supplies [[Grokking Predictors|Predictor #8]] (Higher-Order MI).
- [[Cross-Entropy Loss]] is itself an information-theoretic quantity (KL divergence).
- [[Emergence]] from the information-theory perspective is a synergy-to-redundancy flip.

## Open Questions
Do information measures fire **early** enough for useful lead time on transformer-based grokking (not just tensor networks)? Do they transfer from tensor networks to transformers (thesis transferability claim)? Is the $\Omega$ flip gradual or sharp in the transformer regime?

---
## Related Notes
- [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] · [[Grokking Predictors]] · [[Phase Transition]]
- [[Heavy-Tailed Self-Regularization]] · [[Neural Collapse]] · [[Cross-Entropy Loss]]
- [[The Nine Predictors]] · [[Emergence]] · [[Circuit Formation]]
