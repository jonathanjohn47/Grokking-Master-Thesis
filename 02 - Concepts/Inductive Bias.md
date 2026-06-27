---
tags: [concept, theory, generalization]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Inductive Bias

## Definition
**Inductive bias** is the set of built-in preferences that make a model favour some solutions over others when many would fit the training data equally well. It is the "leaning" a model has before seeing a single training example, embedded in its architecture, optimiser, regularisation, and initialisation.

## In Plain Words
In the [[Overparameterization|overparameterized]] regime there are infinitely many weight configurations that achieve zero training error. The model has to pick one. **Inductive bias** is *how it picks* — the taste it has been given by its design choices. Change the bias, and you change which solution the model converges to. In grokking: memorising and generalising both achieve 100% training accuracy, so what eventually pushes the network toward the generalising solution is its bias — primarily the [[Weight Decay]] pressure toward smaller, simpler weights.

## Sources of Inductive Bias

There are four main sources, all present in the canonical grokking setup:

| Source | Example | Effect on grokking |
|---|---|---|
| **Architecture** | [[Transformer]] (attention, residual) | Attention head can implement trig identities cleanly |
| **Optimiser** | [[AdamW]] | Decoupled weight decay gives clean, reliable bias toward low norm |
| **Regularisation** | [[Weight Decay]] (λ) | Directly favours the minimum-norm solution — the Fourier circuit |
| **Initialisation** | Small init scale | Small init → lazy regime early; large init → richer features faster |

The *combination* matters: a transformer + AdamW + weight decay at the right λ produces grokking. Change any one component and grokking may not occur or may be delayed ([[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]).

## Explicit vs Implicit Bias

- **Explicit bias**: weight decay, dropout, L1 penalty — the choices written into the training script.
- **Implicit bias**: the solution that gradient descent finds *even without any explicit penalty*. The gradient-flow trajectory itself has a preference (often for low-norm, smooth solutions). This implicit bias can alone cause slow, eventual grokking without weight decay ([[Advani - High-dimensional Dynamics of Generalization Error]]).

## Bias in the Context of Grokking

During the grokking plateau, train loss ≈ 0 and gradients from the loss are negligible. What keeps the model moving at all is **inductive bias**:
1. Weight decay: shrinks all weights → erodes the memorising solution.
2. Implicit optimiser bias: gradient flow follows the minimum-norm path → draws toward the Fourier circuit.
3. Architecture bias: the transformer's attention mechanism can efficiently represent the Fourier circuit, so that solution has lower norm than alternatives.

The plateau *length* is roughly the time it takes for these biases to tip the balance from memorisation to generalisation. Adjust λ and the plateau shortens or lengthens — the bias control parameter for grokking ([[Varma - Explaining Grokking Through Circuit Efficiency]]).

## Shortcuts as Bias Failure

When the inductive bias points at the wrong feature — one that works on training data but fails on held-out data — the result is [[Shortcut Learning]]. Examples: a model that uses background colour to classify animals, or a model that memorises specific token positions rather than learning the underlying rule. In grokking, the memorising solution is itself a form of shortcut: it works on training data but is brittle, inconsistent, and eventually beaten by the true rule under weight-decay pressure ([[Geirhos - Shortcut Learning in Deep Neural Networks]]).

## Spectral Bias: Architecture-Level Inductive Bias

The **[[Spectral Bias]]** (frequency principle) is one of the most well-studied forms of inductive bias: neural networks learn low-frequency components of a task faster than high-frequency ones. On modular arithmetic, the correct rule (Fourier / trig-based) is relatively low-frequency, while the memorising lookup table is high-frequency (many sharp transitions). Spectral bias predicts the generalising solution is "preferred" by the architecture — consistent with eventual grokking.

## Key Insights
- Sources of bias: architecture, optimiser, regularisation ([[Weight Decay]]), initialisation.
- A useful bias points the model at the **intended rule**; a poor one points it at a [[Shortcut Learning|shortcut]] ([[Geirhos - Shortcut Learning in Deep Neural Networks]]).
- Gradient descent has its own *implicit* bias — even with no explicit penalty it favours lower-norm, smoother solutions ([[Advani - High-dimensional Dynamics of Generalization Error]]).
- In grokking, inductive bias is the *only* mechanism operating after train loss → 0; the whole grokking transition is bias at work.
- Inductive bias directly shapes the [[Cross-Entropy Loss|loss landscape]] traversal and is part of the [[Inductive Bias|inductive context]] the model operates in.

## Evidence
- [[Geirhos - Shortcut Learning in Deep Neural Networks]] — shortcuts = bias pointing at easy features.
- [[Canatar - Spectral Bias and Task-Model Alignment]] — spectral bias; alignment between model and task determines generalisation.
- [[Advani - High-dimensional Dynamics of Generalization Error]] — implicit optimiser bias analysis.

## Relationship to Other Concepts
- The lever behind [[Memorization]] vs [[Generalization]] and [[Shortcut Learning]].
- Expressed concretely as [[Spectral Bias]], [[Weight Decay]], and [[Neural Tangent Kernel|kernel]] choices.
- [[Cross-Entropy Loss]] + [[Weight Decay]] together form the most important inductive biases in the grokking setup.
- Changing the optimiser (e.g. switching to Muon instead of AdamW) changes the inductive bias — thesis RQ4.

## Open Questions
Which inductive biases reliably produce grokking? Can a predictor read off, mid-plateau, which bias is currently "winning" the memorise-vs-generalise race? How does the Muon optimiser's inductive bias compare to AdamW's for grokking tasks?

---
## Related Notes
- [[Spectral Bias]] · [[Weight Decay]] · [[Shortcut Learning]] · [[Generalization]] · [[Neural Tangent Kernel]]
- [[Geirhos - Shortcut Learning in Deep Neural Networks]] · [[Canatar - Spectral Bias and Task-Model Alignment]]
- [[Memorization]] · [[Cross-Entropy Loss]] · [[AdamW]]
