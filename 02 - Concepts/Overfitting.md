---
tags: [concept, generalization, foundations, core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Overfitting

## Definition
**Overfitting** occurs when a model fits the training data *too well* — including its noise and peculiarities — so it performs well on the training set but poorly on new, unseen data. The model has learned the quirks of the specific training sample rather than the underlying pattern.

## In Plain Words
Imagine studying for an exam by memorising the exact wording of past questions rather than understanding the subject. You'd ace the practice test but flounder on new questions. Overfitting is that: the model is a specialist at the data it saw, not at the general task.

## The Classical Picture

Classical statistics gives a clear story:

```
Test error
   |
   |  \.
   |   '.       ← classical "sweet spot"
   |    '-.____/'-   ← overfitting region
   |              '---
   +----------------------------→ model complexity / training time
       under      optimal     overfitting
```

- **Underfitting (high bias):** model too simple, misses the pattern.
- **Optimal:** just right.
- **Overfitting (high variance):** model too complex or overtrained, chases noise.

## Why Grokking Breaks the Classical Picture

Grokking is the clearest possible violation of "more training = more overfitting":

1. First, the network reaches 100% training accuracy — it has perfectly fit the training data, which classically looks like a textbook case of overfitting.
2. Test accuracy stays near chance — supporting the classical prediction.
3. But then: with **more training**, test accuracy suddenly jumps to 100%.

The network went from "classic overfitting" to "perfect generalisation" by *continuing to train* rather than stopping. Classical theory has no room for this.

The resolution: the classical story assumed we're at the optimal model size. In the **[[Overparameterization|overparameterized]]** regime with [[Weight Decay|regularisation]], "more training" is not the same as "more overfitting" — the regulariser slowly selects a *different*, lower-norm solution from the family of zero-loss options.

## Memorisation vs Overfitting (a key distinction)

A crucial subtlety: **memorising ≠ overfitting** in overparameterized models.

- [[Rocks - Memorizing Without Overfitting]] showed explicitly that models can fit training data exactly (*memorise*) yet still generalise well — **without** the classical overfitting penalty.
- [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] proved networks memorise even random labels, yet generalise on real data.

In the grokking context: the plateau phase looks like overfitting (train accuracy 100%, test accuracy chance), but the model is not "stuck" — it is evolving toward a better solution invisibly.

## Key Insights
- Overfitting is a **relative** concept: it depends on the solution the model has found, not just the train/test gap.
- In overparameterized models, the train/test gap is not a reliable indicator of whether the model is "done" or whether it will improve.
- [[Weight Decay]] fights overfitting by preferring low-norm solutions — which happen to generalise better.
- [[Early Stopping]] is the classical remedy for overfitting, but it would kill grokking if applied too early.

## Evidence
- [[Rocks - Memorizing Without Overfitting]], [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] — fundamental challenges to the classical view.
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] — "generalisation beyond overfitting" is literally in the title.

## Relationship to Other Concepts
- The opposite of [[Generalization]]; the excessive form of [[Memorization]].
- The classical explanation for why [[Early Stopping]] is needed.
- Overturned by [[Overparameterization]] and [[Double Descent]].
- The plateau phase of grokking *looks* like overfitting but is not — this is the central puzzle of [[What Causes Grokking]].

## Open Questions
Is the grokking plateau technically overfitting, or is it a distinct state? Can a predictor distinguish "true overfitting (will never grok)" from "apparent overfitting (on the way to grokking)"?

---
## Related Notes
- [[Generalization]] · [[Memorization]] · [[Early Stopping]]
- [[Overparameterization]] · [[Double Descent]] · [[Weight Decay]]
- [[05 - Memorization vs Generalization]] · [[Bias-Variance Tradeoff]]
