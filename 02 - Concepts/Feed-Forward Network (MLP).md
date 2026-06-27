---
tags: [concept, transformer, mlp, neural-network]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Feed-Forward Network (MLP)

## What Is It?

A **Feed-Forward Network (FFN)** — also called an **MLP** (Multi-Layer Perceptron) — is a small neural network inside each transformer block.

It sits **after** the attention layer and processes each token's representation independently.

The FFN:
- Expands the dimension (e.g., 128 → 512).
- Applies a non-linear function (ReLU or GELU).
- Compresses back to the original dimension (512 → 128).

Then its output is added to the [[Residual Stream|residual stream]].

---

## Why Does It Exist?

### Problem: Attention Isn't Enough

Attention is great for finding relationships between positions:

- Position A looks at position B.
- Position C looks at position A.
- Token relationships are understood.

But attention **cannot store facts** or **retrieve knowledge**. 

For example, if the model needs to know "the capital of France is Paris," or "37 + 61 = 98 mod 97," attention alone cannot handle this. It only says which positions matter, not what they mean.

### Solution: MLPs Store Knowledge

Recent research (especially Neel Nanda) suggests **MLPs act as key-value memory stores**:

- Attention learns: "position A and B are related."
- MLPs learn: "when I see these activation patterns (from attention), retrieve this knowledge."

In a sense:
- **Attention** = "what information matters?"
- **MLP** = "what do I know about it?"

Together, they enable both understanding relationships and using knowledge.

---

## Intuition

Imagine a library system:

**Attention** = the librarian helping you find books:

- "You're looking for books about France?"
- "Here are all the books we have on France."
- (Pointing to relevant books)

**MLP** = the storage and retrieval system:

- A customer arrives asking "What's the capital of France?"
- The MLP looks up "France" in its internal knowledge base.
- It retrieves: "Capital: Paris, Population: 2 million, ..."

Together:
1. Attention points to relevant tokens.
2. MLP retrieves facts related to those tokens.
3. The answer emerges.

---

## How Does It Work?

### Architecture

Here's the standard FFN design in transformers:

```
Input: x (dimension 128)
  │
  ▼
[Dense Layer 1: 128 → 512]    (expand 4×)
  │
  ▼
[Non-linearity: ReLU or GELU]   (add non-linearity)
  │
  ▼
[Dense Layer 2: 512 → 128]    (compress back)
  │
  ▼
Output: x (dimension 128)
```

### Step-by-Step

**Step 1: Expand**

$$h = W_1 \cdot x + b_1$$

Where:
- $W_1$ is a (128 × 512) matrix (actually transposed: 512 × 128).
- $x$ is the input (dimension 128).
- $b_1$ is a bias term.
- $h$ is the intermediate representation (dimension 512).

This is called the **up-projection** — expanding the dimension 4×.

**Step 2: Apply non-linearity**

$$h' = \text{ReLU}(h)$$

Or in modern models:

$$h' = \text{GELU}(h)$$

This applies a non-linear activation function element-wise.

**Step 3: Compress**

$$y = W_2 \cdot h' + b_2$$

Where:
- $W_2$ is a (512 × 128) matrix.
- $y$ is the output (dimension 128).

This is called the **down-projection** — compressing back to the original dimension.

**Step 4: Add to residual stream**

$$x_{\text{new}} = x + y$$

The MLP output is added (not replaced) in the residual stream.

### The Expansion Factor

Most transformers expand 4×:

```
Hidden dim: 128
Expansion factor: 4
Intermediate dim: 128 × 4 = 512
```

Some models use different factors (3× or 8×), but 4× is standard.

---

## Example

Let's trace through a small FFN with concrete numbers:

**Input:** `x = [1.0, 0.5, -0.3]` (dimension 3)

**Step 1: Expand to dimension 12 (4×)**

Suppose $W_1$ is a random 12 × 3 matrix. After multiplication:

$$h = [0.2, -0.1, 0.5, 0.1, -0.3, 0.8, 0.0, 0.4, -0.2, 0.3, 0.1, -0.6]$$

(12 values)

**Step 2: Apply ReLU (remove negatives)**

ReLU sets negative values to 0:

$$h' = [0.2, 0.0, 0.5, 0.1, 0.0, 0.8, 0.0, 0.4, 0.0, 0.3, 0.1, 0.0]$$

(negatives are 0)

**Step 3: Compress back to dimension 3**

Multiply by $W_2$ (a 3 × 12 matrix):

$$y = [0.05, -0.02, 0.08]$$

(back to 3 values)

**Step 4: Add to residual stream**

$$x_{\text{new}} = x + y = [1.0, 0.5, -0.3] + [0.05, -0.02, 0.08] = [1.05, 0.48, -0.22]$$

---

## What Do MLPs Learn?

### In Large Language Models

Research by researchers like Chris Olah and Neel Nanda reveals:

- **Different MLPs specialize in different kinds of knowledge**.
- Some MLPs store facts: "the capital of France is Paris."
- Some MLPs perform operations: "adding 1 to any number."
- Some MLPs route information: "if you're talking about animals, route to the animal MLP."

### In Grokking

In grokking experiments (modular arithmetic), Nanda et al. found:

- Attention heads compute **structured relationships** (e.g., "extract the two numbers").
- MLPs compute **arithmetic operations** (e.g., "add them together" or "apply mod").

The solution emerges from a circuit where attention and MLPs collaborate.

---

## Why 4× Expansion?

Why expand the dimension if you're just going to compress it back?

### Reason 1: Non-linearity needs space

The ReLU (or GELU) function only activates positive values. To represent complex functions, you need the expanded dimension to have enough "room" to express non-linearities.

### Reason 2: Parameter efficiency

Expanding 4× is a balance:

- **Too small** (no expansion): Not enough expressivity.
- **Too large** (10× expansion): Wastes parameters and computation.
- **4× sweet spot**: Good expressivity with manageable parameter count.

### Example of why expansion helps

Without expansion:

```
x (3D) → ReLU → y (3D)
```

You can only represent 3D interactions with ReLU. Limited expressivity.

With expansion:

```
x (3D) → expand to 12D → ReLU → compress to 3D
```

You can represent much more complex relationships in 12D, then compress them into 3D.

---

## ReLU vs GELU

### ReLU (Rectified Linear Unit)

$$\text{ReLU}(x) = \max(0, x)$$

Simple: if negative, set to 0. If positive, keep it.

- **Pros:** Fast, simple, works well.
- **Cons:** Not differentiable at 0, can cause "dead neurons" (neurons that output 0 forever).

### GELU (Gaussian Error Linear Unit)

$$\text{GELU}(x) = x \cdot \Phi(x)$$

Where $\Phi(x)$ is the cumulative Gaussian distribution. Smoother than ReLU.

- **Pros:** Smoother, less likely to kill neurons.
- **Cons:** Slightly slower to compute.

**Modern models (GPT-2+) use GELU.**

---

## MLPs as Memory in Transformers

Recent mechanistic interpretability research (Nanda, Ganev, et al.) suggests:

### A key insight

MLPs don't just transform data — they act like **key-value memories**:

```
Input token features: [is_about_france, is_noun, ...]
     │
     ▼
[MLP's learned keys]
     │
     ├─→ "Does this match 'France'?" YES
     │
     ▼
[MLP's learned values]
     │
     └─→ Retrieve: "capital: Paris, language: French, ..."
```

This explains why LLMs can "know" facts: the MLPs store them as learned key-value pairs.

### Implication for grokking

In grokking, Nanda found:

- Attention heads learn to **extract and align numbers**.
- MLPs learn to **compute the operation** (addition, multiplication, modular reduction).

The Fourier feature solution that grokking discovers is a circuit where:
- **Attention** provides the inputs to MLPs.
- **MLPs** perform the arithmetic.

---

## Analogy — A Brain Metaphor

- **Attention** = neurons that connect distant brain regions (understanding relationships).
- **MLPs** = local processing in each region (memory and computation).

When you recognize a face:

1. **Attention:** Different brain regions activate in parallel, routing information (face → memory → identity).
2. **MLPs:** Local processing in visual cortex retrieves features ("is this a smile?", "are these eyes blue?").

Together: recognition emerges.

---

## Important Terms

**Feed-Forward Network (FFN)** — A small neural network applied after attention, expanding then compressing the hidden dimension.

**MLP** — Multi-Layer Perceptron; synonym for FFN in transformer context.

**Up-projection** — The first dense layer that expands the dimension (128 → 512).

**Down-projection** — The second dense layer that compresses the dimension (512 → 128).

**Activation function** — A non-linear function (ReLU, GELU) applied between the two dense layers.

**ReLU** — Rectified Linear Unit: $\text{ReLU}(x) = \max(0, x)$.

**GELU** — Gaussian Error Linear Unit: a smooth approximation to ReLU.

**Expansion factor** — The ratio of intermediate dimension to hidden dimension (typically 4).

---

## Common Mistakes

**Mistake 1:** "MLPs are just random linear transformations."

**Reality:** MLPs are **learned key-value stores** that retrieve knowledge. They're fundamental to how transformers store facts.

**Mistake 2:** "The expansion (4×) is just for efficiency."

**Reality:** The expansion is for **expressivity**. The non-linearity needs the extra dimensions to represent complex functions. It's a necessity, not just optimization.

**Mistake 3:** "All MLPs in a model learn the same thing."

**Reality:** Different MLPs specialize in different knowledge. In large models, different layers' MLPs focus on different semantic categories.

**Mistake 4:** "Attention and MLPs solve different problems."

**Reality:** They're deeply integrated. Attention routes information; MLPs process and store it. You need both.

---

## Key Takeaways

- **MLPs** are small neural networks inside transformer blocks that expand, apply non-linearity, then compress.
- They **store and retrieve knowledge**, acting as key-value memories.
- Expansion by 4× provides enough dimensionality for non-linear representations.
- **Modern models use GELU** activation instead of ReLU.
- In grokking, MLPs learn to **compute operations** (arithmetic) while attention learns to **route information**.
- Without MLPs, transformers couldn't store facts and would be much less capable.

---

## Related Notes

- [[Transformer]] — the architecture containing MLPs.
- [[Residual Stream]] — the information stream that MLPs read from and write to.
- [[Multi-Head Self-Attention]] — the partner to MLPs; attention + MLPs form complete transformer blocks.
- [[Circuit Formation]] — how attention and MLPs form interpretable circuits.
- [[Mechanistic Interpretability]] — the framework for understanding MLP function.
- [[Activation Function]] — deep dive into ReLU, GELU, and other non-linearities.
