---
tags: [concept, spectral, rmt, predictors]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[09 - Weight Decay and Regularization]]

# Heavy-Tailed Self-Regularization (HTSR)

## Definition
**Heavy-Tailed Self-Regularization (HTSR)** (Martin & Mahoney) is the theory that training *implicitly* regularises networks, leaving a fingerprint in the **eigenvalue spectrum of each weight matrix**: well-trained layers have heavy-tailed (power-law) spectra. The power-law exponent **α** quantifies regularisation strength — smaller α (heavier tail) means better-trained.

## In Plain Words
You can judge how well a network was trained just by looking at the *pattern* in its weight numbers — no data needed. Well-trained layers show a tell-tale "heavy-tailed" pattern: a few very large values among many small ones. A single number, alpha, summarises it; a heavier tail (smaller alpha) usually means better-trained. A fresh random network has a spectrum that looks like a fuzzy disc (the Marchenko-Pastur distribution — all eigenvalues clustered together). A well-trained network blows some eigenvalues outward into a long tail. The further out they go, the better-trained.

## What "Heavy-Tailed" Means Mathematically

For an $n \times m$ weight matrix $W$, compute $X = W^T W / n$ and find all eigenvalues $\{\lambda_i\}$. The **empirical spectral density (ESD)** is the distribution of these eigenvalues.

Two reference distributions from [[Random Matrix Theory|Random Matrix Theory (RMT)]]:

| Distribution | When it appears | What it looks like |
|---|---|---|
| **Marchenko-Pastur (MP)** | Pure random matrix | Bounded support, smooth bulk, no outliers |
| **Power-law (HTSR)** | Well-trained layers | Bulk + heavy tail: $p(\lambda) \sim \lambda^{-(\alpha+1)}$ for large $\lambda$ |

After training, the empirical distribution departs from Marchenko-Pastur: eigenvalues escape the MP bulk and form a heavy tail. The exponent $\alpha$ (fitted by maximum likelihood) describes how quickly the tail decays:
- $\alpha \gg 4$: weak tail, close to random, poorly trained.
- $2 \leq \alpha \leq 4$: "sweet spot" — well-trained, strong generalisation ([[Martin - Predicting Trends in Neural Network Quality]]).
- $\alpha < 2$: tail so heavy it indicates potential rank collapse or instability.

## The WeightWatcher Library
[[Martin - Predicting Trends in Neural Network Quality]] is implemented in the open-source **WeightWatcher** library. It:
1. Loads any PyTorch / TensorFlow model (no data needed).
2. Computes the ESD of every weight matrix.
3. Fits $\alpha$ to each layer's tail.
4. Reports per-layer and summary statistics.

The thesis uses WeightWatcher to compute HTSR Alpha and Correlation Traps throughout training — turning spectral snapshots into a temporal signal.

## How Grokking Shows Up in α

During the grokking plateau, the network is nominally frozen (loss ≈ 0, accuracy flat). But α is not frozen: [[Weight Decay]] continues to shrink weights, gradually shifting eigenvalue mass out of the MP bulk. In principle:

| Training phase | Expected α behaviour |
|---|---|
| Early training (memorisation) | Large α (near-random) |
| Plateau | α decreasing as weight decay accumulates |
| Grokking transition | Sharp drop — circuit's structured eigenvectors pull mass into the tail |
| Post-grokking | α stabilises at low value |

This is the **HTSR Alpha predictor** (Predictor #2 in [[The Nine Predictors]]). A key open question for the thesis (RQ1, RQ2): does α drop *early enough* to give useful lead time?

## Correlation Traps (Anti-Grokking Detector)

Beyond the bulk-to-tail transition, HTSR also diagnoses **anti-grokking** — when a grokked network *loses* generalisation on continued training. The signature is a **correlation trap**: a rank-one perturbation in the weight spectrum that is detectable by comparing the ESD before and after shuffling the rows of $W$. Under [[Anti-Grokking]], a small number of eigenvalues become anomalously large relative to the shuffled baseline — they are "trapped" correlations. This is Predictor #3 (Correlation Traps) in the thesis.

## Why It Matters for the Thesis

HTSR provides two of the nine predictors, both requiring no training data:
- **HTSR Alpha** — detects the approach of grokking (positive predictor).
- **Correlation Traps** — detects the onset of anti-grokking (negative predictor).

These are the only data-free predictors in the benchmark, which is a major practical advantage: monitoring the weight spectrum during training costs O(n²m) per layer — small enough to do every few hundred steps.

## Key Insights
- Power-law (HTSR) metrics out-discriminate norm-based metrics, especially distinguishing well- vs poorly-trained models ([[Martin - Predicting Trends in Neural Network Quality]]).
- The spectrum becomes heavy-tailed as effective [[Weight Decay|self-regularisation]] accumulates — so α can move at the grokking transition before test accuracy does.
- **Correlation traps** (rank-one perturbations detectable by shuffling) uniquely flag the generalisation collapse of [[Anti-Grokking]] (Prakash & Martin, 2025).
- A Marchenko-Pastur bulk with eigenvalues escaping outward is the "clean normal" for a trained layer — any deviation is a signal.

## Relationship to Other Concepts
- Built on [[Random Matrix Theory]] (Marchenko-Pastur distribution, Tracy-Widom law for outlier detection).
- A measurable fingerprint of [[Weight Decay|implicit/explicit regularisation]].
- Supplies two of [[The Nine Predictors]] (HTSR Alpha, Correlation Traps).
- Directly linked to [[Grokking Predictors]] (spectral family), [[Anti-Grokking]], [[Regularization]].
- The spectral signature is the time-domain cousin of static quality metrics used for large pretrained models.

## Evidence
[[Martin - Predicting Trends in Neural Network Quality]] (hundreds of pretrained models; WeightWatcher validation); [[Advani - High-dimensional Dynamics of Generalization Error]] (RMT dynamics of training); [[Random Matrix Theory]] (Marchenko-Pastur, Tracy-Widom).

## Open Questions
Does α move *early* enough to give useful lead time on algorithmic grokking tasks? Is the correlation-trap anti-grokking claim reproducible against competitors (thesis H7)? Can the per-layer α profile localise *which* layer groks first?

---
## Related Notes
- [[Martin - Predicting Trends in Neural Network Quality]] · [[Random Matrix Theory]] · [[Anti-Grokking]]
- [[The Nine Predictors]] · [[Grokking Predictors]] · [[Weight Decay]]
- [[Regularization]] · [[Interpolation Threshold]] · [[Spectral Bias]]
