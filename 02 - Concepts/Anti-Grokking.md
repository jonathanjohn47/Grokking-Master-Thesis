---
tags: [concept, grokking, anti-grokking, predictors]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[11 - Predicting Grokking]]

# Anti-Grokking

## What Is It?

**Anti-grokking** is the reverse of grokking.

In grokking, a network goes from failing on new questions to suddenly succeeding. In anti-grokking, a network that has already learned to succeed on new questions suddenly starts **failing again** — even though its training score stays perfect.

Think of it as: the understanding that was gained is then lost.

---

## Why Does It Exist?

Anti-grokking is not something researchers set out to create. It was discovered when running very long training experiments.

After a network has grokked (gained generalisation), researchers kept training to see what would happen. In some cases, after continuing to train for hundreds of thousands more steps, the test accuracy collapsed back toward zero.

This was puzzling and concerning: if weight decay caused grokking by favouring the efficient generalising solution, can the same weight decay eventually destroy that solution too?

The answer appears to be: **yes, if it goes too far**.

---

## The Timeline of Anti-Grokking

A network that anti-groks goes through three phases:

**Phase 1 — Memorisation:**
- Training accuracy: 100%
- Test accuracy: near 0% (random guessing)
- Same as normal grokking Phase 1

**Phase 2 — Grokking (normal):**
- Training accuracy: 100%
- Test accuracy: jumps to near 100%
- The network has learned the rule

**Phase 3 — Anti-grokking:**
- Training accuracy: stays at 100%
- Test accuracy: collapses back toward 0%
- The generalising solution is being destroyed

The training accuracy never drops. The network still gets every training question right. But it loses the ability to answer new questions.

---

## What Causes Anti-Grokking?

The most likely explanation is that weight decay — the same force that causes grokking — eventually goes too far.

Here is how the process is thought to work:

1. Weight decay causes grokking by eroding the large, memorised solution and letting the small, efficient generalising solution win.
2. After grokking, weight decay keeps running. It keeps shrinking all weights.
3. The generalising solution — while smaller than the memorised solution — still has nonzero weights. These weights keep getting smaller.
4. Eventually, the generalising solution's weights become so small that it can no longer produce confident, correct outputs.
5. The network falls back on some other pattern that fits the training data but does not generalise.
6. Test accuracy collapses.

It is like a student who understood the rule, then studied so obsessively for so long that they started to overthink it and forget the fundamental insight they had gained.

> [!WARNING]
> Anti-grokking is not the same as **catastrophic forgetting** — a different phenomenon where a network forgets old skills when learning new ones. In anti-grokking, no new information is presented. The network is trained on the same data throughout. The collapse happens purely because of weight decay pressure over time.

---

## Why This Matters for the Thesis

Anti-grokking creates a second detection problem on top of grokking:

- You need predictors to tell you when **grokking is coming** (so you do not stop too early).
- You also need predictors to tell you when **anti-grokking is coming** (so you do not train too long).

And the evidence suggests these may require **completely different signals**. A good grokking predictor may be a terrible anti-grokking predictor.

Specifically, the thesis tests two hypotheses about this:

**Hypothesis H7:** A spectral signal called "Correlation Traps" is the only predictor that reliably detects anti-grokking — the other eight grokking predictors fail to detect it.

**Hypothesis H8:** A predictor's ability to detect grokking tells you nothing about its ability to detect anti-grokking. The two skills are uncorrelated.

If these hypotheses are confirmed, it means grokking and anti-grokking are governed by fundamentally different internal dynamics — not just opposite sides of the same coin.

---

## How to Detect Anti-Grokking: Correlation Traps

The proposed detector for anti-grokking is based on **spectral analysis** — analysing the mathematical properties of weight matrices.

Here is how it works in plain terms:

1. Take each weight matrix in the network.
2. Analyse the distribution of values in that matrix.
3. Compare this distribution to what you would get if you randomly shuffled the matrix (removing any patterns but keeping the overall scale).
4. If the real matrix shows a very specific kind of departure from the shuffled baseline — a large, rank-one spike — this is called a "correlation trap."
5. Correlation traps appear when the structure of the generalising solution (the rotation-based algorithm) is being destroyed by over-shrinking.

The key advantage: this detector only needs to look at the weight matrices. It does not need to run the network on any test data. This makes it practical for monitoring very long training runs.

---

## An Everyday Analogy

Imagine a bridge engineer who has designed an excellent bridge. The bridge works perfectly, holding many vehicles.

The engineer is then told: "We need to make the bridge lighter. Remove some metal."

The engineer carefully removes non-essential metal, and the bridge still works perfectly.

More metal is removed. Still works.

More metal is removed. Still works.

Eventually, the engineer removes too much. The bridge collapses — not because it was overloaded, but because it was made too light to function.

Anti-grokking is like the bridge collapse. Weight decay (removing metal) causes grokking initially (the efficient solution wins), but eventually removes so much that the structure cannot hold.

---

## Important Terms

**Anti-grokking:** The collapse of test accuracy after a network has already grokked. Training accuracy stays at 100%.

**Catastrophic forgetting:** A different phenomenon where a network forgets old skills when learning something new. Not the same as anti-grokking (which happens with no new information).

**Spectral analysis:** Analysing the mathematical properties of weight matrices, specifically the distribution of their "eigenvalues" or "singular values." Used to detect correlation traps.

**Correlation traps:** A specific pathological pattern in weight matrices that appears when the generalising solution is being destroyed. Detected using spectral analysis.

**Rank-one spike:** A specific mathematical feature in a weight matrix — all the variation is concentrated in a single direction. This is the specific "correlation trap" signal.

**AUC (Area Under the Curve):** A standard measure of how good a predictor is. 1.0 = perfect, 0.5 = no better than random.

---

## Common Misconceptions

> [!WARNING]
> **Misconception 1:** "Anti-grokking means the network forgot what it learned."
> Not exactly. The network never explicitly "stores" knowledge. The weights that implemented the generalising solution are being gradually eroded by weight decay until they can no longer function. It is more like structural degradation than forgetting.

> [!WARNING]
> **Misconception 2:** "If grokking predictors work, they should detect anti-grokking too."
> Evidence suggests they may not. Good grokking detectors and good anti-grokking detectors may require fundamentally different signals.

---

## Key Takeaways

- Anti-grokking is the collapse of test accuracy after grokking — the network loses generalisation while maintaining perfect training accuracy.
- It is likely caused by weight decay going too far and eroding the generalising solution's weights.
- It requires a different detection approach from grokking — specifically, spectral "correlation trap" signals.
- The thesis tests whether correlation traps uniquely detect anti-grokking and whether grokking-detection skill is correlated with anti-grokking-detection skill.
- Anti-grokking adds a second challenge: practitioners must not only avoid stopping too early (missing grokking) but also avoid training too long (causing anti-grokking).

---

## Related Notes
- [[Grokking]] · [[Heavy-Tailed Self-Regularization]] · [[The Nine Predictors]]
- [[Empirical Evidence Across Studies]] · [[Phase Transition]] · [[Weight Decay]]
- [[Grokking Predictors]] · [[Research Gaps]] · [[Thesis Proposal Summary]]
