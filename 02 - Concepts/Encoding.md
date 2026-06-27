---
tags: [concept, representation, neural-networks, transformers]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Encoding

## What Is It?

**Encoding** is the process of converting raw input (text, numbers, images) into a numerical representation (**embedding**) that a neural network can process.

```
Raw input:  "hello"  →  Encoding  →  Numerical vector: [0.1, -0.3, 0.8, ...]
Raw input:  37       →  Encoding  →  Numerical vector: [0.2, 0.5, -0.1, ...]
```

The encoded representation captures the **meaning** or **essential properties** of the input in a form the network can manipulate mathematically.

---

## Why Does It Exist?

Neural networks understand **numbers**, not words or concepts:

- They compute dot products, matrix multiplications, activations.
- All operations are mathematical.
- But real-world inputs are symbolic: "cat," "Paris," "37."

**Encoding bridges this gap.** It converts symbols into numbers while preserving their meaning.

---

## Intuition

Imagine describing a person to someone who only understands numbers:

**Encoding a person:**
- Height: 180 cm
- Age: 25 years
- Friendliness: 8/10
- Intelligence: 7/10
- Confidence: 6/10

Now someone who only understands numbers can reason about people: "Is person A similar to person B?" (compare vectors), "What is this person like?" (interpret vector).

**Encoding a word:**
- Similar words → similar vectors.
- Meaning → captured in vector geometry.
- Arithmetic relationships → can be discovered.

---

## Types of Encoding

### 1. Token-to-Vector (Embedding)

See: **[[Embedding Matrix]]**

For **discrete symbols** (words, tokens), look up their encoding in an embedding table:

```
Token ID: 42
  ↓
Embedding lookup: W_E[42]
  ↓
Output: [0.1, -0.3, 0.8, ...]  (128-dimensional vector)
```

Different tokens get different vectors. Similar tokens end up close in vector space (learned during training).

**Used in:** Language models, transformers.

### 2. Positional Encoding

See: **[[Positional Embedding]]** and **[[RoPE]]**

For **position in a sequence**, add encoding that represents position:

```
Token: "hello" at position 0
Encoding: [0.1, -0.3, 0.8, ...]

Positional encoding: [1.0, 0.0, 0.0, ...]  (position 0)

Final representation: [0.1, -0.3, 0.8, ...] + [1.0, 0.0, 0.0, ...] = [1.1, -0.3, 0.8, ...]
```

Position 0, 1, 2, ... each have distinct encodings so the network knows order.

### 3. One-Hot Encoding

For **categorical variables**, create a binary vector:

```
Color = "Red"
One-hot: [1, 0, 0]  (first position is 1, others 0)

Color = "Blue"
One-hot: [0, 1, 0]
```

Simple but inefficient (requires one dimension per category). Not used much in deep learning.

### 4. Continuous Encoding

For **numerical inputs** (already numbers), sometimes pass directly or normalize:

```
Input: 37  →  Normalize  →  0.38  (scaled to [0, 1])
```

Or embed into a learned representation:

```
Input: 37  →  Linear layer  →  [0.2, -0.5, 0.9]
```

### 5. Contextual Encoding

Some models encode **context** into the representation:

```
Word: "bank"

In "I sat on the river bank":
Encoding: [0.3, 0.7, 0.1, ...]  (emphasizes geography)

In "I withdrew money from the bank":
Encoding: [0.8, 0.1, 0.2, ...]  (emphasizes finance)
```

The same word gets different encodings based on context. Used in transformer-based models.

---

## Encoding in Transformers

**Step 1: Tokenization**

```
Input text: "The cat sat"
Tokenize: ["The", "cat", "sat"]
Token IDs: [512, 234, 891]
```

**Step 2: Token Embedding**

```
Token ID 512  →  W_E[512]  →  [0.1, -0.3, 0.8, ...]  (128D)
Token ID 234  →  W_E[234]  →  [0.2, 0.5, -0.1, ...]  (128D)
Token ID 891  →  W_E[891]  →  [-0.4, 0.3, 0.2, ...]  (128D)
```

**Step 3: Add Position Encoding**

```
Position 0: [1.0, 0.0, 0.0, ...]
Position 1: [0.8, 0.6, 0.0, ...]
Position 2: [0.6, 0.8, 0.0, ...]

Token 1 final: [0.1, -0.3, 0.8, ...] + [1.0, 0.0, 0.0, ...] = [1.1, -0.3, 0.8, ...]
Token 2 final: [0.2, 0.5, -0.1, ...] + [0.8, 0.6, 0.0, ...] = [1.0, 1.1, -0.1, ...]
Token 3 final: [-0.4, 0.3, 0.2, ...] + [0.6, 0.8, 0.0, ...] = [0.2, 1.1, 0.2, ...]
```

**Step 4: Feed to Transformer Blocks**

The encoded vectors now flow through attention and MLP layers.

---

## Encoding in Grokking

In modular arithmetic experiments:

```
Input: 37
Encoding: W_E[37]  →  [0.15, -0.22, 0.31, ..., -0.08]  (128D)

Input: +
Encoding: W_E[+]   →  [-0.05, 0.18, -0.13, ..., 0.42]

Input: 61
Encoding: W_E[61]  →  [0.28, 0.05, -0.19, ..., 0.11]

Input: =
Encoding: W_E[=]   →  [0.33, -0.27, 0.02, ..., -0.15]
```

Each number and operator gets a learned vector representation.

**Key insight:** During grokking, Nanda et al. found that the embedding matrix encodes numbers as **angles in a high-dimensional space**. The model represents each number as a rotation. This structure **emerges** from training, not by design.

---

## Why Encoding Matters

### Good Encoding

- **Meaningful geometry:** Similar things are close. Opposite things are far.
- **Learnable:** The model can update encodings to improve performance.
- **Efficient:** Captures essential information in fewer dimensions.
- **Interpretable:** Can understand what each dimension means.

### Bad Encoding

- **Random:** No structure. Everything is equally distant.
- **Too large:** Wastes parameters (one dimension per category = huge).
- **Fixed:** Can't improve with training.
- **Irrelevant:** Misses important properties.

---

## Learned vs. Fixed Encodings

### Learned Encodings

The embedding matrix $W_E$ is initialized randomly and **updated during training**.

**Pros:**
- Adapt to the task.
- Can discover task-relevant structure.
- Flexible.

**Cons:**
- Requires training data.
- Can't transfer to new tasks easily.

**Used in:** Transformers, most neural networks.

### Fixed Encodings

Some encodings are **not trained**, like positional encoding using sine/cosine:

$$P(pos, 2i) = \sin(pos / 10000^{2i/d})$$
$$P(pos, 2i+1) = \cos(pos / 10000^{2i/d})$$

**Pros:**
- Works without training.
- Can extrapolate to longer sequences than seen during training.
- Deterministic.

**Cons:**
- May not be optimal.
- Can't adapt.

**Used in:** Original transformers (sine/cosine positional encoding), [[RoPE|RoPE]] (rotary positional encoding).

---

## Analogy — Translation

Imagine translating English to Spanish:

**Encoding is the translation:**

```
"hello" (English)  →  Encode  →  [0.1, -0.3, 0.8, ...]  (semantic meaning)
                                      ↓
                                    Process (transformer)
                                      ↓
                                  [0.2, 0.5, -0.1, ...]
                                      ↓
                                    Decode
                                      ↓
                         "hola" (Spanish)
```

Without encoding, the computer can't understand English. Encoding translates to a language the computer understands: numbers.

---

## Important Terms

**Embedding** — The numerical representation of a symbol. Often used synonymously with "encoding."

**Embedding matrix** ($W_E$) — Lookup table mapping token IDs to embedding vectors.

**Vector space** — The mathematical space where embeddings live (e.g., 128-dimensional space).

**Tokenization** — Breaking raw input (text, numbers) into discrete tokens.

**Token ID** — A unique integer assigned to each token.

**Dimension** — The size of the embedding vector (e.g., 128 dimensions per token).

**Contextual embedding** — Embedding that depends on surrounding tokens (used in transformers via attention).

---

## Common Mistakes

**Mistake 1:** "Encoding is just arbitrary assignment of numbers to words."

**Reality:** Encoding captures **meaning**. Similar words get similar vectors. Arithmetic relationships emerge. It's learned to be meaningful.

**Mistake 2:** "Bigger embedding dimension is always better."

**Reality:** Dimension trades off expressiveness vs. parameters. 128-512 is typical. Too large wastes parameters; too small limits expressiveness.

**Mistake 3:** "Fixed positional encoding is inferior to learned."

**Reality:** Both work. Fixed positional encoding (sine/cosine, RoPE) often generalizes better to longer sequences. Learned can be better for specific tasks.

---

## Key Takeaways

- **Encoding** converts raw input into numerical vectors.
- **Token embeddings** assign vectors to discrete symbols (words, numbers).
- **Positional encodings** tell the model the order of tokens.
- **Learned embeddings** adapt during training to become task-relevant.
- In grokking, embeddings encode numbers as **rotation angles** in high-dimensional space.
- Encoding quality fundamentally affects whether the network can learn.

---

## Related Notes

- [[Embedding Matrix]] — the learned lookup table for token encodings.
- [[Positional Embedding]] — encodes position in a sequence.
- [[RoPE]] — modern rotary positional encoding.
- [[Dense Vector]] — the numerical representation produced by encoding.
- [[Transformer]] — uses token and positional encodings as its first step.
- [[Token]] — the discrete unit being encoded.
