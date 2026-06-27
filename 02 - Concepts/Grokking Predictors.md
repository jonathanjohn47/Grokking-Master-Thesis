---
tags: [concept, predictors, thesis-core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[11 - Predicting Grokking]] · Catalogue: [[The Nine Predictors]]

# Grokking Predictors

## What Are They?

**Grokking predictors** are internal measurements of a neural network that change during the grokking plateau — before the test accuracy changes.

They are early-warning signals: measurements you can take inside the network that tell you "grokking is coming" or "grokking is not coming," even while the external accuracy scores look completely flat.

---

## Why Do They Exist?

During the grokking plateau, both the training score and the test score are flat and unchanged. The network looks stuck. You cannot tell from the outside whether:
- Grokking is 5,000 training steps away (you should keep training), or
- The network will never grok (you should stop and save compute)

This is a real practical problem. Without any guidance, researchers either stop too early (missing grokking) or run forever (wasting resources).

Grokking predictors solve this problem by looking **inside** the network. Even though the external scores are flat, things are changing internally. The right internal measurements can detect those changes and give advance warning.

---

## The Analogy

Think of monitoring a patient in hospital.

The external symptom (whether the patient is conscious or not) gives you very limited information. They are either awake or not.

But internal measurements — heart rate, blood pressure, oxygen levels, brain activity — can tell you far more. They change continuously and give you early warning of what is coming before the external symptom changes.

Grokking predictors are the internal measurements for a neural network. The external symptom (test accuracy) is binary-looking — near 0% or near 100%. The internal measurements change continuously during the plateau.

---

## The Nine Predictors

At least nine different grokking predictors have been proposed. Here is a plain-language description of each:

**Predictor 1 — Commutator Defect:**
Measures a specific property of how the network's gradients are organised. When the generalising circuit is forming, the gradient organisation changes in a specific, detectable way.

**Predictor 2 — HTSR Alpha:**
Measures the statistical distribution of values in the weight matrices. As the network transitions from memorisation to generalisation, the weight matrices develop a specific "heavy-tailed" pattern (a few very large values among many small ones). Alpha (α) is a number that describes how heavy-tailed the pattern is. Smaller alpha = heavier tail = closer to generalisation.

**Predictor 3 — Correlation Traps:**
A specific pathological pattern in weight matrices that signals **anti-grokking** (collapse of generalisation). Detected by comparing the weight matrix to a randomly shuffled version of itself.

**Predictor 4 — Weight-Space PCA:**
PCA (Principal Component Analysis) is a technique for finding the main directions of variation in a dataset. Applied to weight matrices, it measures how concentrated the variation is in a few key directions. As the generalising circuit forms, the variation becomes more concentrated (lower-dimensional), which is detectable.

**Predictor 5 — L2 Weight Norm:**
The total size of all the weights (sum of their squares). The memorised solution has large weights; the generalised solution has smaller weights. As weight decay erodes the memorised solution, the total weight size decreases. This is the simplest and most intuitive predictor.

**Predictor 6 — Spectral Signature:**
Specific patterns in the weight matrices that can be detected early in training and used to forecast whether and when grokking will occur. Aims to provide the earliest possible warning.

**Predictor 7 — AGE (Absolute Gradient Entropy):**
Measures the randomness (entropy) of the gradient signals. During memorisation, gradients are chaotic and high-entropy. As the generalised circuit forms, gradients become more organised and lower-entropy.

**Predictor 8 — Higher-Order Mutual Information:**
Measures how much information different parts of the network share about the task. At grokking, the information structure reorganises — from "synergistic" (where you need all parts together to have the information) to "redundant" (where many parts independently share the same information).

**Predictor 9 — Dropout Robustness:**
Applies dropout (randomly disabling some connections) and measures how much the network's performance drops. A network that has learned the generalising algorithm is robust — even with some connections disabled, it still knows the rule. A memorised network is fragile — removing any connections disrupts the stored answers. Robustness increases as grokking approaches.

---

## The Four Qualities of a Good Predictor

A useful grokking predictor must have four qualities:

**1. Accuracy:** When it says "grokking is coming," grokking should actually be coming. Low false alarm rate.

**2. Earliness:** It should signal well before grokking happens — giving enough lead time to make a decision. Signalling 10 steps before grokking is useless. Signalling 5,000 steps early is very useful.

**3. Transferability:** It should work on tasks other than the one it was tested on. A predictor that only works on clock math but fails on image classification is not very useful.

**4. Cheapness:** Computing the predictor should not require significant extra work. If checking the predictor takes longer than the training step itself, it is impractical.

These four qualities often trade off against each other: the most accurate predictor might not be the earliest, and the cheapest might not transfer well.

---

## Three Families of Predictors

The nine predictors can be grouped by what they measure:

**Spectral predictors** (HTSR Alpha, Spectral Signature, Correlation Traps):
Analyse mathematical patterns in the weight matrices. Grounded in random matrix theory and the theory of self-regularisation. Advantage: require no data — only the weights themselves.

**Geometric predictors** (Weight-Space PCA, L2 Weight Norm):
Measure the size and structure of the weight space. Grounded in neural collapse and weight decay dynamics. Simple and fast to compute.

**Information-theoretic predictors** (Higher-Order MI, AGE):
Measure information flow and gradient patterns. Grounded in information theory and the reorganisation of information during grokking.

---

## Why No Fair Comparison Has Existed

Each predictor was proposed by a different research team, tested on that team's specific tasks and networks, and compared against at most two or three other predictors.

There is no unified leaderboard. There is no standard way to compare them. Every "best predictor" claim was made in a specific context that may not generalise.

**This is the gap the thesis fills:** the first fair, unified comparison of all nine predictors under the same conditions, same tasks, same measurement standards.

---

## Each Predictor as an Order Parameter

From the physics perspective, each grokking predictor is a proposed **order parameter** for the grokking phase transition.

An order parameter is a measurement that distinguishes the two phases: the memorisation phase and the generalisation phase. In water freezing, the order parameter is the density (or crystal structure) — very different in liquid and solid states.

For grokking, each predictor is claiming: "I am the quantity that most clearly distinguishes the memorisation phase from the generalisation phase."

The thesis tests which proposed order parameter is most reliable.

---

## Important Terms

**Grokking predictor:** An internal measurement of a neural network that changes during the plateau before test accuracy does.

**Entropy:** A measure of randomness or disorder. High entropy = very random; low entropy = very ordered/predictable. The AGE predictor measures gradient entropy.

**Heavy-tailed distribution:** A statistical distribution where a few values are very large while most are small. Like wealth distribution in society — a few people have enormous wealth, most have little. HTSR Alpha measures this in weight matrices.

**Principal Component Analysis (PCA):** A technique for finding the main directions of variation in data. Reduces complex data to its most important dimensions.

**Dropout:** A training technique that randomly disables some connections during each training step or evaluation. Used in Predictor 9 to test robustness.

**Mutual information:** A measure of how much two things are related. High mutual information means knowing one thing tells you a lot about the other.

**False alarm rate:** How often a predictor signals "grokking is coming" when it is not. A predictor with too many false alarms is unreliable.

**Order parameter:** A measurement that characterises which phase a system is in. Changes sharply at a phase transition.

**AUC (Area Under the Curve):** A standard measurement of predictor quality. 1.0 = perfect, 0.5 = no better than random.

---

## Key Takeaways

- Grokking predictors are internal measurements that change during the plateau before test accuracy does.
- They solve the practical problem: during the plateau, external scores are flat and give no information about whether grokking is coming.
- Nine different predictors have been proposed by different research teams.
- They can be grouped as spectral (weight matrix patterns), geometric (weight size/structure), or information-theoretic (gradient and activation patterns).
- A good predictor must be accurate, early, transferable, and cheap.
- Each predictor is a proposed order parameter for the grokking phase transition.
- No fair comparison has ever been done — the thesis fills this gap.

---

## Related Notes
- [[The Nine Predictors]] · [[11 - Predicting Grokking]] · [[Methodological Considerations]]
- [[Anti-Grokking]] · [[Early Stopping]] · [[Phase Transition]]
- [[Heavy-Tailed Self-Regularization]] · [[Information-Theoretic Measures]] · [[Neural Collapse]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
