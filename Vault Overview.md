---
tags: [moc, overview, index, grokking]
---
↑ Parent: [[00 - Start Here]]

# Vault Overview

> [!summary]
> A complete map of this Obsidian knowledge base on **[[Grokking]]**, built as the literature foundation for *[[Thesis Proposal Summary|A Unified Benchmark of Grokking Predictors]]*. **102 interconnected notes** synthesise **24 source documents** (23 papers + the research proposal). Every note opens with a plain-language summary, so you can learn the whole topic without prior background. Read this for the bird's-eye view; read [[00 - Start Here]] to begin learning.

## Folder structure

```
Grokking Master Thesis/
├── 00 - Start Here.md            ← home / navigation hub
├── Vault Overview.md             ← you are here
├── Research Timeline.md          ← dated chronology
├── 01 - Learning Path/   (13)    ← guided textbook, read in order
├── 02 - Concepts/        (45)    ← one idea per note
├── 03 - Literature/      (24)    ← one structured note per paper
├── 04 - Synthesis/        (8)    ← cross-paper arguments + comparison tables
└── 05 - Thesis/           (9)    ← gaps, predictors, datasets, metrics, methods
```

## Reading order

1. **[[00 - Start Here]]** → follow the **Learning Path** [[01 - What Is Grokking]] → [[13 - Open Problems and Research Gaps]].
2. Dip into **concept notes** whenever a `[[link]]` invites you deeper.
3. Read **literature notes** for any paper you want in detail.
4. Use **synthesis notes** ([[Competing Theories of Grokking]], [[What Causes Grokking]], [[Empirical Evidence Across Studies]], [[Phase Transitions Across Models]]) for the big picture.
5. Use **thesis notes** ([[Research Gaps]], [[The Nine Predictors]], [[Methodological Considerations]]) to plan the work.

## Major themes

| Theme | Where | Key notes |
|-------|-------|-----------|
| The phenomenon | [[01 - What Is Grokking]], [[02 - The Grokking Training Dynamics]] | [[Grokking]], [[Memorization]], [[Generalization]], [[Anti-Grokking]] |
| Generalisation theory | [[06 - Overparameterization and Interpolation]], [[07 - Double Descent]] | [[Double Descent]], [[Interpolation Threshold]], [[Bias-Variance Tradeoff]], [[Random Matrix Theory]], [[Neural Scaling Laws]] |
| Phase transitions | [[08 - Phase Transitions in Learning]] | [[Phase Transition]], [[Jamming Transition]], [[Phase Transitions Across Models]] |
| Regularisation | [[09 - Weight Decay and Regularization]] | [[Weight Decay]], [[Heavy-Tailed Self-Regularization]], [[Role of Weight Decay]] |
| Mechanism & geometry | [[10 - Mechanistic Explanations and Circuit Formation]] | [[Mechanistic Interpretability]], [[Circuit Formation]], [[Neural Collapse]], [[Simplex ETF]], [[Layer-Peeled Model]], [[Feature Learning]], [[Representation Learning]], [[Mean-Field Limit]], [[Loss Landscape]], [[Margin and Robustness]], [[Neural Manifolds]] |
| Robustness & shortcuts | [[05 - Memorization vs Generalization]] | [[Shortcut Learning]], [[Out-of-Distribution Generalization]], [[Inductive Bias]], [[Margin and Robustness]] |
| Imbalance & failure modes | [[04 - Core Experimental Setup]] | [[Class Imbalance]], [[Minority Collapse]], [[Anti-Grokking]] |
| Foundations | [[02 - The Grokking Training Dynamics]] | [[Gradient Descent]], [[Cross-Entropy Loss]], [[Regularization]], [[Modular Arithmetic]], [[Emergence]] |
| Prediction (thesis core) | [[11 - Predicting Grokking]] | [[Grokking Predictors]], [[The Nine Predictors]], [[Information-Theoretic Measures]] |

## Papers processed (22 documents)

**Grokking-direct:** [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]], [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]], [[Varma - Explaining Grokking Through Circuit Efficiency]], [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]].
**Spectral / predictors:** [[Martin - Predicting Trends in Neural Network Quality]], [[Jiang - Network Properties Determine Neural Network Performance]].
**Double descent / interpolation / dynamics:** [[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]], [[Advani - High-dimensional Dynamics of Generalization Error]], [[Spigler - A Jamming Transition Affects Generalization]], [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]], [[Baldi - Temporal Evolution of Generalization in Linear Networks]], [[Mei - A Mean Field View of Two-Layer Neural Networks]].
**Generalization puzzle / margin / scaling:** [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]], [[Sokolić - Robust Large Margin Deep Neural Networks]], [[Bahri - Explaining Neural Scaling Laws]].
**Shortcuts & robustness:** [[Geirhos - Shortcut Learning in Deep Neural Networks]].
**Neural collapse:** [[Papyan - Prevalence of Neural Collapse]], [[Mixon - Neural Collapse with Unconstrained Features]], [[Xu - Dynamics in Deep Classifiers with the Square Loss]], [[Fang - Layer-Peeled Model and Minority Collapse]].
**Representations / kernels / generative:** [[Canatar - Spectral Bias and Task-Model Alignment]], [[Li - Representations and Generalization in Artificial and Brain Neural Networks]], [[Biroli - Dynamical Regimes of Diffusion Models]].
**Thesis proposal:** [[Thesis Proposal Summary]].

## Key findings across the literature

> [!success] What the corpus collectively shows
> - **Structure forms after zero training error** — the static backbone of grokking's plateau ([[Papyan - Prevalence of Neural Collapse]], [[Xu - Dynamics in Deep Classifiers with the Square Loss]]).
> - **The interpolation point is a phase transition** with a variance/cusp peak, then a second descent ([[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]], [[Spigler - A Jamming Transition Affects Generalization]], [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]]).
> - **Generalisation is predictable from internal quantities without test data** ([[Martin - Predicting Trends in Neural Network Quality]], [[Jiang - Network Properties Determine Neural Network Performance]]).
> - **Grokking is substrate-independent and a genuine internal reorganisation** ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]).
> - **Every grokking predictor is a candidate order parameter** for the transition; spectral, geometric, and information families all recur across models ([[Phase Transitions Across Models]]).

## Suggested thesis directions

The validated gap is the **absence of any fair, head-to-head predictor comparison** ([[Research Gaps]]). The thesis fills it with a unified leaderboard, a 9×4 transfer matrix, a learned ensemble, and the first independent [[Anti-Grokking]] benchmark. Promising extensions in [[Future Directions]]: a universal-order-parameter search, a feature-learning theory of epoch-wise [[Double Descent]], and geometry/collapse metrics as predictors. Concrete questions in [[Potential Thesis Questions]].

## Note conventions
- Top of each note: `← Previous · ↑ Parent · → Next` navigation (learning path) or a parent/hub line.
- Concept notes: Definition · Why It Matters · Key Insights · Evidence · Relationships · Open Questions.
- Literature notes: Citation · Research Question · Methodology · Key Findings · Strengths · Limitations · Relation to Other Papers · Relevance to Thesis · Key Quotes · Tags.
- Bottom of each note: **Related Notes** links.

---
## Related Notes
- [[00 - Start Here]] · [[Research Timeline]] · [[Evolution of Grokking Research]] · [[Research Gaps]] · [[The Nine Predictors]]
