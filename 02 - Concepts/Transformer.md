---
tags: [concept, architecture, transformer, foundations]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# Transformer

## What Is a Transformer?

A **transformer** is a type of neural network — a machine learning model — introduced in 2017 by Vaswani et al. in a famous paper called *"Attention Is All You Need."*

Its defining feature is something called **[[Attention Mechanism|self-attention]]**: instead of reading inputs one-by-one in order (like older models did), the transformer looks at **all inputs at the same time** and figures out which ones are related to each other.

It is the most important architecture in modern AI. GPT, Claude, LLaMA, BERT — all of them are transformers.

> [!NOTE]
> In this vault, the transformer is the model used in **grokking experiments**. Understanding how it works is essential to understanding why and how grokking happens.

---

## Why Does It Exist?

Before transformers, the most popular models for processing sequences (like text) were called **RNNs** (Recurrent Neural Networks). RNNs read one word at a time, left to right, keeping a "memory" of what came before.

This caused two big problems:

- **Slow training** — you had to wait for step 1 before step 2, step 2 before step 3, and so on. You couldn't process words in parallel.
- **Forgetting** — by the time the model reached word 100, it had often "forgotten" what word 1 said.

Transformers solved both problems by processing **all words at the same time** and letting every word directly "look at" every other word, no matter how far apart they are.

> [!TIP]
> Think of an RNN like reading a book one page at a time, covering each page after reading it. A transformer reads the whole book at once and can jump to any page instantly.

---

## How Does It Work?

Here is the step-by-step flow of information through a transformer:

### Step 1 — Tokenization

First, the raw input (text, numbers, etc.) is broken into small pieces called **tokens**. Each token is assigned a number (an ID).

For example, GPT-2 breaks English text into about 50,257 possible tokens (words, parts of words, punctuation).

In grokking experiments, the inputs are much simpler — just numbers like `[37, ◦, 61, =]`.

### Step 2 — Embeddings

Each token ID is converted into a **[[Dense Vector|dense vector]]** — a list of numbers that represents that token mathematically.

This is done using the **[[Embedding Matrix|embedding matrix]]** $W_E$. You can think of it as a lookup table: give it a token ID, it gives back a vector.

Then, a **[[Positional Embedding|positional embedding]]** is added to tell the model *where* in the sequence each token sits — because the attention mechanism itself doesn't know order.

$$\text{token representation} = W_E[\text{token\_id}] + P[\text{position}]$$

> [!NOTE]
> Modern models like LLaMA use a smarter method called **[[RoPE|Rotary Positional Encoding (RoPE)]]** — it encodes position by rotating the internal vectors, and handles very long sequences better.

> [!TIP]
> A remarkable property of learned embeddings: **similar tokens end up close together in vector space**. For example, "king" and "queen" are close, "cat" and "dog" are close. Even arithmetic relationships appear: $\text{vec(king)} - \text{vec(man)} + \text{vec(woman)} \approx \text{vec(queen)}$. In grokking, Nanda et al. found the [[Embedding Matrix|embedding matrix]] encodes numbers as **rotation angles** in a mathematical space — this structure is not designed in, it *emerges* from training.

### Step 3 — Transformer Blocks (Repeated L Times)

The token representations flow through a stack of **transformer blocks**. A typical transformer has `L` blocks stacked on top of each other (in grokking experiments, `L = 1` or `2`). Each block contains two distinct stages:

#### Stage 1: Attention Stage (Communication)

First comes the **self-attention layer**:

1. **Layer Norm** normalizes the input vectors (standardizes scales).
2. **Multi-Head Attention** reads the entire sequence and computes which tokens should pay attention to which other tokens.
3. The output is **added back** to the original input via a **residual connection** (addition, not replacement).

**What it does:** Attention is the **communication stage**. Each token "looks at" every other token in the sequence and asks: *"Which of these tokens are relevant to me?"* The multiple attention heads allow the model to ask this question in parallel, each head specializing in different types of relationships (e.g., one head might track grammar, another might track content relevance).

#### Stage 2: MLP Stage (Processing)

Next comes the **feed-forward network (MLP)**:

1. **Layer Norm** normalizes the input.
2. **FFN/MLP** is a small two-layer neural network that operates **independently on each position** (the same network is applied to each token). It typically expands the hidden dimension (e.g., from 128 to 512) and then contracts back.
3. The output is **added back** to the input via another **residual connection**.

**What it does:** The MLP is the **processing stage**. After attention has figured out which information is relevant, the MLP acts like a **memory store** — it retrieves facts and performs transformations. Think of it as taking the "looked-up" information and converting it into useful features for the next block.

#### How the Two Stages Work Together

Here is the **workflow** at each transformer block:

1. **Input arrives** (the residual stream, updated by all previous blocks).
2. **Attention stage:** Each token figures out what other tokens are saying. The output is *added* to the input.
3. **MLP stage:** Each token uses what it just learned from attention to compute features or retrieve facts. The output is *added* to the accumulated vector.
4. **Output leaves** (now enriched with information from both stages, passed to the next block).

Because both stages use **residual connections** (addition, not replacement), the information flows **additively** through the model. This is crucial: the final prediction is literally a **sum of contributions** from every attention head and every MLP layer — making it traceable and interpretable.

#### Why Both Stages Are Needed

- **Attention alone** can tell tokens what to look at, but cannot store or retrieve specific facts.
- **MLP alone** operates in isolation (each position separately) and cannot integrate information from the whole sequence.

Together, they form a **two-step process:**
1. **Gather context** (attention: "What is relevant?")
2. **Transform and remember** (MLP: "What does this mean, and what should I output?")

This loop repeats `L` times, allowing information to flow deeper through the network and more complex computations to emerge.

#### A Concrete Example — Adding Two Numbers Modulo 7

Let's see how the two stages work together on a real grokking task.

**Task:** Compute $3 + 5 \pmod{7} = 1$

**Input sequence:** `[3, +, 5, =]` (four tokens)

**At transformer block 1:**

*Attention stage:*
- The attention head looks at all four positions.
- It learns to form links: "The `=` token should pay attention to the `3` and `5` tokens."
- Output: a new vector at the `=` position that contains information about "3" and "5".

*MLP stage:*
- The MLP receives this enriched vector (which now "knows" it needs to add 3 and 5).
- The MLP has learned facts during training: "3 + 5 = 8, and 8 mod 7 = 1."
- It outputs: the answer 1 (encoded as a vector).

**At transformer block 2 (if present):**
- Attention refines: looks at the intermediate result and checks if it makes sense.
- MLP refines: confirms or corrects the answer.

**Output:** The unembedding layer reads the final residual stream and outputs the prediction: `1`.

> [!TIP]
> Notice how the **residual connections** matter: at each stage, we *add* to the vector, we don't replace it. This means information accumulates. The final vector contains traces of all the computations that happened before, making the circuit explicit and traceable.

#### The Grand Scheme — How This Helps Grokking

In the grokking transformer, these repeated attention-MLP blocks are where the **algorithm is learned and stored**.

For the modular arithmetic example above:
- **Attention heads** learn to extract the operands `a` and `b` from the input and route them to the right positions.
- **MLP layers** learn to store the lookup table of mathematical facts (e.g., "3 + 5 mod 7 = 1") and perform the computation.

By stacking blocks, the model can:
- **Layer 1:** Extract operands, identify the operation, compute intermediate results.
- **Layer 2:** Refine and verify the result.

This is why [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Nanda et al.]] found that grokking creates **explicit circuits** — the computations are literally encoded in the patterns of attention and MLP weights. Without both stages, the model cannot form these circuits.

**In short:** Attention **gathers and routes information**, while the MLP **stores facts and performs transformations**. Repeated together, they create a learnable algorithm.

### Step 4 — The Final Prediction

After all transformer blocks, the last layer's output is passed through a **linear layer** called the **unembedding matrix** $W_U$. This produces **logits** — one number per possible output token. The highest logit is the model's prediction.

---

## The Residual Stream — A Key Idea

→ **See dedicated note: [[Residual Stream]]**

The **residual stream** is the vector flowing through each transformer block, updated additively by attention and MLP. This additive structure is essential for [[Mechanistic Interpretability]] — the final output is literally the sum of all component contributions, making it traceable.

---

## Causal Masking — Decoder-Only Models

→ **See dedicated note: [[Causal Masking]]**

In decoder-only transformers, **causal masking** prevents each position from attending to future positions (enforced by setting future attention scores to $-\infty$). This ensures fair training on [[Next-Token Prediction|next-token prediction]].

---

## How Text Is Generated — Next-Token Prediction

→ **See dedicated note: [[Next-Token Prediction]]**

Decoder-only transformers are trained and generate text via **next-token prediction**: given context, predict the next token. This simple objective, at scale, forces models to internalise knowledge and discover underlying rules.

---

## Transformer Variants

The original transformer (Vaswani et al., 2017) had an **Encoder** and a **Decoder**. Researchers found that for many tasks, only one part is needed:

| Type | Example | Best For |
|------|---------|----------|
| **Encoder-only** | BERT | Understanding text, classification, Q&A |
| **Decoder-only** | GPT, Claude, LLaMA, Mistral | Generating text, conversation, completion |
| **Encoder-Decoder** | T5 | Translation, summarisation |

**Decoder-only transformers are now the dominant architecture for large language models (LLMs).** The grokking experiments in this vault use a decoder-only setup: the model reads `[a, ◦, b, =]` and predicts the result from the `=` position. For detailed explanation of causal masking and decoder-only models, see [[Decoder-Only Dominance]].

---

## Simple Example — The Grokking Transformer

Here is exactly what the transformer looks like in grokking experiments, based on [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets|Power et al. (2022)]] and [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Nanda et al. (2023)]]:

| Component | Typical Value |
|-----------|--------------|
| Layers | 1–2 |
| Hidden dimension | 128 |
| Attention heads | 4 |
| Feed-forward width | 512 |
| Total parameters | ~100–250K |
| Optimiser | [[AdamW]] |
| Weight decay | 1.0 (key grokking lever) |
| Vocab | Numbers 0–96, plus operator token |

**Input:** `[a, ◦, b, =]` as a 4-token sequence.
**Task:** Predict the result of $a \circ b \pmod{p}$ from the embedding at the `=` position.

This tiny model — only ~100–250K parameters — is small enough to be **fully understood**. Every weight and activation can be logged at every training step. This is what makes grokking research possible.

---

## Analogy — The Reading Room

Imagine a reading room with several **expert readers** sitting at a round table. A document is passed around:

1. Each reader **reads the whole document** (self-attention — every token looks at every other token).
2. Each reader **adds their own notes** in the margin (residual connection — they add, not replace).
3. The notes are passed to a **specialist** who processes each paragraph independently (MLP).
4. Finally, a **summariser** reads the final annotated document and writes a one-word verdict (unembedding layer → prediction).

The causal mask means: when predicting word 5, readers can only see words 1–4. They keep the answer covered.

---

## Important Terms

- **Token** — A small piece of input (word, sub-word, or number).
- **[[Dense Vector|Dense vector]]** — A numerical representation of a token; similar tokens have similar vectors.
- **[[Embedding Matrix|Embedding matrix]]** ($W_E$) — Lookup table converting token IDs to vectors.
- **[[Positional Embedding|Positional embedding]]** — Encodes token position in the sequence.
- **[[RoPE|RoPE]]** — Rotation-based positional encoding used in modern models.
- **[[Attention Mechanism|Self-attention]]** — Mechanism for computing relevance between all positions.
- **[[Attention Mechanism|Attention head]]** — One independent copy of attention; multiple heads run in parallel.
- **[[Feed-Forward Network (MLP)|FFN/MLP]]** — Two-layer network operating on each position independently; acts as memory store.
- **[[Residual Connections|Residual connection]]** — Output added to input (not replacing it).
- **[[Residual Stream|Residual stream]]** — The vector flowing through blocks, updated additively by each component.
- **[[Causal Masking|Causal mask]]** — Prevents attending to future positions.
- **Logits** — Raw output scores; highest = predicted token.
- **$W_U$** — Unembedding matrix. Maps residual stream to logits.
- **[[Layer Normalization|Pre-LayerNorm]]** — Applies layer norm before each sub-layer (modern standard).
- **[[AdamW]]** — Optimizer used in grokking. Weight decay controls grokking timing.

---

## Why the Transformer Is the Right Model for Grokking

1. **Attention can compute structured algorithms.** The Fourier-circuit solution that grokking discovers — adding angles, multiplying embeddings — maps naturally onto attention and MLP layers. A CNN or basic MLP could not represent this as cleanly.
2. **It is small enough to fully instrument.** At ≤ 250K parameters it fits in memory and every weight and activation can be logged at every training step.
3. **It is the dominant LLM architecture.** Grokking on toy transformers may carry implications for emergent capabilities in large language models — a frontier question explored in [[Future Directions]].

---

## Key Takeaways

- A transformer processes all inputs **simultaneously**, using self-attention to find relationships between positions.
- It is built from stacked blocks, each with an **attention layer** and an **MLP layer**, connected by residual connections.
- The **residual stream** is a river of information that flows through the model and is updated additively by every component.
- **Decoder-only** transformers use causal masking and are trained on next-token prediction — the dominant paradigm for LLMs.
- In grokking experiments, the model is tiny (1–2 layers, ~128 hidden dim) but uses the same architecture as GPT and Claude.
- Every grokking result in this vault depends on understanding this architecture.

> [!WARNING]
> A common mistake: assuming the transformer "reads left to right" like an RNN. It does not. Attention processes all positions **simultaneously**. The causal mask only prevents a position from *seeing future positions* — it doesn't change the order of computation.

---

## Common Misconceptions

- **"Bigger is always better."** In grokking, a 1-layer transformer is enough to generalise — and is much easier to understand.
- **"The MLP just transforms data."** Research suggests MLPs act as **key-value memory stores**, retrieving facts based on what the attention heads looked up.
- **"Positional embeddings are just index numbers."** They are full dense vectors that are **learned** (or constructed via rotation in RoPE) and carry rich positional information.

---

## Evidence

- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] — the original grokking experiments using this architecture.
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — full mechanistic reverse-engineering of what the transformer learns during grokking.
- [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] — shows grokking also occurs in tensor networks (non-transformer), so it is not a transformer artefact.

---

## Open Questions

- How does transformer depth and width affect grokking timing and predictor reliability? (Thesis RQ4.)
- Does grokking in tiny transformers carry any implication for emergent capabilities in GPT-scale models?

---

## Relationship to Other Concepts

- Contains [[Attention Mechanism]] (its defining feature) and is trained with [[AdamW]].
- The specific circuit it learns is made of [[Fourier Features]].
- Its weight matrices are analysed via [[Heavy-Tailed Self-Regularization]] and [[Random Matrix Theory]].
- The **residual stream** is the information substrate analysed by [[Mechanistic Interpretability]]; each attention head and MLP layer reads from and writes to it.
- **Causal masking** enforces autoregressive structure; the **[[Embedding Matrix|embedding matrix]] + [[Positional Embedding|positional encoding]]** (including [[RoPE]] in modern models) are the model's interface to raw inputs.
- MLPs are analysed as key-value memory stores in [[Circuit Formation]] research; attention heads are analysed as information-routing mechanisms.

---

## Related Notes

**Core components & mechanisms:**
- [[Residual Stream]] · [[Residual Connections]] · [[Causal Masking]]
- [[Multi-Head Self-Attention]] · [[Feed-Forward Network (MLP)]] · [[Layer Normalization]]
- [[Attention Mechanism]] · [[AdamW]]

**Input/embedding:**
- [[Embedding Matrix]] · [[Dense Vector]] · [[Positional Embedding]] · [[RoPE]]

**Training & prediction:**
- [[Next-Token Prediction]] · [[Decoder-Only Dominance]]

**Analysis & interpretation:**
- [[Mechanistic Interpretability]] · [[Circuit Formation]]
- [[Fourier Features]] · [[Heavy-Tailed Self-Regularization]] · [[Random Matrix Theory]]

**Experimental context:**
- [[04 - Core Experimental Setup]] · [[Modular Arithmetic]]
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] · [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
- [[Grokking Predictors]] · [[Future Directions]]