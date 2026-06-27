---
tags: [literature, neural-collapse, theory, geometry]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Neural Collapse]]

# Mixon — Neural Collapse with Unconstrained Features

# Citation
Mixon, D. G., Parshall, H., & Pi, J. (2020). *Neural collapse with unconstrained features.* arXiv:2011.11619 [cs.LG].

# The Gist (Plain Words)
Strip a network down to just its last layer and you can prove the tidy "neural collapse" geometry is the best possible solution — which is why training keeps drifting toward it.

# Research Question
Why does **[[Neural Collapse]]** emerge? Can a minimal, tractable model reproduce it and explain it via the loss landscape?

# Methodology
Proposed the **unconstrained features model**: treat last-layer features as free variables (drop the network that produces them) and study the landscape of empirical risk over (features, classifier). Analysed minimisers and showed neural collapse arises empirically and structurally.

# Key Findings
- The **Simplex ETF** collapsed geometry is the (essentially global) **minimiser** of the unconstrained-features risk.
- Provides a landscape-level explanation: the dynamics are *drawn* to the collapsed configuration.
- Confirms neural collapse is not an architecture artefact but a property of the optimisation objective.

# Strengths
- Clean, analyzable model that isolates the cause of collapse.
- Foundational for the large "unconstrained features" theory literature.

# Limitations
- Idealised: ignores the feature map / real network constraints.
- Balanced-class assumption; square/CE specifics.
- Static minimiser analysis, not training dynamics.

# Relation to Other Papers
- Theoretical companion to the empirical [[Papyan - Prevalence of Neural Collapse]].
- Its dynamic/low-rank extension is [[Xu - Dynamics in Deep Classifiers with the Square Loss]].

# Relevance to Thesis
Moderate. Explains *why* terminal-phase structure forms — relevant to using collapse geometry as a grokking order parameter, and to the "generalising solution is special" argument.

# Key Quotes
> "We propose a simple unconstrained features model in which neural collapse also emerges empirically ... we provide some explanation ... in terms of the landscape of empirical risk."

# Tags
#neural-collapse #theory #geometry #terminal-phase

---
## Related Notes
- [[Neural Collapse]] · [[Papyan - Prevalence of Neural Collapse]] · [[Xu - Dynamics in Deep Classifiers with the Square Loss]]
