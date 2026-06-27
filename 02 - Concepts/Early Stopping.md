---
tags: [concept, optimization, generalization, foundations]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Early Stopping

## What Is It?

**Early stopping** is one of the most common techniques used to prevent neural networks from memorising training data (overfitting).

The idea is simple: keep watching how well the network performs on new data (the validation set). When performance stops improving and starts getting worse, stop training.

You "stop early" — before the network has fully memorised the training data.

---

## Why Does It Exist?

In classical machine learning, there was a well-known problem called overfitting: if you train a model for too long, it memorises the training data so thoroughly that it starts to fail on new data.

Imagine studying for an exam by memorising the answers to the exact practice questions. You ace the practice test, but then fail the real exam because the questions are slightly different. That is overfitting.

Early stopping was designed to prevent this: watch the performance on new questions (not the same ones being trained on), and stop when that performance peaks.

---

## How It Works (Classical Version)

During training, you track two things:
- **Training loss:** How wrong the network is on the training data. Usually keeps decreasing.
- **Validation loss:** How wrong the network is on new data held out from training.

In the classical scenario:
1. Training loss decreases → The network is learning.
2. Validation loss also decreases → The network is generalising.
3. Validation loss starts increasing → The network is overfitting. Stop here.

You save the model weights from the point just before validation loss started rising. This is your final model.

---

## The Problem with Early Stopping in Grokking

Early stopping works well in classical settings. But in grokking, it would be **catastrophic**.

Here is why:

In grokking, after the initial memorisation phase:
- Training accuracy: 100% (perfect)
- Test accuracy: near 0% (random guessing)
- Both scores look frozen for tens of thousands of training steps

From the outside, this looks exactly like overfitting: the network is 100% on training data and failing on new data. A standard early stopping rule would say: "Stop — this model has overfit."

But stopping here would mean missing the grokking event entirely. The understanding was still coming — it just hadn't arrived yet.

```
Accuracy
  |
  |   Training accuracy: ████████████████████████████████████████
  |
  |   Test accuracy:     ██████████████████████████████
  |                      ← plateau looks like overfitting
  |                      (but it's not)                 ↗ grokking
  |   _____________________________________________________/______
  |
  +---------------------------------------------------------> steps
       Early stopping          Still plateau           Grokking
       would stop here!
```

> [!WARNING]
> If the researchers who discovered grokking had used early stopping, they would never have found grokking at all. They discovered it precisely because they kept training far past the point where early stopping would have suggested stopping.

---

## Why the Plateau Looks Like Overfitting (But Isn't)

In classical overfitting, the network's test performance gets worse as it memorises training data quirks. The training score keeps improving but the test score deteriorates.

In grokking's plateau:
- Training score is already at 100% (memorisation is complete)
- Test score is near 0% — but NOT because it is deteriorating. It was never good to begin with.
- The test score is flat, not declining. The network is just... stuck.

The difference is subtle but important:
- **Overfitting:** Test performance was good, then got worse.
- **Grokking plateau:** Test performance was never good, and stays flat for a long time.

If you look carefully, the validation loss does not increase during the plateau in grokking (which it would in classical overfitting). It just stays flat. But most early stopping implementations would still stop — the performance is not improving, so why continue?

---

## The Practical Decision Problem

This is the core challenge the thesis is trying to solve.

During the grokking plateau:
- You cannot tell from training/test scores whether grokking is coming or not.
- The scores look identical whether grokking is 5,000 steps away or will never happen.
- Early stopping gives you no guidance.

The only solution is to look **inside** the network — at internal measurements that change during the plateau before the test accuracy does. This is what grokking predictors are for.

A grokking predictor gives you the information early stopping cannot: "This network is on its way to grokking" or "This network will never grok."

> [!TIP]
> Think of it as upgrading early stopping: instead of watching only external scores (training and test accuracy), you also watch internal health metrics. A doctor does not just ask "How do you feel today?" — they also take blood pressure, check oxygen levels, run tests. Grokking predictors are the equivalent of internal health tests for neural networks.

---

## A Connection to Other Phenomena

Early stopping also relates to a broader phenomenon called the **interpolation threshold** and **double descent**.

When you stop training at the right moment (just before the validation loss starts rising), you are essentially picking a model at a specific complexity level. This moment often corresponds to the network being near the interpolation threshold — where it can just barely fit the training data.

Researchers found that stopping at this point avoids the worst behaviour (the variance spike at the threshold) but also misses the eventual improvement (the second descent, or grokking). Stopping just removes the sharp cusp — you avoid the worst but also the best.

---

## Important Terms

**Early stopping:** A training technique where you stop training when validation performance stops improving. Prevents classical overfitting but can prevent grokking.

**Validation set:** A held-out portion of data not used for training. Used to monitor how well the network generalises during training.

**Validation loss:** The loss computed on the validation set. Used to detect overfitting: if it starts increasing, the network is overfitting.

**Overfitting:** When a network memorises training data quirks and fails on new data. Test performance was once good but deteriorates.

**Plateau:** A period during grokking when both training and test scores look flat. Different from overfitting — test performance was never good, not declining from a better state.

**Interpolation threshold:** The model size (or training duration) where the model just barely fits all training data. Error often peaks here.

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "If test accuracy is at 0%, the network has overfit."
> Not necessarily. In grokking, the network's test accuracy is near 0% during the plateau not because it overfit (which means performance declined from a better state) but because it never generalised in the first place. The test performance is flat, not declining.

> [!WARNING]
> **Misconception:** "Early stopping is always good practice."
> It is good practice in classical settings where the risk is overfitting. In grokking settings, it would prevent the network from ever reaching generalisation.

---

## Key Takeaways

- Early stopping monitors validation performance and stops training when it stops improving.
- It prevents classical overfitting — but would prevent grokking if applied during the plateau.
- The grokking plateau looks like overfitting from the outside (100% training, 0% test) but is fundamentally different: test performance was never good, not declining.
- The practical consequence: practitioners cannot use early stopping in grokking settings without internal signals to guide them.
- Grokking predictors are the replacement for early stopping: internal measurements that reveal whether grokking is coming.

---

## Related Notes
- [[Overfitting]] · [[Generalization]] · [[Grokking Predictors]]
- [[Double Descent]] · [[Jamming Transition]] · [[Interpolation Threshold]]
- [[05 - Memorization vs Generalization]] · [[Methodological Considerations]]
