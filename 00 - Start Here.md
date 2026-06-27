---
title: Start Here
tags: [moc, home, grokking, index]
---

# 00 - Start Here

> [!summary]
> This is the home page and navigation hub for a self-contained knowledge base on the **[[Grokking]]** phenomenon in deep learning, built as the literature foundation for the master's thesis *[[Thesis Proposal Summary|A Unified Benchmark of Grokking Predictors]]* (Jonathan John, M.Sc. AI). You can learn the entire topic by following the reading order below — without opening the original papers first.

## What is this vault?

Twenty-three research papers plus the thesis proposal have been synthesised into a connected web of notes. The notes act simultaneously as a **literature review**, a **study guide**, a **research map**, and a **thesis preparation system**. Every note opens with a plain-language summary ("In Plain Words" / "The Gist"), so you can follow the whole topic without a technical background. Start at the top of the learning path and move downward; every note links to the concepts, papers, and syntheses it depends on.

## How to read this vault

> [!tip] Recommended reading order
> Follow the **Learning Path** in sequence. Each note ends with links to the concept notes and papers that go deeper. When a term appears in `[[double brackets]]`-style links, it is a clickable note you can open at any time.

### The Learning Path (start-to-finish)

1. [[01 - What Is Grokking]] — the phenomenon in one note
2. [[02 - The Grokking Training Dynamics]] — the three phases (memorise → plateau → grok)
3. [[03 - Historical Background]] — where the idea came from
4. [[04 - Core Experimental Setup]] — modular arithmetic, splits, architectures
5. [[05 - Memorization vs Generalization]] — the central tension
6. [[06 - Overparameterization and Interpolation]] — fitting more than you "should"
7. [[07 - Double Descent]] — the test-error curve that breaks classical statistics
8. [[08 - Phase Transitions in Learning]] — grokking as a transition between regimes
9. [[09 - Weight Decay and Regularization]] — the engine behind delayed generalisation
10. [[10 - Mechanistic Explanations and Circuit Formation]] — what the network actually learns
11. [[11 - Predicting Grokking]] — early-warning signals (the thesis core)
12. [[12 - Modern Developments]] — 2023–2026 frontier
13. [[13 - Open Problems and Research Gaps]] — where the thesis fits

## Map of Content

> [!info] The four note types
> - **[[01 - What Is Grokking|Learning Path]]** — a guided textbook, read in order.
> - **Concept notes** (`02 - Concepts/`) — one idea each, e.g. [[Double Descent]], [[Neural Collapse]], [[Weight Decay]], [[Heavy-Tailed Self-Regularization]].
> - **Literature notes** (`03 - Literature/`) — one per paper, structured and tagged.
> - **Synthesis notes** (`04 - Synthesis/`) — cross-paper arguments, e.g. [[Competing Theories of Grokking]], [[What Causes Grokking]].
> - **Thesis notes** (`05 - Thesis/`) — [[Research Gaps]], [[Future Directions]], [[The Nine Predictors]], [[Common Datasets]], [[Common Evaluation Metrics]].

### Key concept hubs

- Phenomenon: [[Grokking]] · [[Anti-Grokking]] · [[Memorization]] · [[Generalization]] · [[Emergence]]
- Generalisation theory: [[Double Descent]] · [[Overparameterization]] · [[Interpolation Threshold]] · [[Bias-Variance Tradeoff]] · [[Random Matrix Theory]] · [[Neural Scaling Laws]]
- Robustness & shortcuts: [[Shortcut Learning]] · [[Out-of-Distribution Generalization]] · [[Inductive Bias]] · [[Margin and Robustness]]
- Transitions & geometry: [[Phase Transition]] · [[Jamming Transition]] · [[Neural Collapse]] · [[Simplex ETF]] · [[Minority Collapse]] · [[Class Imbalance]]
- Foundations: [[Gradient Descent]] · [[Loss Landscape]] · [[Cross-Entropy Loss]] · [[Regularization]] · [[Modular Arithmetic]]
- Mechanism & prediction: [[Mechanistic Interpretability]] · [[Circuit Formation]] · [[Feature Learning]] · [[Representation Learning]] · [[Mean-Field Limit]] · [[Layer-Peeled Model]] · [[Grokking Predictors]] · [[Heavy-Tailed Self-Regularization]]

### Big-picture syntheses

- [[Competing Theories of Grokking]]
- [[What Causes Grokking]]
- [[Evolution of Grokking Research]]
- [[Empirical Evidence Across Studies]]
- [[Research Timeline]]

### Thesis launchpad

- [[Thesis Proposal Summary]] — the project this vault supports
- [[The Nine Predictors]] — the predictors being benchmarked
- [[Research Gaps]] · [[Future Directions]] · [[Potential Thesis Questions]]

## Orientation note

> [!important]
> Most of the collected papers are **not about grokking directly**. They are the *theoretical foundations of generalization in overparameterized models* — double descent, neural collapse, phase transitions, random matrix theory, kernel/feature learning. Grokking is best understood as a **dynamical, in-time version** of these static, model-complexity phenomena. The vault is organised to make that bridge explicit. See [[The Generalization Puzzle]] and [[What Causes Grokking]].

---
## Related Notes
- [[Vault Overview]] — full map, folder structure, and statistics
- [[Research Timeline]]
- [[13 - Open Problems and Research Gaps]]
