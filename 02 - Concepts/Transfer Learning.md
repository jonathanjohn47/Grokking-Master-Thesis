---
tags: [concept, machine-learning, training, fundamentals]
---
↑ Parent: [[Language Models]] · Related: [[Supervised Fine-Tuning]] · [[Representation Learning]] · [[Feature Learning]]

# Transfer Learning

## What Is It?

**Transfer learning** is the idea of taking knowledge a model learned from one task and **reusing it** on a different task.

Instead of training a model from scratch every time, you start with a model that already knows a lot — and then adapt it.

> [!TIP]
> Think of it as **not starting from zero**. If you already know how to ride a bicycle, learning to ride a motorbike is much easier. You transfer your existing knowledge.

---

## Why Does It Exist?

### The Problem With Training From Scratch

Training a neural network from zero requires:

* **Massive amounts of data** — millions or billions of examples.
* **Enormous compute** — hundreds of GPUs running for weeks.
* **Huge cost** — millions of dollars for large models.

Most people and organisations cannot afford this.

### The Solution

Transfer learning lets you:

1. Train a **large model once** on lots of data (this is called **pre-training**).
2. **Share** that model freely.
3. Let others **adapt** it cheaply for their own specific task (this is called **fine-tuning**).

> [!NOTE]
> This is how almost all modern AI is built. GPT-4, Claude, Gemini — all of these are pre-trained on huge datasets, then fine-tuned for specific uses.

---

## Intuition

### Analogy: Medical Specialist

Imagine training a doctor.

**Without transfer learning:**
- You would need to teach every doctor from absolute scratch.
- Each new doctor would have to re-learn biology, chemistry, anatomy, and everything else before specialising.

**With transfer learning:**
- All doctors first go to **medical school** — learning a broad base of knowledge.
- Then each doctor **specialises** (cardiology, surgery, etc.) using only a fraction of extra training.

The medical school degree is the **pre-trained model**.
The specialisation is the **fine-tuning**.

---

## How Does It Work?

### Step 1: Pre-Training

A large model is trained on a **large, general dataset**:

* For language models: billions of words from the internet, books, and websites.
* For image models: millions of labelled photographs.

The model learns **general features**:
* For language: grammar, facts, reasoning, writing style.
* For images: edges, shapes, textures, objects.

```
Large general dataset (billions of examples)
               ↓
         [Pre-training]
               ↓
    Pre-trained model (rich general knowledge)
```

---

### Step 2: Fine-Tuning

The pre-trained model is then adapted on a **smaller, task-specific dataset**:

* A customer service company fine-tunes on their support conversations.
* A hospital fine-tunes on medical notes.
* A law firm fine-tunes on legal documents.

```
Pre-trained model + small task-specific dataset
               ↓
          [Fine-tuning]
               ↓
    Specialised model (expert at this task)
```

> [!NOTE]
> Fine-tuning updates the model's weights based on the new data. The model keeps most of what it learned in pre-training and adjusts slightly for the new task.

---

## Worked Example

### Task: Classifying Movie Reviews as Positive or Negative

**Without transfer learning:**
- You would need to train a model from scratch.
- You would need hundreds of thousands of labelled reviews.
- Training might take days.

**With transfer learning:**
1. Start with a pre-trained language model (e.g. BERT, GPT).
2. Add a small **classification head** on top (a few extra layers).
3. Fine-tune on just a few thousand labelled movie reviews.
4. Achieve excellent results in hours.

The pre-trained model already understands words, grammar, and sentiment — you only need to teach it the final classification step.

---

## Real-World Applications

| Application | Pre-trained on | Fine-tuned on |
|---|---|---|
| Medical diagnosis | General image data | X-ray scans |
| Legal document review | General text | Legal contracts |
| Code generation | General text + code | Programming tasks |
| Customer chatbots | General language | Company FAQs |
| Sentiment analysis | General text | Product reviews |
| Translation | Multilingual text | Specific language pairs |

---

## What Gets Transferred?

### Low-Level Features (Early Layers)

In the first layers of a neural network, the model learns very basic patterns:

* In images: edges, corners, colours.
* In text: common words, basic grammar.

These are **universally useful** and transfer well to almost any task.

### High-Level Features (Later Layers)

Deeper layers learn more specific patterns:

* In images: faces, cars, animals.
* In text: complex reasoning, domain-specific vocabulary.

These are **more task-specific** and may need to be fine-tuned more carefully.

> [!TIP]
> A common strategy: **freeze** the early layers (don't update them) and only train the later layers. This is faster and requires less data.

---

## Types of Transfer Learning

### 1. Feature Extraction

* Take a pre-trained model.
* **Freeze all the weights** — don't update anything during training.
* Use the model as a fixed **feature extractor**.
* Only train a new small classifier on top.

Best when: your dataset is small and very different from the pre-training data.

---

### 2. Fine-Tuning

* Take a pre-trained model.
* **Unfreeze some or all weights**.
* Continue training on your new dataset with a small learning rate.
* The whole model adapts to the new task.

Best when: your dataset is similar to the pre-training data and large enough.

---

### 3. Domain Adaptation

* The model is adapted to a **new domain** (different type of data) rather than a completely different task.

Example: A model trained on news articles adapted to scientific papers.

---

## The Relationship to Grokking

Transfer learning is relevant to [[Grokking]] research in an indirect but important way:

* Grokking asks: *how does a model go from memorisation to true generalisation?*
* Transfer learning shows that **learned representations can transfer** — suggesting that grokking may correspond to the model discovering a transferable, structured representation of the task.
* When a model **groks** modular arithmetic, it learns an internal [[Fourier Features|Fourier-based circuit]] — a structured representation that is arguably more "general" and potentially more transferable than raw memorised answers.

> [!NOTE]
> See [[Representation Learning]] for more on how the structure of what a model learns relates to its ability to generalise.

---

## Analogy

### The Expert Who Moves Teams

Imagine a brilliant engineer who has spent 10 years building bridges.

They move to a new company that builds tunnels.

They don't start over. They bring their deep understanding of:
* Materials and structural forces.
* Project planning.
* Engineering mathematics.
* Safety standards.

They just need a few months to learn the specifics of tunnels.

That's transfer learning — the **deep general knowledge transfers**, and only the **surface specifics need learning**.

---

## Important Terms

**Pre-training:**
Training a model on a large general dataset before any task-specific training.

**Fine-tuning:**
Continuing training on a smaller, task-specific dataset after pre-training. See [[Supervised Fine-Tuning]].

**Frozen weights:**
Weights that are not updated during training. The model uses them as-is.

**Feature extractor:**
Using a trained model to convert raw inputs (images, text) into learned representations, without updating the model's weights.

**Domain:**
The type or style of data (e.g. medical text vs. news articles).

**Classification head:**
A small set of extra layers added on top of a pre-trained model to perform a specific classification task.

**Representation:**
The internal description a neural network builds for an input — usually a set of numbers in a hidden layer. See [[Representation Learning]].

---

## Common Mistakes and Misconceptions

> [!WARNING]
> **Misconception: "Fine-tuning always makes the model better."**
> Fine-tuning on bad or insufficient data can make the model worse. If the fine-tuning dataset is too small, noisy, or mislabelled, performance can degrade.

> [!WARNING]
> **Misconception: "Transfer learning replaces the need for data."**
> You still need task-specific data for fine-tuning. Transfer learning reduces how much you need, but does not eliminate it.

> [!WARNING]
> **Misconception: "The whole model needs to be fine-tuned."**
> Often, freezing early layers and only fine-tuning later ones works just as well and is much cheaper.

> [!WARNING]
> **Misconception: "Transfer learning only works for similar tasks."**
> Modern large language models trained on general text can be fine-tuned for very specific domains (medicine, law, code) even though those domains look quite different from the pre-training data.

---

## Key Takeaways

* Transfer learning means **reusing knowledge** from a previously trained model on a new task.
* It works because neural networks learn **general features** in early layers that are useful across many tasks.
* The two main steps are: **pre-training** (general, expensive) and **fine-tuning** (task-specific, cheap).
* Modern AI relies heavily on transfer learning — almost no large models are trained from scratch for specific applications.
* Freezing early layers and only updating later layers is a common efficient strategy.
* The connection to [[Grokking]] is through **representation learning** — both phenomena involve the model discovering structured, generalisable internal representations.

---

## Related Notes

- [[Supervised Fine-Tuning]] — the most common application of transfer learning
- [[Representation Learning]] — what gets transferred between tasks
- [[Feature Learning]] — how models learn useful features during training
- [[Language Models]] — the primary context where transfer learning is used today
- [[Generalization]] — the ultimate goal that transfer learning tries to achieve
- [[Grokking]] — delayed generalisation may involve discovering transferable representations
- [[Few-Shot Learning]] — a related paradigm for learning from very little data
