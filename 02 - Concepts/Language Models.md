---
tags: [concept, nlp, ai, transformers]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Language Models

## What Is It?

A **language model** is a machine learning model trained to predict the next token in a sequence, given previous tokens.

$$P(\text{next token} \mid \text{previous tokens})$$

It learns to assign probabilities to sequences: which continuations are likely, which are unlikely.

Large language models (LLMs) like GPT, Claude, and LLaMA are transformers trained as language models on massive amounts of text.

---

## Why Does It Exist?

Before neural language models, people used **n-gram models**:

```
If you see "The quick brown ___"
The model has memorized: "fox" appears 90% of the time
So it outputs "fox"
```

These required explicit memorization of common phrases. They didn't generalize.

Neural language models learn **underlying patterns** in language:

- Grammar rules (which words can follow which).
- Semantic relationships (related concepts).
- Factual knowledge (world facts).
- Reasoning patterns (how to think step-by-step).

From a simple objective (predict the next token), they learn remarkably intelligent behavior.

---

## Intuition

Imagine playing a word prediction game:

**Round 1:** "The capital of France is ___"

You naturally predict "Paris"—you've learned the fact.

**Round 2:** "She walked to the store and bought ___"

You predict something reasonable: "groceries," "milk," "bread." You know what stores sell.

**Round 3:** "The theorem states that if X then ___"

You reason through the logic to complete it.

A language model learns all these patterns from examples, the way you do.

---

## How Do They Work?

### Training Objective

Train on massive text corpus:

```
"The quick brown fox jumps over the lazy dog"
```

Create training pairs (using [[Causal Masking|causal masking]]):

```
Pair 1: [The] → quick
Pair 2: [The, quick] → brown
Pair 3: [The, quick, brown] → fox
... (one pair for each position)
```

**Loss:** Compare model's prediction to actual next token.

**Update:** Adjust weights to predict better.

**Repeat:** On billions of examples.

### Why It Works

By predicting the next token billions of times on diverse text:

1. **Grammar** — Model learns syntactic rules (subject-verb agreement, word order).
2. **Semantics** — Model learns meaning (synonyms, antonyms, related concepts).
3. **Facts** — Model learns world knowledge (Paris is in France, E=mc², etc.).
4. **Reasoning** — Model learns to think through problems step-by-step.

All from one simple objective.

---

## Training vs. Generation

### Training (Parallel)

During training, all positions are predicted simultaneously:

```
Input: [The, quick, brown, fox, jumps]

Position 1: predict "quick" from [The]
Position 2: predict "brown" from [The, quick]
Position 3: predict "fox" from [The, quick, brown]
Position 4: predict "jumps" from [The, quick, brown, fox]
Position 5: predict ??? from [The, quick, brown, fox, jumps]

All computed in parallel on GPU.
```

### Generation (Sequential)

At test time, tokens are generated one-by-one:

```
Step 1: Start with prompt [The]
        Model outputs: "quick" (most likely next token)

Step 2: Now have [The, quick]
        Model outputs: "brown"

Step 3: Now have [The, quick, brown]
        Model outputs: "fox"

... (continue until model outputs [END])
```

Each step is slower, but the **logic is identical** to training (thanks to [[Causal Masking|causal masking]]).

---

## Scaling Laws

A remarkable empirical finding: **larger models are better at language modeling.**

```
Model Size | Validation Loss (lower is better)
-----------|-----------------------------------
10M params | 4.5
100M       | 3.2
1B         | 2.1
10B        | 1.4
100B       | 0.9
```

With more parameters and more data, the model learns to predict better.

This improved prediction ability transfers to better reasoning, world knowledge, and task performance.

---

## Connection to Grokking

Grokking experiments use the **same** training paradigm:

**Language Model:**
```
Training pairs: [The, capital, of, France] → [is]
Then: [The, capital, of, France, is] → [Paris]
```

**Grokking Model:**
```
Training pairs: [37, +, 61, =] → [1]  (37+61=98≡1 mod 97)
Then: [22, ×, 14, =] → [63]  (22×14=308≡63 mod 97)
```

**Same objective**, different domain.

Grokking is [[Next-Token Prediction|next-token prediction]] on toy arithmetic. Both are about discovering underlying rules through predicting the next symbol.

---

## Common Misconceptions

### Misconception 1: "LLMs are just pattern matchers."

**Reality:** They learn underlying **rules** and **knowledge**, not just surface patterns. Evidence: they generalize to new combinations of known concepts.

### Misconception 2: "LLMs memorize training data."

**Reality:** They memorize some, but mostly learn generalizable patterns. Evidence: they work on unseen texts.

### Misconception 3: "Language modeling is just statistical trick."

**Reality:** It's a deep learning problem. Larger models learn more sophisticated patterns. It's genuinely hard.

---

## Analogy — Learning a Language

Imagine learning French by reading books, one word at a time:

- You see "Le chat est ___" (the cat is ___).
- You predict the next word.
- You get feedback: "noir" (black) is common.

After reading millions of sentences, you've internalized:
- Grammar rules.
- Vocabulary.
- Cultural knowledge.
- Reasoning patterns.

Not from explicit rules, but from prediction practice.

**Language models learn the same way.**

---

## Important Terms

**Language model** — A model that assigns probabilities to sequences of tokens.

**Next-token prediction** — The training objective: predict the next token given previous ones.

**Perplexity** — A metric measuring language model quality. Lower is better. (Exponentiated cross-entropy loss.)

**Autoregressive** — Generating one token at a time, feeding previous outputs back as input.

**Pre-training** — Training on [[Next-Token Prediction|next-token prediction]] on massive unlabeled text.

**Fine-tuning** — Additional training on specific tasks (e.g., question answering, summarization).

**Prompt** — Initial text given to the model. The model continues from there.

**Beam search** — During generation, keeping multiple candidate sequences and choosing the best.

---

## Common Mistakes

**Mistake 1:** "Language models are trained on labeled data."

**Reality:** They're trained on raw text. No labels needed. It's self-supervised.

**Mistake 2:** "You need billions of parameters to be a language model."

**Reality:** Even small models (millions of params) are language models. Grokking models are language models by this definition.

**Mistake 3:** "Language models can only be applied to language."

**Reality:** The same architecture works on any sequential data: code, protein sequences, time series, modular arithmetic.

---

## Key Takeaways

- **Language models** predict the next token given context.
- Trained via [[Next-Token Prediction|next-token prediction]] on massive text corpora.
- From this simple objective, they learn grammar, knowledge, and reasoning.
- [[Scaling Laws|Scaling laws]] show larger models learn better.
- Grokking is language modeling on toy arithmetic—same principles, different domain.
- The success of language models is a testament to the power of the [[Next-Token Prediction|next-token prediction]] objective.

---

## Related Notes

- [[Transformer]] — the architecture used in modern language models.
- [[Next-Token Prediction]] — the training objective.
- [[Causal Masking]] — enables fair language model training.
- [[Decoder-Only Dominance]] — why decoder-only transformers became standard for language modeling.
- [[Mechanistic Interpretability]] — understanding what language models learn.
