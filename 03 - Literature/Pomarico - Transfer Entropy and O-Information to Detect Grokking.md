---
tags: [literature, grokking, information-theory, tensor-networks, primary-evidence]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Grokking]] · [[Information-Theoretic Measures]]

# Pomarico — Transfer Entropy and O-Information to Detect Grokking

# Citation
Pomarico, D., Cilli, R., Monaco, A., et al. (2025). *Transfer entropy and O-information to detect grokking in tensor network multi-class classification problems.* arXiv:2507.23346 [quant-ph].

# The Gist (Plain Words)
Grokking isn't only a neural-network thing. In a very different model (tensor networks), the same memorise-then-suddenly-understand jump appears, and it lines up with a sharp change in information measures.

# Research Question
Can grokking be observed and **detected with information-theoretic order parameters** in a non-neural, quantum-inspired model (Matrix Product State classifiers), and what distinguishes a grokking model from a merely overfitted one?

# Methodology
Trained **MPS (tensor-network) classifiers** on three-class problems using Fashion-MNIST and hyperspectral satellite imagery. Tracked **entanglement entropy**, **local magnetization**, and accuracy across training sweeps. Applied **transfer entropy** (causal dependencies between label-specific quantum masks) and **O-information** (synergy vs redundancy among class outputs).

# Key Findings
- Grokking on Fashion-MNIST **coincides with a sharp entanglement transition** and a **peak in redundant information** (O-information shifts synergistic→redundant).
- The **overfitted** hyperspectral model **retains synergistic, disordered** behaviour — never makes the transition.
- A "competition arises between fast, memorizing modes and slower, generalizing modes" in over-parameterized regimes.

# Strengths
- Rare **direct, instrumented** observation of grokking outside neural nets — strong evidence of substrate-independence.
- Provides concrete, computable **order parameters** for the transition.
- Clean contrast between grokking vs non-grokking runs.

# Limitations
- Tensor-network setting differs from the transformer/algorithmic-task canon; transfer to transformers is assumed, not shown.
- Two datasets only; small class count (3).
- Information estimators can be sensitive to discretisation/sample size.

# Relation to Other Papers
- Provides the **Higher-Order MI** family of [[The Nine Predictors|predictors]] and motivates information-based detection.
- Echoes the slow/fast-mode competition of [[Advani - High-dimensional Dynamics of Generalization Error]].
- Its entanglement transition is a concrete instance of the [[Phase Transition]] framework shared with [[Spigler - A Jamming Transition Affects Generalization]] and [[Biroli - Dynamical Regimes of Diffusion Models]].

# Relevance to Thesis
High. Direct evidence that grokking is a genuine internal reorganisation; supplies an information-theoretic predictor and the synergy→redundancy order parameter for the benchmark.

# Key Quotes
> "grokking in the fashion MNIST task coincides with a sharp entanglement transition and a peak in redundant information, whereas the overfitted hyperspectral model retains synergistic, disordered behavior."

# Tags
#grokking #information-theory #tensor-networks #phase-transition #primary-evidence

---
## Related Notes
- [[Information-Theoretic Measures]] · [[Grokking]] · [[Anti-Grokking]] · [[10 - Mechanistic Explanations and Circuit Formation]]
