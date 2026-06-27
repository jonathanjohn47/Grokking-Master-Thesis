---
tags: [concept, transformer, attention, architecture]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Multi-Head Self-Attention

## What Is It?

**Multi-head self-attention** is a mechanism where multiple independent **attention heads** run in parallel, each learning to focus on different relationships between tokens.

Instead of one attention mechanism looking at all positions, you have $h$ heads (e.g., 4 or 8) each asking: *"which other positions matter to me?"* with different learned priorities.

---

## Why Does It Exist?

A single attention head can only compute one "view" of relationships:

- Head 1 might focus on: "which tokens are subjects?"
- Head 2 might focus on: "which tokens are verbs?"
- Head 3 might focus on: "which tokens are pronouns?"

Without multiple heads, one head would need to handle all these relationships simultaneously—it's like asking one person to listen for melody, rhythm, and lyrics at once. Much harder than having specialists.

**Multiple heads provide different perspectives in parallel.**

---

## Intuition

Imagine reviewing a document with a team of specialists:

- **Lawyer** focuses on legal implications.
- **Accountant** focuses on financial aspects.
- **Engineer** focuses on technical feasibility.

Each reviews the whole document but attends to different details. Together, their perspectives create a complete understanding.

**Multi-head attention works similarly.** Each head attends to the whole sequence but emphasizes different relationships.

---

## How Does It Work?

### Architecture

```
Input: x (all positions)
  │
  ├─ Head 1 → [compute Q₁, K₁, V₁] → attention₁
  ├─ Head 2 → [compute Q₂, K₂, V₂] → attention₂
  ├─ Head 3 → [compute Q₃, K₃, V₃] → attention₃
  └─ Head 4 → [compute Q₄, K₄, V₄] → attention₄
  │
  ▼
[Concatenate all outputs]
  │
  ▼
[Linear projection]
  │
  ▼
Output
```

### Step by Step

**Step 1: Split the hidden dimension across heads**

For a 128-dimensional vector with 4 heads:
- Each head gets 128 ÷ 4 = 32 dimensions.

**Step 2: Each head independently computes attention**

Head $i$ computes:
$$Q_i = x W_Q^{(i)}$$
$$K_i = x W_K^{(i)}$$
$$V_i = x W_V^{(i)}$$

Then:
$$\text{attention}_i = \text{softmax}\left(\frac{Q_i K_i^T}{\sqrt{d_k}}\right) V_i$$

where $d_k = 128 / 4 = 32$ is the head dimension.

**Step 3: Concatenate all head outputs**

$$\text{concat} = [\text{attention}_1, \text{attention}_2, \text{attention}_3, \text{attention}_4]$$

This produces a 128-dimensional vector (4 heads × 32 dimensions each).

**Step 4: Linear projection**

$$\text{output} = \text{concat} \cdot W_O$$

where $W_O$ is a learned projection matrix.

---

## Example

Let's trace through with a small example:

**Input sequence:** `[The, cat, sat]` (3 tokens, 6D vectors)

**Setup:** 2 heads, 3D per head

**Head 1** (learns to focus on grammatical role):

```
Q₁ = [0.1, -0.2, 0.3]  (for each token)
K₁ = [0.2, 0.1, -0.1]
V₁ = [0.5, -0.3, 0.2]

Attention computed for all positions...
attention₁_output = [0.4, -0.2, 0.3]  (for first token)
```

**Head 2** (learns to focus on semantic role):

```
Q₂ = [-0.1, 0.3, 0.1]
K₂ = [0.1, -0.2, 0.3]
V₂ = [-0.1, 0.4, 0.2]

attention₂_output = [-0.05, 0.15, 0.1]  (for first token)
```

**Concatenate:**

```
concat = [0.4, -0.2, 0.3, -0.05, 0.15, 0.1]
```

**Project:**

```
output = concat · W_O = [0.35, -0.1, 0.25]  (back to 6D)
```

---

## Why Multiple Heads?

### Reason 1: Redundancy and Robustness

If one head fails or learns something irrelevant, other heads can compensate. The model isn't dependent on a single pathway.

### Reason 2: Parallel Computation

Modern GPUs/TPUs can compute multiple heads in parallel very efficiently. It's faster than using one mega-head.

### Reason 3: Different Learned Patterns

Research shows different heads learn different relationships:

- Some heads learn local dependencies (nearby tokens).
- Some heads learn long-range dependencies (distant tokens).
- Some heads learn syntactic patterns (grammar).
- Some heads learn semantic patterns (meaning).

In grokking, different heads learn different arithmetic operations.

---

## Head Specialization in Grokking

In modular arithmetic experiments, Nanda et al. found:

- **Head A:** Extracts the first number from the sequence.
- **Head B:** Extracts the second number.
- **Head C:** Attends to the operator token.
- **Head D:** Aggregates information for the final operation.

Each head plays a specific role in the circuit.

---

## Analogy — Orchestra

An orchestra has:
- **Violins** attending to melody.
- **Cellos** attending to harmony.
- **Drums** attending to rhythm.
- **Horns** attending to emphasis.

Each section focuses on one aspect, but together they create a complete musical experience.

**Multi-head attention is the orchestra of transformers.**

---

## How Many Heads?

Common numbers:

| Model | Heads | Dimension |
|-------|-------|-----------|
| GPT-2 | 12 | 768 |
| GPT-3 | 96 | 12,288 |
| BERT | 12 | 768 |
| Grokking | 4 | 128 |

Typically: 64 dimensions per head is a sweet spot.

More heads = more specialization, but diminishing returns.

---

## Important Terms

**Attention head** — One independent copy of the attention mechanism, operating on a subset of the hidden dimension.

**Query (Q)** — What this position is looking for.

**Key (K)** — What other positions are offering.

**Value (V)** — The actual information to aggregate.

**Head dimension** ($d_k$) — Dimension per head; usually hidden_dim ÷ num_heads.

**Multi-head attention** — Multiple attention heads running in parallel, their outputs concatenated.

---

## Common Mistakes

**Mistake 1:** "Multiple heads means the model computes attention multiple times (slower)."

**Reality:** Modern hardware executes heads in parallel, so it's not slower. Just different organization of computation.

**Mistake 2:** "All heads learn the same thing."

**Reality:** Heads learn different patterns. Some focus on positions, others on semantics, etc.

**Mistake 3:** "You need many heads to work well."

**Reality:** Even 4 heads (as in grokking) are often sufficient. Diminishing returns after that.

---

## Key Takeaways

- **Multi-head attention** runs $h$ independent attention mechanisms in parallel.
- Each head operates on hidden_dim ÷ h dimensions.
- Outputs are concatenated and projected back to the original dimension.
- Different heads learn different relationships (syntactic, semantic, positional).
- Multiple heads provide robustness and parallel efficiency.
- In grokking, each head plays a specific role in computing modular arithmetic.

---

## Related Notes

- [[Attention Mechanism]] — the single-head mechanism that multi-head extends.
- [[Transformer]] — contains multi-head self-attention in each block.
- [[Residual Stream]] — the vector that attention heads read from and write to.
- [[Circuit Formation]] — how attention heads combine to form interpretable circuits.
- [[Mechanistic Interpretability]] — framework for understanding what each head learns.
