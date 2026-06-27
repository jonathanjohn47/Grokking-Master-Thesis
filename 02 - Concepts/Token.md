---
tags: [concept, foundations, nlp, transformer, beginner]
---
↑ Parent: [[Transformer]] · Related: [[Embedding Matrix]] · [[Attention Mechanism]] · [[Positional Embedding]]

# Token

## What is it?

A **token** is the smallest piece of text that a language model processes.

When you type a sentence into a language model, the model does not read it letter by letter, and it does not always read it word by word either. Instead, it breaks the text into **tokens** first — small chunks — and then processes each token one at a time.

> [!NOTE]
> Think of a token as the model's "unit of reading." Just like you might read a book word by word, a language model reads text token by token.

---

## Why does it exist?

### The Problem: Computers Cannot Read Raw Text

A language model is a mathematical system. It works with **numbers**, not letters or words.

So the first challenge is: **how do we convert human language into numbers?**

You might think: "Just assign a number to each letter." That could work, but it creates problems:

- There are only 26 letters in English, but the model would need to learn that "c", "a", "t" together mean *cat*. This requires a lot of extra computation.
- Different languages have very different character sets (Arabic, Chinese, Japanese, etc.).

Another option: "Assign a number to each word." This is closer, but also has problems:

- There are hundreds of thousands of words in English. Giving each one a number creates a huge list (called a vocabulary) that is difficult to work with.
- New words, names, and technical terms would be completely unknown to the model.
- Different forms of the same word ("run", "running", "ran") would be treated as totally unrelated.

### The Solution: Tokens

**Tokens** are a middle ground between letters and words.

A token is typically a **common word or a piece of a word**. The tokeniser (the system that creates tokens) learns which combinations of letters appear together most often, and treats those as single units.

This means:
- Common short words ("the", "is", "a") each become one token.
- Long or rare words get split into smaller pieces ("unbelievable" → "un", "believ", "able").
- Numbers, punctuation, and special characters get their own tokens too.

> [!TIP]
> Tokens allow the model to handle any text — including words it has never seen before — by breaking unknown words into familiar pieces.

---

## Intuition First

### The Lego Brick Analogy

Think of tokens like **Lego bricks**.

A Lego set has a fixed collection of brick shapes. You can build almost anything by combining those bricks — even shapes that the designers never planned for.

Tokens work the same way. The model has a fixed vocabulary of tokens (typically 30,000 to 100,000 tokens). Any text — no matter how unusual — can be built from combinations of these tokens.

A word the model has never seen before can be assembled from familiar token pieces:

```
"ChatGPT" → ["Chat", "G", "PT"]
"tokenization" → ["token", "ization"]
"Schwarzenegger" → ["Schwar", "zen", "egger"]
```

### What Does a Token Look Like?

Here is a concrete example. Take the sentence:

```
The quick brown fox jumps.
```

A typical tokeniser might split this into:

```
["The", " quick", " brown", " fox", " jumps", "."]
```

That is 6 tokens. Notice:
- Spaces are often included at the start of tokens (not at the end).
- Punctuation becomes its own token.
- Common short words stay as single tokens.

A more complex sentence like:

```
The transformer architecture uses self-attention.
```

Might become:

```
["The", " transformer", " architecture", " uses", " self", "-", "attention", "."]
```

Here, "self-attention" was split into three tokens because the hyphenated compound word is less common.

---

## Formal Definition

> A **token** is a discrete unit from a fixed vocabulary that a language model uses as input. Every piece of text is converted into a sequence of tokens before the model processes it.

The fixed list of all possible tokens is called the **vocabulary**. The process of converting text into tokens is called **tokenisation**.

Each token is assigned a unique integer (a whole number):
- Token "the" might be assigned number 464.
- Token "cat" might be assigned number 8227.
- Token "." might be assigned number 13.

These numbers are what the model actually receives as input. It then looks up each number in its [[Embedding Matrix]] to get a vector (a list of numbers) that it can compute with.

---

## How Does it Work? Step by Step

Here is the full journey from raw text to what the model processes.

### Step 1: Raw Text Arrives

The user types or submits some text. For example:

```
"Cats are great pets."
```

### Step 2: Tokenisation

The text is split into tokens by a **tokeniser**. The tokeniser is a separate program that runs before the model.

The most common tokenisation method used in modern LLMs is called **Byte-Pair Encoding (BPE)**. Here is how it works at a high level:

1. Start with every individual character as its own token.
2. Find the pair of tokens that appears most often in the training data.
3. Merge that pair into a single new token.
4. Repeat steps 2–3 many thousands of times.

The result is a vocabulary of tokens that reflects the most common patterns in the language.

After tokenisation, our sentence becomes:

```
["Cats", " are", " great", " pets", "."]
```

### Step 3: Convert to Token IDs

Each token is converted to its integer ID (its number in the vocabulary):

```
["Cats", " are", " great", " pets", "."]
   →
[  9524,   389,   1049,  13926,   13 ]
```

(These are approximate numbers for illustration — the real IDs depend on the specific tokeniser.)

### Step 4: Look Up Embeddings

Each token ID is used to look up a **dense vector** in the [[Embedding Matrix]]. This vector is a list of hundreds or thousands of numbers that encodes the meaning of the token.

```
9524 → [0.3, -0.5, 0.8, 0.1, ..., 0.2]   ← "Cats" vector (512 numbers)
 389 → [0.1,  0.9, 0.2, 0.7, ..., 0.4]   ← "are" vector
...
```

### Step 5: Add Positional Encoding

Because the transformer cannot tell word order by itself, a [[Positional Embedding]] is added to each token's vector. This tells the model which position in the sequence each token occupies.

### Step 6: The Transformer Processes the Tokens

The transformer now processes these vectors using the [[Attention Mechanism]]. It produces an output vector for each token, which is eventually used to generate the next token or to produce some other output.

---

## Worked Example

Let's trace the word "unbelievable" through tokenisation.

### Input

```
"unbelievable"
```

### Tokenisation

This word is uncommon enough that the tokeniser splits it:

```
["un", "believ", "able"]
```

Three tokens, not one.

### Token IDs (approximate)

```
"un"      →  555
"believ"  → 4231
"able"    →   70
```

### Embeddings

Each ID is looked up in the embedding matrix:

```
555  → [0.2, -0.3,  0.7, ...]
4231 → [0.5,  0.8, -0.1, ...]
70   → [0.1,  0.3,  0.4, ...]
```

### Positional Encoding

Assuming "un" is at position 0, "believ" at position 1, and "able" at position 2, positional information is added to each vector.

### What the Model Sees

Three separate vectors — one per token — each blending meaning and position. The model processes all three and can attend across them using self-attention.

> [!TIP]
> Even though the three tokens came from one word, the model can learn to treat them as a group. Through the attention mechanism, "un" can attend to "believ" and "able" and build up a joint representation of the full word.

---

## Real-World Applications

Tokens are fundamental to every modern language model. Here are some practical implications:

**Token counts matter for cost and speed.**
Most APIs for language models (like the Claude API or OpenAI API) charge per token. A typical English word is roughly 1.3 tokens on average. A page of text is roughly 500–750 tokens.

**Context length is measured in tokens.**
When you hear "this model supports 100,000 tokens of context," it means the model can process a sequence up to 100,000 tokens long at once. That is roughly 75,000 English words, or about 300 pages.

**Code and non-English text tokenise differently.**
Code often has more tokens per "word" because identifiers, punctuation, and symbols each become separate tokens. Languages with non-Latin scripts (Chinese, Japanese, Arabic) also tend to use more tokens per character than English.

**Example token counts:**

| Text | Approximate Token Count |
|---|---|
| "Hello, world!" | 4 tokens |
| One average English sentence | 15–20 tokens |
| One page of English text | 500–750 tokens |
| A short story (5,000 words) | ~6,500 tokens |
| A novel (80,000 words) | ~104,000 tokens |

---

## Analogy

### The Syllable Analogy

When children learn to read, they often first learn **syllables** — the sound chunks that make up words. "Un-be-liev-a-ble" has five syllables.

Syllables are a middle ground between individual letters (too small to carry meaning) and whole words (too many to learn from scratch).

Tokens are the machine learning equivalent of syllables. They are:
- Larger than individual characters (so they carry meaning).
- Smaller than whole words (so they handle any word, even unknown ones).
- Countable in a fixed set (so the model has a manageable vocabulary).

> [!TIP]
> Just as a child can sound out any word they've never seen before by breaking it into familiar syllables, a language model can process any word it's never seen before by breaking it into familiar tokens.

---

## Important Terms

**Token**
The smallest unit of text that a language model processes. Can be a whole word, part of a word, a punctuation mark, or a special symbol.

**Vocabulary**
The complete set of all tokens the model knows. Typically contains 30,000 to 100,000 tokens for modern LLMs.

**Tokeniser**
The program that converts raw text into a sequence of tokens. Runs before the model sees the text.

**Token ID**
The unique integer assigned to each token. The model receives token IDs as input, not the text itself.

**Byte-Pair Encoding (BPE)**
The most common tokenisation algorithm. It builds a vocabulary by iteratively merging the most frequent pairs of characters or token pieces.

**Context Length (Context Window)**
The maximum number of tokens a model can process at once. Everything beyond this limit is not seen by the model.

**Embedding**
A vector (list of numbers) that represents a token. Looked up in the [[Embedding Matrix]] using the token ID.

**Special Tokens**
Extra tokens added by the tokeniser for structural purposes. Examples: `<BOS>` (beginning of sequence), `<EOS>` (end of sequence), `<PAD>` (padding), `<SEP>` (separator). The model is trained to recognise and respond to these.

---

## Common Mistakes and Misconceptions

> [!WARNING]
> **Misconception: A token is always a whole word.**
>
> Not true. A token can be a whole word, part of a word, a punctuation mark, a number, a space, or even a single character. The tokeniser decides how to split text based on what is most common in the training data.

> [!WARNING]
> **Misconception: The model reads letters.**
>
> The model never sees individual letters unless a letter happens to be a token by itself. It processes tokens, not characters.

> [!WARNING]
> **Misconception: Every language uses the same tokens.**
>
> No. Different models are trained with different tokenisers. A model trained mostly on English text will tokenise English efficiently (common English words become single tokens) but may tokenise other languages less efficiently (splitting words into many small pieces). Multilingual models are trained on text from many languages to avoid this.

> [!WARNING]
> **Misconception: "1000 words" and "1000 tokens" are the same thing.**
>
> They are not. On average, English text has about 1.3 tokens per word. So 1000 words ≈ 1300 tokens. For code or non-English languages, the ratio can be much higher.

> [!WARNING]
> **Misconception: The model "understands" tokens the way humans understand words.**
>
> The model processes tokens as vectors of numbers. It learns statistical relationships between tokens from training data. This is different from the way a human consciously understands the meaning of a word, though the model's behaviour often reflects something like understanding.

---

## Key Takeaways

1. **A token is the model's unit of reading.** Everything the model processes is broken into tokens first.

2. **Tokens are a middle ground between letters and words.** Common words are one token; rare or long words are split into multiple tokens.

3. **Every token gets a unique ID and a vector.** The ID is looked up in the embedding matrix to retrieve the vector, which is what the model actually computes with.

4. **Tokenisation happens before the model.** The tokeniser is a separate step. The model never sees raw text.

5. **Context length is measured in tokens, not words.** When a model supports 128,000 tokens of context, that is roughly 100,000 words.

6. **Different tokenisers produce different tokens.** GPT models, Claude, LLaMA, and others each use different tokenisers and therefore different vocabularies.

> [!TIP]
> **One-sentence summary:**
>
> A token is the small chunk of text — usually a word or part of a word — that a language model treats as its basic unit of input, converting it into a number and then into a vector before any processing begins.

---

## Related Notes

- [[Embedding Matrix]] — the lookup table that converts each token ID into a vector
- [[Positional Embedding]] — the position information added to each token's vector
- [[Attention Mechanism]] — the mechanism that processes token vectors
- [[Transformer]] — the architecture that processes sequences of tokens
- [[Self-Attention]] — how tokens attend to each other
- [[RoPE]] — how position is added to tokens in modern LLMs
- [[Sinusoidal Positional Encoding]] — the original method for adding position to token vectors
