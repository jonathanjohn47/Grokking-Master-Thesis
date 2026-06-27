---
tags: [thesis, datasets, reference]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# Common Datasets

> [!summary]
> Tasks and datasets used across grokking and generalisation studies in this vault — what to use, and why each matters.

> [!tip] In plain words
> The menu of tasks grokking studies use — mostly clock-math and simple logic puzzles — and why each one is handy.

## Algorithmic tasks (the grokking canon)

| Task | Definition | Role |
|------|-----------|------|
| Modular addition | $(a+b)\bmod p$, $p=97$ | Canonical grokking benchmark; known Fourier circuit |
| Modular multiplication | $(a\times b)\bmod p$ | Tests structure beyond addition |
| Parity | $\text{parity}(x_1\dots x_n)$ | Classic hard-to-learn Boolean function |
| Boolean | $a\oplus b\oplus c$ (XOR) | Tiny, fast; transfer check |

> [!important]
> Algorithmic tasks are ideal because they have an **exact rule**: "test accuracy" measures true [[Generalization]], not interpolation noise. A small train split (~30%) is what exposes the memorise→grok gap ([[04 - Core Experimental Setup]]).

## Datasets in the foundational papers

| Dataset | Used by | Purpose |
|---------|---------|---------|
| Fashion-MNIST | [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] | grokking in tensor networks |
| Hyperspectral satellite imagery | [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] | non-grokking (overfit) contrast |
| ImageNet + 5 transfer datasets | [[Jiang - Network Properties Determine Neural Network Performance]] | early-training model selection |
| 7 canonical image datasets (MNIST, CIFAR, etc.) | [[Papyan - Prevalence of Neural Collapse]] | terminal-phase collapse |
| Synthetic / Gaussian-mixture / sphere | [[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]], [[Barbier - Optimal Errors and Phase Transitions in High-Dimensional GLMs]], [[Biroli - Dynamical Regimes of Diffusion Models]] | exact, solvable theory |

## Takeaway for the thesis
The benchmark stays on **algorithmic tasks** (clean ground truth, laptop-scale) but borrows the **information** ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]) and **collapse** ([[Papyan - Prevalence of Neural Collapse]]) measurements developed on richer data.

---
## Related Notes
- [[Common Evaluation Metrics]] · [[Experimental Designs Used in Literature]] · [[04 - Core Experimental Setup]]
