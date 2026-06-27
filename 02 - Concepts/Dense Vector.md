---
tags: [concept, foundations, embeddings, representations]
---
↑ Parent: [[Transformer]] · Related: [[Embedding Matrix]] · [[Representation Learning]]

# Dense Vector

## What is it?

A **dense vector** is a list of numbers where **every slot contains a meaningful value**.

It is just a row of numbers, like this:

```
[0.32, -0.71, 0.14, 0.89, -0.45, 0.02, 0.66, -0.23]
```

That list of 8 numbers is a dense vector of size 8. In machine learning, this list represents something — a word, a token, an image patch, or any other piece of information.

## Why does it exist?

Computers cannot work directly with words like "cat" or "king." They can only do maths with numbers.

So the challenge is: **how do you turn a word into something a computer can calculate with?**

The naive approach would be to give every word a single unique number — like "cat = 1," "dog = 2," "king = 3." But that has a big problem: it implies "dog" is somehow in between "cat" and "king," which is nonsense.

A better approach is to give every word a **whole list of numbers** — a vector — where the numbers together capture meaning, relationships, and similarities. That is exactly what a dense vector does.

> [!NOTE]
> The word "dense" just means that nearly all values in the vector are non-zero and carry information. This is the opposite of a "sparse" vector, where most values are zero (like a one-hot encoding).

## How does it work?

A dense vector is learned during training. The model starts with random numbers in each slot. Over millions of training steps, it adjusts those numbers so that **similar things end up with similar vectors**.

Think of it as placing objects in a coordinate space. After training:
- "cat" and "dog" might end up near each other (both are pets).
- "king" and "queen" might end up near each other (both are royalty).
- "cat" and "king" would be far apart.

The distance and direction between vectors encodes real-world meaning.

## Simple Example

Suppose you represent three words with 3-dimensional dense vectors (real models use hundreds of dimensions):

| Word  | Vector              |
|-------|---------------------|
| cat   | [0.9, 0.1, 0.2]    |
| dog   | [0.8, 0.2, 0.1]    |
| king  | [0.1, 0.9, 0.7]    |

You can see that "cat" and "dog" have similar-looking vectors (both high in position 1, low elsewhere). "King" is clearly different. The model has learned that cats and dogs are more alike than a cat and a king.

## Analogy

Think of a person described by their characteristics:

```
Height: 5'9"    Friendliness: 8/10    Speed: 6/10    Intelligence: 9/10
```

That person is a "dense vector" of four values. Another person with similar characteristics would have a similar vector. You can measure how similar two people are by comparing their vectors. Words and tokens work the same way — the vector is just a description encoded in numbers.

## Important Terms

- **Vector**: A list of numbers arranged in a specific order.
- **Dimension**: How many numbers are in the list. GPT-2 uses 768-dimensional vectors. LLaMA uses 4096-dimensional vectors.
- **Dense**: Every slot holds a meaningful, non-zero value. (Opposite of sparse.)
- **Sparse vector**: A vector where most values are zero. Example: a one-hot encoding where only one slot is 1 and everything else is 0.
- **Embedding**: The process (or result) of converting a token into a dense vector. See [[Embedding Matrix]].

## Dense vs Sparse: Side by Side

| Property         | Sparse (one-hot)         | Dense vector             |
|------------------|--------------------------|--------------------------|
| Size             | Vocabulary size (50,000+)| Small (128–4096)         |
| Most values      | Zero                     | Non-zero                 |
| Captures meaning | No                       | Yes                      |
| Can compute distances | Meaningless         | Meaningful               |

## Key Takeaways

- A dense vector is a list of numbers that represents something (a token, a word, a concept).
- Every value in the list carries information — nothing is wasted.
- Similar things end up with similar vectors after training.
- Dense vectors make it possible to do maths with language.
- The numbers are not hand-crafted — they are **learned automatically** from data.

> [!TIP]
> Dense vectors are sometimes called **embeddings**. When people say "the model creates embeddings," they mean it converts tokens into dense vectors.

---
## Related Notes
- [[Embedding Matrix]] — the lookup table that stores a dense vector for every token
- [[Positional Embedding]] — a dense vector added to encode *where* in the sequence a token sits
- [[Representation Learning]] — the broader field of learning useful vector representations
- [[Transformer]] — the architecture that uses dense vectors as its input format
- [[Fourier Features]] — in grokking, dense vectors encode numbers as rotation angles
