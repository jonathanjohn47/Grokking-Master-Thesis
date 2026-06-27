---
tags: [concept, deep-learning, empirical, large-language-models]
---
↑ Parent: [[Language Models]] · Learning path: [[04 - Core Experimental Setup]]

# Scaling Laws

## What Is It?

**Scaling laws** are empirical relationships describing how model performance improves as you increase:

- **Model size** (number of parameters)
- **Dataset size** (amount of training data)
- **Compute** (training time and resources)

They quantify: *"How much better does my model get if I make it bigger?"*

---

## Why Does It Matter?

Before scaling laws were discovered, people thought:

> "Bigger models might not be better. There's probably some optimal size."

But empirical research (especially by OpenAI and others) found:

$$\text{Performance} \propto \text{Model Size}^{\alpha}$$

**Performance keeps improving with scale.** There's no plateau (at least not yet observed).

This changed AI development strategy: **invest in scale.**

---

## Intuition

Imagine learning to play chess:

**With 1 game:**
- You're terrible. (Small dataset)

**With 100 games:**
- You're mediocre. (Small dataset)

**With 10,000 games:**
- You're decent. (Medium dataset)

**With 1,000,000 games:**
- You're very good. (Large dataset)

More experience → better performance. There's a **relationship** between experience and skill.

Scaling laws quantify this relationship mathematically.

---

## The Chinchilla Scaling Laws

In 2022, DeepMind's Hoffman et al. published the most influential scaling laws:

$$L(N, D) = E + \frac{A}{N^\alpha} + \frac{B}{D^\beta}$$

Where:

- $L$ = loss (lower is better)
- $N$ = model size (parameters)
- $D$ = dataset size (tokens)
- $E, A, B, \alpha, \beta$ = empirically determined constants

**Key findings:**

$$\alpha \approx 0.07, \quad \beta \approx 0.16$$

- **Reducing model size by 10%** → loss increases by ~7% (exponent 0.07).
- **Reducing data by 10%** → loss increases by ~16% (exponent 0.16).

**Critical insight:** Data matters more than model size. Doubling data is better than doubling parameters.

---

## Common Scaling Relationships

### Loss vs. Model Size

$$L(N) = A N^{-\alpha}$$

where $\alpha \approx 0.07$ (empirically observed).

**Interpretation:**

```
Model size | Loss (lower better)
-----------|-------------------
10M        | 4.5
100M       | 3.8
1B         | 3.2
10B        | 2.7
100B       | 2.2
```

Each 10× increase in model size → ~30% improvement in loss.

### Loss vs. Data Size

$$L(D) = B D^{-\beta}$$

where $\beta \approx 0.16$ (empirically observed).

**Interpretation:**

```
Data size  | Loss
-----------|---
10M tokens | 4.2
100M       | 3.7
1B         | 3.2
10B        | 2.8
100B       | 2.4
```

Each 10× increase in data → ~40% improvement in loss.

### Loss vs. Compute

$$L(C) = C_c C^{-\lambda}$$

where $\lambda \approx 0.05$ (compute scaling exponent).

If you can do 10× more compute, you get similar improvements to scaling model or data.

---

## Implications

### 1. Optimal Allocation

**Chinchilla's finding:** For a given compute budget, allocate:

- **50%** to model parameters
- **50%** to dataset size

(Not the common practice of having huge models with insufficient data!)

### 2. Predicting Performance

If you observe current performance and scaling exponents, you can **predict future performance**:

$$\text{Loss}_{\text{future}} = A (N_{\text{future}})^{-0.07}$$

Example: If a 10B model has loss 2.7, what's a 100B model's loss?

$$\text{Loss}_{100B} = 2.7 \times \left(\frac{10}{100}\right)^{0.07} = 2.7 \times 0.87 = 2.35$$

### 3. Compute-Optimal Training

For a fixed compute budget, you can **trade off model size and training time**:

- Option A: Large model, few training steps.
- Option B: Small model, many training steps.

Both can achieve similar performance if compute budgets are equal.

---

## Scaling Laws in Grokking

**Grokking is a scaling phenomenon at small scale.**

In grokking experiments:

- Small models (100K parameters).
- Small datasets (1K-10K examples).
- Different behavior than large language models.

**Questions:**

1. Do scaling laws apply to grokking models?
2. Does a 1M parameter model grokk faster/better than 100K?
3. Do scaling laws predict when generalization occurs?

These are **open research questions** in grokking literature.

---

## Limitations of Scaling Laws

### 1. Empirical, Not Fundamental

Scaling laws are **observed patterns**, not derived from theory. They may not hold for:

- Completely different architectures.
- Different domains (grokking vs. language).
- Extreme scales not yet observed.

### 2. Assumes Sufficient Data

Scaling laws assume you have enough data to train effectively. If data is small relative to model, you get overfitting instead of scaling benefits.

### 3. Ignores Optimization Details

Scaling laws don't capture:

- Learning rate schedules.
- Weight decay effects.
- Other hyperparameter interactions.

### 4. No Theoretical Explanation

We don't know **why** these particular exponents (0.07, 0.16). It's empirical.

---

## Example Calculation

**Scenario:** You have a 7B model trained on 1T tokens. Loss = 2.5.

**Question:** What loss would a 70B model achieve with 3T tokens?

**Solution:**

Using Chinchilla's formula:

$$L(N, D) = E + \frac{A}{N^\alpha} + \frac{B}{D^\beta}$$

From the 7B model, we can estimate $E$ (irreducible loss):

Current model loss: 2.5
Contributions: 
- Model size: $\frac{A}{(7B)^{0.07}}$
- Data size: $\frac{B}{(1T)^{0.16}}$

For the 70B model with 3T data:
- Model contribution: $\frac{A}{(70B)^{0.07}}$ (smaller, better)
- Data contribution: $\frac{B}{(3T)^{0.16}}$ (smaller, better)

Predicted loss $\approx 1.8$ (rough estimate).

---

## Analogy — Improving a Recipe

Imagine optimizing a recipe for chocolate cake:

**Scaling the ingredients:**
- Double all ingredients → cake is twice as good.
- Triple all ingredients → cake is three times as good.

But there's a **diminishing return**:
- From bad to OK: doubling ingredients helps a lot.
- From OK to excellent: doubling ingredients helps some.
- From excellent to perfect: doubling ingredients barely helps.

**Scaling laws capture this diminishing return mathematically.**

---

## Important Terms

**Scaling law** — Empirical relationship between model size/data and performance.

**Loss** — Measure of prediction error. Lower is better.

**Model size** — Number of parameters in the neural network.

**Dataset size** — Total amount of training data (often counted in tokens).

**Compute** — Total computational cost of training (measured in FLOPs or other units).

**Exponent** — The power in the scaling relationship (e.g., $\alpha = 0.07$).

**Chinchilla allocation** — Optimal split of compute between model and data: 50-50.

**Compute-optimal** — Achieving best performance for a given compute budget.

---

## Common Mistakes

**Mistake 1:** "Bigger is always better; scale infinitely."

**Reality:** Scaling laws show improvements, but exponent is small (0.07). 10× larger model → only ~30% better performance. Diminishing returns.

**Mistake 2:** "Scaling laws apply to all domains equally."

**Reality:** Observed in language modeling. May differ for grokking, vision, other tasks.

**Mistake 3:** "You can achieve scaling laws with any amount of data."

**Reality:** Need sufficient data. If data is small, you overfit instead of benefiting from scale.

**Mistake 4:** "Scaling laws predict exact performance."

**Reality:** They predict approximate trends. Actual performance varies with hyperparameters, optimization, data quality.

---

## Key Takeaways

- **Scaling laws** describe how performance improves with model and data size.
- Power laws govern: loss $\propto (\text{size})^{-0.07}$ and $(\text{data})^{-0.16}$.
- **Data scales better** than model size (steeper exponent).
- **Chinchilla optimal:** Allocate compute 50% to model, 50% to data.
- Scaling is empirical, not derived from theory.
- Whether scaling laws apply to grokking is an open question.

---

## Related Notes

- [[Language Models]] — scaling laws discovered in language model training.
- [[Transformer]] — architecture studied under scaling laws.
- [[Generalization]] — scaling improves generalization on test data.
- [[Overfitting]] — risk when data is insufficient relative to model size.
- [[Mechanistic Interpretability]] — understanding what scales and why.
