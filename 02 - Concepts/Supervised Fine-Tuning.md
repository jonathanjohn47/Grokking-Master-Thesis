---
tags: [concept, training, language-models, ai]
---
↑ Parent: [[Language Models]] · Learning path: [[04 - Core Experimental Setup]]

# Supervised Fine-Tuning

## What Is It?

**Supervised fine-tuning (SFT)** is a training process where you take a model already trained on a broad objective (like [[Next-Token Prediction|next-token prediction]]) and train it further on **labeled task-specific data** to make it better at that specific task.

```
Pre-trained model (trained on billions of tokens)
         ↓
    Fine-tuning (trained on 10K-100K labeled examples)
         ↓
    Task-specific model (optimized for that task)
```

---

## Why Does It Exist?

### Pre-training vs. Fine-tuning

**Pre-training:**
- Objective: [[Next-Token Prediction|Next-token prediction]] on huge, diverse datasets.
- Result: General knowledge, reasoning, language understanding.
- Cost: Massive compute (weeks/months on thousands of GPUs).

**Fine-tuning:**
- Objective: Specific task performance (question answering, summarization, instructions).
- Data: Curated labeled examples (expensive but smaller scale).
- Cost: Much cheaper (hours/days on small GPUs).

### The Strategy

1. **Expensive pre-training once** (shared knowledge).
2. **Cheap fine-tuning** for each task (task-specific adaptation).

Much more efficient than training separate models for each task.

---

## Intuition

Imagine learning to drive:

**Pre-training (general knowledge):**
- Learn physics: how cars work, friction, momentum.
- Learn safety: traffic laws, road signs, hazards.
- Practice: normal driving, different weather, various roads.
- Cost: Years of practice.

**Fine-tuning (taxi driving):**
- You already know driving.
- Now practice: efficient routes, passenger comfort, regulations.
- Cost: Few weeks of practice.

You don't re-learn physics; you build on existing knowledge.

**Pre-trained language models work the same way.**

---

## How Does It Work?

### Step 1: Start with Pre-trained Model

Model trained on [[Next-Token Prediction|next-token prediction]]:

```
Input: "The capital of France is"
Output (probability distribution): [Paris: 0.8, London: 0.05, Berlin: 0.02, ...]
```

The model already knows facts and patterns.

### Step 2: Prepare Task-Specific Data

Collect labeled examples for your task:

```
Example 1:
  Input: "Summarize this article: [article text]"
  Target: "[summary]"

Example 2:
  Input: "Translate to French: Hello, how are you?"
  Target: "Bonjour, comment allez-vous?"

Example 3:
  Input: "Solve: 2 + 3 = ?"
  Target: "5"
```

Each example shows: input → desired output.

### Step 3: Fine-tune the Model

Train the pre-trained model on your labeled data:

```
Loss = - log P(target | input)

For each example:
  1. Compute prediction (forward pass).
  2. Compare to target (compute loss).
  3. Backpropagation (compute gradients).
  4. Update weights (small learning rate, ~10× smaller than pre-training).

Repeat for all examples, multiple epochs.
```

### Step 4: Deploy

Use the fine-tuned model on new examples:

```
User input: "Summarize this text..."
Fine-tuned model: [outputs summary]
```

---

## Example: ChatGPT-Style Training

**Pre-training phase (OpenAI):**
- Objective: Predict next token on 300B+ tokens from diverse internet text.
- Model: GPT-3.5 (175B parameters).
- Cost: ~100+ GPU-years.
- Result: Capable but not aligned with human values.

**Supervised fine-tuning phase:**
- Data: ~10K high-quality examples (instruction-response pairs) written by humans.
- Objective: Predict good responses given instructions.
- Model: Same GPT-3.5, updated weights.
- Cost: ~100 GPU-hours (1000× cheaper).
- Result: ChatGPT (follows instructions, more helpful, safer).

**Reinforcement Learning phase (optional):**
- Further align using human preference feedback.
- Result: Even better alignment.

Without fine-tuning, the model would be much less useful (more likely to be unhelpful, unsafe, or incoherent).

---

## Learning Rate in Fine-tuning

**Critical:** Use a **much smaller learning rate** than pre-training.

### Why?

Pre-trained weights are already good. You want to adapt them slightly, not overwrite them.

```
Pre-training learning rate: 1e-4 (larger, broad optimization)
Fine-tuning learning rate: 1e-5 or 1e-6 (smaller, gentle adjustment)

10× smaller or more.
```

If you use pre-training's learning rate during fine-tuning:
- Model forgets pre-trained knowledge.
- Overfits to the small fine-tuning dataset.
- Performs worse, not better.

---

## Data Requirements

### Pre-training

Needs massive data (billions+ of tokens) to work well. Small datasets don't teach broad knowledge.

### Fine-tuning

Much less data needed. Studies show:

- 100 examples: Some improvement.
- 1K examples: Noticeable improvement.
- 10K examples: Strong task performance.
- 100K+ examples: Diminishing returns.

**Why fine-tuning needs less data:**

The model already understands language, facts, reasoning. It just needs to adapt these to your task.

---

## Fine-tuning Strategies

### Full Fine-tuning

Update **all** weights in the model.

**Pros:** Maximum adaptation to task.
**Cons:** Requires lots of GPU memory. Risk of forgetting pre-trained knowledge.

### Parameter-Efficient Fine-tuning

Update only a small fraction of weights (e.g., using LoRA, adapters, prefix tuning).

**Pros:** Much less memory/compute. Less risk of forgetting.
**Cons:** Slightly less adaptation.

**Modern practice:** Often use parameter-efficient methods for large models.

---

## Common Pitfalls

### 1. Too Large Learning Rate

Model forgets pre-training. Fine-tuning doesn't help or hurts performance.

**Fix:** Use 10-100× smaller learning rate than pre-training.

### 2. Overfitting on Small Dataset

With small labeled dataset and large model, risk overfitting.

**Fix:** Use [[Regularization|regularization]], early stopping, data augmentation.

### 3. Domain Mismatch

If pre-training data and fine-tuning data are very different:

- Example: Pre-train on English news, fine-tune on medical documents.
- The model's pre-trained knowledge may not transfer well.

**Fix:** If possible, use pre-training data similar to your domain.

### 4. Catastrophic Forgetting

Fine-tuning on one task can degrade performance on other tasks.

**Fix:** Multi-task fine-tuning or continual learning approaches.

---

## Fine-tuning vs. Prompting

Modern LLMs can do two things:

**Prompting (no training):**
```
Prompt: "Summarize: [article]. Summary: "
Output: [model generates summary directly]
```

No fine-tuning. Just write a good prompt.

**Fine-tuning (with training):**
```
Fine-tune on 1K summary examples.
Then: Input: "[article]"
      Output: [high-quality summary]
```

**When to use each:**

| Need | Prompting | Fine-tuning |
|------|-----------|-------------|
| Quick solution | ✓ | ✗ |
| Limited labeled data | ✓ | Maybe |
| High performance | ✗ | ✓ |
| Cost-sensitive | ✓ | ✗ |
| Domain-specific | ~ | ✓ |

---

## Fine-tuning in Research

Many grokking and mechanistic interpretability papers fine-tune models:

1. **Train base model** on modular arithmetic.
2. **Fine-tune on different operation** or dataset.
3. **Study how solution transfers** between tasks.

This reveals whether learned algorithms are **general** or **task-specific**.

---

## Analogy — Tuning an Instrument

Imagine a piano that's already roughly tuned:

**Pre-training:** Initial tuning by the factory (broad, general).

**Fine-tuning:** Musician adjusts specific notes for a concert (task-specific).

The musician doesn't retune from scratch. They make small adjustments to optimize for the specific performance.

---

## Important Terms

**Supervised fine-tuning (SFT)** — Training on labeled task-specific data.

**Pre-trained model** — Model trained on broad, generic objective first.

**Transfer learning** — Using knowledge from one task to improve another.

**Domain** — The distribution of data (e.g., medical text, code, recipes).

**Catastrophic forgetting** — Loss of pre-trained knowledge when fine-tuning on new tasks.

**Parameter-efficient fine-tuning** — Methods updating only a subset of weights (LoRA, etc.).

**Instruction fine-tuning** — Fine-tuning on instruction-response pairs (used in ChatGPT).

---

## Common Mistakes

**Mistake 1:** "Fine-tuning is training a new model from scratch."

**Reality:** Fine-tuning starts from a pre-trained model. It's adaptation, not from-scratch learning.

**Mistake 2:** "Bigger learning rate makes fine-tuning faster."

**Reality:** Bigger learning rate makes fine-tuning worse (forgets pre-training). Smaller is better.

**Mistake 3:** "You need fine-tuning for every task."

**Reality:** Modern large models often work well with prompting alone. Fine-tuning helps but isn't always necessary.

**Mistake 4:** "Fine-tuning requires as much data as pre-training."

**Reality:** Fine-tuning needs 10-1000× less data than pre-training.

---

## Key Takeaways

- **Supervised fine-tuning** adapts pre-trained models to specific tasks using labeled data.
- Uses **much smaller learning rate** than pre-training (10-100× smaller).
- Needs **much less data** than pre-training (100s-10Ks instead of billions).
- Efficient: leverage pre-training's knowledge, then customize for your task.
- Modern LLMs like ChatGPT = pre-training + SFT + RLHF.

---

## Related Notes

- [[Language Models]] — usually pre-trained, then fine-tuned.
- [[Next-Token Prediction]] — the pre-training objective.
- [[Training Objectives]] — SFT uses supervised loss on labeled data.
- [[RLHF]] — additional step after SFT for alignment.
- [[Transfer Learning]] — broader concept of which fine-tuning is an example.
