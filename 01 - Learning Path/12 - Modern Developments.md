---
tags: [learning-path, modern, frontier]
---
← Previous: [[11 - Predicting Grokking]]  ↑ Parent: [[00 - Start Here]]  → Next: [[13 - Open Problems and Research Gaps]]

# 12 - Modern Developments

## What Is This Note About?

Since grokking was named in 2022, research has moved quickly. In just a few years, the field has made major advances in four directions:

1. Grokking has been found **outside of neural networks** — in entirely different types of systems.
2. New early-warning signals (predictors) have been discovered and refined.
3. The training algorithm itself turns out to affect how fast grokking happens.
4. The same mathematical tools used to understand grokking have been applied to other AI systems.

This note surveys these modern developments and shows where the thesis fits on the current research frontier.

---

## Development 1: Grokking Beyond Neural Networks

One of the most important recent discoveries is that grokking happens in systems that are **not neural networks at all**.

Researchers (Pomarico et al., 2025) studied grokking in a type of mathematical model from physics called a **tensor network**. (A tensor network is a different way of representing and computing with information, used in quantum physics — not the same as a neural network.)

They found:
- The same three phases of grokking: memorisation → plateau → sudden generalisation.
- At the grokking moment, a specific internal quantity called **entanglement entropy** changed sharply.
- This entanglement entropy acted like an order parameter — near zero in the memorisation phase, then jumping at the generalisation transition.

They tested this on real image classification tasks (Fashion-MNIST and hyperspectral imagery) — not just toy problems.

**Why this matters:**
- Grokking is not a quirk of transformer architecture or neural networks in general.
- It is a property of how **learning systems** in general behave.
- This makes grokking more fundamental and more broadly relevant.

---

## Development 2: Spectral Methods Go Mainstream

"Spectral" methods are techniques that analyse the mathematical properties of weight matrices — specifically, the distribution of their "singular values" (a measure of how much variation is in each direction of the matrix).

Researchers (Martin and colleagues, WeightWatcher project) found that these spectral patterns carry rich information about a network's health and generalisation ability — **without needing to run the network on any data**.

Key discoveries:
- The distribution of singular values follows a mathematical pattern called a "power law" in well-trained, generalising networks.
- This power-law pattern changes as the network transitions from memorisation to generalisation.
- The exponent of the power law (called alpha, α) can be used to predict grokking.

More recently, researchers found that specific pathological patterns in weight matrices — called "correlation traps" — predict **anti-grokking** (when the network collapses after generalising).

**Why this matters:**
- Spectral analysis is cheap — it only requires looking at weight values, not running training data through the network.
- It can potentially predict grokking and anti-grokking from weight matrices alone.
- These are among the most practical predictors for real-world use.

---

## Development 3: Early-Training Predictors

A new direction: predicting grokking from information available **very early in training** — potentially before the memorisation phase is even complete.

Researchers (Jiang et al., 2024) developed a measurement called **neural capacitance** that can predict a network's final performance from its structure early in training.

The idea: certain properties of the network's structure (specifically, the pattern of which connections are active in early training) predict how well it will eventually generalise.

**Why this matters:**
- If you can predict grokking from the first few hundred training steps, you can make training decisions much earlier.
- This could dramatically reduce the compute wasted on networks that will never grok.
- It connects grokking prediction to a broader project: model selection without long training runs.

---

## Development 4: How the Training Algorithm Affects Grokking

A surprising discovery: the choice of **training algorithm** (the specific method used to update the weights at each step) has a major effect on how fast grokking happens.

Standard grokking experiments use an algorithm called **AdamW**. But researchers (Tveit et al., 2025) found that a newer algorithm called **Muon** causes grokking to happen dramatically faster.

**What is AdamW?** AdamW is an enhanced version of a basic algorithm called gradient descent. It adapts the step size separately for each weight, using information about recent gradient history. The "W" in AdamW refers to the way it handles weight decay — separately from the gradient update.

**What is Muon?** Muon is a newer algorithm that uses a different mathematical approach to computing the update at each step. The details are technical, but the key result is: networks trained with Muon seem to transition from memorisation to generalisation much faster.

**Why this matters for the thesis:**
- If two predictors work well with AdamW but one fails with Muon, that is an important finding.
- The choice of training algorithm becomes an experimental variable that must be included in any fair comparison of predictors.
- This is one of the research questions the thesis addresses.

---

## Development 5: Representation Geometry and Neuroscience

Researchers (Li et al., 2024) found connections between how neural networks represent information and how biological brains represent information.

Both artificial networks and biological brains organise their internal representations with specific geometric properties:
- How many dimensions are "active" (called intrinsic dimensionality)
- How spread out the representations are (called radius)

These geometric properties are related to how well the system generalises. Better generalisation tends to correlate with lower-dimensional, more compact representations.

**Why this matters for grokking:**
- As a network groks, its internal representations become more compact and geometric — this is related to neural collapse.
- Geometric measurements of representations could serve as grokking predictors.
- The connections to neuroscience suggest that grokking might tell us something about how biological learning works.

---

## Development 6: Grokking-Like Behaviour in Generative AI

Researchers (Biroli et al., 2024) found that **diffusion models** — the type of AI used to generate images — show phase-transition-like behaviour similar to grokking.

Diffusion models work by learning to reverse a noise-adding process. During generation, they start with pure noise and gradually remove it to produce an image.

Researchers found two sharp transitions during generation:
1. **Speciation transition:** The model shifts from generating generic content to generating content that belongs to a specific category (e.g., "this will be a dog").
2. **Collapse transition:** The model commits to a specific instance within that category (e.g., "this will be a brown dog sitting on grass").

These transitions are mathematically similar to phase transitions and can be detected using spectral tools.

**Why this matters:**
- The same mathematical tools used to study grokking apply to diffusion models.
- Grokking research may provide insights into how modern generative AI systems work.
- The spectral analysis tools developed for grokking could be used to understand and improve generative AI.

---

## Where the Thesis Fits

The thesis sits at the intersection of developments 1, 2, 3, and 4:

- **Development 1:** Testing predictors on multiple tasks (not just clock math) to check transferability.
- **Development 2:** Including spectral predictors (HTSR Alpha, Spectral Signature, Correlation Traps) in the benchmark.
- **Development 3:** Measuring how early each predictor fires.
- **Development 4:** Testing predictors under different training algorithms (AdamW vs. Muon).

The thesis provides the first **unified benchmark** — putting all nine predictors on the same experiments, with the same rules, to find out which is most reliable.

---

## Important Terms

**Tensor network:** A mathematical model from physics that represents information as a network of interconnected tensors (multi-dimensional arrays). Not a neural network, but can learn and generalise, and can show grokking.

**Entanglement entropy:** A measure from quantum physics of how correlated different parts of a tensor network are. Found to be an order parameter for grokking in tensor-network systems.

**Singular values:** Mathematical quantities derived from a matrix that describe how much variation exists in each direction. Analysing singular values is called "spectral analysis."

**Power law:** A mathematical relationship where one quantity follows a specific pattern determined by an exponent (alpha, α). Well-trained networks tend to show power-law distributions in their weight singular values.

**Correlation traps:** Pathological patterns in weight matrices that predict anti-grokking (network collapse after generalisation).

**Neural capacitance:** A measurement of network structure that predicts final generalisation performance from early training.

**AdamW:** A widely-used training algorithm that adapts step sizes separately for each weight and applies weight decay separately from the gradient update.

**Muon:** A newer training algorithm that appears to cause grokking to happen much faster than AdamW.

**Diffusion model:** A type of AI that generates images by learning to reverse a noise-adding process. Used in systems like DALL-E and Stable Diffusion.

---

## Key Takeaways

- Grokking has been found in non-neural-network systems, confirming it is a general learning phenomenon.
- Spectral analysis of weight matrices (without running any data) can predict grokking — a practical and efficient approach.
- Early-training predictors can forecast grokking from the first few hundred steps.
- The training algorithm (AdamW vs. Muon) affects grokking speed — this is a new experimental variable.
- The same mathematical tools used for grokking apply to diffusion models and other modern AI systems.
- The thesis provides the first fair comparison of all nine predictors across these modern settings.

---

## Related Notes
- [[Evolution of Grokking Research]] · [[Research Timeline]]
- [[Heavy-Tailed Self-Regularization]] · [[Information-Theoretic Measures]]
- [[13 - Open Problems and Research Gaps]]
