---
tags: [learning-path, predictors, thesis-core]
---
← Previous: [[10 - Mechanistic Explanations and Circuit Formation]]  ↑ Parent: [[00 - Start Here]]  → Next: [[12 - Modern Developments]]

# 11 - Predicting Grokking

## What Is This Note About?

This note describes the core practical problem that the thesis is trying to solve.

We know grokking happens. We know roughly why it happens. But there is still a serious unsolved problem:

> **During the plateau, how do you know if grokking is coming?**

This note explains the prediction problem, introduces the nine proposed early-warning signals (called predictors), and explains why a fair comparison of them matters.

---

## The Prediction Problem

Imagine you are a researcher training a neural network. You watch it reach 100% training accuracy in the first few hundred steps. Then, for the next 30,000 steps, both the training score and the test score look completely flat.

You face a decision: keep training, or stop?

- If grokking is coming in another 10,000 steps, you should **keep training**.
- If the network will never grok (it is stuck in the memorised solution permanently), you should **stop** — continuing is a waste of computing resources.

But the accuracy curves tell you nothing. They are flat. They look identical whether grokking is 5,000 steps away or will never happen.

This is the prediction problem. Without a reliable early-warning signal, you have no basis for your decision.

---

## The Solution: Internal Early-Warning Signals

The idea behind grokking predictors is:

> Even though the external scores (training accuracy, test accuracy) are flat during the plateau, things are changing **inside** the network. Some of those internal changes happen **before** the test accuracy jumps.

If you can find the right internal measurement, you can detect those changes during the plateau and forecast that grokking is approaching.

The internal measurements researchers have proposed are called **grokking predictors**.

---

## What Makes a Good Predictor?

A good predictor must satisfy four requirements:

**1. Accurate:** When it says "grokking is coming," grokking should actually be coming. It should have a low false-alarm rate.

**2. Early:** It should signal grokking well before it actually happens — giving enough lead time to make a useful decision. Signalling 10 steps before grokking is not useful. Signalling 5,000 steps early is useful.

**3. Transferable:** It should work not just on the specific task it was originally tested on. A predictor only tested on clock math might fail on parity or image classification. A good predictor should work across different tasks and network sizes.

**4. Cheap:** Computing the predictor should not require large amounts of extra work. If the predictor requires running the full test set every step, it defeats the purpose.

---

## The Nine Predictors

Researchers have proposed at least nine different predictors. Here is a plain-English description of each:

### Predictor 1: Commutator Defect
- **What it measures:** A property of how the gradients (signals that drive learning) are changing.
- **Intuition:** When the generalised circuit is forming, the pattern of gradient changes becomes more organised in a specific way. This predictor detects that organisation.

### Predictor 2: HTSR Alpha (Spectral Heavy-Tail Exponent)
- **What it measures:** The statistical distribution of the values in the weight matrices.
- **Intuition:** As the network transitions from memorisation to generalisation, the pattern of values in its weight matrices changes in a specific, measurable way. The pattern becomes "heavier-tailed" (a few large values dominate, rather than values being spread evenly).

### Predictor 3: Correlation Traps
- **What it measures:** Statistical patterns in shuffled weight matrices.
- **Intuition:** A network heading toward anti-grokking (collapse) shows a specific pathological pattern in its weights. This predictor detects that pattern before it causes collapse.

### Predictor 4: Weight-Space PCA
- **What it measures:** How concentrated the variation in weight matrices is.
- **Intuition:** As the generalised circuit forms, the meaningful variation in the weights concentrates into fewer dimensions. This "concentration" is detectable before the test accuracy jumps.

### Predictor 5: L2 Weight Norm
- **What it measures:** The total size of all the weights (sum of squares).
- **Intuition:** The memorised solution has large weights; the generalised solution has smaller weights. As weight decay erodes the memorised solution, the total weight size decreases. A decreasing weight norm is a sign of approaching grokking.
- **Note:** This is the simplest predictor and the most intuitive. It directly reflects the weight-decay mechanism.

### Predictor 6: Spectral Signature
- **What it measures:** Specific patterns in the weight matrix values, measured early in training.
- **Intuition:** Certain patterns in the weight matrices, visible very early in training, can forecast whether and when grokking will occur. This predictor tries to detect those patterns as early as possible.

### Predictor 7: AGE (Gradient Entropy)
- **What it measures:** The randomness of the gradient signals.
- **Intuition:** During memorisation, gradients are chaotic and high-entropy. As the generalised circuit forms, gradients become more organised and lower-entropy. This predictor tracks that organisation.

### Predictor 8: Higher-Order Mutual Information
- **What it measures:** How much information different parts of the network share about the task.
- **Intuition:** At grokking, the information inside the network reorganises from a "synergistic" pattern (where the parts together have information that no single part has) to a "redundant" pattern (where many parts share the same information). This reorganisation is detectable before test accuracy changes.

### Predictor 9: Dropout Robustness
- **What it measures:** How much the network's performance changes when some of its connections are randomly switched off.
- **Intuition:** A network that has learned the actual rule is robust — even if you randomly disable some connections, it still knows the rule and can compute the answer. A network that has only memorised is fragile — removing any connection disrupts its memorised answers. This robustness difference is detectable before the test accuracy jump.

---

## A Summary Table

| # | Predictor Name | What It Measures |
|---|---------------|-----------------|
| 1 | Commutator Defect | Organisation of gradient change patterns |
| 2 | HTSR Alpha | Distribution pattern of weight matrix values |
| 3 | Correlation Traps | Pathological patterns in weights (anti-grokking detector) |
| 4 | Weight-Space PCA | Concentration of variation in weight matrices |
| 5 | L2 Weight Norm | Total size of all weights |
| 6 | Spectral Signature | Weight matrix patterns measured early in training |
| 7 | AGE (Gradient Entropy) | Randomness of gradient signals |
| 8 | Higher-Order Mutual Information | How much the network's parts share task information |
| 9 | Dropout Robustness | How robust the network's performance is to random connection removal |

---

## Why a Fair Comparison Is Needed

Each of these predictors was:
- Proposed by a different research team
- Tested on that team's specific task and network architecture
- Compared against at most two or three other predictors

No one has put all nine predictors on the same experiment, on the same tasks, and compared them fairly.

This means:
- We do not know which predictor is most reliable overall.
- We do not know which works earliest.
- We do not know which transfers best to new tasks and architectures.
- We do not know whether some work for detecting anti-grokking while others only detect grokking.
- We do not know if combining multiple predictors (an ensemble) works better than any single predictor.

The thesis fills this gap by creating the first unified, fair benchmark of all nine predictors.

---

## The Connection to Phase Transitions

As discussed in the previous note ([[08 - Phase Transitions in Learning]]), grokking is a phase transition.

Each predictor is, in essence, a proposed **order parameter** for this transition — a measurement that changes at the transition point.

The thesis is asking: **which proposed order parameter is most reliable?**

This is a fundamental scientific question about the nature of the grokking transition, not just a practical engineering question about tools.

---

## Important Terms

**Grokking predictor:** An internal measurement of a neural network that changes during the plateau phase, before the test accuracy jumps. Used to forecast whether and when grokking will occur.

**False alarm rate:** How often a predictor says "grokking is coming" when it actually does not come. A predictor with too many false alarms is not useful.

**Lead time:** How far in advance of the actual grokking event a predictor fires. More lead time means more useful.

**Transferability:** Whether a predictor calibrated on one task (e.g., clock math) still works on different tasks (e.g., image classification). Crucial for a predictor to be generally useful.

**Weight norm:** The total size of all weights in the network, measured by adding their squares. Predictor 5 tracks this.

**Gradient entropy:** A measure of how random or organised the gradient signals are. Predictor 7 tracks this.

**Mutual information:** A measure of how much two things are related. Predictor 8 tracks this between different parts of the network.

**Dropout:** A technique of randomly switching off some connections in a network during testing. Used in Predictor 9 to measure robustness.

**Ensemble:** A combination of multiple predictors, where the combined signal is used instead of any single predictor.

**AUC:** "Area Under the Curve" — a standard way to measure how good a predictor is. An AUC of 1.0 is perfect; an AUC of 0.5 is no better than random.

---

## Key Takeaways

- The prediction problem: during the plateau, external scores are flat and give no information about whether grokking is coming.
- Grokking predictors are internal measurements that change before test accuracy does, giving early warning.
- A good predictor must be accurate, early, transferable, and cheap.
- At least nine different predictors have been proposed by different research teams.
- No fair, unified comparison of all nine predictors exists — this is the gap the thesis fills.
- Each predictor is a proposed order parameter for the grokking phase transition.

---

## Related Notes
- [[The Nine Predictors]] · [[Grokking Predictors]]
- [[Thesis Proposal Summary]] · [[Methodological Considerations]]
- [[Common Evaluation Metrics]] · [[Anti-Grokking]]
- [[12 - Modern Developments]]
