---
tags: [concept, transformer, normalization, training]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Layer Normalization

## What Is It?

**Layer Normalization** is a technique that **rescales** the values in a vector to have a consistent range.

It takes a vector like `[0.5, 100.2, -3.1, 0.002]` and transforms it so all values are roughly centered around 0 with similar magnitudes.

In transformers, layer normalization is applied **before** each component (attention or MLP) to stabilize training.

---

## Why Does It Exist?

### Problem: Unstable Training

During training, the values inside the model can become:

- **Very large** — producing huge gradients that cause the model to "jump" far away and crash.
- **Very small** — producing tiny gradients where training stalls and nothing is learned.
- **Wildly inconsistent** — some dimensions are huge, others are tiny, making optimization difficult.

### Solution: Normalize

Layer normalization **rescales** all values to a consistent range, preventing these extremes.

Think of it as:

- Measuring all values in the vector.
- Computing their average (mean) and spread (standard deviation).
- Rescaling so they cluster around 0 with standard deviation around 1.

This keeps training stable without the learning rate bouncing around.

---

## Intuition

Imagine a teacher grading papers on a scale of 0–100:

```
Student A: 95 points
Student B: 3 points
Student C: 88 points
```

The average grade is 62, and the spread is large.

**Layer normalization** rescales to a standardized grading scale:

```
Subtract the average (62):
Student A: 95 - 62 = 33
Student B: 3 - 62 = -59
Student C: 88 - 62 = 26

Divide by the spread (standard deviation ≈ 40):
Student A: 33 / 40 ≈ 0.82 standard deviations above average
Student B: -59 / 40 ≈ -1.47 standard deviations below average
Student C: 26 / 40 ≈ 0.65 standard deviations above average
```

Now all grades are on a **consistent scale**. You can compare them meaningfully.

---

## How Does It Work?

### Step-by-Step

Given a vector $x = [x_1, x_2, \ldots, x_d]$ of dimension $d$ (e.g., 128):

**Step 1: Compute the mean**

$$\mu = \frac{1}{d} \sum_{i=1}^{d} x_i$$

Sum all values and divide by the number of values.

**Step 2: Compute the standard deviation (spread)**

$$\sigma = \sqrt{\frac{1}{d} \sum_{i=1}^{d} (x_i - \mu)^2 + \epsilon}$$

The $\epsilon$ (a tiny number like 0.00001) prevents division by zero.

**Step 3: Normalize**

$$\hat{x}_i = \frac{x_i - \mu}{\sigma}$$

For each value, subtract the mean and divide by the standard deviation.

**Step 4: Scale and shift (optional)**

$$y_i = \gamma \hat{x}_i + \beta$$

Multiply by a learned parameter $\gamma$ (scale) and add a learned parameter $\beta$ (shift).

These allow the model to **undo** the normalization if useful, or keep it if it helps.

---

## Example

Let's normalize the vector `[1.0, 4.0, 7.0]`:

**Step 1: Compute mean**

$$\mu = \frac{1 + 4 + 7}{3} = \frac{12}{3} = 4$$

**Step 2: Compute standard deviation**

$$\sigma = \sqrt{\frac{(1-4)^2 + (4-4)^2 + (7-4)^2}{3} + \epsilon}$$

$$= \sqrt{\frac{9 + 0 + 9}{3}} = \sqrt{6} \approx 2.45$$

**Step 3: Normalize**

$$\hat{x}_1 = \frac{1 - 4}{2.45} = \frac{-3}{2.45} \approx -1.22$$

$$\hat{x}_2 = \frac{4 - 4}{2.45} = \frac{0}{2.45} = 0$$

$$\hat{x}_3 = \frac{7 - 4}{2.45} = \frac{3}{2.45} \approx 1.22$$

**Result:** `[-1.22, 0, 1.22]`

The normalized vector:
- Has mean = 0
- Has standard deviation = 1
- Maintains the relative relationships (first value is smallest, middle is average, third is largest)

---

## Pre-Norm vs. Post-Norm

Transformers apply layer normalization at slightly different points:

### Pre-Norm (Modern)

Layer normalization is applied **before** each component:

```
Input x
  │
  ▼
[LayerNorm]
  │
  ▼
[Attention]
  │
  x = x + output
  ▼
Output
```

**Why pre-norm is better:**
- More stable training.
- Requires smaller learning rates.
- Used in GPT-2 onwards, LLaMA, Claude.

### Post-Norm (Older)

Layer normalization is applied **after** each component:

```
Input x
  │
  ▼
[Attention]
  │
  x = x + output
  │
  ▼
[LayerNorm]
  │
  ▼
Output
```

**Why post-norm was used:**
- Simpler mathematically.
- But less stable — requires larger learning rates and careful tuning.
- Original transformer used post-norm (Vaswani et al., 2017).

> [!NOTE]
> Modern transformers (GPT-2, GPT-3, LLaMA, Claude) use **pre-norm**, making training easier.

---

## Why Layer Normalization Is Critical

### Without layer normalization

```
Initial embedding:     [0.5, 0.3, 0.8]
After attention:       [100.2, -50.1, 200.5]   (unstable!)
After MLP:             [1000.5, -200.1, 5000.8]   (exploding!)
```

Values blow up. Gradients become huge. Training crashes or diverges.

### With layer normalization

```
Initial embedding:     [0.5, 0.3, 0.8]
After LayerNorm:       [0.3, -0.2, 0.7]
After attention:       [0.05, 0.10, -0.08]     (stable!)
After LayerNorm:       [0.2, 0.5, -0.3]
After MLP:             [0.01, 0.02, -0.01]     (stable!)
```

Values stay manageable. Training is stable.

---

## Analogy — Volume Control

Imagine a band with many instruments:

- The **drums** are very loud.
- The **strings** are very quiet.
- The **vocals** are in between.

Without a **mixer** (volume control), the drums drown out everything else.

**Layer normalization** is the mixer:

- Measure the loudness of each instrument.
- Adjust each to a consistent volume (e.g., all at medium level).
- Now all instruments can be heard clearly.

The **mixer doesn't erase** the instruments — it just rescales them so they work together.

---

## Important Terms

**Normalization** — Rescaling values to a consistent range (typically mean=0, standard deviation=1).

**Mean** ($\mu$) — The average value: $\frac{1}{d} \sum x_i$.

**Standard deviation** ($\sigma$) — The spread of values around the mean.

**Epsilon ($\epsilon$)** — A tiny number (like 0.00001) added to prevent division by zero.

**Pre-norm** — Applying layer normalization **before** a component (used in modern transformers).

**Post-norm** — Applying layer normalization **after** a component (used in older transformers).

**Affine transformation** — Multiplying by $\gamma$ and adding $\beta$; allows the model to learn whether to apply normalization.

---

## Common Mistakes

**Mistake 1:** "Layer normalization removes important differences between values."

**Reality:** It rescales them, not removes them. A value that was 100× larger than another stays 100× larger after normalization (in units of standard deviation).

**Mistake 2:** "We need layer normalization only for very large models."

**Reality:** Even small models (like 1-layer grokking transformers with 128 hidden dim) benefit from layer normalization. It stabilizes all training.

**Mistake 3:** "Layer normalization is the same as batch normalization."

**Reality:** They're different. Batch norm normalizes across different training examples; layer norm normalizes within a single vector. Layer norm is preferred in transformers.

---

## Key Takeaways

- **Layer normalization** rescales vector values to have mean ≈ 0 and standard deviation ≈ 1.
- It stabilizes training by preventing values from exploding or becoming too small.
- **Modern transformers use pre-norm** — apply layer norm before attention/MLP.
- Layer norm is applied **to each vector independently** (unlike batch norm, which uses statistics across the batch).
- Without layer norm, transformer training would be unstable and slow.
- The parameters $\gamma$ and $\beta$ allow the model to learn whether normalization helps.

---

## Related Notes

- [[Transformer]] — the architecture using layer normalization.
- [[Multi-Head Self-Attention]] — a component that benefits from layer normalization.
- [[Feed-Forward Network (MLP)]] — a component that benefits from layer normalization.
- [[Residual Stream]] — the vector being normalized at each step.
- [[Training Stability]] — the broader topic of keeping neural networks trainable.
