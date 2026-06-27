---
tags: [synthesis, evidence, comparison]
---
↑ Parent: [[00 - Start Here]]

# Empirical Evidence Across Studies

> [!summary]
> A cross-paper map of *what was measured, on what, and what was found*. Useful for seeing how directly each paper bears on grokking and for spotting agreements and gaps.

> [!tip] In plain words
> A big side-by-side table of who tested what, on which data, and what they found — so you can see at a glance where the papers agree and where the gaps are.

## Master comparison table

| Paper | Model / system | Task / data | Key measurable | Bearing on grokking |
|-------|----------------|-------------|----------------|---------------------|
| [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] | MPS tensor network | Fashion-MNIST, hyperspectral | entanglement entropy, O-information, transfer entropy | **Direct**: order parameters for the transition |
| [[Martin - Predicting Trends in Neural Network Quality]] | 100s of pretrained CNNs | ImageNet etc. | weight-spectrum power-law α | **High**: source of HTSR/Correlation-Trap predictors |
| [[Jiang - Network Properties Determine Neural Network Performance]] | 17 ImageNet models | 5 datasets + NAS | neural capacitance (graph) | **Method**: early-training prediction |
| [[Papyan - Prevalence of Neural Collapse]] | 3 architectures | 7 datasets | NC1–NC4 collapse metrics | **High (concept)**: structure after zero error |
| [[Mixon - Neural Collapse with Unconstrained Features]] | unconstrained-features model | synthetic | risk-landscape minimisers | **Concept**: why collapse forms |
| [[Xu - Dynamics in Deep Classifiers with the Square Loss]] | deep classifiers (theory) | classification | low rank, margin, NC, bounds | **High**: which zero-loss solution generalises |
| [[Mei - Generalization Error of Random Features Regression]] | random-features regression | sphere data | exact test-error asymptotics | **Foundational**: double descent |
| [[Rocks - Memorizing Without Overfitting]] | linear / 2-layer nets | synthetic | analytic bias/variance | **Foundational**: variance spike |
| [[Advani - High-dimensional Dynamics of Generalization Error]] | linear nets (RMT) | synthetic | error **dynamics**, frozen subspace | **High (concept)**: training-time analogue |
| [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]] | random GLMs | synthetic | mutual info, optimal error | **Foundational**: rigorous transition |
| [[Spigler - A Jamming Transition Affects Generalization]] | deep nets | image data | gen-error vs width, cusp | **Foundational**: jamming/double descent |
| [[Biroli - Dynamical Regimes of Diffusion Models]] | diffusion models | Gaussian mix + real | speciation/collapse times | **Analogical**: transitions are pervasive |
| [[Canatar - Spectral Bias and Task-Model Alignment]] | kernel / NTK | real + synthetic | spectral bias, alignment | **Boundary**: lazy-regime limits |
| [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] | ANN + brain | vision | manifold geometry | **High (concept)**: geometric order params |
| [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] | SOTA CNNs | random-label / random-noise | train/test gap under randomization | **Foundational**: memorise ≠ generalise |
| [[Baldi - Temporal Evolution of Generalization in Linear Networks]] | linear nets (1991) | identity + noise | validation-curve dynamics | **High (concept)**: earliest plateau/temporal view |
| [[Sokolić - Robust Large Margin Deep Neural Networks]] | DNNs (theory) | MNIST/CIFAR/ImageNet | margin + Jacobian spectral norm | **Moderate**: margin/robustness order param |
| [[Mei - A Mean Field View of Two-Layer Neural Networks]] | 2-layer nets (mean-field) | synthetic | distributional (PDE) dynamics | **High (concept)**: feature-learning regime |
| [[Bahri - Explaining Neural Scaling Laws]] | random-feature + pretrained | standard | power-law loss vs D, P | **Context**: smooth scaling vs transition |

## Agreements that recur

> [!success] Convergent findings
> - **Structure forms after zero training error** ([[Papyan - Prevalence of Neural Collapse]], [[Xu - Dynamics in Deep Classifiers with the Square Loss]]).
> - **The interpolation point is a transition with a variance/cusp peak** ([[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]], [[Spigler - A Jamming Transition Affects Generalization]]).
> - **Generalisation is predictable from internal quantities without test data** ([[Martin - Predicting Trends in Neural Network Quality]], [[Jiang - Network Properties Determine Neural Network Performance]]).
> - **Memorisation capacity ≠ generalisation, and delayed generalisation is intrinsic to learning dynamics** ([[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]], [[Baldi - Temporal Evolution of Generalization in Linear Networks]]).

## Tensions / gaps

> [!warning]
> - Only **one** paper ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]) measures grokking *directly*; the rest are foundations measured on vision/synthetic data.
> - **Feature-learning** accounts ([[Li - Representations and Generalization in Artificial and Brain Neural Networks]]) vs **lazy/kernel** accounts ([[Canatar - Spectral Bias and Task-Model Alignment]]) disagree on whether fixed-kernel theory can explain real generalisation.
> - No paper here compares grokking predictors head-to-head — the thesis gap ([[Research Gaps]]).

---
## Related Notes
- [[Competing Theories of Grokking]] · [[Phase Transitions Across Models]] · [[Research Gaps]]
