---
tags: [concept, architecture, transformer, foundations]
---
↑ Parent: [[00 - Start Here]] · Related: [[Transformer]]

# Attention Mechanism

## What Is It?

The **attention mechanism** is the key computational idea inside a transformer — the type of neural network used in grokking experiments and modern AI systems like ChatGPT.

In plain terms: attention lets every position in a sequence look at every other position and decide how much to pay attention to each one.

---

## Why Does It Exist?

Before attention, neural networks processed sequences step-by-step. Each step only had access to the immediately previous step. To understand a word far back in a sentence, information had to be passed through many intermediate steps, often losing accuracy along the way.

Attention solved this by letting every position look directly at every other position simultaneously — skipping the chain of intermediate steps entirely.

**A concrete example:**

Consider: *"The animal did not cross the street because it was too tired."*

To understand what "it" refers to, you need to look at "animal" (not "street"). With attention, the word "it" can directly examine "animal" and "street" simultaneously and figure out which is more relevant. Without attention, this information would have to be passed through many intermediate words, often getting distorted.

---

## The Core Idea: Query, Key, Value

The attention mechanism uses three concepts, best understood as an analogy:

Think of a **library system**:
- **Query (Q):** What you are looking for. "I need books about Italian cooking."
- **Key (K):** The label on each book. "Italian recipes," "French cooking," "Mathematics."
- **Value (V):** The actual content of each book.

The attention mechanism:
1. Compares your query to every key (how well does each book match what I want?)
2. Assigns a weight to each book based on how well it matches (books about Italian cooking get high weights)
3. Returns a weighted combination of the book contents (you get mostly Italian cooking content, with a little French cooking mixed in if it was somewhat relevant)

In a neural network:
- Every position in the input sequence generates a query, key, and value.
- The attention computes how much each query matches each key.
- It then returns a weighted combination of the values, where the weights reflect the query-key matches.

---

## How It Works: Step by Step

**Input:** A sequence of items (numbers in grokking; words in language models). Each item is represented as a list of numbers (a vector).

**Step 1 — Create queries, keys, and values:**
Three different sets of learned weights are applied to each position to produce three vectors: a query, a key, and a value. These weights are learned during training.

**Step 2 — Compute match scores:**
For each position, compute how well its query matches every other position's key. A simple dot product (multiply the numbers element-by-element and sum them up) measures this similarity.

**Step 3 — Scale and convert to weights:**
The match scores are scaled down (to avoid extremely large values) and then converted to weights that sum to 1 using a function called **softmax**. Think of softmax as converting scores into percentages.

**Step 4 — Combine the values:**
Each value vector is multiplied by its corresponding weight, and all the weighted values are summed together. The result is the attention output for that position — a combination of information from all other positions, weighted by relevance.

**Step 5 — Repeat for all positions:**
Steps 1-4 happen simultaneously for every position in the sequence. Every position attends to every other position at the same time.

---

## Multi-Head Attention

In practice, attention is run in **parallel groups** called "heads."

Each head uses a different set of learned weights, so each head learns to look for different kinds of patterns:
- One head might look at syntactic relationships
- Another might focus on semantic meaning
- Another might track long-range dependencies

The outputs of all heads are combined to give a richer representation.

In the small grokking transformer, there are typically 4 heads. Large language models have many more (GPT-3 has 96 heads).

---

## Causal Masking: Preventing Future Peeking

In grokking experiments (and in language models that generate text), the model must make predictions using only the current and past positions — not future ones.

For example, when predicting the answer to "37 + 61 = ?", the model should only use "37", "+", and "61" — not peek at the answer.

This is enforced by **causal masking**: setting the match scores for future positions to negative infinity before converting them to weights. After the conversion, future positions receive zero weight — effectively invisible.

This masking happens in a specific triangular pattern:
- Position 1 can only see position 1
- Position 2 can see positions 1 and 2
- Position 3 can see positions 1, 2, and 3
- And so on

---

## How Attention Relates to Grokking

When a transformer groks the clock-math task (addition mod 97), researchers reverse-engineered what the attention heads are doing.

They found that the attention heads implement a specific, elegant algorithm:
- The embedding layer encodes each input number as a rotation angle on a circle
- The attention heads compute products of these angles that implement a mathematical addition-of-rotations formula
- The result is then read off to give the correct answer

This "Fourier circuit" (based on wave mathematics) is the specific algorithm the grokked network learns. Understanding attention is essential to understanding what this circuit is and how it works.

---

## Special Types of Attention Heads

Research in mechanistic interpretability has found that attention heads often specialise into specific roles:

**Induction Heads:**
These head pairs detect and complete repeated patterns. If the sequence "...A B ... A..." has appeared, when the model sees "A" again, an induction head predicts "B" will follow. These heads are thought to be crucial for in-context learning — where the model figures out a pattern from a few examples in the context window.

**Previous-Token Heads:**
These heads almost exclusively look at the immediately preceding position. They provide nearby context.

**Copying Heads:**
These heads copy information from one position to another without modification.

Understanding these specialised roles helps researchers understand what computational functions are being performed at each layer.

---

## Important Terms

**Attention mechanism:** The computation inside a transformer that lets each position look at and gather information from all other positions simultaneously.

**Query (Q):** What a position is "looking for." Generated by applying learned weights to the position's representation.

**Key (K):** What each position "offers" for matching. Generated by applying learned weights to the position's representation.

**Value (V):** The actual information a position contributes when attended to. Generated by applying learned weights to the position's representation.

**Dot product:** A way to measure similarity between two lists of numbers (vectors). Multiply corresponding elements and sum the results.

**Softmax:** A function that converts a list of numbers into a list of weights that sum to 1. Used to convert match scores into attention weights.

**Multi-head attention:** Running multiple attention computations in parallel, each learning different patterns. The results are combined.

**Causal masking:** Preventing each position from attending to future positions. Used in language models and grokking experiments to ensure predictions are made only from past context.

**Induction heads:** Attention head pairs that detect and complete repeated patterns. Important for in-context learning.

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "Attention tells the model what to focus on."
> More precisely: attention determines how information from different positions is combined. Every position's output is a weighted mixture of all positions' values — not just the "focused" one. High attention weight means more of that position's value is included in the output.

> [!TIP]
> Think of attention less like a spotlight (focus on one thing) and more like a mixing board (adjusting how much of each instrument you hear in the final output).

---

## Key Takeaways

- Attention lets every position in a sequence look at and gather information from every other position simultaneously.
- It uses queries, keys, and values — a library-search analogy where you match what you're looking for against what's available.
- Multi-head attention runs multiple parallel attention computations, each learning different patterns.
- Causal masking prevents future peeking, enabling autoregressive generation.
- In the grokked clock-math network, attention heads implement a specific rotation-based algorithm.
- Specialised head types (induction, previous-token, copying) emerge during training.

---

## Related Notes
- [[Transformer]] · [[Fourier Features]] · [[Heavy-Tailed Self-Regularization]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
- [[Circuit Formation]] · [[Mechanistic Interpretability]]
- [[Self-Attention]]
