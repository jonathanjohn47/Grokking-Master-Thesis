---
tags: [concept, foundations, positional-encoding, transformer, embeddings]
---
↑ Parent: [[Positional Embedding]] · Related: [[Transformer]] · [[Attention Mechanism]] · [[RoPE]]

# Sinusoidal Positional Encoding

## What is it?

**Sinusoidal Positional Encoding** is a method for telling a transformer model the position of each word in a sentence.

It does this by creating a unique list of numbers for each position using **sine and cosine waves** — a type of repeating mathematical pattern.

These numbers are then added to each word's representation before the transformer processes it.

> [!NOTE]
> Sinusoidal Positional Encoding was introduced in the original Transformer paper: "Attention Is All You Need" by Vaswani et al. (2017). It was the very first positional encoding method used in transformers and is historically important.

---

## Why does it exist?

### The Problem: Transformers Don't Know Word Order

A [[Transformer]] uses a mechanism called [[Attention Mechanism|attention]] to process text. Attention lets every word look at every other word in the sentence simultaneously.

But here is the critical problem:

> **Attention has no built-in sense of order.**

If you give a transformer the sentence:

```
The cat sat on the mat.
```

And then rearranged it to:

```
Mat sat the on cat the.
```

Without positional information, the transformer processes **both sentences identically**. It cannot tell the difference.

This is a serious problem. Word order completely changes meaning. "Dog bites man" and "Man bites dog" contain the same words, but mean entirely different things.

### The Solution: Add Position Information

The fix is simple in principle:

> Before processing, add some information to each word that tells the model its position in the sequence.

The challenge is: **how do you encode position in a way that is useful for a neural network?**

Sinusoidal Positional Encoding was the original answer to this question.

---

## Intuition First

Before looking at any formulas, let's build the right mental picture.

### The Radio Wave Analogy

Think about radio stations. Each station broadcasts at a different **frequency** — how many times the wave goes up and down per second.

- Station A broadcasts at 100 MHz (very fast waves).
- Station B broadcasts at 88 MHz (slightly slower waves).
- Station C broadcasts at 101.5 MHz (slightly faster than A).

Every station is different. No two stations are the same frequency. Your radio can tune into exactly the right one.

**Sinusoidal Positional Encoding works similarly.** Each dimension of the positional vector uses a different frequency. Together, all the frequencies create a unique "fingerprint" for every position.

- Position 1 has one pattern.
- Position 2 has a slightly different pattern.
- Position 100 has a completely different pattern.
- No two positions have the same pattern.

> [!TIP]
> The key idea is that **each position gets a unique vector**. The transformer can use this vector to know exactly where each word is.

### The Ruler Analogy

Imagine a ruler with markings at every centimetre. Each mark is unique — you can always tell whether you are at the 5 cm mark or the 23 cm mark.

But a sinusoidal encoding is more like a ruler with **multiple overlapping patterns** — one pattern repeating every 2 cm, another repeating every 10 cm, another every 100 cm, and so on. By combining all these patterns, you can pinpoint any position precisely.

This is exactly how sine and cosine waves at different frequencies work together to encode position.

---

## Background: What is a Sine Wave?

> [!NOTE]
> If you already know what sine and cosine are, skip this section.

A **sine wave** is a smooth, repeating curve. It goes up, comes back down, goes below zero, comes back up, and repeats forever.

```
  1 |    ╭──╮           ╭──╮
    |   ╱    ╲         ╱    ╲
  0 |──╱──────╲───────╱──────╲───
    |          ╲     ╱        ╲
 -1 |           ╰──╯            ╰──
    └──────────────────────────────→
       Position
```

The key property: **the value of a sine wave at any position is a number between -1 and +1.**

A **cosine wave** is the same shape, but shifted slightly — it starts at 1 instead of 0:

```
  1 |╮           ╭──╮
    | ╲         ╱    ╲         ╱
  0 |──╲───────╱──────╲───────╱──
    |   ╲     ╱        ╲     ╱
 -1 |    ╰──╯            ╰──╯
    └──────────────────────────────→
       Position
```

The **frequency** of a wave controls how quickly it repeats:
- High frequency → the wave repeats many times in a short space.
- Low frequency → the wave repeats slowly, with long stretches between peaks.

```
High frequency (repeats fast):
  1 |╮ ╭╮ ╭╮ ╭╮ ╭╮ ╭
    | ╰╯ ╰╯ ╰╯ ╰╯ ╰╯
 -1 |

Low frequency (repeats slowly):
  1 |╭──────╮
    |╯      ╰──────╮
 -1 |               ╰────
```

> [!TIP]
> You don't need to memorise the math of sine and cosine. Just remember: they produce smooth, repeating patterns between -1 and +1, and different frequencies give different patterns.

---

## Formal Definition

Here is the formula. Don't worry if it looks scary — we will break it down piece by piece right below it.

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

This just means: **go through each pair of dimensions, and fill one with sine and one with cosine.**

---

### Breaking Down the Formula — One Piece at a Time

**What is $pos$?**

$pos$ is simply the position of the word in the sentence. The first word is position 0, the second is position 1, the third is position 2, and so on.

**What is $i$?**

$i$ is which pair of dimensions we are filling. The positional vector has many dimensions. We fill them two at a time — one with sine, one with cosine. The first pair is $i = 0$, the second pair is $i = 1$, and so on.

**What is $d_{model}$?**

$d_{model}$ is the total number of dimensions in the model. Typical value: 512. This controls how many pairs of dimensions there are.

**What is $10000^{2i/d_{model}}$?**

This is the most confusing part. Let's simplify it.

It is just a number that gets **bigger and bigger** as $i$ increases.

- When $i = 0$: the value is $10000^0 = 1$ (very small denominator)
- When $i = 1$: the value is larger
- When $i$ is large: the value becomes very large

**Why does this matter?**

Because we divide $pos$ by this number to get an angle. A bigger denominator gives a smaller angle. A smaller angle means the sine/cosine wave moves more slowly.

> [!TIP]
> Think of it this way:
> - **Early dimensions** ($i$ is small) → small denominator → big angle → wave moves **fast**
> - **Later dimensions** ($i$ is large) → big denominator → small angle → wave moves **slow**

This is the key idea. Different pairs of dimensions oscillate at different speeds.

**What is the "angle"?**

When you write $\sin(\text{something})$, the "something" is called the angle. Here, the angle is just $\frac{pos}{10000^{2i/d_{model}}}$ — a number we compute by dividing the position by a scaling factor.

You can think of the angle as: "how far around the circle has this wave turned?"

> [!NOTE]
> **Summary in one sentence:**
>
> For each position, we compute a vector by filling pairs of dimensions with sine and cosine values — each pair at a different speed. Early dimensions oscillate fast, later dimensions oscillate slowly. Together they create a unique pattern for every position.

**The even-numbered dimensions (0, 2, 4, ...) use sine. The odd-numbered dimensions (1, 3, 5, ...) use cosine.** That is the only difference between the two lines of the formula.

---

## How Does it Work? Step by Step

Let's walk through exactly what happens when sinusoidal positional encoding is applied.

### Step 1: The Word Gets Converted to a Vector

First, each word (token) in the sentence is converted into a vector of numbers through a process called [[Embedding Matrix|word embedding]]. This vector captures what the word *means*, but contains no information about *where* it appears.

For example, the word "cat" might become a vector of 512 numbers:

```
cat_embedding = [0.3, -0.5, 0.8, 0.1, ..., 0.2]  ← 512 numbers
```

### Step 2: A Positional Encoding Vector is Created

A separate positional encoding vector is created for this position — also 512 numbers.

The values are computed using the sine and cosine formulas above:

```
positional_encoding = [sin(angle₀), cos(angle₀), sin(angle₁), cos(angle₁), ...]
```

Each pair of dimensions uses a different angle. The angle gets **smaller and smaller** as you move through the pairs (because the denominator in the formula grows larger). Here is what that means practically:

- The **first two dimensions** (pair 0) use a large angle — the wave goes up and down very quickly as the position changes. Even moving from position 0 to position 1 causes a big change.
- The **last two dimensions** (pair 255, if $d_{model} = 512$) use a tiny angle — the wave moves so slowly that it barely changes even across hundreds of positions.

> [!TIP]
> **Analogy: Clock hands**
>
> Think of a clock. The seconds hand moves fast — it completes a full circle every 60 seconds. The minutes hand moves slower. The hours hand moves slowest of all.
>
> But you need **all three hands** to know the exact time. The fast hand tells you about small differences (seconds). The slow hand tells you about large differences (hours).
>
> Sinusoidal encoding works the same way. Fast dimensions detect small position differences. Slow dimensions detect large position differences. Together, they uniquely identify every position.

### Step 3: Add the Two Vectors Together

The positional encoding vector is simply **added** to the word embedding vector:

```
final_vector = word_embedding + positional_encoding
```

This is it. The transformer then processes this combined vector. The word meaning and the position information are now blended together in a single vector.

### Step 4: The Transformer Processes Everything

The transformer receives the combined vectors for every token in the sentence and proceeds with attention as normal. The positional information is now embedded in every token's representation.

---

## Worked Example

Let's trace through a concrete example.

### Setup

Suppose we have the sentence:

```
"cats sleep"
```

- "cats" is at position 0.
- "sleep" is at position 1.

Suppose we are using a tiny model with $d_{model} = 4$ dimensions (normally 512 or more, but 4 is easier to show).

### Computing the Positional Encoding for Position 0 ("cats")

We need to fill 4 dimensions. We have 2 pairs: (dim 0, dim 1) and (dim 2, dim 3).

---

**Pair 0 (i = 0):**

Step 1 — Compute the denominator:

$$10000^{2 \times 0 / 4} = 10000^{0} = 1$$

> [!NOTE]
> Any number raised to the power of 0 equals 1. So $10000^0 = 1$.

Step 2 — Compute the angle:

$$\text{angle} = \frac{pos}{\text{denominator}} = \frac{0}{1} = 0$$

Step 3 — Apply sine and cosine:

- $PE_{(0, 0)} = \sin(0) = 0.000$
- $PE_{(0, 1)} = \cos(0) = 1.000$

---

**Pair 1 (i = 1):**

Step 1 — Compute the denominator:

$$10000^{2 \times 1 / 4} = 10000^{0.5} = 100$$

> [!NOTE]
> $10000^{0.5}$ means "the square root of 10000". The square root of 10000 is 100, because $100 \times 100 = 10000$.

Step 2 — Compute the angle:

$$\text{angle} = \frac{0}{100} = 0$$

Step 3 — Apply sine and cosine:

- $PE_{(0, 2)} = \sin(0) = 0.000$
- $PE_{(0, 3)} = \cos(0) = 1.000$

---

So the positional encoding for position 0 is:

```
PE(0) = [0.000, 1.000, 0.000, 1.000]
```

> [!NOTE]
> Position 0 always gives [0, 1, 0, 1, 0, 1, ...] because sin(0) = 0 and cos(0) = 1, no matter what the denominator is. The position number (0) divided by anything is still 0.

---

### Computing the Positional Encoding for Position 1 ("sleep")

---

**Pair 0 (i = 0):**

Step 1 — Denominator: $10000^{0} = 1$ (same as before)

Step 2 — Angle: $\frac{1}{1} = 1.0$

Step 3 — Apply sine and cosine:

- $PE_{(1, 0)} = \sin(1.0) \approx 0.841$
- $PE_{(1, 1)} = \cos(1.0) \approx 0.540$

> [!NOTE]
> We just plug the angle (1.0) into the sine and cosine functions. A calculator or the model's code does this — you don't need to compute it by hand. The point is that the value changed a lot compared to position 0.

---

**Pair 1 (i = 1):**

Step 1 — Denominator: $10000^{0.5} = 100$ (same as before)

Step 2 — Angle: $\frac{1}{100} = 0.01$ ← Notice this angle is much smaller than in Pair 0

Step 3 — Apply sine and cosine:

- $PE_{(1, 2)} = \sin(0.01) \approx 0.010$
- $PE_{(1, 3)} = \cos(0.01) \approx 1.000$

> [!NOTE]
> Because the angle here is tiny (0.01 instead of 1.0), the sine and cosine values barely changed compared to position 0. This is exactly the "slow oscillation" behaviour we wanted for later dimensions.

---

So the positional encoding for position 1 is:

```
PE(1) = [0.841, 0.540, 0.010, 1.000]
```

### Comparing the Two Positions

| Dimension | Position 0 | Position 1 |
|---|---|---|
| 0 (sin, fast) | 0.000 | 0.841 |
| 1 (cos, fast) | 1.000 | 0.540 |
| 2 (sin, slow) | 0.000 | 0.010 |
| 3 (cos, slow) | 1.000 | 1.000 |

Notice:
- The **fast dimensions** (0 and 1) changed a lot between position 0 and position 1.
- The **slow dimensions** (2 and 3) barely changed at all.

This is by design.

> [!TIP]
> **Why do we need both fast and slow dimensions?**
>
> Imagine trying to tell apart 1000 different people using only one feature. That's hard — one feature isn't enough.
>
> But with multiple features at different "scales", it becomes easy:
> - A fast dimension changes a lot between position 1 and position 2. It is good at telling **nearby positions** apart.
> - A slow dimension barely changes between position 1 and position 2, but changes noticeably between position 1 and position 500. It is good at telling **faraway positions** apart.
>
> Together, fast and slow dimensions can uniquely identify any position — whether it is 1 step away or 1000 steps away.

### Final Step: Add to Word Embedding

Suppose "cats" has the word embedding:

```
cats_embedding = [0.3, -0.5, 0.8, 0.1]
```

The final input to the transformer is:

```
final = [0.3 + 0.000, -0.5 + 1.000, 0.8 + 0.000, 0.1 + 1.000]
      = [0.300, 0.500, 0.800, 1.100]
```

The word meaning and position have been merged into one vector.

---

## Real-World Applications

Sinusoidal Positional Encoding was used in:

- **The original Transformer** (2017) — the paper that introduced the transformer architecture.
- **Early BERT models** — though BERT later switched to learned positional embeddings.
- **Many early translation and text generation models**.

Today, sinusoidal encoding has largely been replaced by newer methods like [[RoPE]] (used in LLaMA, Mistral, Gemma) and learned positional embeddings (used in GPT-2, early BERT). However, understanding sinusoidal encoding is essential because:

1. It introduced the key ideas that all later methods build on.
2. It shows why multi-frequency encoding is a powerful concept.
3. Many research papers still reference it as a baseline.

---

## Analogy

### The Music Sheet Analogy

Imagine a piece of sheet music. Each note has two pieces of information:

1. **What note is it?** (C, D, E, F, G...) — this is like the word's meaning.
2. **When does it play?** (beat 1, beat 2, beat 3...) — this is like the word's position.

In sheet music, you write the note and its timing together on the same line. You cannot separate them — a note without timing is meaningless.

Sinusoidal positional encoding does the same thing. It merges the word (what) with the position (when) into a single vector. The transformer then works with this combined information.

> [!TIP]
> Just as a musician can read a note and instantly know both its pitch and its timing, the transformer can read a combined vector and process both the word's meaning and its position simultaneously.

### The Binary Clock Analogy

Here is an even more precise analogy.

A **binary clock** shows time using columns of lights — one column for hours, one for tens of minutes, one for single minutes, and so on. Each column blinks at a different rate.

- The rightmost column (single seconds) blinks very fast — once per second.
- The next column (tens of seconds) blinks slower — once every 10 seconds.
- The next column (minutes) blinks even slower.
- The leftmost column (hours) barely moves at all.

At any given moment, the pattern of lights gives a unique representation of the time.

Sinusoidal Positional Encoding is almost exactly like a binary clock, but using smooth sine and cosine waves instead of blinking lights, and using many more "columns" (dimensions).

---

## Why Sine and Cosine? (The Clever Part)

You might wonder: why use sine and cosine specifically? Why not just use the position number directly?

### Why Not Just Use the Position Number?

You could give each position its number directly: position 0 gets the value 0, position 1 gets 1, position 50 gets 50.

But this causes two problems:

**Problem 1 — The numbers get too big.**
If a sentence has 10,000 words, the last position gets the value 10,000. This huge number would overwhelm the small decimal values in the word embeddings. The model would get confused.

**Problem 2 — The model cannot generalise.**
If the model is trained on sentences up to length 100, it has never seen position 101. It has no idea what to do with a new number it has never encountered.

### Why Sine and Cosine Are Better

Sine and cosine always stay between -1 and +1. No matter how large the position number gets, the encoding values stay small and manageable. This makes them safe to add to word embeddings.

Also, sine and cosine create **smooth, predictable patterns**. The encoding for position 101 is very similar to position 100. The model can make reasonable guesses about positions it has never seen during training.

### The Relative Distance Property

The original paper also noticed something clever. Because of how sine and cosine work mathematically, the encoding for position 7 and the encoding for position 10 have a consistent relationship — a relationship that is the same as the one between position 1 and position 4 (both are 3 apart).

In theory, this means the model could learn to detect that "these two words are 3 positions apart" just by looking at the difference between their positional encodings.

> [!WARNING]
> **This did not work as well as hoped in practice.** Models trained with sinusoidal encoding struggled to reliably use this relative-distance information. Understanding "word A is 3 positions before word B" turned out to be hard to learn from this encoding.
>
> This is the main reason [[RoPE]] was invented — RoPE directly encodes relative distances in a way the model finds much easier to use.

---

## Important Terms

**Sine (sin)**
A mathematical function that produces smooth waves oscillating between -1 and +1. Given an angle, it returns a number between -1 and +1. At angle 0: sin(0) = 0. At angle 90° (π/2 radians): sin(π/2) = 1.

**Cosine (cos)**
Like sine, but shifted. At angle 0: cos(0) = 1. At angle 90°: cos(90°) = 0. Cosine is always "ahead" of sine by a quarter cycle.

**Frequency**
How many times a wave completes a full cycle per unit of distance. High frequency = fast oscillation. Low frequency = slow oscillation.

**Positional Encoding Vector**
A vector (list of numbers) that encodes the position of a token. In sinusoidal encoding, this is computed using sine and cosine at multiple frequencies.

**Word Embedding**
A vector that encodes the *meaning* of a word. Every word in the vocabulary has its own embedding vector.

**$d_{model}$**
The number of dimensions (numbers) in each vector in the model. Typical values: 512 (original Transformer), 768 (BERT), 4096 (large LLMs).

**Position ($pos$)**
The index of a token in the sequence. The first token has position 0, the second has position 1, and so on.

**Dimension Index ($i$)**
Which pair of dimensions in the positional vector we are computing. Pair 0 uses the fastest frequency, pair 1 the next fastest, and so on.

**10000**
A large constant in the denominator of the frequency formula. It was chosen by the original paper's authors to create a nice spread of frequencies across the model's dimensions. It has no special mathematical significance beyond this.

---

## Sinusoidal vs. Other Positional Encodings

| Feature | Sinusoidal | Learned Embeddings | RoPE |
|---|---|---|---|
| How it works | Adds a fixed sine/cosine vector to each token | Adds a learned vector to each token | Rotates Q and K vectors inside attention |
| Fixed or learned? | Fixed (computed by formula) | Learned during training | Fixed (computed by formula) |
| Handles long sequences? | Reasonably | Poor (no vector for unseen positions) | Well |
| Captures relative positions? | Weakly (the property exists in theory but models struggle to use it) | Weakly | Directly |
| Extra parameters? | None | Yes (one vector per possible position) | None |
| Used in | Original Transformer (2017) | GPT-2, early BERT | LLaMA, Mistral, Gemma, Qwen |

---

## Common Mistakes and Misconceptions

> [!WARNING]
> **Misconception: The positional encoding replaces the word embedding.**
>
> Wrong. The positional encoding is **added** to the word embedding. Both are kept. The result is a single vector that contains both meaning and position information blended together.

> [!WARNING]
> **Misconception: The model learns the sine and cosine values during training.**
>
> Wrong. The values are computed by a fixed mathematical formula before training begins. They never change. There are no learnable parameters in sinusoidal positional encoding. (This is different from **learned** positional embeddings, which are trained.)

> [!WARNING]
> **Misconception: All dimensions of the positional vector use the same frequency.**
>
> Wrong. Different dimensions use different frequencies. Early dimensions (low $i$) oscillate fast. Later dimensions (high $i$) oscillate slowly. This multi-frequency design is the whole point — it allows the encoding to uniquely represent every position.

> [!WARNING]
> **Misconception: The transformer can directly learn relative positions from sinusoidal encoding.**
>
> Not effectively. While the math technically allows relative positions to be expressed as linear combinations of the positional encodings, models struggle to learn this in practice. This limitation motivated the development of [[RoPE]], which encodes relative positions directly.

> [!WARNING]
> **Misconception: Sinusoidal encoding is still used in modern LLMs.**
>
> Not typically. Modern large language models (LLaMA, GPT-4, Claude, Gemma, etc.) use [[RoPE]] or learned positional embeddings. Sinusoidal encoding is primarily used in research baselines and is important historically.

---

## Key Takeaways

1. **Transformers cannot tell word order without positional encoding.** Attention treats the sentence like a bag of words unless position information is explicitly added.

2. **Sinusoidal encoding creates a unique fingerprint for every position.** It uses sine and cosine waves at different frequencies to produce a vector that no two positions share.

3. **It is added to the word embedding.** The transformer receives a single vector per token that blends word meaning and word position.

4. **Fast dimensions encode fine-grained position differences.** Slow dimensions encode coarse, long-range differences. Together they handle any distance.

5. **No training required.** The values are computed by a fixed formula. No parameters are learned for positional encoding.

6. **It works reasonably well but has limitations.** It generalises to longer sequences better than learned embeddings, but encodes relative positions only weakly compared to [[RoPE]].

7. **It is historically foundational.** Understanding sinusoidal encoding is the key to understanding all modern positional encoding methods, which are improvements on this original idea.

> [!TIP]
> **One-sentence summary:**
>
> Sinusoidal Positional Encoding gives each position in a sequence a unique vector by combining sine and cosine waves at many different frequencies, then adds this vector to the word's meaning vector before the transformer processes it.

---

## Related Notes

- [[Positional Embedding]] — the broader concept; sinusoidal encoding is one approach
- [[RoPE]] — the modern replacement for sinusoidal encoding; rotates Q and K instead of adding to embeddings
- [[Transformer]] — the original architecture that introduced and used this encoding
- [[Attention Mechanism]] — the mechanism that is blind to word order without positional encoding
- [[Self-Attention]] — where positional information matters most
- [[Embedding Matrix]] — word embeddings that sinusoidal encoding is added to
- [[Token]] — each token gets a positional encoding added to its embedding
