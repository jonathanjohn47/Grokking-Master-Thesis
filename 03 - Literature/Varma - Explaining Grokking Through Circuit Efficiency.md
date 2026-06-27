---
tags: [literature, grokking, circuit-efficiency, weight-decay, regularization, primary-evidence]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Circuit Formation]] · [[Weight Decay]] · [[Grokking]]

# Varma — Explaining Grokking Through Circuit Efficiency

# Citation
Varma, V., Shah, R., Kenton, Z., Kramár, J., & Kumar, R. (2023). *Explaining grokking through circuit efficiency.* arXiv:2309.02390 [cs.LG].

# The Gist (Plain Words)
This paper answers the key question: *why* does the generalising circuit eventually win? The answer: it is more efficient — it achieves the same correct training outputs using **less weight norm** than the memorising solution. Under [[Weight Decay|weight decay]], the norm is penalised, so given enough time the efficient circuit is the one that survives. Grokking is just the moment the tipping-point is crossed.

# Research Question
Why does a network, having already reached perfect training accuracy via [[Memorization|memorisation]], *eventually* switch to a [[Generalization|generalising]] solution? What is the mechanism behind the delayed transition?

# Methodology
- Built on the **canonical grokking setup** of [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets|Power et al. (2022)]] and the **mechanistic account** of [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Nanda et al. (2023)]].
- Theoretical analysis of the **weight norms** of the memorising circuit vs. the generalising Fourier circuit.
- Supported by controlled experiments: measured weight norm of each "circuit component" independently and tracked their relative dominance during training.
- Tested predictions of the efficiency account by ablating weight decay.

# Key Findings
1. **Circuit efficiency is the key.** The generalising (Fourier) circuit produces the same correct logits as the memorising circuit but with **lower total weight norm**.
2. **Weight decay tips the balance.** Once training loss is near zero, weight decay's norm penalty is the dominant remaining gradient signal. It preferentially shrinks the memorising circuit (higher norm) faster than the generalising one (lower norm). Eventually the generalising circuit dominates the output — this is grokking.
3. **The plateau length is set by the efficiency gap.** A more efficient generalising circuit (lower norm ratio) = shorter plateau; a less efficient one = longer plateau.
4. **Grokking can be accelerated** by increasing weight decay (speeds up norm erosion) or by any intervention that makes the generalising circuit relatively more norm-efficient.
5. **The same logic predicts [[Anti-Grokking]]**: if the generalising circuit becomes *less* norm-efficient than some re-emerging memorising pattern under extended training, test accuracy can collapse again.

# Strengths
- Simple, clean, and well-supported mechanistic account.
- Makes quantitative predictions (plateau length scales inversely with efficiency gap) that are confirmed.
- Unifies the [[Weight Decay|regularisation]] and [[Mechanistic Interpretability|mechanistic]] perspectives into one story.
- Consistent with [[Neural Collapse]] terminal-phase dynamics (the "cleanup" process selecting the low-norm structure).

# Limitations
- Relies on the specific **Fourier circuit structure** identified for modular arithmetic; generality to other tasks is not fully demonstrated.
- Does not explain *how* the Fourier circuit forms — only why it eventually wins once formed.
- The exact definition of "circuit efficiency" requires knowing which circuit the network uses, which is task-specific.

# Relation to Other Papers
- **Discovery:** [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] gave the phenomenon.
- **Mechanism:** [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] identified the Fourier circuit Varma et al. explain.
- **Weight-decay dynamics:** [[Xu - Dynamics in Deep Classifiers with the Square Loss]] proves rigorously that weight decay + normalisation drives low-norm, efficient solutions with provable generalisation bounds.
- **Implicit regularisation:** [[Advani - High-dimensional Dynamics of Generalization Error]] shows gradient descent provides implicit regularisation even without explicit weight decay.
- **Spectral evidence:** [[Martin - Predicting Trends in Neural Network Quality]] shows the self-regularisation induced by training is visible in heavy-tailed weight spectra.

# Relevance to Thesis
**High.** The circuit efficiency account is one of the five main theories in [[Competing Theories of Grokking]] and informs:
- Why the **L2-norm predictor** tracks the transition (it measures norm erosion directly).
- Why the **Commutator Defect** is the expected top performer (it captures Hessian geometry of circuit efficiency).
- The [[Role of Weight Decay]] synthesis note and [[What Causes Grokking]] causal chain.

# Key Quotes
> "We identify the reason networks grok: the generalising circuit is more efficient — it achieves the same training loss with lower weight norm. Under L2 regularisation, the network eventually converges to the more efficient solution."

> "We find that grokking occurs at a predictable time that is inversely related to the efficiency gap between the memorising and generalising solutions."

# Tags
#grokking #circuit-efficiency #weight-decay #mechanistic #regularization #primary-evidence

---
## Related Notes
- [[Circuit Formation]] · [[Weight Decay]] · [[Role of Weight Decay]] · [[What Causes Grokking]]
- [[Mechanistic Interpretability]] · [[Grokking Predictors]] · [[The Nine Predictors]]
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] · [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
