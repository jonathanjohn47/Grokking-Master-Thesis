---
tags: [concept, transformer, architecture, mechanistic-interpretability]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Residual Stream

## What Is It?

The **residual stream** is a continuous "river of information" that flows through the entire transformer model.

Think of it as a **shared workspace** that every component in the model can read from and write to.

Every attention head and MLP block:
1. Reads information from the stream
2. Computes something useful
3. Adds a small update back to the stream (without replacing anything)

The final prediction is literally the **sum of all these tiny contributions**.

> [!NOTE]
> The residual stream is Neel Nanda's central insight from [[Mechanistic Interpretability]]. It's why transformers are mathematically tractable — you can trace exactly where each piece of information came from.

---

## Why Does It Exist?

Without the residual stream, each layer would completely replace the previous layer's output:

```
x → [Layer 1] → completely new x → [Layer 2] → completely new x
```

This causes two problems:

1. **Information loss** — useful information from earlier gets thrown away.
2. **Hard to trace** — if the output is wrong, you can't tell which layer made the mistake.

The residual stream solves both by **preserving all contributions**:

```
x → [Layer 1] → x + layer1_contribution → [Layer 2] → x + layer1 + layer2 → output
```

Every piece of the computation stays visible. This is what makes understanding transformers possible.

---

## Intuition

Imagine a group of doctors examining a patient.

1. **Doctor 1** examines the patient and writes their observations on a clipboard.
2. **Doctor 2** reads the clipboard, adds their observations.
3. **Doctor 3** reads the whole clipboard, adds their observations.
4. At the end, you read the **entire clipboard** — every doctor's contribution is there.

The clipboard is the residual stream.

If instead each doctor erased everything and wrote only their own findings, the patient would lose information. By adding to the previous analysis instead of replacing it, the full picture emerges.

---

## How Does It Work?

### The Mathematical Flow

Here's how information flows through a transformer block:

$$x_0 = \text{embedding}(\text{token}) + \text{position\_encoding}$$

$$x_1 = x_0 + \text{Attn}(x_0)$$

$$x_2 = x_1 + \text{MLP}(x_1)$$

$$x_3 = x_2 + \text{Attn}(x_2)$$

$$\text{logits} = x_3 \cdot W_U$$

Notice the pattern: **every new value = old value + component's output**.

### Step by Step

**Step 1: Initial representation**

The token is embedded (converted to a vector) and position information is added.

```
x₀ = [0.1, -0.3, 0.8, ...]  (this is the residual stream at layer 0)
```

**Step 2: Attention reads and adds**

The attention head reads x₀, computes which other tokens are relevant, and produces an output called `attn_out`.

```
attn_out = [0.05, 0.02, -0.1, ...]
x₁ = x₀ + attn_out = [0.15, -0.28, 0.7, ...]
```

The stream has been updated but x₀ is still present (it's been added to, not replaced).

**Step 3: MLP reads and adds**

The MLP reads x₁ and produces `mlp_out`.

```
mlp_out = [0.01, 0.05, 0.03, ...]
x₂ = x₁ + mlp_out = [0.16, -0.23, 0.73, ...]
```

Again, the old information is preserved.

**Step 4: Repeat for each layer**

This pattern repeats through every transformer block. Each layer reads from the stream and adds its contribution.

**Step 5: Final prediction**

The final representation passes through the **unembedding matrix** to produce logits:

```
logits = x_final · W_U
```

The model's prediction comes from the accumulated contributions of every attention head and MLP across all layers.

---

## Why This Matters for Grokking

In grokking research, the residual stream is **the key to understanding** what the model learns:

1. **Decomposability** — You can trace each contribution separately. If a grokking solution uses 4 attention heads and 2 MLPs, you can analyse each one.

2. **Linearity** — Because everything adds (never replaces), the final output is a **linear combination** of all component contributions. This makes it mathematically elegant.

3. **Interpretability** — Nanda et al.'s breakthrough: they logged the residual stream at every step of training, watching the Fourier features emerge step by step.

> [!TIP]
> Without the residual stream architecture, understanding grokking mechanistically would be almost impossible. The additive structure is what makes reverse-engineering the solution feasible.

---

## Example — Predicting a Number

Imagine the model is learning modular addition: `(37 ◦ 61) mod 97 = ?`

**Input tokens:** `[37, +, 61, =]`

**Position 4 (the `=` token):**

```
x₀ = [-0.2, 0.5, ...]  (just the embedding for "=")

After Attn_head_1:
x₁ = x₀ + [+0.3, -0.1, ...]  = [0.1, 0.4, ...]
     (head 1 attended to "37" and "61", extracted their values)

After MLP_1:
x₂ = x₁ + [+0.05, +0.02, ...]  = [0.15, 0.42, ...]
     (MLP 1 retrieved that 37+61=98)

After Attn_head_2:
x₃ = x₂ + [+0.01, -0.05, ...]  = [0.16, 0.37, ...]
     (head 2 computed mod 97)

After MLP_2:
x₄ = x₃ + [-0.02, +0.08, ...]  = [0.14, 0.45, ...]

Final logits = x₄ · W_U  = [..., 0.98, ...]
                           ↑ highest logit = the number "1" (the answer)
```

Each step **preserves** previous information while adding new information. The final answer is the sum of all contributions.

---

## Analogy — Collaborative Writing

Imagine writing a book collaboratively:

- **Author 1** writes the first draft.
- **Author 2** reads it and adds notes in the margins.
- **Author 3** reads the annotated draft and adds more notes.
- The final book is the original draft plus all the notes combined.

You never erase the original text. You only add to it.

The residual stream works the same way: the original embedding is never erased, only added to.

---

## Important Terms

**Attention head** — A component that reads the residual stream and outputs a small update.

**MLP (Feed-Forward Network)** — A component that reads the residual stream and outputs a small update.

**Layer** — One complete block containing one attention head (or multi-head attention) and one MLP. Both read from and write to the residual stream.

**Unembedding matrix** ($W_U$) — The final linear layer that converts the residual stream into logits (prediction scores).

**Logits** — The raw prediction scores. The highest logit is the predicted token.

---

## Common Mistakes

**Mistake 1:** "The residual stream just passes information unchanged."

**Reality:** The residual stream *accumulates* information. Each component adds its contribution. The stream changes at every step.

**Mistake 2:** "Residual connections are just a technical trick."

**Reality:** They are fundamental. They make transformers work, prevent vanishing gradients, and enable mechanistic interpretability. Without them, transformers would fail.

**Mistake 3:** "Later layers overwrite earlier layers."

**Reality:** No. Every layer's contribution remains in the final output. The output is the sum of all contributions.

---

## Key Takeaways

- The residual stream is a **shared workspace** flowing through the transformer.
- Every component reads from it and **adds** a small contribution (never replaces).
- The final output is literally the **sum of all component contributions**.
- This additive structure is what makes transformers **interpretable** — you can decompose the output contribution by contribution.
- Without the residual stream, understanding grokking would be almost impossible.
- In the model's hidden dimension (e.g., 128), the residual stream is a **128-dimensional vector** updated at every step.

---

## Related Notes

- [[Transformer]] — the architecture containing the residual stream.
- [[Mechanistic Interpretability]] — the framework for understanding what the residual stream encodes.
- [[Circuit Formation]] — how attention heads and MLPs form interpretable circuits within the residual stream.
- [[Residual Connections]] — the technical mechanism enabling the residual stream.
- [[Multi-Head Self-Attention]] — a component that reads from and writes to the stream.
- [[Feed-Forward Network (MLP)]] — a component that reads from and writes to the stream.
