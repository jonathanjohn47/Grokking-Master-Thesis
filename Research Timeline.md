---
tags: [timeline, history, moc]
---
↑ Parent: [[00 - Start Here]] · Narrative: [[Evolution of Grokking Research]]

# Research Timeline

> [!summary]
> A dated chronology of the work in this vault and the key grokking milestones around it. Three colours of work: **foundations** (generalisation theory), **grokking proper**, and **prediction/consolidation**.

## 1991 — Foundations: the temporal view begins
- **[[Baldi - Temporal Evolution of Generalization in Linear Networks]]** — analytical proof that even linear nets show **plateaus, multiple validation minima, and optimal stopping** over training. The earliest ancestor of grokking dynamics.

## 2016 — Foundations: margin & robustness
- **[[Sokolić - Robust Large Margin Deep Neural Networks]]** — generalisation bounded by classification [[Margin and Robustness|margin]] and Jacobian spectral norm, independent of depth/width.

## 2017 — Foundations: dynamics & transitions
- **[[Advani - High-dimensional Dynamics of Generalization Error]]** — training-time generalisation dynamics via [[Random Matrix Theory]]; frozen subspace; the closest classical analogue to the grokking plateau.
- **[[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]]** — rigorous learnable/non-learnable [[Phase Transition]] in GLMs.

## 2018–2019 — Foundations: interpolation, double descent & feature learning
- **[[Spigler - A Jamming Transition Affects Generalization]]** (2018) — interpolation peak as a physical [[Jamming Transition]].
- **[[Mei - A Mean Field View of Two-Layer Neural Networks]]** (2018) — SGD as distributional-dynamics PDE; rigorous [[Mean-Field Limit|feature-learning]] regime.
- **[[Mei - Generalization Error of Random Features Regression]]** (2019) — first exact model of the [[Double Descent]] curve.

## 2020 — Foundations: collapse & memorisation
- **[[Papyan - Prevalence of Neural Collapse]]** — terminal-phase [[Neural Collapse]]; structure forms after zero error.
- **[[Mixon - Neural Collapse with Unconstrained Features]]** — landscape explanation of collapse.
- **[[Rocks - Memorizing Without Overfitting]]** — bias/variance of interpolation; "memorize without overfitting."

## 2021 — Foundations: kernels, scaling & the generalization puzzle restated
- **[[Canatar - Spectral Bias and Task-Model Alignment]]** — [[Spectral Bias]] / task-model alignment for kernels & NTK.
- **[[Martin - Predicting Trends in Neural Network Quality]]** — [[Heavy-Tailed Self-Regularization]]; predict quality with no data (WeightWatcher).
- **[[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]]** — randomization test (CACM update of the 2017 ICLR paper): memorise random labels yet generalise; regularization neither necessary nor sufficient.
- **[[Bahri - Explaining Neural Scaling Laws]]** — four [[Neural Scaling Laws|scaling regimes]]; resolution-limited exponents from kernel/data-manifold spectra.

## 2022 — Grokking named
- **Power et al.** — grokking on modular arithmetic (the founding observation; summarised in [[01 - What Is Grokking]]).

## 2023 — Grokking explained; first predictors
- **Nanda et al.** — [[Mechanistic Interpretability|mechanistic]] Fourier-circuit account + progress measures.
- **Varma et al.** — circuit-efficiency explanation ([[Role of Weight Decay]]).
- **[[Xu - Dynamics in Deep Classifiers with the Square Loss]]** — low-rank/collapse dynamics + bounds (square loss).
- **Notsawo et al.** — Spectral Signature predictor ("predicting grokking long before it happens").
- **Tan & Huang** — L2-norm predictor.

## 2024 — Prediction proliferates; new lenses
- **[[Jiang - Network Properties Determine Neural Network Performance]]** — neural-capacitance early predictor.
- **[[Li - Representations and Generalization in Artificial and Brain Neural Networks]]** — [[Neural Manifolds|manifold-geometry]] order parameters.
- **[[Biroli - Dynamical Regimes of Diffusion Models]]** — speciation/collapse transitions in generative models.
- **Clauw et al.** — Higher-Order Mutual Information predictor.

## 2025 — Detection matures; grokking generalises
- **[[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]** — grokking in tensor networks; O-information / transfer-entropy detection.
- **Prakash & Martin** — HTSR Alpha & Correlation Traps (grokking + [[Anti-Grokking]]).
- **Zhou et al.** — Absolute Gradient Entropy (AGE) predictor.
- **Salah & Yevick** — Dropout-robustness predictor.
- **Tveit et al.** — Muon optimiser dramatically reduces grokking time.

## 2026 — Consolidation
- **[[Thesis Proposal Summary]]** — *A Unified Benchmark of Grokking Predictors*: the first head-to-head comparison of all nine predictors. Xu (2026) Commutator Defect & Weight-Space PCA predictors.

> [!important]
> Pattern: **discover → explain → predict → consolidate.** The thesis is the consolidation step. See [[Evolution of Grokking Research]] and [[Research Gaps]].

---
## Related Notes
- [[Evolution of Grokking Research]] · [[03 - Historical Background]] · [[The Nine Predictors]] · [[12 - Modern Developments]]
