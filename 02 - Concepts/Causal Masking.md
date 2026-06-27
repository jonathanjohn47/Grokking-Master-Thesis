---
tags: [concept, transformer, attention, decoder]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Causal Masking

## What Is It?

**Causal masking** is a rule that prevents a token from "looking at" tokens that come **after** it in a sequence.

In a decoder-only transformer (like GPT or Claude), each position can only attend to itself and **earlier positions** — never future ones.

For example, in the sequence `[The, cat, sat, on, the, mat]`:

- Position 1 ("The") can attend to: **[The]**
- Position 2 ("cat") can attend to: **[The, cat]**
- Position 3 ("sat") can attend to: **[The, cat, sat]**
- Position 4 ("on") can attend to: **[The, cat, sat, on]**

Position 4 **cannot** look ahead to "the" or "mat".

---

## Why Does It Exist?

### Problem: Unfair Training

Imagine you're training a model to predict the next word:

```
Input:   The cat sat on the ___
Target:  mat
```

Without causal masking, during training, the model could "cheat":

- It could look at the entire sequence **including** "mat".
- It would learn: "whenever I see [The, cat, sat, on, the, mat], the next word is mat."
- But at test time, "mat" isn't there yet — it's what we're trying to predict!

The model would fail immediately on new sequences.

### Solution: Causal Masking

By preventing the model from looking forward, it's forced to predict fairly:

- At training, position 5 (the blank) can only see `[The, cat, sat, on, the]`.
- It must predict "mat" using **only** those words.
- At test time, the same rule applies — the model knows how to work with incomplete sequences.

**Causal masking makes training and testing consistent.**

---

## Intuition

Imagine you're in a quiz show where:

1. You hear a question.
2. You must answer **before** hearing the answer (revealed later).
3. You cannot look back after answering.

This is exactly what causal masking enforces: each position makes decisions based on information **up to that point**, not information that comes later.

Without this rule, the quiz would be unfair:

- You'd see the answer first.
- You'd memorize: "this question → this answer."
- But on a new quiz, you'd fail — you hadn't actually learned anything.

---

## How Does It Work?

### The Attention Matrix

In a transformer, **attention** is computed as a matrix showing which positions attend to which.

Without any masking, the full attention matrix looks like this (where ✓ = can attend, ✗ = cannot attend):

```
        From:  T1  T2  T3  T4  T5
To T1:        [ ✓   ✓   ✓   ✓   ✓ ]
To T2:        [ ✓   ✓   ✓   ✓   ✓ ]
To T3:        [ ✓   ✓   ✓   ✓   ✓ ]
To T4:        [ ✓   ✓   ✓   ✓   ✓ ]
To T5:        [ ✓   ✓   ✓   ✓   ✓ ]
```

Every position can look at every other position.

With **causal masking**, the matrix becomes triangular (lower triangular):

```
        From:  T1  T2  T3  T4  T5
To T1:        [ ✓   ✗   ✗   ✗   ✗ ]
To T2:        [ ✓   ✓   ✗   ✗   ✗ ]
To T3:        [ ✓   ✓   ✓   ✗   ✗ ]
To T4:        [ ✓   ✓   ✓   ✓   ✗ ]
To T5:        [ ✓   ✓   ✓   ✓   ✓ ]
```

Each position can only attend to itself and **earlier** positions. This is the causal mask.

### The Mathematical Implementation

Here's how causal masking is actually implemented:

**Step 1:** Compute attention scores (before masking):

$$\text{scores} = \frac{Q \cdot K^T}{\sqrt{d}}$$

For our 5-token example, this produces a 5×5 matrix of raw attention scores.

**Step 2:** Apply the causal mask (set future positions to $-\infty$):

$$\text{scores[i, j]} = \begin{cases} \text{scores[i, j]} & \text{if } j \leq i \\ -\infty & \text{if } j > i \end{cases}$$

**Step 3:** Apply softmax:

$$\text{attention\_weights} = \text{softmax}(\text{scores})$$

When you take softmax of $-\infty$, it becomes exactly **0**.

So the weights for future positions are **zero** — they contribute nothing.

```python
# Pseudo-code
scores = query @ key.T / sqrt(d)

# Apply causal mask
scores = scores.masked_fill(torch.triu(torch.ones(...), diagonal=1).bool(), float('-inf'))

# Softmax (and -inf becomes 0)
weights = softmax(scores)

# Compute weighted average of values
output = weights @ values
```

---

## Example

Let's trace through a concrete example: predicting from `[A, B, C]`

**Input sequence:** `[A, B, C]`

**Step 1: Compute attention scores (3×3 matrix)**

Suppose the model computes these raw attention scores:

```
     To:  A    B    C
From A: [0.5  0.3  0.8]
From B: [0.2  0.6  0.1]
From C: [0.4  0.5  0.7]
```

**Step 2: Apply causal mask**

Set future positions to $-\infty$:

```
     To:   A      B       C
From A: [0.5   -∞     -∞   ]
From B: [0.2   0.6   -∞   ]
From C: [0.4   0.5   0.7  ]
```

- Position A: can only attend to itself (position A is "future" relative to itself, but we allow self-attention).
- Position B: can attend to A and B, but not C.
- Position C: can attend to A, B, and C.

**Step 3: Apply softmax**

$-\infty$ becomes 0 after softmax:

```
     To:  A      B      C
From A: [1.0   0.0    0.0  ]     (all weight on A)
From B: [0.2   0.8    0.0  ]     (20% from A, 80% from B)
From C: [0.2   0.3    0.5  ]     (20% from A, 30% from B, 50% from C)
```

**Interpretation:**
- When predicting from position A: use only A.
- When predicting from position B: use 20% from A, 80% from B.
- When predicting from position C: use 20% from A, 30% from B, 50% from C.

Future positions (C for position B) contribute **zero**.

---

## Why Causal Masking Matters for Grokking

In grokking experiments, the model learns modular arithmetic:

```
Input:  [37, +, 61, =]
Output: 1     (because 37 + 61 = 98 ≡ 1 (mod 97))
```

The causal mask means:

- The **`=` token** (position 4) can look at positions 1, 2, 3 (the numbers and operator).
- The **`=` token** cannot look at the answer (position 5).

This forces the model to learn the actual arithmetic, not just memorize "when I see [37, +, 61, =, 1], output 1."

Without causal masking, the model could cheat and look directly at the answer. The model would memorize, not generalize.

> [!NOTE]
> Causal masking enforces that grokking is *true generalization*, not memorization.

---

## Decoder-Only vs. Encoder-Only

### Decoder-Only Models (GPT, Claude, LLaMA)

- **Use causal masking.**
- Each position predicts the next token.
- Trained on next-token prediction.
- Can generate text autogressively (predict one token, add it, predict the next).

### Encoder-Only Models (BERT)

- **No causal masking** — each position can see all positions (bidirectional).
- Trained on masked language modeling (predict a masked word using context from both sides).
- Used for understanding text, not generating it.

### Encoder-Decoder Models (T5)

- **Encoder:** no masking (bidirectional).
- **Decoder:** causal masking.
- Can see full input, then generate output autoregressively.

---

## Parallel Training vs. Autoregressive Generation

Here's a subtle but important point:

### During Training (Parallel)

All positions are processed **simultaneously**, but with causal masking:

```
Tokens:  [A, B, C, D]

All computed in parallel:
- Position A predicts from [A]
- Position B predicts from [A, B]
- Position C predicts from [A, B, C]
- Position D predicts from [A, B, C, D]

Loss computed on all 4 predictions at once.
```

This is **fast** because positions don't have to wait for each other.

### During Generation (Autoregressive)

Tokens are generated **one at a time**:

```
Step 1: Prompt = [A]
        Model predicts position 2: outputs "B"

Step 2: Prompt = [A, B]
        Model predicts position 3: outputs "C"

Step 3: Prompt = [A, B, C]
        Model predicts position 4: outputs "D"
```

Each step is slower because you compute one new position, then feed it back in.

But **the logic is identical** — position 2 at training time used the same rule (can see positions up to 2) as step 2 at generation time.

> [!TIP]
> Causal masking allows fast parallel training while maintaining the same distribution as slow sequential generation. This is brilliant.

---

## Important Terms

**Decoder-only model** — A transformer that only generates text (no understanding of future context). Uses causal masking.

**Encoder-only model** — A transformer that only understands text (can see full context). No causal masking.

**Bidirectional attention** — Every position can attend to every other position. Used in encoders.

**Unidirectional attention** — Each position can only attend to earlier positions. Used in decoders (with causal masking).

**Autoregressive** — Generating one token at a time, feeding each output back as input. Enabled by causal masking.

**Masked language modeling** — Training by hiding a word and predicting it from context. Typically used with bidirectional attention (BERT).

**Next-token prediction** — Training by predicting the next token in a sequence. Uses causal masking.

---

## Common Mistakes

**Mistake 1:** "Causal masking means the model processes tokens left-to-right."

**Reality:** No. During training, all positions are processed **in parallel**. Causal masking only prevents each position from *attending to* future positions. The computation order is parallel, not sequential.

**Mistake 2:** "Causal masking prevents the model from using future information."

**Reality:** It prevents the model from *attending to* future information during training, ensuring fair training and generalization. During generation, there is no future information anyway.

**Mistake 3:** "We need causal masking to make the model efficient."

**Reality:** Causal masking is about **correctness** (fair training), not efficiency. In fact, without causal masking, you could compute in parallel but it would be unfair. Causal masking enables both fairness *and* parallel efficiency.

---

## Key Takeaways

- **Causal masking** prevents each position from attending to tokens that come **later** in the sequence.
- It is implemented by setting future attention scores to $-\infty$, which become 0 after softmax.
- It ensures **fair training** — the model cannot cheat by looking at answers.
- It enables **autoregressive generation** — predict one token, add it, predict the next.
- **Decoder-only models** (GPT, Claude, LLaMA) use causal masking; **encoder models** (BERT) do not.
- Without causal masking in decoder-only models, the model would memorize instead of generalize.

---

## Related Notes

- [[Transformer]] — the architecture using causal masking in decoder blocks.
- [[Attention Mechanism]] — the mechanism that causal masking constrains.
- [[Next-Token Prediction]] — the training objective enabled by causal masking.
- [[Decoder-Only Dominance]] — why decoder-only models with causal masking became the standard.
- [[Multi-Head Self-Attention]] — where causal masking is applied.
