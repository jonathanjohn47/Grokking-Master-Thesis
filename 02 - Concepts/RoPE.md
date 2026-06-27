---
tags: [concept, foundations, embeddings, transformer, position, modern]
---
↑ Parent: [[Positional Embedding]] · Related: [[Attention Mechanism]] · [[Transformer]]

# RoPE — Rotary Positional Encoding

## What is it?

**RoPE** stands for **Rotary Positional Encoding**.

It is a method for telling a language model **where each word is located** inside a sentence.

That's it at the highest level. A language model needs to know the order of words. RoPE is one way to give it that information.

> [!NOTE]
> RoPE is used inside almost every modern large language model (LLM). LLaMA, Mistral, Gemma, Qwen, and many others all use RoPE. It has become the standard approach.

---

## Why does it exist?

Before you can understand RoPE, you need to understand the problem it solves.

### The Problem: Transformers Are Word-Order Blind

A [[Transformer]] model processes words using a mechanism called [[Attention Mechanism|attention]].

Attention lets every word "look at" every other word in the sentence. But here is the critical problem:

> **Attention does not know the order of words by itself.**

If you gave a transformer the sentence:

```
The cat sat on the mat.
```

And then shuffled it to:

```
Mat the on cat sat the.
```

Without positional information, the transformer would process both sentences **identically**. It cannot tell the difference. This is obviously a huge problem — word order completely changes meaning.

> [!WARNING]
> This is one of the most important things to understand about transformers. The attention mechanism treats the sentence like a **bag of words** with no order unless you explicitly add positional information.

### The Solution: Positional Encoding

The fix is to add **positional information** to each word before the transformer processes it. This tells the model: "this word is at position 1, this word is at position 2, this word is at position 3," and so on.

Researchers have tried different approaches to this problem. RoPE is the approach that became dominant in modern models.

### Why Not Just Use the Old Approaches?

There were two main older approaches. Both had problems.

**Approach 1: Learned Positional Embeddings**

In this approach, the model *learns* a special vector (a list of numbers) for each position during training.

- Position 1 gets one vector.
- Position 2 gets another vector.
- And so on.

The problem: **the model can only handle positions it has seen during training**. If it was trained on sequences up to length 2048, it has no learned vector for position 5000. It simply breaks when given longer text.

**Approach 2: [[Sinusoidal Positional Encoding]]**

This approach uses mathematical formulas (sine and cosine waves) to create positional vectors. No learning required.

The problem: **it is not good at capturing relative distances between words**.

What matters in language is often not "this word is at position 47" but rather "these two words are 3 positions apart." Sinusoidal encoding is not really designed to express that.

> [!QUESTION]
> What do we mean by "relative distance"?
>
> Consider the sentence: "The cat, which was sleeping peacefully, suddenly woke up."
>
> The words "cat" and "woke" are the main subject and verb. They are closely connected in meaning. But they might be 6 positions apart in the sentence. A model that understands **relative distances** can capture this "6 apart" relationship — no matter where in the sentence the pair of words appears.

**RoPE was created to solve both problems at once.**

---

## Intuition First

Before any math, let's build the right mental picture.

### The Core Idea in One Sentence

RoPE gives each word a **rotation** — like spinning a clock hand — based on its position. Words that are close together in the sentence will have similar rotations. The attention mechanism then naturally "sees" the gap between any two words by comparing their rotations.

### The Clock Analogy

Imagine a clock hand. It points in a direction. That direction is an **angle**.

- At 12 o'clock, the angle is 0°.
- At 3 o'clock, the angle is 90°.
- At 6 o'clock, the angle is 180°.

Now imagine two people standing at different positions on the clock face.

- Person A at "3 o'clock" (90°), Person B at "5 o'clock" (150°) → the gap between them is 60°.
- Person A at "7 o'clock", Person B at "9 o'clock" → the gap is still 60°.

No matter where they stand in absolute terms, the **gap** between them is the same.

> [!TIP]
> **RoPE works exactly like this.** Each word gets "rotated" to a position on a circle based on where it appears in the sentence. When two words interact in the attention mechanism, only the **gap** between their rotations matters — not their absolute positions.

---

## Background: What Does "Rotating a Vector" Actually Mean?

This is the concept that confuses most beginners. Let's explain it very carefully.

### What is a Vector?

A [[Dense Vector|vector]] is just a list of numbers. For example:

```
[0.8, 0.6]
```

If you have just two numbers, you can imagine them as a point on a flat grid — like coordinates on a map. The first number is how far right you go (x), and the second is how far up you go (y).

So `[0.8, 0.6]` is a point that is 0.8 units to the right and 0.6 units up.

You can also imagine it as an **arrow** drawn from the center of the grid (0, 0) out to that point.

```
        ↑ y
    1.0 |
    0.6 |............*  ← the point [0.8, 0.6]
        |          ↗
    0.0 └───────────────→ x
        0.0      0.8  1.0
```

### What Does "Rotating" Mean?

**Rotating** this arrow means spinning it around the center point by some angle. The arrow stays the same length — it just points in a different direction.

For example, rotating the arrow by 45°:

```
Before rotation (0°):       After rotating 45°:

        ↑                         ↑   ↗
        |                         | ↗
   ─────┼──→                 ─────┼─────
        |                         |
```

The arrow was pointing right. Now it points up and to the right. Same length, different direction.

> [!TIP]
> Think of it like a compass needle. If you rotate the compass 45°, the needle points in a new direction — but it is still the same needle, same length. Rotation just changes direction.

### Why Does Rotation Preserve Information?

When you rotate a vector, **no information is lost**. The arrow is the same length. You can always rotate it back to the original direction. Rotation just re-orients the information — it does not delete or add anything.

This is important for RoPE. We want to add position information to a vector *without* destroying the word's meaning that is already stored in it.

### Rotating Real Vectors (With More Than 2 Numbers)

In a real language model, vectors have hundreds or thousands of numbers — not just 2.

RoPE handles this by splitting the vector into **pairs of two numbers at a time** and rotating each pair independently. Each pair is treated as one small 2D arrow.

```
Full vector: [0.8, 0.6, 0.4, -0.2, 0.9, 0.1, ...]

Split into pairs:
  Pair 0: (0.8, 0.6)   → rotate this pair by angle A
  Pair 1: (0.4, -0.2)  → rotate this pair by angle B
  Pair 2: (0.9, 0.1)   → rotate this pair by angle C
  ...
```

Each pair gets its own rotation angle. We will explain how those angles are chosen in the next section.

---

## Background: What Are Query and Key Vectors?

> [!NOTE]
> If you already understand the [[Attention Mechanism]], skip this section.

Inside a transformer, every word produces three vectors:

- **Query (Q)**: "What information am I looking for?"
- **Key (K)**: "What information do I have?"
- **Value (V)**: "Here is my actual content."

The attention mechanism compares every word's Query against every other word's Key. The comparison is done by computing a **dot product** — a number that measures how similar two vectors are.

The higher the dot product, the more attention Word A pays to Word B.

```
Attention score between word A and word B = Q_A · K_B
```

(The dot symbol "·" means dot product: multiply the matching numbers together and add them all up.)

**RoPE modifies this by rotating Q and K before computing the dot product.**

The Value vector V is never rotated. It just carries the content.

---

## How Does it Work? Step by Step

### Step 1: Produce the Query and Key Vectors as Usual

A transformer processes each word (called a [[Token|token]]) and produces a Query vector Q and a Key vector K through its normal computation.

Let's say the Query vector for a word at position 1 is:

```
q = [0.8, 0.6, 0.4, -0.2]
```

This vector has 4 numbers (in reality it would have hundreds or thousands).

### Step 2: Split the Vector into Pairs

RoPE splits this vector into pairs of two numbers:

```
Pair 0: (0.8, 0.6)
Pair 1: (0.4, -0.2)
```

Each pair will be rotated independently.

### Step 3: Assign a Rotation Speed to Each Pair

This is a key design decision. **Different pairs rotate at different speeds** as the position changes.

Think of it like a clock:
- The **seconds hand** moves very fast — one full circle every 60 seconds.
- The **minutes hand** moves slower — one full circle every 60 minutes.
- The **hours hand** moves slowest — one full circle every 12 hours.

But all three hands together let you know the exact time.

RoPE does the same thing. Each pair of dimensions is like a different clock hand. Some pairs rotate fast, some rotate slowly. Together they can encode any position precisely.

The rotation speed for each pair is called its **frequency** ($\theta_i$):

$$\theta_i = \frac{1}{10000^{2i/d}}$$

Let's break this down piece by piece:

- $d$ is the total number of dimensions in the vector (e.g., 4, 512, 4096).
- $i$ is which pair we are computing (0, 1, 2, ...).
- $10000$ is a large constant chosen to spread the speeds across a wide range.
- The higher $i$ is, the larger $10000^{2i/d}$ becomes, and therefore the smaller $\theta_i$ becomes → **slower rotation**.

In plain English: **earlier pairs rotate fast, later pairs rotate slowly.**

> [!EXAMPLE]
> With $d = 4$ dimensions and 2 pairs:
>
> - **Pair 0** ($i = 0$): $\theta_0 = \frac{1}{10000^{0}} = \frac{1}{1} = 1.0$ ← fast
> - **Pair 1** ($i = 1$): $\theta_1 = \frac{1}{10000^{0.5}} = \frac{1}{100} = 0.01$ ← slow
>
> Pair 0 rotates 100 times faster than Pair 1. After 100 positions, Pair 0 has done many full circles; Pair 1 has barely moved.

### Step 4: Compute the Rotation Angle for This Token's Position

For a token at position $m$, each pair $i$ is rotated by:

$$\text{angle} = m \times \theta_i$$

So:
- A token at position 1 rotates Pair 0 by $1 \times 1.0 = 1.0$ radian.
- A token at position 2 rotates Pair 0 by $2 \times 1.0 = 2.0$ radians.
- A token at position 10 rotates Pair 0 by $10 \times 1.0 = 10.0$ radians.

The further along in the sentence, the larger the rotation.

> [!NOTE]
> **What is a radian?**
>
> A radian is just a unit for measuring angles — like degrees, but different. Here is a rough guide:
> - 0 radians = 0° (no rotation, pointing right)
> - 1.57 radians ≈ 90° (pointing up)
> - 3.14 radians ≈ 180° (pointing left)
> - 6.28 radians ≈ 360° (one full circle, back to pointing right)
>
> You don't need to memorise this. Just know that bigger angle = more rotation.

### Step 5: Apply the Rotation

To rotate a pair $(x, y)$ by an angle $\alpha$, you use this calculation:

$$x' = x \cdot \cos(\alpha) - y \cdot \sin(\alpha)$$
$$y' = y \cdot \cos(\alpha) + x \cdot \sin(\alpha)$$

This looks scary, but let's walk through what it actually says in plain English:

> The new x value ($x'$) is computed by taking a bit of the old x and subtracting a bit of the old y.
> The new y value ($y'$) is computed by taking a bit of the old y and adding a bit of the old x.

The "bit" is controlled by $\cos(\alpha)$ and $\sin(\alpha)$, which are just two numbers that depend on the angle.

> [!TIP]
> You don't need to understand *why* this formula rotates the vector. Just trust that it does. Think of it as a recipe: put in $(x, y)$ and an angle, get out a new point $(x', y')$ that is the same distance from the center but pointing in a new direction.

This is applied to **every pair** in the Query vector. The same process is applied to every pair in the Key vector of every other token.

### Step 6: Compute Attention as Normal

After rotating Q and K, the attention computation proceeds exactly as before:

```
Attention scores = softmax(Q_rotated × K_rotated^T / √d)
```

These scores are used to weight and sum the Value vectors V.

> [!NOTE]
> **The Value vector V is NOT rotated.** Only Q and K are rotated. V carries the actual content and does not need positional information in the same way.

---

## Why Does This Encode Relative Positions?

This is the clever insight at the heart of RoPE. Let's build up to it carefully.

### First, Let's Think About a Simple Example

Imagine two arrows on a flat grid. Arrow A points to the right. Arrow B also points to the right.

If I rotate Arrow A by 30° and Arrow B by 30°, both arrows now point up-right — but the **angle between them** is still 0°. The gap between them did not change.

Now imagine Arrow A at 0° and Arrow B at 45°. The angle between them is 45°. If I rotate Arrow A to 30° and Arrow B to 75° (both rotated by 30°), the angle between them is still 45°.

> **Key insight: When you rotate two arrows by the same amount, the angle between them stays the same.**

### How This Applies to RoPE

In RoPE:
- Token at position $m$ has its Q vector rotated by angle $m \times \theta$.
- Token at position $n$ has its K vector rotated by angle $n \times \theta$.

The **difference** between those two rotation angles is:

$$m \times \theta - n \times \theta = (m - n) \times \theta$$

This difference depends only on $(m - n)$ — the gap between the two positions.

The dot product between Q and K (which computes their attention score) essentially measures the angle between the two vectors. Since the angle between them depends only on $(m - n)$, the attention score depends only on how far apart the two tokens are.

> [!TIP]
> **In plain English:**
>
> Imagine you're at position 5, and you rotate your Q arrow by 5 steps. I'm at position 8, and I rotate my K arrow by 8 steps. When your Q and my K compare themselves, what matters is not "you're at 5 and I'm at 8" — what matters is "we are 3 steps apart." That's the gap. RoPE guarantees the comparison reflects only the gap.

This is written mathematically as:

$$Q_m \cdot K_n = f(m - n)$$

This says: the attention score is a function of only the **difference** $(m - n)$, not of $m$ and $n$ separately.

> [!NOTE]
> This is what "encoding relative positions" means. The model does not need to know "word A is at position 5 and word B is at position 8." It only needs to know "word A and word B are 3 positions apart." RoPE builds this automatically into how Q and K interact.

---

## Worked Example

Let's trace through a concrete example.

### Setup

Sentence: `"The dog barked"`

- "The" → position 0
- "dog" → position 1
- "barked" → position 2

We'll use a tiny Query vector with just 4 dimensions.

Query vector for "dog" (position 1):

```
q = [0.8, 0.6, 0.4, -0.2]
```

### Step 1: Split into Pairs

```
Pair 0: (0.8, 0.6)
Pair 1: (0.4, -0.2)
```

### Step 2: Compute Rotation Speeds

With $d = 4$ and 2 pairs:

**Pair 0** ($i = 0$):
$$\theta_0 = \frac{1}{10000^{2 \times 0 / 4}} = \frac{1}{10000^{0}} = \frac{1}{1} = 1.0$$

> $10000^0 = 1$ because any number raised to the power of 0 equals 1.

**Pair 1** ($i = 1$):
$$\theta_1 = \frac{1}{10000^{2 \times 1 / 4}} = \frac{1}{10000^{0.5}} = \frac{1}{100} = 0.01$$

> $10000^{0.5}$ means "the square root of 10000." Since $100 \times 100 = 10000$, the square root is 100.

### Step 3: Compute Rotation Angles for Position 1

"Dog" is at position $m = 1$.

- Pair 0: angle = $1 \times 1.0 = 1.0$ radian ≈ 57°
- Pair 1: angle = $1 \times 0.01 = 0.01$ radian ≈ 0.57°

Pair 0 rotates a lot. Pair 1 barely rotates at all.

### Step 4: Apply the Rotations

#### Rotating Pair 0 by 1.0 radian

The pair is $(x, y) = (0.8, 0.6)$ and the angle $\alpha = 1.0$.

First, look up (or compute) $\cos(1.0)$ and $\sin(1.0)$:
- $\cos(1.0) \approx 0.540$
- $\sin(1.0) \approx 0.841$

Now apply the rotation formula:

$$x' = x \cdot \cos(\alpha) - y \cdot \sin(\alpha)$$
$$x' = 0.8 \times 0.540 - 0.6 \times 0.841$$
$$x' = 0.432 - 0.505 = -0.073$$

$$y' = y \cdot \cos(\alpha) + x \cdot \sin(\alpha)$$
$$y' = 0.6 \times 0.540 + 0.8 \times 0.841$$
$$y' = 0.324 + 0.673 = 0.997$$

Rotated Pair 0: $(-0.073,\ 0.997)$

> [!NOTE]
> Let's check our work. The original pair $(0.8, 0.6)$ has a length of $\sqrt{0.8^2 + 0.6^2} = \sqrt{0.64 + 0.36} = \sqrt{1.0} = 1.0$.
> The rotated pair $(-0.073, 0.997)$ has a length of $\sqrt{(-0.073)^2 + 0.997^2} \approx \sqrt{0.005 + 0.994} \approx 1.0$.
> Same length — rotation preserved the information!

#### Rotating Pair 1 by 0.01 radian

The pair is $(x, y) = (0.4, -0.2)$ and the angle $\alpha = 0.01$.

$\cos(0.01) \approx 0.99995$ and $\sin(0.01) \approx 0.01$.

$$x' = 0.4 \times 0.99995 - (-0.2) \times 0.01 = 0.400 + 0.002 = 0.402$$
$$y' = (-0.2) \times 0.99995 + 0.4 \times 0.01 = -0.200 + 0.004 = -0.196$$

Rotated Pair 1: $(0.402,\ -0.196)$

> [!NOTE]
> Almost unchanged! The angle was so tiny (0.01 radian) that the rotation barely moved the pair. This is the "slow" behaviour of later dimensions.

### Step 5: Reassemble the Rotated Vector

```
Original:  [0.800,  0.600, 0.400, -0.200]
Rotated:   [-0.073, 0.997, 0.402, -0.196]
```

The first pair changed a lot (big rotation). The second pair barely changed (tiny rotation).

This rotated vector is the Query for "dog" that gets used in the attention computation.

The same process is applied to the Key vectors of "The" and "barked." When the dot product is computed between any two rotated vectors, the result naturally reflects only the gap between their positions.

---

## Real-World Applications

RoPE is used in virtually every state-of-the-art language model built since 2023:

- **LLaMA** (Meta's open-source model family) — uses RoPE
- **Mistral** — uses RoPE
- **Gemma** (Google DeepMind) — uses RoPE
- **Qwen** (Alibaba) — uses RoPE
- **Falcon** — uses RoPE

This is not a coincidence. RoPE was adopted so broadly because it solves real practical problems:

1. **Better generalisation to long sequences** — Models trained on 4096 tokens can be extended to handle 32,000+ tokens with techniques like YaRN (which builds on RoPE).
2. **Better understanding of relative word distances** — Important for things like coreference ("she" refers to "Mary" from 10 words earlier).
3. **No learned parameters** — RoPE uses fixed mathematical formulas, not learned vectors. This means it adds no extra parameters to the model.

---

## Analogy

### The Clock Hands Analogy

Think of a clock with three hands:

- A **second hand** that moves fast.
- A **minute hand** that moves medium.
- An **hour hand** that moves slow.

All three hands together tell you the exact time. No single hand gives the full picture alone.

RoPE works the same way. Each **pair of dimensions** in the vector is like a different clock hand:

- **Early pairs** rotate fast (like the second hand). They encode fine-grained differences — whether two tokens are 1 or 2 positions apart.
- **Middle pairs** rotate at medium speed (like the minute hand). They encode medium-range differences.
- **Later pairs** rotate slowly (like the hour hand). They encode coarse, long-range differences — whether two tokens are 100 or 200 positions apart.

Together, all the pairs give the model a **rich, multi-scale understanding** of how far apart any two words are.

> [!TIP]
> Just like you can tell the exact time by combining all three clock hands, the attention mechanism can tell the exact relative distance between any two tokens by combining information across all the pairs.

### The Spinning Arrow Analogy

Imagine marking the position of each word on a clock face, where the clock hand spins faster for each new word.

- Word 1 → arrow points at 10°
- Word 2 → arrow points at 20°
- Word 3 → arrow points at 30°

When the model compares word 1 and word 3, it compares arrows pointing at 10° and 30°. The angle between them is 20°. That 20° gap is the relative distance.

Compare word 5 and word 7: arrows at 50° and 70°. Gap is still 20°. The model correctly recognises "these two words are the same distance apart as words 1 and 3."

---

## Important Terms

**Token**
A single unit of text that the model processes. Usually a word or part of a word.

**Vector**
A list of numbers. For example, [0.5, -0.3, 0.8, 0.1]. In RoPE, vectors are treated as collections of 2D arrows that can be rotated.

**Query (Q)**
A vector that each token produces to represent "what information am I looking for?" Used in the attention mechanism.

**Key (K)**
A vector that each token produces to represent "what information do I have?" Compared against Query vectors to compute attention scores.

**Value (V)**
A vector containing the actual content of a token. Retrieved based on attention scores. RoPE does **not** rotate V.

**Dot Product**
A way of comparing two vectors. You multiply matching numbers together and add them all up. A high dot product means the vectors point in similar directions.

**Rotation**
Spinning a vector around the center point (origin) by some angle. Changes the direction of the vector but not its length. No information is lost.

**Rotation Angle**
How much a vector is rotated. In RoPE, the angle = position × frequency. Bigger position = bigger rotation.

**Frequency ($\theta_i$)**
A number that controls how fast a pair of dimensions rotates as the position increases. Earlier pairs have higher frequencies (rotate fast). Later pairs have lower frequencies (rotate slowly).

**Relative Position**
The distance between two tokens in the sequence. If "cat" is at position 3 and "slept" is at position 7, their relative position is 4 (= 7 − 3).

**Absolute Position**
The index of a token from the start of the sequence. "cat" is at absolute position 3.

**Radian**
A unit for measuring angles. 1 radian ≈ 57.3 degrees. A full circle = $2\pi \approx 6.28$ radians.

**Cosine / Sine**
Mathematical functions that return numbers between -1 and +1 based on an angle. Used in the rotation formula to compute the new x and y values after spinning.

---

## Common Mistakes and Misconceptions

> [!WARNING]
> **Misconception: RoPE adds positional information to the word embeddings.**
>
> This is wrong. Older methods (sinusoidal, learned) added a positional vector to the token's input embedding. RoPE does NOT touch the input embeddings. Instead, it rotates the Query and Key vectors **inside the attention computation**. This is a fundamentally different approach.

> [!WARNING]
> **Misconception: RoPE rotates the Value vectors too.**
>
> RoPE only rotates Q and K. The Value vector V is left unchanged. The positional information is embedded in how Q and K interact — V does not need it.

> [!WARNING]
> **Misconception: Rotation changes or destroys the information in the vector.**
>
> Rotation preserves all information. It changes the direction of the vector but not its length. You can always rotate it back to the original. Nothing is lost.

> [!WARNING]
> **Misconception: RoPE makes attention aware of absolute positions.**
>
> RoPE makes attention aware of **relative positions** — the distance between tokens. This is actually better for most language tasks. Knowing "these two words are 5 apart" is usually more useful than knowing "this word is at position 47."

> [!WARNING]
> **Misconception: All dimension pairs rotate at the same speed.**
>
> No — each pair has its own frequency. Earlier pairs rotate fast, later pairs rotate slowly. This multi-speed design is essential to RoPE's ability to encode position at many different scales.

---

## RoPE vs Other Positional Encodings

| Feature | Sinusoidal | Learned Embeddings | RoPE |
|---|---|---|---|
| How it is applied | Added to input token embeddings | Added to input token embeddings | Rotates Q and K inside attention |
| Requires training? | No — uses fixed formulas | Yes — learned during training | No — uses fixed formulas |
| Captures relative positions? | Weakly | Weakly | Directly and exactly |
| Handles long sequences? | Reasonably | Poor (breaks on unseen positions) | Well (can be extended) |
| Used in | Original Transformer (2017) | GPT-2, BERT | LLaMA, Mistral, Gemma, Qwen |
| Extra parameters? | None | Yes (one vector per position) | None |

---

## Key Takeaways

1. **Transformers are word-order blind by default.** Without positional encoding, a transformer treats "cat bites dog" and "dog bites cat" the same.

2. **RoPE rotates each word's Q and K vectors.** The rotation angle depends on the word's position in the sentence.

3. **The further along in the sentence, the bigger the rotation.** Token at position 1 → small rotation. Token at position 100 → large rotation.

4. **Attention scores automatically reflect relative distances.** After rotating Q and K, the dot product $Q_m \cdot K_n$ depends only on the gap $(m - n)$ between the tokens — not on their absolute positions.

5. **Different dimension pairs rotate at different speeds.** Fast pairs encode fine-grained differences. Slow pairs encode large-scale differences. Together they handle any distance.

6. **Rotation preserves all information.** The vector's length is unchanged. Only its direction changes. Nothing is lost.

7. **RoPE generalises better to long sequences.** Unlike learned embeddings, RoPE never "runs out" of positions. It can always rotate by a larger angle for a larger position number.

8. **RoPE is the dominant positional encoding in modern LLMs.** LLaMA, Mistral, Gemma, and many others all use it.

> [!TIP]
> **The one-sentence summary of RoPE:**
>
> RoPE rotates each word's Query and Key vectors by an angle proportional to its position in the sentence, so that when two words interact in attention, the result reflects only how far apart they are — not where they are.

---

## Related Notes

- [[Positional Embedding]] — the broader concept; RoPE is one approach to positional encoding
- [[Attention Mechanism]] — where RoPE is applied (to Q and K before computing attention scores)
- [[Self-Attention]] — the mechanism that is position-blind without RoPE or another positional encoding
- [[Transformer]] — the architecture that uses RoPE in modern implementations
- [[Token]] — each token gets its Q and K vectors rotated by RoPE
- [[Dense Vector]] — Q and K vectors that RoPE rotates are dense vectors
- [[Sinusoidal Positional Encoding]] — the older fixed approach that RoPE improves upon
- [[Learned Positional Embeddings]] — the older learned approach that RoPE improves upon
