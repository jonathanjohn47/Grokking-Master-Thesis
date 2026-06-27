---
tags: [concept, training, machine-learning, objectives]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Training Objectives

## What Is It?

A **training objective** (or **loss function**) is a measure of how wrong the model's predictions are. The model is trained to minimize this objective.

Different objectives lead to different model behaviors. Choosing the right objective is fundamental to what the model learns.

---

## Why Does It Exist?

Without an objective, there's no way to guide training:

- How do we know if the model is getting better?
- What should it learn?
- How should we update weights?

A training objective provides a **numerical score** that measures performance. The model's job is to make this score as small (or large) as possible.

---

## Common Training Objectives

### 1. Next-Token Prediction (Language Modeling)

See: **[[Next-Token Prediction]]**

$$\text{Loss} = -\sum \log P(\text{next token} \mid \text{context})$$

**What the model learns:** Predict the next token given previous tokens.

**Used for:** Language models (GPT, Claude, LLaMA), grokking experiments.

**Why it works:** By predicting billions of tokens, the model learns language structure, facts, and reasoning.

---

### 2. Masked Language Modeling (MLM)

Used in **BERT** and similar models.

$$\text{Loss} = -\sum \log P(\text{masked token} \mid \text{context})$$

Instead of predicting the next token, mask a random token and predict it from **both sides** (left and right context).

**What the model learns:** Understanding text (both directions).

**Used for:** Classification, question answering (tasks requiring understanding, not generation).

**Difference from next-token prediction:** Bidirectional (can see future context) vs. unidirectional.

---

### 3. Contrastive Learning

$$\text{Loss} = -\log \frac{\exp(\text{similarity}(\text{anchor}, \text{positive}))}{\sum \exp(\text{similarity}(\text{anchor}, \text{negative}))}$$

**What the model learns:** Similar things should have similar representations; different things should be far apart.

**Used for:** Representation learning, embedding models, similarity learning.

**Example:** Training on sentence pairs where similar sentences should be close in vector space.

---

### 4. Supervised Fine-Tuning (SFT)

$$\text{Loss} = -\log P(\text{target output} \mid \text{input})$$

After pre-training on [[Next-Token Prediction|next-token prediction]], fine-tune on labeled task data.

**What the model learns:** To follow instructions, answer questions, complete specific tasks.

**Used for:** ChatGPT, Claude, etc. (pre-trained on language modeling, then fine-tuned with human-labeled examples).

**Data requirement:** Labeled examples (expensive to create).

---

### 5. Reinforcement Learning from Human Feedback (RLHF)

See: **[[RLHF]]**

$$\text{Loss} = -\mathbb{E}[\text{reward from human preferences}]$$

Train a reward model on human preferences, then fine-tune the language model to maximize this reward.

**What the model learns:** To produce outputs humans prefer (helpfulness, harmlessness, honesty).

**Used for:** Aligning LLMs with human values (ChatGPT-style models).

**Data requirement:** Human feedback (expensive but more scalable than labeling every example).

---

### 6. Reconstruction Loss (Autoencoders)

$$\text{Loss} = \| x - \text{reconstruction}(x) \|^2$$

**What the model learns:** Compress and reconstruct inputs. Forces the model to learn important features.

**Used for:** Learning representations, dimensionality reduction, anomaly detection.

---

### 7. Adversarial Loss (GANs)

$$\text{Loss}_{\text{generator}} = -\log P(\text{discriminator fooled})$$
$$\text{Loss}_{\text{discriminator}} = -\log P(\text{real}) - \log(1 - P(\text{fake}))$$

**What the model learns:** To generate realistic samples (generator) by competing with a discriminator.

**Used for:** Image generation, data synthesis.

---

## Connection to Grokking

In grokking experiments, the training objective is **[[Next-Token Prediction]]** on modular arithmetic:

```
Input: [37, +, 61, =]
Target: 1  (because 37 + 61 ≡ 1 mod 97)

Loss = -log P(1 | [37, +, 61, =])
```

Initially, the model memorizes the training data (low loss but poor generalization).

With weight decay, the model transitions to discovering the underlying **algorithmic pattern**, then generalizes to unseen examples.

---

## Why Choice of Objective Matters

### Example: Different Objectives, Different Models

**Objective 1:** Minimize reconstruction loss on images

→ Creates an autoencoder (compresses images)

**Objective 2:** Minimize classification error

→ Creates a classifier (recognizes object categories)

**Objective 3:** Minimize next-token prediction loss

→ Creates a language model (generates text)

Same architecture, different objective = completely different behavior.

---

## How to Choose an Objective?

1. **Ask: What do I want the model to do?**
   - Generate text? → Next-token prediction.
   - Understand text? → Masked language modeling.
   - Rank similarity? → Contrastive learning.
   - Follow instructions? → Supervised fine-tuning.

2. **Ask: What data do I have?**
   - Unlabeled text? → Next-token prediction.
   - Labeled pairs? → Supervised loss.
   - Human preferences? → RLHF.

3. **Ask: What behavior do I want?**
   - General knowledge? → Broad pre-training objective.
   - Specific task? → Task-specific fine-tuning objective.

---

## Analogy — Teaching by Example

Imagine teaching someone to cook:

**Objective 1 (Next-Token Prediction):**
"Here's a recipe. Predict the next step."

After 1000 recipes, they learn cooking patterns implicitly.

**Objective 2 (Supervised Fine-Tuning):**
"Cook this dish, and here's the correct way to do it."

They learn to follow specific instructions.

**Objective 3 (RLHF):**
"Cook anything. I'll taste it and tell you if it's good."

They learn to optimize for my preferences.

Different objectives → different learning → different skills.

---

## Important Terms

**Loss function** — A function measuring how wrong predictions are.

**Objective** — What the model is trying to optimize (minimize or maximize).

**Cross-entropy loss** — Standard loss for [[Next-Token Prediction|next-token prediction]]; measures difference between predicted and actual distributions.

**Pre-training objective** — Objective used for training on massive unlabeled data (e.g., next-token prediction).

**Fine-tuning objective** — Objective used for task-specific training on labeled data.

**Reward model** — In RLHF, a learned model that predicts human preferences.

---

## Common Mistakes

**Mistake 1:** "Any loss function works equally well."

**Reality:** Objective choice fundamentally affects what the model learns. Wrong objective = wrong behavior.

**Mistake 2:** "Pre-training objective and fine-tuning objective can be the same."

**Reality:** Usually different. Pre-training is broad (next-token prediction); fine-tuning is task-specific.

**Mistake 3:** "Minimizing loss always leads to good models."

**Reality:** You need the right objective. Memorizing training data minimizes loss but fails on test data.

---

## Key Takeaways

- **Training objectives** guide what models learn.
- **[[Next-Token Prediction]]** is the most common for language models and grokking.
- Different objectives suit different tasks and data.
- Choice of objective is a fundamental design decision.
- Grokking studies how models transition from a [[Memorization|memorization]] objective to a generalization objective with weight decay.

---

## Related Notes

- [[Next-Token Prediction]] — the primary objective for this vault's grokking experiments.
- [[Language Models]] — trained via next-token prediction.
- [[Supervised Fine-Tuning]] — task-specific training objective.
- [[RLHF]] — aligning models with human preferences.
- [[Cross-Entropy Loss]] — standard loss for next-token prediction.
- [[Mechanistic Interpretability]] — understanding what models learn under different objectives.
