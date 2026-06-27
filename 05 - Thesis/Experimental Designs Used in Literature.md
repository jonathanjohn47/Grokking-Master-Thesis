---
tags: [thesis, methodology, experiments]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# Experimental Designs Used in Literature

> [!summary]
> The experimental templates across this corpus — the grokking benchmark's factorial design plus the foundational papers' setups — so the thesis can position its protocol and reuse proven methods.

> [!tip] In plain words
> The recipes researchers actually run — model sizes, data splits, weight-decay settings, and how long they train — collected here so they can be compared.

## The thesis factorial design

| Variable | Levels |
|----------|--------|
| Predictor | all 9 ([[The Nine Predictors]]) |
| Task | $(a+b)\bmod p$, $(a\times b)\bmod p$, parity, boolean XOR |
| Modulus / length | $p\in\{59,97\}$; bit-length $n\in\{6,8\}$ |
| Seeds | 10 canonical, 5 per variation cell |
| Architecture | 1–2 layer transformers; dim ∈ {64,128,256}; heads ∈ {1,4} |
| Optimiser | AdamW, weight decay ∈ {0, 0.01, 1.0}; Muon (secondary) |
| Steps | 100K main; 200K anti-grokking |
| Split | 30% train / 70% test |

~100 runs, ≤250K params each, ~30–80 min/run on Apple M1 MPS. **Validation gate:** reproduce canonical grokking first ([[Methodological Considerations]]).

## Foundational-paper designs (methods to borrow)

| Paper | Design | Reusable technique |
|-------|--------|--------------------|
| [[Papyan - Prevalence of Neural Collapse]] | 3 architectures × 7 datasets, track TPT | NC1–NC4 metrics as candidate signals |
| [[Martin - Predicting Trends in Neural Network Quality]] | meta-analysis of 100s of pretrained nets | WeightWatcher α extraction (data-free) |
| [[Jiang - Network Properties Determine Neural Network Performance]] | 17 models × 5 datasets, early-training | early-signal → final-performance protocol |
| [[Spigler - A Jamming Transition Affects Generalization]] | sweep width across transition, ± early stopping | controlled crossing of a transition |
| [[Mei - Generalization Error of Random Features Regression]] | exact asymptotics, $N,n,d\to\infty$ | analytic baseline for epoch-wise double descent |
| [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] | track entropy/info across sweeps | information order-parameter pipeline |

## Design principles distilled
- **Control the transition:** vary one parameter across the critical point.
- **Instrument the plateau:** log internal signals at high frequency (every 100 steps), save weight snapshots (every 5,000) for re-evaluation without retraining.
- **Pre-register** hypotheses and definitions ([[Potential Thesis Questions]]).

---
## Related Notes
- [[Common Datasets]] · [[Common Evaluation Metrics]] · [[Methodological Considerations]] · [[04 - Core Experimental Setup]]
