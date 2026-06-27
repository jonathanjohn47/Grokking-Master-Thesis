---
tags: [concept, foundations, embeddings, transformer, position]
---
↑ Parent: [[Transformer]] · Related: [[Embedding Matrix]] · [[RoPE]] · [[Self-Attention]]

# Positional Embedding

## What is it?

A **positional embedding** is a [[Dense Vector|dense vector]] that encodes **where** a token appears in a sequence.

It is added to the token's embedding so the model knows not just *what* the token is, but also *where* it sits in the sentence.

$$\text{token representation} = W_E[\text{token\_id}] + P[\text{position}]$$

Where $P[\text{position}]$ is the positional embedding for that position.

## Why does it exist?

The [[Attention Mechanism|attention mechanism]] inside a transformer is **position-blind by default**.

When attention computes relationships between tokens, it treats all positions symmetrically — it has no built-in notion of "this word comes before that word." Every token can attend to every other token equally, regardless of order.

This is a problem. Word order matters enormously in language:

> "The cat bit the dog." ≠ "The dog bit the cat."

Without positional information, both sentences would look identical to the attention mechanism — the same tokens, just in different order, but the model would not be able to distinguish them.

**Positional embeddings solve this** by adding a unique signal to each position. Now, even if two tokens are identical words, their full representations differ because they have different positions.

> [!NOTE]
> This is sometimes called the "permutation problem." Attention is permutation-equivariant — it does the same computation regardless of input order. Positional embeddings break this symmetry and inject order information.

## How does it work?

Each position in the sequence (position 0, position 1, position 2, ...) gets its own vector. This vector is added to the token embedding at that position.

$$\text{input to transformer} = W_E[\text{token\_id}] + P[\text{position}]$$

The result is a single vector per token that contains both:
1. **What** the token is (from $W_E$)
2. **Where** the token is (from $P$)

## Three Types of Positional Encoding

There are three main approaches, each with different trade-offs:

### 1. Sinusoidal (Original Transformer, Vaswani et al. 2017)
Each position is encoded using sine and cosine waves of different frequencies:

$$P[\text{pos}, 2i] = \sin\!\left(\frac{\text{pos}}{10000^{2i/d_{\text{model}}}}\right)$$
$$P[\text{pos}, 2i+1] = \cos\!\left(\frac{\text{pos}}{10000^{2i/d_{\text{model}}}}\right)$$

In plain English: each position gets a vector of sine and cosine values at many different frequencies, like a unique musical "chord." Different positions produce different chords. This was the original design — **fixed** (not learned), and it works reasonably well.

### 2. Learned Positional Embeddings (GPT-2)
Instead of computing positions from a formula, the model simply **learns** a vector for each position during training, just like it learns token embeddings.

This is simpler: a matrix $P \in \mathbb{R}^{\text{max\_length} \times d_{\text{model}}}$ is trained alongside everything else. Each row is the positional embedding for one position.

**Trade-off:** The model can only handle sequences up to `max_length` because there is no embedding for positions beyond that.

### 3. Rotary Positional Encoding — RoPE (LLaMA, modern models)
Instead of adding a positional vector to the token embedding, RoPE **rotates** the Query and Key vectors inside the attention mechanism based on position. See [[RoPE]] for a full explanation.

RoPE is the current state of the art and is used in most modern large language models.

> [!TIP]
> The key difference: sinusoidal and learned embeddings are **added to the input** before attention. RoPE is **applied inside the attention computation** itself — it modifies Q and K directly.

## Simple Example

Imagine the sentence: `"The cat sat"`

| Position | Token | Token Embedding | Positional Embedding | Final Input     |
|----------|-------|-----------------|----------------------|-----------------|
| 0        | The   | [0.1, 0.5, ...]  | [0.0, 1.0, ...]      | [0.1, 1.5, ...] |
| 1        | cat   | [0.9, 0.2, ...]  | [0.84, 0.54, ...]    | [1.74, 0.74, ...]|
| 2        | sat   | [0.3, 0.7, ...]  | [0.91, -0.42, ...]   | [1.21, 0.28, ...]|

Each token's final representation is the sum of its meaning and its position. Now the model can tell that "cat" is in position 1 and "sat" is in position 2 — even if both words appeared again elsewhere in the text.

## Analogy

Think of a concert hall with numbered seats. Two different people (tokens) might be wearing the same colour shirt (same meaning) but sitting in different seats (different positions). The positional embedding is like the **seat number tag** each person wears — it tells you not just *who* someone is, but *where* they are sitting.

Without seat tags, you cannot describe "the person in seat 7." With seat tags, every person has a unique full description: "Person wearing red (token), seat 7 (position)."

## Important Terms

- **Permutation-equivariant**: A property of the attention mechanism meaning it treats all positions the same. Positional embeddings break this by adding position-specific information.
- **Sinusoidal encoding**: A fixed mathematical formula using sine and cosine waves to generate position vectors. Not learned.
- **Learned positional embedding**: A positional vector that is trained alongside the model's other parameters.
- **RoPE**: Rotary Positional Encoding. A modern alternative that rotates Q/K vectors instead of adding a vector to the input. See [[RoPE]].
- **Max length**: The maximum sequence length a model can handle. A limitation of learned embeddings (they have no representation for positions beyond this limit).

## Key Takeaways

- The attention mechanism cannot tell where in a sequence a token appears — it is position-blind.
- Positional embeddings add a unique vector to each position so the model knows token order.
- The final token representation = token meaning + token position.
- There are three main types: sinusoidal (fixed formula), learned (trained), and RoPE (applied inside attention).
- RoPE is the modern standard for most large language models.

> [!WARNING]
> Positional embeddings are **added**, not concatenated. The same vector dimension holds both token meaning and position information at the same time. This is possible because the model learns to separate these two signals during training.

---
## Related Notes
- [[Embedding Matrix]] — provides the token meaning half of the representation
- [[Dense Vector]] — what a positional embedding is (a vector of numbers)
- [[RoPE]] — the modern approach to positional encoding, used in LLaMA and other recent models
- [[Self-Attention]] — the mechanism that is position-blind and therefore needs positional embeddings
- [[Transformer]] — the architecture where positional embeddings are used
- [[Fourier Features]] — sinusoidal positional encoding is related to Fourier representations
