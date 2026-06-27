---
tags: [concept, foundations, embeddings, transformer]
---
↑ Parent: [[Transformer]] · Related: [[Dense Vector]] · [[Positional Embedding]]

# Embedding Matrix

## What is it?

The **embedding matrix** is a giant lookup table that converts token IDs into [[Dense Vector|dense vectors]].

It is usually written as $W_E$ (W for "weight," E for "embedding").

Think of it as a dictionary: you give it a number (the token's ID), and it gives you back a long list of numbers (the token's dense vector).

## Why does it exist?

A neural network cannot process the word "cat" directly. It needs numbers.

The naive solution — give every token a single unique number — does not work, because it implies false relationships (e.g., cat=1, dog=2 implies "dog is bigger than cat by exactly 1," which is meaningless).

The embedding matrix solves this by giving every token its own **rich, multi-dimensional representation** — a dense vector — that can capture actual meaning and similarity.

> [!NOTE]
> The embedding matrix is one of the first things that happens when text enters a language model. Before any attention or computation, every token is "looked up" in this matrix.

## How does it work?

**Step 1 — Build the vocabulary.**
Every unique token gets a unique integer ID. GPT-2 has 50,257 tokens. Each token maps to one integer.

**Step 2 — Create the matrix.**
The embedding matrix $W_E$ has one row per token in the vocabulary. Each row is a dense vector of size $d_{\text{model}}$ (the model's hidden dimension — e.g., 768 for GPT-2 Small, 4096 for LLaMA-7B).

$$W_E \in \mathbb{R}^{\text{vocab\_size} \times d_{\text{model}}}$$

So for GPT-2 Small: $W_E \in \mathbb{R}^{50257 \times 768}$. That is a table with 50,257 rows and 768 columns.

**Step 3 — Look up the token.**
When token with ID 4321 enters the model, the embedding step simply retrieves row 4321 from $W_E$:

$$\text{embedding} = W_E[\text{token\_id}]$$

This gives a dense vector of 768 numbers representing that token.

**Step 4 — Learn better representations.**
At the start of training, these vectors are random. During training, the model adjusts every row in $W_E$ so that tokens that appear in similar contexts end up with similar vectors. This happens automatically via gradient descent — no one hand-labels any vectors.

## Simple Example

Suppose a tiny vocabulary of 5 tokens and $d_{\text{model}} = 4$:

| Token ID | Word   | Embedding Vector      |
|----------|--------|-----------------------|
| 0        | cat    | [0.9, 0.1, 0.2, 0.4] |
| 1        | dog    | [0.8, 0.2, 0.1, 0.3] |
| 2        | king   | [0.1, 0.9, 0.7, 0.6] |
| 3        | queen  | [0.2, 0.8, 0.8, 0.5] |
| 4        | the    | [0.0, 0.0, 0.1, 0.9] |

When the word "king" (ID=2) arrives, the model retrieves `[0.1, 0.9, 0.7, 0.6]` from row 2 of the matrix.

Notice: cat and dog have similar vectors. King and queen have similar vectors. "The" is very different from all of them.

## Analogy

Imagine a library where every book has a unique ID number. The embedding matrix is the **catalogue**: you give it an ID number, and it hands back a detailed profile of that book — genre, length, reading level, themes, etc. Each "profile" is a dense vector. Books about similar topics will have similar profiles.

## What Emerges in Training

A remarkable property of learned embeddings: **arithmetic relationships appear spontaneously**.

The classic example:

$$\text{vec}(\text{king}) - \text{vec}(\text{man}) + \text{vec}(\text{woman}) \approx \text{vec}(\text{queen})$$

Nobody programmed this. The model discovered it because "king is to man as queen is to woman" is a pattern that appears constantly in text. This shows the embedding matrix captures genuine semantic structure.

> [!TIP]
> In the grokking context, [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Nanda et al.]] discovered that the embedding matrix encodes numbers (0 to 96) as **rotation angles in Fourier space** — the model invents its own number line made of circular frequencies. See [[Fourier Features]].

## The Unembedding Matrix

There is also an **unembedding matrix** $W_U$, which works in the opposite direction: it takes the model's final dense vector and converts it back into scores (logits) over the vocabulary — one score per possible next token. Softmax then converts these scores into probabilities.

$$\text{logits} = x_{\text{final}} \cdot W_U$$

## Important Terms

- **Vocabulary**: The complete set of tokens the model knows. Each token has a unique integer ID.
- **Token ID**: The integer that identifies a token in the vocabulary.
- $W_E$: The standard notation for the embedding matrix.
- $d_{\text{model}}$: The size of each embedding vector (the "width" of the model).
- **Lookup**: The operation of retrieving a row from the matrix using a token ID.
- **Gradient descent**: The process that adjusts the rows of $W_E$ during training.

## Key Takeaways

- The embedding matrix $W_E$ is a table with one row per vocabulary token.
- Each row is a [[Dense Vector|dense vector]] representing that token.
- Looking up a token is just retrieving its row from the table.
- The vectors start random and become meaningful through training.
- Learned embeddings capture real semantic relationships — arithmetic, analogies, and more.
- In grokking, the embedding matrix learns to encode numbers as angles on a circle.

> [!WARNING]
> The embedding matrix is **not hand-designed**. People do not decide that "cat" should have the vector `[0.9, 0.1, ...]`. All values are learned automatically during training. If you see a claim that embeddings are hand-crafted, that is incorrect.

---
## Related Notes
- [[Dense Vector]] — what each row of the embedding matrix is
- [[Positional Embedding]] — the additional vector added to encode token position
- [[Transformer]] — the architecture that contains the embedding matrix
- [[Fourier Features]] — the structure the embedding matrix learns in grokking experiments
- [[Representation Learning]] — the broader field of learning good vector representations
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — shows the embedding matrix encodes residues as Fourier angles
