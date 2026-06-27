---
tags: [concept, architecture, transformer, foundations, attention, beginner]
---
↑ Parent: [[00 - Start Here]] · Deep dive: [[Self-Attention]] · Related: [[Attention Mechanism]] · [[Transformer]]

# Self-Attention Mechanisms in Neural Networks

> [!NOTE]
> This note is a beginner-friendly introduction. For the full technical detail — including the math, causal masking, multi-head attention, and the grokking circuit — see [[Self-Attention]].

---

## What Is It?

**Self-attention** is a way for a neural network to figure out which parts of its input are most relevant to each other — all at the same time, in a single step.

The word "self" is the key part. The network is not comparing two separate things. It is looking at **one sequence** and asking every part of that sequence: *"Which other parts of this same sequence should I pay attention to?"*

---

## Why Does It Exist?

Before self-attention, neural networks processed text by reading it **one word at a time**, left to right. This created a big problem: by the time the network reached the end of a long sentence, it had often "forgotten" what was at the beginning.

Self-attention solves this by letting **every word look at every other word simultaneously**. There is no forgetting, because no information is ever left behind.

> [!TIP]
> Think of it like reading a sentence and being able to instantly draw a line between any two words that are related — no matter how far apart they are.

---

## How Does It Work?

Here is the process in plain English, step by step.

**Step 1 — Every word asks a question.**
Each word in the sequence generates a *query*: a kind of question that says "what am I looking for?" For example, the word "it" might ask: "which earlier noun am I referring to?"

**Step 2 — Every word puts up an answer.**
At the same time, every word also generates a *key*: a description of what it contains. "The cat" might say: "I contain a noun, a living creature."

**Step 3 — Match questions to answers.**
The network compares every query against every key. When a question and an answer match well (high similarity), that pair gets a high score.

**Step 4 — Collect the information.**
Each word then collects information from the words it matched with, weighted by how strong the match was. A word that matched perfectly contributes a lot. A word that matched poorly contributes almost nothing.

**Step 5 — Update every word's meaning.**
Each word now has a new, richer representation — one that has been updated by the context of the whole sequence.

This entire process happens for every word, simultaneously, in a single pass.

---

## Simple Example

Consider the sentence:

> *"The animal didn't cross the street because it was too tired."*

The word **"it"** is ambiguous. Does "it" refer to the animal or the street?

A human knows instantly: the animal is tired, not the street. But the network needs to figure this out from the data.

With self-attention, the word "it" can look at every other word in the sentence at once. It finds that "animal" is the best match — animals get tired, streets do not. So "it" pays heavy attention to "animal" and updates its own meaning accordingly.

Without self-attention, the network would have had to somehow remember "animal" from many steps ago. Self-attention makes the connection directly and immediately.

---

## Analogy

Imagine you are in a room full of people, and everyone is trying to find the other people most relevant to them.

- Each person wears a badge describing **what they are looking for** (their *query*).
- Each person also wears a badge describing **what they know** (their *key*).
- People scan each other's "what I know" badges and compare them to their own "what I am looking for" badge.
- Whoever matches best, you walk over and listen carefully. The closer the match, the more weight you give their words.

In the end, everyone has updated their own understanding based on the most relevant conversations in the room — all happening at the same time.

That is self-attention.

---

## Important Terms

**Query**
A vector (list of numbers) representing what a word is "looking for" in the sequence. Think of it as a question.

**Key**
A vector representing what a word "contains" or "offers." Think of it as a label describing what this word can answer.

**Value**
The actual information a word passes on when it gets attended to. The key says "here is what I am about"; the value says "here is what I actually give you."

**Attention weight**
A number between 0 and 1 that says how much one word should attend to another. High weight = strong match. The weights for each word always sum to 1 across the whole sequence.

**Attention score**
The raw similarity between a query and a key, before being converted into a weight. Computed as a dot product.

**Softmax**
A mathematical function that converts raw scores into probabilities that sum to 1. Applied to attention scores to produce attention weights.

**Context vector**
The new, updated representation of a word after it has gathered information from the rest of the sequence. It carries the meaning of the word in context.

**Dot product**
A simple way to measure how similar two vectors are. When two vectors point in similar directions, their dot product is large. When unrelated, it is near zero.

> [!NOTE]
> You do not need to understand the mathematics to grasp the idea. The core intuition is: *similarity between query and key determines how much one word pays attention to another.*

---

## Bidirectional vs. One-Directional Self-Attention

There are two flavours of self-attention, used in different types of models.

**Bidirectional self-attention** lets every word look at every other word — both left and right. This gives richer understanding because you can use the full context. BERT uses this approach. The downside: you cannot use bidirectional attention to *generate* text, because generating word 5 would require looking at words 6, 7, 8... which do not yet exist.

**Causal (one-directional) self-attention** lets each word only look at itself and the words that came before — never words ahead. This is what GPT, Claude, and LLaMA use. It makes text generation possible: when generating word 5, you only use words 1–4, which are already known.

> [!TIP]
> Bidirectional = better at understanding. Causal = necessary for generating. Both use the same self-attention mechanism — the only difference is which connections are allowed.

---

## Why Multiple Attention Heads?

A single self-attention layer can only learn one type of relationship at a time. Real language has many: who did what to whom (grammar), what refers to what (coreference), which words are similar in meaning (semantics), and more.

**Multi-head attention** runs self-attention several times in parallel — each time with different learned projections. Each "head" specialises in a different type of relationship. The results from all heads are combined at the end.

Think of it like asking several different experts to read the same sentence, each focused on a different question, then pooling all their observations.

---

## Connection to Grokking

In grokking experiments, the network is trained to solve modular arithmetic — for example, computing $(37 + 61) \bmod 97$.

The input looks like: `[37, +, 61, =]`

The `=` token needs to look back at `37` and `61` and compute their interaction. Self-attention is exactly the mechanism that lets `=` attend to both numbers simultaneously.

When the network first trains, this attention pattern is noisy — it is effectively memorising lookup tables. After grokking, the attention heads have converged on a clean, structured pattern that implements a real mathematical algorithm. The mechanism did not change — but what the heads *learned to pay attention to* did.

> [!TIP]
> Grokking, at a mechanistic level, is the story of self-attention weights reorganising from a messy lookup table into a clean, general algorithm.

---

## Key Takeaways

- Self-attention lets every part of a sequence attend to every other part, all at once.
- It solves the "forgetting" problem of older sequential models by making all connections direct.
- Every word generates a query (what it needs), a key (what it offers), and a value (what it gives).
- Similarity between query and key determines the attention weight.
- Bidirectional attention uses full context (understanding); causal attention is left-to-right only (generation).
- Multi-head attention runs self-attention in parallel multiple times so different relationship types can be learned simultaneously.
- In grokking, self-attention is the mechanism through which the model learns the algorithmic structure of the task.

> [!WARNING]
> A common misconception: self-attention has no built-in sense of word order. "Cat chased dog" and "dog chased cat" contain the same words, and self-attention alone cannot tell them apart. **Positional encodings** are added to each word before self-attention begins, to inject information about position in the sequence.

---

## Related Notes

- [[Self-Attention]] — full technical deep-dive with mathematics, QKV projections, causal masking, and the grokking circuit
- [[Attention Mechanism]] — the broader family of attention mechanisms
- [[Transformer]] — the architecture built around self-attention
- [[Masked Language Modelling]] — uses bidirectional self-attention (BERT)
- [[Decoder-Only Dominance]] — uses causal self-attention (GPT, Claude, LLaMA)
- [[Circuit Formation]] — how attention heads in grokking form interpretable circuits
- [[Fourier Features]] — the specific pattern attention heads learn in the grokked modular arithmetic circuit
- [[Positional Embedding]] — how word order is injected into a self-attention model
