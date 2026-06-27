---
tags: [literature, grokking, founding-paper, primary-evidence, algorithmic-tasks]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Grokking]] · [[Memorization]] · [[Generalization]]

# Power — Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets

# Citation
Power, A., Burda, Y., Edwards, H., Babuschkin, I., & Misra, V. (2022). *Grokking: Generalisation beyond overfitting on small algorithmic datasets.* arXiv:2201.02177 [cs.LG].

# The Gist (Plain Words)
The paper that named the phenomenon. A tiny transformer trained to do clock-math first memorises all the answers, then sits frozen for a very long time, and then — out of nowhere — suddenly learns the actual rule and aces every unseen question. They called this "grokking." Everything in this vault descends from this observation.

# Research Question
When training small [[Transformer|transformers]] on small **algorithmic datasets** (modular arithmetic, permutations, etc.), does test accuracy ever improve after the model has already reached 100% training accuracy — and if so, how and why?

# Methodology
- **Architecture:** single-layer and two-layer transformers (≤ 250K parameters).
- **Tasks:** modular arithmetic ($(a \bmod p)$, $(a \times b) \bmod p$ for prime $p \in \{59, 97, 113\}$), permutation composition, others.
- **Split:** ~30% of all input pairs as training data, ~70% as test.
- **Optimiser:** AdamW with [[Weight Decay|weight decay]] (key variable swept).
- **Training budget:** $10^4$–$10^5$ steps, far past zero training loss.
- Tracked train and test accuracy/loss at every step.

# Key Findings
1. **The phenomenon is real and reproducible.** After reaching 100% training accuracy, test accuracy stays near chance for thousands of steps — then jumps, often within hundreds of steps, to near 100%. The delay can be 100× or more the time to memorisation.
2. **Weight decay is the main lever.** Without weight decay the generalisation jump is absent or hugely delayed; larger weight decay shortens the plateau.
3. **Algorithmic structure matters.** Tasks with an exact underlying rule (e.g. modular addition) grok reliably; less structured tasks grok less cleanly.
4. **Small train fraction is necessary.** With too large a training set the model generalises immediately (no plateau); with too small a set it may never grok. There is a window.
5. **The phenomenon is not specific to one architecture** — observed across depth/width variants of the transformer.

# Strengths
- First discovery and clear naming of the grokking phenomenon.
- Clean, reproducible experimental setup that became the canonical benchmark.
- Systematic sweep of hyperparameters (weight decay, train fraction, task type).
- Opened an entire research direction.

# Limitations
- **No mechanism.** Power et al. observe and characterise but do not explain *why* it happens. The mechanism was worked out by Nanda et al. (2023) — see [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]].
- **Algorithmic tasks only.** Whether grokking generalises to vision or language is left open.
- **No predictor.** No internal signal is provided to forecast when grokking will arrive — the gap the [[Thesis Proposal Summary|thesis]] fills.

# Relation to Other Papers
- **Mechanism:** [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] reverse-engineers the Fourier circuit the grokked network runs.
- **Cause:** [[Varma - Explaining Grokking Through Circuit Efficiency]] gives the circuit-efficiency explanation of *why* grokking eventually wins.
- **Foundations:** most of the vault ([[Double Descent]], [[Phase Transition]], [[Neural Collapse]]) provides the theoretical skeleton the observation implies.
- **Beyond transformers:** [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] shows the same memorise→generalise jump in tensor networks.
- **Prediction:** [[The Nine Predictors]] is the thesis's response to the lack of any predictor in Power et al.

# Relevance to Thesis
**Central.** This paper is the primary observation the thesis builds on. The thesis takes the exact setup of Power et al. (modular arithmetic, small transformer, AdamW with weight decay, 30% split) as its benchmark environment, then asks: "can we forecast *when* grokking will arrive?"

# Key Quotes
> "We show that such models undergo a phase transition from memorisation to generalisation, often many thousands of gradient steps after training loss has converged."

> "We call the occurrence of delayed generalisation 'grokking', after the term coined by Robert Heinlein."

> "Regularisation has a large effect on whether grokking occurs."

# Tags
#grokking #founding-paper #modular-arithmetic #weight-decay #phase-transition #primary-evidence

---
## Related Notes
- [[Grokking]] · [[01 - What Is Grokking]] · [[02 - The Grokking Training Dynamics]] · [[04 - Core Experimental Setup]]
- [[Weight Decay]] · [[Modular Arithmetic]] · [[Transformer]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] · [[Varma - Explaining Grokking Through Circuit Efficiency]]
