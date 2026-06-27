---
tags: [concept, training, language-model, objective]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Next-Token Prediction

## What Is It?

**Next-token prediction** is a simple training objective: given a sequence of tokens, predict the next one.

```
Input:  [The, cat, sat, on, the]
Target: mat
```

The model reads all the input tokens and outputs a probability distribution over possible next tokens. It learns by comparing its prediction to the actual next token.

This simple task, repeated on billions of examples, causes large language models to learn world knowledge, reasoning, and language understanding.

---

## Why Does It Work?

### The Key Insight

To predict the next token, the model must **understand** the context.

For example:

```
Input:  [The capital of France is]
Target: Paris
```

To predict "Paris," the model must:
- Recognize "capital" and "France."
- Know the relationship between them.
- Retrieve the fact "Paris is the capital of France."

By training on millions of such examples, the model **internalizes world knowledge**.

### It's Self-Supervised

No human labels are needed. The next token is automatically available in the text:

```
Training example: "The cat sat on the mat"
Input:  [The, cat, sat, on, the]
Target: mat (just the next token in the sequence)
```

Any text corpus provides unlimited training examples without manual annotation.

### Emergent Capabilities

Scaling this simple objective to massive models and data produces:

- **World knowledge:** Facts about history, geography, science.
- **Reasoning:** Multi-step logical thinking.
- **Language understanding:** Grammar, semantics, pragmatics.
- **Code generation:** Understanding programming patterns.

All from one objective.

---

## Intuition

Imagine teaching a child to predict stories:

**Parent:** "Once upon a time, in a dark forest, there lived a..."

**Child's guess:** "...wolf?"

**Parent:** "No, try again. There lived a... **wise old**... what?"

**Child:** "...wizard!"

**Parent:** "Good! Now, the wizard waved his wand and suddenly..."

**Child:** "...the forest lit up!"

By practicing this prediction game millions of times with different stories, the child learns:

- Story patterns.
- Character archetypes.
- Cause and effect.
- Language.

**That's next-token prediction.**

The child doesn't need to be explicitly taught grammar or plot structure — both emerge from predicting what comes next.

---

## How Does It Work?

### The Training Loop

**Step 1: Prepare training data**

Take a text corpus (e.g., Common Crawl, books, code):

```
"The quick brown fox jumps over the lazy dog. Then..."
```

**Step 2: Create input-target pairs**

```
Pair 1:
  Input:  [The, quick, brown, fox, jumps, over, the, lazy, dog]
  Target: .

Pair 2:
  Input:  [quick, brown, fox, jumps, over, the, lazy, dog, .]
  Target: Then

Pair 3:
  Input:  [brown, fox, jumps, over, the, lazy, dog, ., Then]
  Target: ...
```

Every position in the sequence becomes a training example (using [[Causal Masking|causal masking]], each position only sees earlier tokens).

**Step 3: Forward pass**

Feed the input tokens through the transformer. The output is logits (prediction scores) for the next token at each position.

Focus on the last position (where we're predicting the target).

**Step 4: Compute loss**

Compare the model's prediction to the actual target using [[Cross-Entropy Loss|cross-entropy]]:

$$\text{Loss} = -\log(\text{P(target)}$$

If the model predicted the right token with high confidence, loss is low. If it got it wrong or was uncertain, loss is high.

**Step 5: Backpropagate and update**

Update weights to reduce the loss.

**Step 6: Repeat**

Train on billions of examples until the model learns to predict well.

---

## Example: Training on Arithmetic

In grokking experiments, next-token prediction is adapted to modular arithmetic:

**Input sequence:** `[37, +, 61, =]`

**Target:** `1` (because 37 + 61 = 98 ≡ 1 mod 97)

The model reads:
- Token 0: "37"
- Token 1: "+"
- Token 2: "61"
- Token 3: "="

And predicts:
- Token 4: "?" (the answer)

This is exactly next-token prediction, but on synthetic mathematical sequences instead of natural language.

**During training:**

1. The model sees `[37, +, 61, =]` thousands of times.
2. It learns to predict `1`.
3. When shown `[22, +, 34, =]`, it initially guesses randomly.
4. With weight decay (in AdamW), it eventually grokks the **underlying rule** instead of memorizing.
5. Suddenly, it can predict the answer for unseen combinations (generalizes).

---

## Why It Matters for Grokking

### Connection 1: Same Objective, Smaller Scale

Grokking uses next-token prediction on toy arithmetic, just as large language models use it on text.

The difference is scale and domain:

| Aspect | LLM | Grokking |
|--------|-----|----------|
| Domain | Natural language | Modular arithmetic |
| Dataset size | Billions of tokens | Thousands of examples |
| Model size | Billions of parameters | ~100K parameters |
| Task | Predict next word | Predict operation result |
| Generalization | To unseen texts | To unseen number pairs |

The core mechanism is identical.

### Connection 2: Understanding Generalization

In LLMs, we ask: "How do models generalize to unseen text when trained only on data loss?"

In grokking, we ask: "How do models generalize to unseen number pairs when trained on memorization?"

Grokking is a controlled experiment on this question. By isolating next-token prediction on toy data, we can watch generalization happen in slow motion.

### Connection 3: Emergent Capabilities

Just as LLMs develop reasoning from predicting text, the toy transformer develops **algorithmic capability** from predicting the result of modular arithmetic.

> [!NOTE]
> Grokking is mechanistic interpretability applied to next-token prediction at tiny scale. It asks: "What circuit does the model build when solving this next-token task?"

---

## Causal Masking Is Essential

Next-token prediction **requires** [[Causal Masking|causal masking]] to work fairly.

### Why

Without causal masking, the model could "cheat":

```
Input:  [The, cat, sat, on, the]
Target: mat
```

The model sees the whole sequence **including "mat"** at position 6. It could learn:

"When I see [The, cat, sat, on, the, mat], the next token is... something."

This is memorization, not generalization. On new sequences, it fails.

### With Causal Masking

The model can only see positions **up to the target position**:

```
Position 5 (where we predict "mat"):
  Can see: [The, cat, sat, on, the]
  Cannot see: mat (that's what we're predicting)
```

The model must predict "mat" using **only** context from earlier tokens. This forces true understanding.

**During generation:** The same rule applies. When generating position 6, the model can only use positions 1–5. This ensures training and inference are consistent.

---

## Distribution Shift Between Training and Inference

### Challenge: Exposure Bias

During training, the model always sees the **correct previous tokens**:

```
Train position 2: Input = [The, cat]          (correct)
                  Predict: sat
```

But during generation, it sees **its own predictions** (which might be wrong):

```
Test position 1: Model predicts "the"         (wrong)
Test position 2: Input = [The, the]           (wrong context!)
                 Predict: ? (now confused)
```

If the model made an error at position 1, it must recover from that error. It was never trained on its own mistakes.

This is **exposure bias** or **distribution shift**.

### Mitigation

- **Scheduled sampling:** Sometimes feed the model its own predictions during training.
- **Large-scale training:** Exposure to enough diverse data that the model learns to be robust.
- **Beam search:** At test time, keep multiple hypotheses to hedge against early errors.

In grokking experiments, this isn't a big issue because sequences are short (4 tokens) and the task is fully deterministic (no ambiguity).

---

## Connection to Other Training Objectives

### Masked Language Modeling (MLM)

Used in BERT:

```
Input:  [The, [MASK], sat, on, the, mat]
Target: cat
```

The model sees **all positions** (bidirectional). It must predict the masked word.

**Difference from next-token prediction:**
- MLM sees future context.
- Next-token prediction doesn't.

MLM is good for understanding; next-token is good for generation.

### Supervised Fine-Tuning (SFT)

After pre-training on next-token prediction, models are sometimes fine-tuned on specific tasks with human labels.

Example:

```
Input:  "Summarize this essay in one sentence:"
Target: [human-written summary]
```

But the foundation is **next-token prediction** on massive data.

---

## Why Scaling Works

A remarkable empirical finding: **bigger models are better at next-token prediction.**

This suggests the objective has a rich structure:

- At 1M parameters: memorize patterns.
- At 10M parameters: learn shallow rules.
- At 100M parameters: learn deeper reasoning.
- At 1B+ parameters: develop world knowledge.

Each scale unlock new capabilities.

> [!TIP]
> Scaling is not magic. It's that next-token prediction is a deep problem. Larger models can learn richer representations and more complex algorithms.

---

## Analogy — Jigsaw Puzzle

Imagine teaching someone to complete jigsaw puzzles:

**Training:** Show them 10,000 partially-filled puzzles. For each, they predict the next piece.

- Puzzle 1: [corner piece, edge piece, edge piece, ?]
- Puzzle 2: [red piece, red piece, blue piece, ?]
- ...

After training on many puzzles, the person learns:

- Corner pieces fit in corners.
- Edges connect to edges.
- Color is important.
- Shape matters.

Now, given a new puzzle, they can predict what piece comes next **without memorization** — they've learned the **underlying rules** of puzzles.

**Next-token prediction** is learning puzzle-completion by doing it billions of times.

---

## Important Terms

**Token** — A unit of input (word, sub-word, or number) that the model processes.

**Logits** — Raw prediction scores (before probabilities). Highest logit = model's top prediction.

**Cross-entropy loss** — A loss function measuring how wrong the model's prediction was compared to the actual token.

**Perplexity** — A metric of next-token prediction quality. Lower perplexity = better predictions. (Defined as $\text{exp}(\text{loss})$.)

**Autoregressive** — Generating one token at a time, feeding predictions back as input.

**Pre-training** — Training on next-token prediction on massive unlabeled data.

**Fine-tuning** — Additional training on specific tasks or labeled data.

**Distribution shift** — When training and test distributions differ (e.g., correct tokens vs. predicted tokens).

**Exposure bias** — The model trained on correct tokens but tests on its own (possibly wrong) predictions.

---

## Common Mistakes

**Mistake 1:** "Next-token prediction is too simple to produce intelligent models."

**Reality:** The objective is simple, but it's deep. Billions of examples + massive scale unlock remarkable capabilities.

**Mistake 2:** "Models memorize the training data."

**Reality:** Models memorize some, but mostly learn generalizable patterns. Evidence: they work well on unseen data.

**Mistake 3:** "Large language models are just doing pattern matching."

**Reality:** Pattern matching is what learning is. But the patterns learned are sophisticated (world knowledge, reasoning, code generation).

**Mistake 4:** "Grokking contradicts the next-token prediction objective."

**Reality:** Grokking is next-token prediction on toy data. The model initially memorizes; weight decay pushes it toward the generalizable solution.

---

## Key Takeaways

- **Next-token prediction** is the training objective: given context, predict the next token.
- It's self-supervised, requiring no human labels.
- Scaling this objective to trillions of tokens produces LLMs with world knowledge and reasoning.
- [[Causal Masking|Causal masking]] ensures that training is fair (no peeking at the answer).
- In grokking, next-token prediction on toy arithmetic reveals the circuit models build to solve the task.
- The simplicity of the objective belies the depth of what can be learned.

---

## Related Notes

- [[Transformer]] — the architecture trained with next-token prediction.
- [[Causal Masking]] — the mechanism ensuring fair next-token prediction.
- [[Language Models]] — models trained primarily on next-token prediction.
- [[Training Objectives]] — other objectives (MLM, supervised fine-tuning, reinforcement learning).
- [[Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets|Grokking]] — next-token prediction on modular arithmetic revealing phase transitions.
