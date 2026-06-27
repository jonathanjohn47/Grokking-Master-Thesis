---
tags: [concept, transformer, architecture, mechanism, information-flow]
---
↑ Parent: [[Transformer]] · Related: [[Self-Attention]] · [[Feed-Forward Network (MLP)]]

# Attention to MLP Information Flow

## The Key Insight: What the MLP Actually Receives

When you read "the MLP looks into key-value," it's natural to think the MLP inspects the key-value pairs that attention computed internally.

**This is incorrect.**

The MLP does **not** access the internal query (Q), key (K), or value (V) matrices from attention.

Instead, the MLP receives **the output of the attention mechanism** — which has already mixed and weighted the values. The MLP processes this result.

---

## The Complete Information Flow Through One Transformer Block

Let me walk through exactly what happens, step by step.

### Step 1: Input Arrives at the Block

The **residual stream** vector arrives at transformer block $\ell$.

Let's call it `x` (dimension 128 in grokking experiments).

```
residual stream: x = [0.5, -0.2, 0.3, ...]  (128 values)
    │
    ▼
```

### Step 2: Attention Stage — Internal Q, K, V

Attention creates three copies of the input:

$$Q = x \cdot W_Q$$
$$K = x \cdot W_K$$
$$V = x \cdot W_V$$

Where $W_Q$, $W_K$, $W_V$ are learned matrices.

> [!NOTE]
> These Q, K, V projections are **internal to the attention mechanism**. They are temporary working vectors, not part of the final output.

**What happens next (still inside attention):**

1. Compute attention scores: $\text{scores} = Q \cdot K^T$ (this is an $n \times n$ matrix for $n$ positions)
2. Apply softmax to convert scores to weights: `attention_weights = softmax(scores)`
3. **Weighted sum of values**: 

$$\text{attention_output} = \text{attention_weights} \cdot V$$

This is the **only thing that leaves the attention mechanism**.

```
Internal to Attention:
  Q, K, V computed
  Attention scores computed (Q·K^T)
  Attention weights computed (softmax)
  ▼
  Weighted sum: attention_output = weights · V
    │
    └─→ (Q, K, V discarded; only output leaves)
```

### Step 3: Residual Connection

The attention output is **added** to the original residual stream:

$$x_{\text{after\_attention}} = x + \text{attention_output}$$

This is still a 128-dimensional vector.

```
residual stream enriched: x_after_attention = x + attention_output
    │
    ▼
```

### Step 4: MLP Stage — What It Receives

The **MLP receives the enriched residual stream vector**:

$$\text{MLP_input} = x_{\text{after\_attention}}$$

**This is the key point: the MLP does NOT see Q, K, or V.**

The MLP sees the **output** that attention produced — which is already a mixed, weighted combination of the values.

```
MLP receives: x_after_attention = [0.52, -0.15, 0.35, ...]
    │
    ▼
MLP expands 128 → 512
    │
    ▼
MLP applies ReLU/GELU
    │
    ▼
MLP compresses 512 → 128
    │
    ├─→ mlp_output = [0.03, 0.01, -0.02, ...]
    │
```

### Step 5: Second Residual Connection

The MLP output is added back:

$$x_{\text{final}} = x_{\text{after\_attention}} + \text{mlp\_output}$$

This leaves the transformer block and enters the next block (or the unembedding layer, if it's the last block).

```
Final residual stream: x_final = x_after_attention + mlp_output
    │
    └─→ passes to next block
```

---

## The Complete Picture: One Transformer Block

```
┌─────────────────────────────────────────────────────┐
│  TRANSFORMER BLOCK ℓ                                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Input: x (residual stream, dim 128)                │
│    │                                                │
│    ▼                                                │
│  ┌────────────────────────────────────┐             │
│  │ ATTENTION STAGE                     │             │
│  │ ┌──────────────────────────────┐    │             │
│  │ │ Internal: compute Q, K, V     │    │             │
│  │ │ Internal: compute Q·K^T       │    │             │
│  │ │ Internal: softmax weights     │    │             │
│  │ │ Internal: weights · V         │    │             │
│  │ └──────────────────────────────┘    │             │
│  │ Output: attention_output (dim 128)  │             │
│  └────────────────────────────────────┘             │
│    │                                                │
│    ▼                                                │
│  x_after_att = x + attention_output                 │
│    │                                                │
│    ▼                                                │
│  ┌────────────────────────────────────┐             │
│  │ MLP STAGE                           │             │
│  │ Input: x_after_att (dim 128) ◄─────┤─ receives  │
│  │ Expand: 128 → 512                   │  what att. │
│  │ ReLU/GELU                           │  output    │
│  │ Compress: 512 → 128                 │             │
│  │ Output: mlp_output (dim 128)        │             │
│  └────────────────────────────────────┘             │
│    │                                                │
│    ▼                                                │
│  x_final = x_after_att + mlp_output                │
│    │                                                │
└────┼─────────────────────────────────────────────────┘
     │
     └─→ to next block (or unembedding)
```

---

## Why This Matters for Grokking

In the grokking circuit:

1. **Attention learns to identify and route operands**: 
   - The `=` token's query learns what to look for
   - The `a` and `b` tokens' keys advertise what they contain
   - The weighted sum of values (`V`) mixes the two operands

2. **The MLP receives this mixed result and computes the arithmetic**:
   - Input: a vector that "knows" which operands it should process
   - The MLP has learned: "when I see this activation pattern, output the result of adding them mod p"

The key insight: **attention provides context, MLP provides knowledge**.

---

## Common Misconception

**Wrong:** "The MLP looks into the key-value pairs that attention computed."

**Correct:** "The MLP processes the output that attention produced — which is a weighted mixture of value vectors, not the K-V pairs themselves."

The Q, K, V matrices are **ephemeral** — they exist only during the attention computation and are discarded afterward. What persists is their combined effect: the attention-weighted values, which are added to the residual stream.

---

## In Concrete Terms

Imagine the `=` token in `[3, +, 5, =]`:

**Attention stage:**
- The `=` token's query asks: "What are the operands?"
- The `3` token's key responds: "I am the first operand."
- The `5` token's key responds: "I am the second operand."
- The softmax weights determine how much each key-value pair contributes.
- The **output** is a single vector mixing the concepts "first operand = 3" and "second operand = 5".
- The internal Q, K, V matrices are discarded.

**MLP stage:**
- The MLP **receives** this mixed vector.
- The MLP has learned: "this pattern means I should compute 3 + 5 = 8, then 8 mod 7 = 1."
- The MLP outputs the prediction.

The MLP never inspects the original Q, K, V — it only works with what attention delivered.

---

## Key Takeaways

- **Attention's Q, K, V are internal computations**, not visible to the MLP.
- **The MLP receives the attention output** — a weighted combination of values, now enriched in the residual stream.
- **Attention decides what matters; MLPs decide what to do about it**.
- The residual stream is the **information highway** between both stages.
- Because both use **residual connections** (addition, not replacement), we can trace what each component contributes.

---

## Related Notes

- [[Transformer]] — contains both attention and MLP stages
- [[Self-Attention]] — detailed explanation of how Q, K, V work internally
- [[Feed-Forward Network (MLP)]] — what the MLP does with what it receives
- [[Residual Stream]] — the information substrate flowing between stages
- [[Circuit Formation]] — how attention and MLPs collaborate in the grokking circuit
