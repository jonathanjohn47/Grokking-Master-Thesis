---
tags: [concept, training, optimization, neural-networks]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Training Stability

## What Is It?

**Training stability** refers to whether a neural network's training process remains controlled and predictable during learning.

An **unstable** training:
- Loss spikes randomly or explodes.
- Model weights become huge or NaN (not-a-number).
- Training crashes or diverges.

A **stable** training:
- Loss decreases smoothly.
- Weights stay within reasonable ranges.
- Training completes successfully.

---

## Why Does It Matter?

Without stability:

- The model never finishes training.
- Weights become corrupted (NaN, infinity).
- Results are unpredictable (sometimes works, sometimes doesn't).
- It's hard to debug what went wrong.

With stability:

- Training runs reliably.
- Progress is predictable.
- Different seeds give similar results.
- Hyperparameters can be tuned systematically.

---

## Intuition

Imagine driving a car:

**Unstable driving:**
- Jerking the wheel left and right.
- Accelerating and braking suddenly.
- Skidding, nearly crashing.
- Exhausting.

**Stable driving:**
- Smooth, predictable movements.
- Constant speed.
- Safe and efficient.

Training stability is the "smooth driving" of neural networks.

---

## Common Causes of Instability

### 1. Exploding Gradients

During backpropagation, gradients can **multiply** through layers:

$$\frac{\partial \text{loss}}{\partial w_1} = \frac{\partial \text{loss}}{\partial \text{output}} \cdot \frac{\partial \text{output}}{\partial w_2} \cdot \frac{\partial w_2}{\partial w_1}$$

If each term is > 1:

$$\frac{\partial \text{loss}}{\partial w_1} = 2 \times 3 \times 4 = 24 \text{ (reasonable)}$$

But with many layers:

$$2^{50} = 1.1 \times 10^{15} \text{ (HUGE!)}$$

Weights get updated by enormous amounts. Training becomes chaotic.

**Solution:** [[Gradient Clipping|Gradient clipping]] — cap gradient magnitude.

### 2. Vanishing Gradients

Alternatively, gradients can **shrink** through layers:

$$0.5 \times 0.5 \times 0.5 \times \cdots = 0.5^{50} ≈ 0 \text{ (vanishing)}$$

Early layers get nearly zero gradients. They don't learn.

**Solution:** [[Residual Connections|Residual connections]] — provide gradient shortcut.

### 3. Poor Initialization

If weights start too large or too small:

**Too large:**
$$z = W x \text{ where } W \text{ is huge}$$
$$z \text{ becomes very large} \rightarrow \text{activation saturates} \rightarrow \text{gradients vanish}$$

**Too small:**
$$z = W x \text{ where } W \text{ is tiny}$$
$$z ≈ 0 \rightarrow \text{no signal} \rightarrow \text{training stalls}$$

**Solution:** Careful initialization (Xavier, He initialization).

### 4. Batch Size Mismatch

With tiny batch size (e.g., 1 sample):
- Gradient estimates are noisy.
- Updates are erratic.
- Training is chaotic.

With huge batch size:
- Updates become smoother but less frequent.
- May converge slowly or get stuck.

**Solution:** Choose batch size that balances (typically 32–512).

### 5. Learning Rate Too High

$$w_{\text{new}} = w - \text{lr} \cdot \text{gradient}$$

If learning rate is huge:

$$w_{\text{new}} = w - 10.0 \cdot \text{gradient}$$

Weights jump far from the optimum. Training oscillates wildly.

**Solution:** Use adaptive learning rates (Adam, AdamW) or learning rate scheduling.

---

## Techniques for Stable Training

### 1. Layer Normalization

[[Layer Normalization|Layer Normalization]] rescales activations to have consistent range:

- Prevents values from exploding.
- Keeps gradients well-behaved.
- Essential in transformers.

### 2. Residual Connections

[[Residual Connections|Residual connections]] provide direct gradient paths:

$$\frac{\partial}{\partial x} (x + f(x)) = 1 + \frac{\partial f}{\partial x}$$

Even if $f$'s gradient is small, the total gradient includes the 1, keeping it strong.

### 3. Gradient Clipping

Cap gradient magnitude during backpropagation:

$$\text{gradient} = \text{gradient} \cdot \min(1, \text{threshold} / \|\text{gradient}\|)$$

If gradient is too large, scale it down. Prevents explosions.

### 4. Adaptive Optimizers

Algorithms like **[[AdamW]]** adjust learning rates per parameter:

- Parameters with small gradients get higher learning rates.
- Parameters with large gradients get lower learning rates.
- Balances progress across all parameters.

### 5. Careful Initialization

Initialize weights from a distribution with appropriate scale:

**Xavier initialization:**
$$W \sim \text{Uniform}\left(-\sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}}, \sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}}\right)$$

**He initialization:**
$$W \sim \text{Normal}\left(0, \sqrt{\frac{2}{n_{\text{in}}}}\right)$$

Empirically chosen to keep activations stable through early training.

### 6. Batch Normalization / Layer Normalization

See: **[[Layer Normalization]]**

Rescales internal activations to stay in a reasonable range across the entire batch or within each sample.

---

## Stability in Grokking

In grokking experiments, training stability is crucial:

1. **Phase 1 (Memorization):** Model memorizes training data. Gradients are large but well-behaved (loss decreases monotonically).

2. **Transition (Jamming):** Loss plateaus. Gradients become small. Model is internally reorganizing.

3. **Phase 2 (Generalization):** Model discovers the algorithm. Loss suddenly drops. Gradients recover and become strong.

Without stable training, the model might:
- Crash during Phase 1.
- Get stuck and never generalize.
- Become chaotic and produce useless solutions.

**Stability enables grokking to occur.**

---

## Monitoring for Instability

**Red flags during training:**

- Loss spikes randomly.
- Loss becomes NaN or Inf.
- Weights become NaN or Inf.
- Loss oscillates wildly (doesn't decrease smoothly).
- Learning plateaus and never recovers.

**Green flags:**

- Loss decreases monotonically (or mostly).
- Weights stay within reasonable ranges (e.g., [-1, 1] per parameter).
- No NaN or Inf.
- Smooth progress toward goal.

---

## Analogy — Flying a Plane

**Unstable training** is like a plane that:
- Lurches left and right.
- Altitude fluctuates wildly.
- Engine sputters and fails.
- Crashes.

**Stable training** is like a plane that:
- Climbs smoothly.
- Maintains altitude control.
- Engines run reliably.
- Reaches destination safely.

Pilots use controls (flaps, throttle, trim) to maintain stability. Engineers use layer norm, residual connections, and optimizers for neural network stability.

---

## Important Terms

**Gradient explosion** — Gradients grow exponentially through layers, causing huge weight updates.

**Gradient vanishing** — Gradients shrink exponentially, leaving early layers unable to learn.

**Numerical instability** — Computations involving very large or very small numbers producing NaN or Inf.

**Loss spike** — Sudden temporary increase in loss during training.

**Divergence** — Training process fails to converge; loss keeps growing.

**Convergence** — Training process successfully reduces loss and stabilizes.

---

## Common Mistakes

**Mistake 1:** "Any learning rate works fine."

**Reality:** Learning rate is critical. Too high causes instability; too low stalls training.

**Mistake 2:** "Larger batch size always makes training more stable."

**Reality:** Very large batches can hurt convergence. Moderate batch sizes (32-512) often work best.

**Mistake 3:** "Layer normalization is optional."

**Reality:** In transformers, layer norm is essential for stability. Without it, training fails.

---

## Key Takeaways

- **Training stability** ensures loss decreases smoothly without crashes.
- Caused by: exploding/vanishing gradients, poor initialization, high learning rate.
- **Solutions:** layer norm, residual connections, gradient clipping, adaptive optimizers.
- **Transformers** use all these techniques to maintain stable training.
- In grokking, stability is prerequisite for the phase transition to occur.

---

## Related Notes

- [[Layer Normalization]] — critical for stable training.
- [[Residual Connections]] — prevent vanishing gradients.
- [[AdamW]] — adaptive optimizer used in grokking; has mechanisms for stability.
- [[Gradient Flow]] — how gradients propagate; relates to stability.
- [[Training Objectives]] — different objectives require different stability measures.
- [[Transformer]] — uses multiple stability techniques together.
