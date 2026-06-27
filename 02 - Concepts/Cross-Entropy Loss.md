---
tags: [concept, optimization, foundations]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# Cross-Entropy Loss

## What Is It?

**Cross-entropy loss** is the mathematical measurement used to tell a neural network how wrong its predictions are during training.

It is the most common "score" used in classification tasks (tasks where the answer is one of several possible categories). In grokking experiments, it is the standard choice.

---

## Why Does It Exist?

During training, the network needs feedback after every attempt: "How wrong were you? By how much should you change?"

This feedback is provided by the **loss function** — a single number that gets larger when the network is wrong and smaller when the network is right.

The training process adjusts the network's weights to make this number as small as possible.

Cross-entropy loss was designed for classification tasks because it has a very useful property: it measures not just whether the answer was wrong, but **how confidently wrong it was**.

---

## How It Works: Plain English

When a network classifies something, it outputs a score for each possible category. For clock math with 97 possible answers, the network outputs 97 scores.

These scores are converted to probabilities (summing to 100%) using a function called **softmax**. Think of it as distributing 100 percentage points across all possible answers.

Cross-entropy loss then asks: **what probability did the network give to the correct answer?**

- If the network gave the correct answer 99% probability → very small loss (nearly right)
- If the network gave the correct answer 50% probability → medium loss
- If the network gave the correct answer 1% probability → very large loss (confidently wrong)

The loss is calculated as: **negative log of the probability given to the correct answer**.

(Logarithms make the math work well — they convert probabilities near 0 and near 1 to manageable numbers.)

---

## A Concrete Example

Suppose the task is clock math with 5 possible answers (0, 1, 2, 3, 4) and the correct answer is 2.

**Well-calibrated network:**
Probabilities: [0.05, 0.05, 0.80, 0.05, 0.05]
The network gives 80% probability to the correct answer (2). Loss is low.

**Uncertain network:**
Probabilities: [0.20, 0.20, 0.20, 0.20, 0.20]
The network gives equal probability to everything (20% each). Loss is medium.

**Confidently wrong network:**
Probabilities: [0.05, 0.05, 0.05, 0.05, 0.80]
The network gives 80% probability to the wrong answer (4), and only 5% to the correct answer (2). Loss is very high.

The loss pushes the network in the right direction:
- It rewards increasing the probability of the correct answer.
- It punishes giving high probability to wrong answers.

---

## Why Cross-Entropy Never "Finishes"

An important and subtle property of cross-entropy loss: **it always wants the network to be more confident**.

Even if the network gives 99% probability to the correct answer, the loss is still slightly above zero. There is still a small gradient pushing for 99.9%, then 99.99%, and so on.

This means even after the network gets all training answers right, the loss is still pushing the weights to increase the confidence in correct answers.

Why does this matter for grokking?

During the plateau, when training accuracy is already 100%, the loss is near zero but not exactly zero. The cross-entropy gradient is still pushing for more confidence. At the same time, weight decay is pushing all weights toward zero.

This creates a tug-of-war:
- Cross-entropy says: "Make the correct-answer weights bigger."
- Weight decay says: "Make all weights smaller."

This tug-of-war is what drives the internal reorganisation during the plateau. The terminal-phase structure of the network (including the neat geometric arrangement called neural collapse) emerges from this tension.

---

## Cross-Entropy vs Square Loss

There is another commonly used loss function called **square loss** (or mean squared error). It measures the squared difference between the predicted output and the true output.

Both can be used for classification. They produce similar results in practice, but:

- Cross-entropy is more common in practice and is what grokking experiments use.
- Square loss is easier to analyse mathematically, so theorists prefer it for proving theorems.
- Both, combined with weight decay, drive the network toward the same final geometric arrangement (called the Simplex ETF).

---

## An Analogy

Imagine a weather forecaster who says "70% chance of rain" and it rains.

One scoring system: "You were right!" (binary — just right or wrong)

Cross-entropy scoring: "You were 70% confident it would rain, and it did. Your score is based on exactly that 70%." If you had said 99% and it rained, you would get a better score. If you had said 10% and it rained, you would get a terrible score.

This scoring system pushes the forecaster to be accurate AND confident. Cross-entropy loss does the same for neural networks.

---

## Important Terms

**Loss function:** A mathematical measurement of how wrong a network's predictions are. The training process minimises this.

**Cross-entropy loss:** A loss function that measures how much probability the network assigned to the correct answer. Penalises being confidently wrong, rewards being confidently right.

**Classification:** A task where the answer is one of several categories (like "this clock-math answer is 37" or "this image is a cat").

**Softmax:** A function that converts a list of raw scores (logits) into probabilities that sum to 1.

**Logits:** The raw, unnormalised scores that a network outputs before they are converted to probabilities.

**Gradient:** The signal that tells each weight how to change to reduce the loss.

**Square loss (MSE):** An alternative loss function that measures the squared difference between prediction and truth. Mathematically simpler to analyse, but less common in practice.

**Neural collapse:** A geometric phenomenon where the network's internal representations of different categories converge to a maximally symmetric arrangement. Emerges from the tension between cross-entropy and weight decay.

**Simplex ETF:** The specific symmetric geometric arrangement that neural collapse converges to. Every category's representation is equally spaced from all others.

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "Once the network scores 100% accuracy on training data, the loss is zero."
> Not quite. 100% accuracy means the network gives the correct answer the highest probability. But the loss is zero only if the network gives 100% probability to the correct answer — which never happens in practice. The loss approaches zero but never quite reaches it.

> [!TIP]
> This is actually useful for grokking: because the loss never truly reaches zero, there is always a small gradient driving the network toward more confident representations. This is what keeps the network changing during the plateau, even when accuracy looks flat.

---

## Key Takeaways

- Cross-entropy loss measures how much probability the network gives to the correct answer.
- It rewards confidence in the right answer and punishes confidence in wrong answers.
- It never "finishes" — there is always a small push toward more confidence, even at 100% accuracy.
- The tension between cross-entropy (increase confidence) and weight decay (shrink weights) drives internal reorganisation during the grokking plateau.
- Cross-entropy is used in all standard grokking experiments; square loss is used in theoretical analyses.

---

## Related Notes
- [[Weight Decay]] · [[Neural Collapse]] · [[Simplex ETF]] · [[Gradient Descent]] · [[AdamW]]
- [[Xu - Dynamics in Deep Classifiers with the Square Loss]] · [[Fang - Layer-Peeled Model and Minority Collapse]]
- [[Inductive Bias]] · [[Information-Theoretic Measures]] · [[Minority Collapse]]
