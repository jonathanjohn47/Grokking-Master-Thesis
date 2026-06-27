---
tags: [literature, neural-collapse, theory, class-imbalance, phase-transition]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Layer-Peeled Model]] · [[Minority Collapse]]

# Fang — Layer-Peeled Model & Minority Collapse

# Citation
Fang, C., He, H., Long, Q., & Su, W. J. (2021). *Exploring deep neural networks via the Layer-Peeled Model: Minority collapse in imbalanced training.* Proceedings of the National Academy of Sciences (PNAS), 118(43).

# Research Question
Deep networks have too many layers to analyse all at once. Can we build a **simple stand-in model** that still behaves like a real trained network — and use it to both *explain* known patterns and *predict* new ones?

# The Big Idea (in plain words)
"Peel off" the top layer of the network and treat everything below it as a free knob. You are left with just two things to study: the **last-layer features** and the **last-layer classifier**. This stripped-down model — the **Layer-Peeled Model** — is small enough to solve with math, yet it reproduces real training behaviour. With it, the authors re-explain [[Neural Collapse]] and discover a brand-new failure mode they call **Minority Collapse**.

# Methodology
- Define the **[[Layer-Peeled Model]]**: minimise the loss over (last-layer weights, last-layer features) under simple size limits ("norm budgets") on each. The data only enters through these budgets.
- Solve it analytically for cross-entropy, contrastive, and general softmax-based losses.
- Test the predictions on real deep networks (VGG13 on subsets of CIFAR-10) with [[Weight Decay]].

# Key Findings
- **Balanced data → Neural Collapse.** Any best solution of the Layer-Peeled Model forms a **[[Simplex ETF]]** (classes spread out as symmetrically as possible). This gives a clean reason *why* [[Neural Collapse]] appears.
- **Imbalanced data → Minority Collapse.** When some classes have far fewer examples than others, the rare ("minority") classes' classifiers get pushed together until they become **identical directions** — the network can no longer tell them apart. See [[Minority Collapse]] and [[Class Imbalance]].
- **A sharp threshold (phase transition).** As the imbalance ratio R grows, nothing much happens — until R crosses a critical point, after which minority classifiers snap to parallel. The Layer-Peeled Model **predicts this tipping point in advance**, and real networks match it closely. See [[Phase Transition]].
- **The model predicts before it is confirmed.** Minority Collapse was first seen in the toy model, then found in the real network — evidence the surrogate is genuinely useful.

# Strengths
- Turns an intractable network into a solvable model **without losing the key behaviour**.
- Makes a falsifiable prediction (the tipping point) that experiments confirm.
- Practically important: explains *why* models fail on rare classes and hints at fixes.

# Limitations
- Idealised: the layers below the top are summarised by a single budget, so fine architecture details are dropped.
- Focuses on the terminal phase (long after zero training error), not the full training path.
- Assumes the network can reach a true minimum.

# Relation to Other Papers
- Sibling to [[Mixon - Neural Collapse with Unconstrained Features]] — both use a stripped-down last-layer model; Fang adds the imbalanced case and the phase transition.
- Extends the empirical [[Papyan - Prevalence of Neural Collapse]] with a tractable theory.
- The dynamic, training-time version of these ideas is [[Xu - Dynamics in Deep Classifiers with the Square Loss]].

# Relevance to Thesis
Moderate. Three hooks: (1) a clean **order-parameter / phase-transition** story (the imbalance tipping point) that parallels grokking's transition; (2) **[[Simplex ETF]] geometry** as a candidate signal for "good structure has formed"; (3) a caution for grokking benchmarks — on **imbalanced** algorithmic tasks, minority collapse could mask or mimic a grok, so class balance is a variable worth controlling.

# Key Quotes
> "Any solution to this model forms a simplex equiangular tight frame, which in part explains the recently discovered phenomenon of neural collapse."

> "Our analysis of the Layer-Peeled Model reveals a hitherto unknown phenomenon that we term Minority Collapse, which fundamentally limits the performance of deep learning models on the minority classes."

# Tags
#neural-collapse #layer-peeled-model #minority-collapse #class-imbalance #phase-transition #theory

---
## Related Notes
- [[Layer-Peeled Model]] · [[Minority Collapse]] · [[Class Imbalance]] · [[Simplex ETF]]
- [[Neural Collapse]] · [[Mixon - Neural Collapse with Unconstrained Features]] · [[Papyan - Prevalence of Neural Collapse]] · [[Xu - Dynamics in Deep Classifiers with the Square Loss]]
