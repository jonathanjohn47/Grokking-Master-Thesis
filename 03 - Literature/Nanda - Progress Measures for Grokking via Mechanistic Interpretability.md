---
tags: [literature, grokking, mechanistic-interpretability, circuits, fourier, primary-evidence]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Mechanistic Interpretability]] · [[Circuit Formation]] · [[Grokking]]

# Nanda — Progress Measures for Grokking via Mechanistic Interpretability

# Citation
Nanda, N., Lawrence, L., Chan, T., MacDiarmid, T., & Driscoll, C. (2023). *Progress measures for grokking via mechanistic interpretability.* In *Proceedings of the International Conference on Learning Representations (ICLR 2023)*. arXiv:2301.05217.

# The Gist (Plain Words)
This paper opened the "black box" of the grokked transformer. Researchers reverse-engineered the trained network and found it had secretly learned to do clock-math by treating numbers as angles on a clock face, adding those angles using trigonometry, and reading off the result. They also defined "progress measures" — internal metrics that rise during the plateau *before* test accuracy does — the conceptual ancestor of the [[Grokking Predictors|grokking-predictor literature]].

# Research Question
What algorithm does a transformer actually implement after grokking on modular arithmetic — and can we build **internal "progress measures"** that track the formation of this algorithm during the silent plateau, *before* test accuracy moves?

# Methodology
- **Architecture:** same single-layer transformer as [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets|Power et al. (2022)]], trained on $(a+b)\bmod 97$.
- **Reverse-engineering:** used weight-visualisation and activation patching (causal tracing) to read out the algorithm embedded in trained weights.
- **Progress measures:** defined multiple internal quantities — e.g. "excluded loss" (loss on a restricted Fourier frequency set), "Fourier multiplicity," cosine similarity of weights with the predicted circuit structure — and tracked them across the training run.

# Key Findings
1. **The algorithm is Fourier/trig-based.** The grokked transformer implements $(a+b)\bmod p$ by:
   - Embedding $a$ and $b$ as rotations (points on a circle), using a handful of key frequencies $\omega_k = 2\pi k / p$.
   - Adding the angle representations.
   - Reading off the modular sum from the combined rotation using trig identities: $\cos(\omega_k (a+b)) = \cos(\omega_k a)\cos(\omega_k b) - \sin(\omega_k a)\sin(\omega_k b)$.
   - See [[Fourier Features]] for the conceptual explanation.
2. **The plateau is active.** Progress measures rise *monotonically* during the flat plateau — the circuit is under construction the whole time, invisible in loss or accuracy.
3. **Generalisation is abrupt.** Once progress measures cross a threshold, test accuracy follows in a sudden jump.
4. **The mechanism is interpretable and exact** — the circuit is not a vague "learned feature" but a specific, human-readable computation.

# Strengths
- First complete reverse-engineering of a grokked model.
- Progress measures are the conceptual prototype for all subsequent [[Grokking Predictors|predictor research]].
- Mechanistic account unifies [[Weight Decay|weight-decay]] and [[Circuit Formation]] explanations.
- Open-sourced weights and code; highly reproducible.

# Limitations
- Only $(a+b)\bmod p$; whether other tasks produce interpretable circuits is open.
- Progress measures are **task-specific** (they exploit knowledge of the Fourier circuit structure); the thesis tests whether more general, task-agnostic predictors can do as well.
- Small transformer; scalability is unknown.

# Relation to Other Papers
- **Discovery:** [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] gave the phenomenon to explain.
- **Why it works:** [[Varma - Explaining Grokking Through Circuit Efficiency]] explains *why* the Fourier circuit wins via lower weight norm.
- **Information view:** [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] sees the same transition in tensor networks via information theory.
- **Terminal-phase geometry:** [[Papyan - Prevalence of Neural Collapse]] and [[Xu - Dynamics in Deep Classifiers with the Square Loss]] show the structure-forming-after-zero-loss pattern Nanda et al. observe.

# Relevance to Thesis
**Central.** This paper provides:
1. The **canonical grokking setup** the thesis replicates.
2. The **mechanistic account** that grounds several predictors (Commutator Defect tracks Hessian geometry of the circuit; Spectral Signature tracks early-spectrum precursors).
3. The **validation baseline**: the thesis must reproduce Nanda et al.'s grokking before testing any predictor.

# Key Quotes
> "We find a natural, post-hoc explanation of the mechanism behind grokking via a beautiful algorithm that the network has learned: treating each element as a vector in a 2D Fourier basis."

> "We find progress measures which are tracked monotonically — they are a precise notion of 'how close is the network to having learned the algorithm.'"

> "We hypothesise that grokking occurs when a generalising circuit and a memorising circuit are both present, and the generalising circuit becomes more efficient."

# Tags
#grokking #mechanistic-interpretability #fourier-circuits #progress-measures #primary-evidence

---
## Related Notes
- [[Mechanistic Interpretability]] · [[Circuit Formation]] · [[Fourier Features]] · [[Grokking Predictors]]
- [[10 - Mechanistic Explanations and Circuit Formation]] · [[Mechanistic Explanations]]
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] · [[Varma - Explaining Grokking Through Circuit Efficiency]]
