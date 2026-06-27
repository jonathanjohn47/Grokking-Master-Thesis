---
tags: [concept, transformer, architecture, gradient-flow]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Residual Connections

## What Is It?

A **residual connection** is a simple architectural pattern: instead of **replacing** data, you **add** new information to existing data.

```
x_new = x_old + f(x_old)

Instead of:

x_new = f(x_old)
```

The term "residual" refers to the **residue** (leftovers) — in this case, the original information that isn't replaced.

Residual connections are the **core mechanism** that makes transformers work and enables [[Mechanistic Interpretability]].

---

## Why Does It Exist?

### Problem 1: Vanishing Gradients

In deep neural networks, gradients get smaller as they flow backward through layers:

```
Output error: 0.5
After layer 20: gradient ≈ 0.001
After layer 10: gradient ≈ 0.00001
After layer 1: gradient ≈ 0.0000001
```

With tiny gradients, early layers don't learn (weights barely change).

This made training **very deep networks impossible** before residual connections were invented.

### Problem 2: Information Loss

Without residual connections, each layer's output completely replaces the previous:

```
Layer 0: x_0 = embedding
Layer 1: x_1 = f1(x_0)  ← x_0 information is gone
Layer 2: x_2 = f2(x_1)  ← x_1 information is gone
```

Information from earlier layers can't directly influence later layers. This limits expressivity.

### Solution: Residual Connections

By **adding** instead of replacing, you:

1. **Preserve information** — earlier layers' outputs flow directly to later layers.
2. **Improve gradient flow** — gradients have a direct path backward.

---

## Intuition

Imagine a relay race where runners pass a baton:

### Without Residual Connections

Runner 1 hands the baton to runner 2.

Runner 2 **modifies the baton** (changes its shape, color).

Runner 3 receives the **modified baton** from runner 2.

If runner 2's modification was bad, runners 3+ have no way to recover the original baton's properties.

### With Residual Connections

Runner 1 passes the baton to runner 2.

Runner 2 adds a **ribbon** to the baton (adds information) but keeps the original baton intact.

Runner 3 receives the original baton **plus the ribbon**.

If the ribbon is useless, runner 3 can ignore it. The original baton always flows forward.

---

## How Does It Work?

### Mathematically

A standard layer transformation:

$$y = f(x)$$

A residual transformation:

$$y = x + f(x)$$

### Step by Step

**Step 1: Input arrives**

```
x = [0.1, -0.3, 0.8, ...]  (the residual stream)
```

**Step 2: Pass through sub-layer (e.g., attention)**

```
f_output = Attention(LayerNorm(x))
         = [0.05, 0.02, -0.1, ...]
```

**Step 3: Add to original**

```
y = x + f_output
  = [0.1, -0.3, 0.8, ...] + [0.05, 0.02, -0.1, ...]
  = [0.15, -0.28, 0.7, ...]
```

The original `x` is preserved; only the update is added.

---

## Example: Tracing Through a Transformer

Let's trace the residual stream through one transformer block:

**Input:** `x_0 = [0.2, -0.1, 0.5]`

**Sub-layer 1: Attention**

```
attn_output = Attention(LayerNorm(x_0)) = [0.1, 0.05, -0.02]
x_1 = x_0 + attn_output = [0.3, -0.05, 0.48]
```

**Sub-layer 2: MLP**

```
mlp_output = MLP(LayerNorm(x_1)) = [0.01, 0.02, -0.01]
x_2 = x_1 + mlp_output = [0.31, -0.03, 0.47]
```

Notice: **`x_0` is still present** in `x_2` (it was added and never removed).

In fact:

$$x_2 = x_0 + \text{attn\_output} + \text{mlp\_output}$$

The final output is the **sum of all contributions**.

---

## Gradient Flow

### Without Residual Connections

```
Loss gradient at output: ∂L/∂y = 1.0

After layer 3: ∂L/∂x_3 = ∂L/∂y · ∂y/∂x_3 = 1.0 · 0.1 = 0.1
After layer 2: ∂L/∂x_2 = 0.1 · 0.1 = 0.01
After layer 1: ∂L/∂x_1 = 0.01 · 0.1 = 0.001  ← very small!
After layer 0: ∂L/∂x_0 = 0.001 · 0.1 = 0.0001  ← vanishing!
```

Gradients vanish quickly. Early layers don't learn.

### With Residual Connections

Each layer has a **direct gradient path**:

$$\frac{\partial x_{i+1}}{\partial x_i} = \frac{\partial (x_i + f(x_i))}{\partial x_i} = 1 + \frac{\partial f}{\partial x_i}$$

The `1` term means: even if the layer's gradient is small, there's a direct path (gradient = 1).

```
Loss gradient at output: ∂L/∂y = 1.0

After layer 3: ∂L/∂x_3 = 1.0 · (1 + tiny) ≈ 1.0
After layer 2: ∂L/∂x_2 = 1.0 · (1 + tiny) ≈ 1.0
After layer 1: ∂L/∂x_1 = 1.0 · (1 + tiny) ≈ 1.0  ← NOT vanishing!
After layer 0: ∂L/∂x_0 = 1.0 · (1 + tiny) ≈ 1.0  ← strong gradient!
```

Gradients stay strong throughout the network. All layers can learn.

---

## Residual Connections Enable Mechanistic Interpretability

This is the key insight for [[Mechanistic Interpretability]]:

### Additivity

Because everything adds (never replaces), the final output is literally the **sum of all contributions**:

$$\text{output} = \text{embedding} + \text{head1\_contribution} + \text{head2\_contribution} + \cdots + \text{mlp\_contribution}$$

You can track exactly where each piece came from.

### Decomposition

You can decompose the output:

```
Final logit = 0.98

Contributions:
  - Embedding: +0.1
  - Head 1: +0.3
  - Head 2: +0.05
  - Head 3: -0.02
  - Head 4: +0.2
  - MLP 1: +0.15
  - MLP 2: +0.2
  Total: +0.98 ✓
```

This makes understanding what the model learned **tractable**.

Without residual connections, the output would be opaque:

```
output = MLP2(MLP1(Head1(...)))  ← nested, hard to decompose
```

---

## Pre-Residual vs. Post-Residual

There's a subtle choice: where to apply [[Layer Normalization|layer normalization]]?

### Pre-Residual (Modern)

```
x → [LayerNorm] → [SubLayer] → y = x + output
```

Layer norm applied **before** the sub-layer.

**Advantages:**
- More stable gradient flow.
- Better for deep networks.
- Used in GPT-2+, modern models.

### Post-Residual (Older)

```
x → [SubLayer] → [LayerNorm] → y = x + output
```

Layer norm applied **after** the sub-layer.

**Disadvantages:**
- Less stable.
- Harder to train.
- Original transformer used this.

---

## Analogy — Foundation and Building

Imagine constructing a tall building:

**Without residual connections:**

```
Foundation: concrete slab
Floor 1: decorative tile (replaces foundation)
Floor 2: marble (replaces floor 1)
Floor 3: wood (replaces floor 2)
```

Each floor completely covers what's below. If floor 3 is broken, floor 1's strength doesn't help.

**With residual connections:**

```
Foundation: concrete slab
Floor 1: marble (sits on foundation, foundation visible from above)
Floor 2: carpet (sits on floor 1, floor 1 visible underneath)
Floor 3: rug (sits on floor 2, floor 2 visible underneath)
```

Each level adds on top but doesn't erase. If floor 2 is weak, floor 1's strength provides support.

---

## Why Transformers Use Residual Connections

Transformers have:

1. **Many layers** (12–24+ in large models).
2. **Deep computation** (each attention head is a function).
3. **Need for gradient flow** (backpropagation through all layers).
4. **Need for interpretability** (understanding what each component learned).

Residual connections provide all of this.

Without them, training would be unstable and understanding would be nearly impossible.

---

## Important Terms

**Skip connection** — Synonym for residual connection (the path that "skips" the sub-layer).

**Residual branch** — The sub-layer (f(x)) in the residual connection.

**Main branch** — The identity path (just x) in the residual connection.

**Bottleneck** — A residual block where f(x) has lower dimension than x (used to reduce parameters).

**Highway networks** — An earlier architecture using gated residual connections (precursor to modern residual connections).

---

## Common Mistakes

**Mistake 1:** "Residual connections just pass information unchanged."

**Reality:** They **preserve** information while allowing the sub-layer to add updates. Old information + new updates = new state.

**Mistake 2:** "Residual connections make the model too simple."

**Reality:** They make the model more expressive. By preserving information, sub-layers can focus on small, interpretable updates.

**Mistake 3:** "We don't need residual connections in shallow networks."

**Reality:** Shallow networks benefit too — better information flow, easier optimization, more interpretability.

**Mistake 4:** "Residual connections are just for deep networks."

**Reality:** They're fundamental to how modern architectures (transformers) work, even small ones.

---

## Key Takeaways

- **Residual connections** add sub-layer output to input instead of replacing it.
- They **preserve information** — older layers' outputs remain accessible to later layers.
- They **improve gradient flow** — gradients have a direct path for backpropagation.
- They **enable interpretability** — output is literally the sum of all contributions, traceable and decomposable.
- **Transformers couldn't work** without residual connections.
- This is why understanding residual connections is fundamental to understanding transformers.

---

## Related Notes

- [[Transformer]] — the architecture built entirely on residual connections.
- [[Residual Stream]] — the "river" created by stacking residual connections.
- [[Layer Normalization]] — typically applied alongside residual connections.
- [[Mechanistic Interpretability]] — enabled by the additivity of residual connections.
- [[Gradient Flow]] — deep dive into how residual connections affect backpropagation.
