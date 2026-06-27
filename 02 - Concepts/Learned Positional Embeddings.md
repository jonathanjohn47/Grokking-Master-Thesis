---
tags: [concept, foundations, positional-encoding, transformer, embeddings]
---
↑ Parent: [[Positional Embedding]] · Related: [[Sinusoidal Positional Encoding]] · [[RoPE]] · [[Transformer]]

# Learned Positional Embeddings

## What is it?

**Learned Positional Embeddings** are a method for telling a transformer model the position of each word in a sentence.

Unlike other methods that use fixed mathematical formulas, this approach lets the model **learn the positional information itself** during training — just like it learns everything else.

Each position in the sequence gets its own vector (a list of numbers). These vectors start random and are gradually adjusted during training until they become useful representations of position.

> [!NOTE]
> Learned positional embeddings were used in **GPT-2** (OpenAI, 2019) and early versions of **BERT** (Google, 2018). They were one of the first major alternatives to the sinusoidal encoding from the original Transformer paper.

---

## Why does it exist?

### The Starting Point: Transformers Are Word-Order Blind

A [[Transformer]] model processes words using [[Attention Mechanism|attention]], which lets every word look at every other word simultaneously. But attention has no built-in sense of order.

Without any positional information:

```
"The cat chased the dog."
```

and

```
"The dog chased the cat."
```

look completely identical to the transformer. Same words, same vectors, same everything.

This is obviously wrong — word order completely changes meaning. Positional encoding is the fix.

### The Problem with Sinusoidal Encoding

The original Transformer used [[Sinusoidal Positional Encoding]] — fixed vectors computed from sine and cosine formulas. This worked, but researchers noticed a limitation:

> **The formula-computed vectors might not be the best possible representations of position.**

They are designed by humans based on mathematical intuition. But a language model is trained on millions of examples. Could it learn **better** positional representations by itself?

This was the motivation for learned positional embeddings: let the model figure out the best way to represent positions from the data.

---

## Intuition First

### The "Name Tags at a Party" Analogy

Imagine you are organising a party. You want guests to know their assigned seat number (position). You could:

**Option A: Use a fixed badge design.**
Print badges that say "Seat 1", "Seat 2", etc., using a specific font and layout you designed in advance.

**Option B: Let guests design their own badges.**
Give each guest a blank badge and let them write their seat number however feels most natural to them. Over many parties, they learn which style of writing is easiest for others to read.

**Sinusoidal encoding** is like Option A — the badges are pre-designed using a fixed formula.

**Learned positional embeddings** are like Option B — the model starts with random "badges" and gradually refines them through experience.

> [!TIP]
> The key intuition: instead of computing positional vectors by formula, we let the model learn them during training. The model may discover positional representations that are more useful for the specific tasks it is trained on.

### Starting Random, Ending Useful

At the beginning of training, learned positional embeddings are **random noise** — meaningless lists of numbers. But as the model trains on millions of examples, these random values gradually shift.

The model keeps adjusting them (via [[Gradient Descent]]) until they represent position in a way that actually helps the model perform better.

By the end of training, each positional embedding encodes something meaningful about that position — though exactly *what* it encodes is not designed by humans. The model finds it on its own.

---

## Formal Definition

> **Learned positional embeddings** are a matrix of trainable vectors $P \in \mathbb{R}^{L \times d}$, where $L$ is the maximum sequence length and $d$ is the model's dimension. The vector at row $i$ is added to the token embedding at position $i$.

In plain English:

- There is a table with one row per possible position (e.g., positions 0 through 2047 for a model with maximum sequence length 2048).
- Each row is a vector of numbers (e.g., 768 numbers for BERT).
- These numbers start random and are updated during training.
- During inference (when the model is used), the vector for position $i$ is simply looked up and added to the token embedding at that position.

---

## How Does it Work? Step by Step

### Step 1: Initialise the Embedding Table

Before training begins, a positional embedding table is created. It has one row per possible position:

```
Position 0:  [0.03, -0.12,  0.87, ...]  ← random initial values
Position 1:  [0.54,  0.22, -0.31, ...]
Position 2:  [-0.09, 0.67,  0.14, ...]
...
Position 2047: [0.41, -0.55, 0.09, ...]
```

These are just random numbers at first.

### Step 2: Each Token Gets Its Positional Embedding

When a sequence is processed, the model looks up the positional embedding for each token's position.

For the sentence "The cat sat":

- "The" is at position 0 → looks up row 0 of the positional embedding table.
- "cat" is at position 1 → looks up row 1.
- "sat" is at position 2 → looks up row 2.

### Step 3: Add to the Word Embedding

The positional embedding is **added** to the word embedding (the vector representing the word's meaning):

```
"cat" at position 1:
  word_embedding   = [0.3, -0.5,  0.8, ...]   ← what "cat" means
  pos_embedding[1] = [0.54, 0.22, -0.31, ...]  ← what position 1 means
  ──────────────────────────────────────────
  combined         = [0.84, -0.28, 0.49, ...]  ← meaning + position
```

### Step 4: The Model Processes the Combined Vectors

The transformer receives the combined vectors and proceeds normally with attention.

### Step 5: Training Adjusts the Embeddings

During training, every time the model makes a mistake, the error signal flows back through the network via [[Gradient Descent|backpropagation]]. This updates:
- The model's weights (as usual).
- **The positional embedding table** — treating it just like any other learned parameter.

Over thousands of training steps, the positional embeddings gradually shift from random noise to useful representations of position.

---

## Worked Example

Let's walk through a concrete example to see the difference between this approach and sinusoidal encoding.

### Setup

Suppose we train a small model on the task: "predict the next word in a sentence."

We use sequences of up to 8 positions. The model's vectors have 4 dimensions each.

### Initial State (Before Training)

The positional embedding table might look like this:

```
Position 0:  [ 0.03, -0.12,  0.87, -0.45]  ← random
Position 1:  [ 0.54,  0.22, -0.31,  0.67]  ← random
Position 2:  [-0.09,  0.67,  0.14, -0.88]  ← random
Position 3:  [ 0.91, -0.33,  0.52,  0.11]  ← random
...
```

These vectors mean nothing yet.

### After Training

After training on millions of sentences, the table might look like this:

```
Position 0:  [ 1.20,  0.05,  0.03, -0.02]  ← learned something about being first
Position 1:  [ 0.85,  0.42, -0.15,  0.08]  ← learned something about being second
Position 2:  [ 0.61,  0.63,  0.11,  0.03]  ← learned something about being third
Position 3:  [ 0.40,  0.75,  0.31, -0.05]  ← ...
...
```

Notice a pattern might emerge: the first dimension might slowly decrease while the second increases, forming a gradient across positions. But the exact pattern is whatever the model found most useful — not what a human designed.

> [!NOTE]
> We cannot interpret what the learned values "mean" in human terms. The model has encoded positional information in a way that works mathematically, but that does not translate into a simple human explanation. This is typical of learned representations in deep learning.

---

## Real-World Applications

Learned positional embeddings are used in:

- **GPT-2** (2019, OpenAI) — maximum 1024 positions, 768-dimensional vectors.
- **GPT-3** (2020, OpenAI) — maximum 2048 positions.
- **BERT** (2018, Google) — maximum 512 positions, 768-dimensional vectors.
- **RoBERTa** (2019, Facebook) — built on BERT, same approach.

The key practical consequence: these models have a **hard maximum sequence length**. GPT-2 cannot process text longer than 1024 tokens. GPT-3 cannot process text longer than 2048 tokens. There is simply no learned embedding for position 2049.

This was one of the main motivations for developing [[RoPE]] and other methods that can generalise beyond the training length.

---

## Analogy

### The House Number Analogy

Imagine you are building a new neighbourhood. You need to assign numbers to every house so that visitors can find them.

**Option A (sinusoidal):** Use a fixed system designed before construction. "Odd numbers on the left, even on the right. Numbers increase as you walk away from the entrance." Simple, logical, works for any neighbourhood.

**Option B (learned):** Let the residents assign their own numbers based on what is most useful to them. Over time, through trial and error (deliveries, guests getting lost, etc.), the numbering system evolves into whatever the neighbourhood finds most practical.

The learned approach might produce a numbering system that is more convenient for that specific neighbourhood — but it also means visitors cannot intuit the system from first principles. They just have to learn it.

> [!TIP]
> Learned positional embeddings can represent position better for specific tasks, but they cannot generalise beyond what they were trained on. If you add houses (positions) beyond the original plan, there are no numbers for them.

---

## Important Terms

**Positional Embedding**
A vector added to each token's representation to tell the model where that token appears in the sequence.

**Learnable Parameter**
Any value in a neural network that is updated during training. Learned positional embeddings are learnable parameters, just like the model's attention weights.

**Embedding Table / Embedding Matrix**
A lookup table where each row is a vector. For positional embeddings, the table has one row per position. For word embeddings, one row per token in the vocabulary. See [[Embedding Matrix]].

**Maximum Sequence Length**
The longest input the model can process. For models using learned positional embeddings, this is fixed at training time. There is no embedding for positions beyond this limit.

**Backpropagation**
The algorithm that calculates how much each parameter (including positional embeddings) needs to change after a training mistake. It flows the error signal backwards through the network.

**Initialisation**
The starting values assigned to parameters before training. Positional embeddings are typically initialised randomly.

**Fine-tuning**
Continuing to train an already-trained model on new data. Positional embeddings can be updated during fine-tuning, which is sometimes used to extend a model's effective sequence length.

---

## Learned vs. Sinusoidal vs. RoPE

| Feature | Learned | Sinusoidal | RoPE |
|---|---|---|---|
| How it is applied | Added to token embeddings | Added to token embeddings | Rotates Q and K inside attention |
| Fixed or learned? | Learned during training | Fixed formula | Fixed formula |
| Extra parameters? | Yes — one vector per position | None | None |
| Handles long sequences? | Poor — hard limit at training length | Reasonably | Well |
| Captures relative positions? | Weakly | Weakly | Directly |
| Interpretable? | No — black box | Partially (frequency-based design) | Partially |
| Used in | GPT-2, GPT-3, BERT | Original Transformer | LLaMA, Mistral, Gemma, Qwen |
| Can exceed training length? | No | Somewhat | Yes (with techniques like YaRN) |

---

## Advantages

**1. Can learn task-specific positional representations.**
The model is not constrained by a human-designed formula. If certain positional patterns are more useful for the training task, the model can learn them.

**2. Seamless integration with training.**
No separate design step is needed. Positional embeddings are just another matrix of parameters that gradient descent optimises.

**3. Empirically competitive.**
In practice, learned positional embeddings perform comparably to sinusoidal encoding on standard benchmarks — and sometimes better on specific tasks.

---

## Disadvantages

**1. Hard maximum sequence length.**
The model can only handle sequences up to the length it was trained on. Position 2049 simply does not exist if training only went to 2048.

**2. Extra parameters.**
For a model with 2048 positions and 768 dimensions, the positional embedding table has $2048 \times 768 = 1{,}572{,}864$ extra parameters. This is small relative to modern LLMs, but it is not zero.

**3. Weak relative position understanding.**
Like sinusoidal encoding, learned embeddings do not explicitly encode relative distances between tokens. "These words are 5 apart" is not directly represented — the model has to infer it from the absolute positional vectors.

**4. Does not generalise to unseen positions.**
A model trained on sequences up to 512 tokens has learned nothing about how to handle position 600. The embedding for position 600 simply does not exist.

---

## Common Mistakes and Misconceptions

> [!WARNING]
> **Misconception: Learned positional embeddings are always better than sinusoidal.**
>
> Not necessarily. On many tasks and benchmarks, the two perform similarly. The advantage of learned embeddings is flexibility; the disadvantage is the hard length limit.

> [!WARNING]
> **Misconception: The model can handle any sequence length as long as it is "smart enough."**
>
> No. With learned positional embeddings, the length limit is absolute. There is no vector for position 2049 if the table only goes up to 2048. The model cannot attend to tokens beyond this limit at all.

> [!WARNING]
> **Misconception: Learned positional embeddings replace word embeddings.**
>
> No. They are separate and additional. The word embedding encodes *what* the token is; the positional embedding encodes *where* it is. Both are added together before the transformer processes the token.

> [!WARNING]
> **Misconception: The learned positional vectors are human-interpretable.**
>
> Generally not. Unlike sinusoidal encodings, which have a clear frequency-based design, learned positional embeddings are just whatever pattern the training process found useful. You cannot look at the numbers and explain what they mean.

> [!WARNING]
> **Misconception: Fine-tuning can easily extend the sequence length.**
>
> It is possible to continue training with longer sequences to extend the effective length, but this requires careful setup and significant computation. It does not work simply by running training for a few more steps.

---

## Key Takeaways

1. **Learned positional embeddings are a lookup table.** One row per position, each row a vector of numbers. Looked up by position index and added to the token embedding.

2. **They start random and become useful through training.** Gradient descent adjusts them just like any other model parameter.

3. **They have a hard maximum sequence length.** The model cannot handle positions it was not trained on. This is the main disadvantage.

4. **They can learn task-specific positional representations.** Unlike fixed formulas, the model decides what is most useful to encode about position.

5. **They add a small number of extra parameters.** Unlike sinusoidal encoding (no parameters), each position needs a full embedding vector to be stored.

6. **They were superseded by RoPE in modern LLMs.** RoPE encodes relative positions directly and generalises to longer sequences, solving the main weakness of learned embeddings.

> [!TIP]
> **One-sentence summary:**
>
> Learned positional embeddings are a trainable lookup table — one vector per position — where the model learns during training what each position should "look like," rather than computing it from a fixed formula.

---

## Related Notes

- [[Positional Embedding]] — the broader category; learned embeddings are one approach
- [[Sinusoidal Positional Encoding]] — the original fixed-formula alternative
- [[RoPE]] — the modern approach that replaced learned embeddings in most LLMs
- [[Transformer]] — the architecture that uses positional embeddings
- [[Embedding Matrix]] — the word embedding table, which works on the same lookup principle
- [[Token]] — what gets a positional embedding added to it
- [[Gradient Descent]] — the algorithm that updates the positional embedding values during training
- [[Attention Mechanism]] — the mechanism that is position-blind without positional embeddings
