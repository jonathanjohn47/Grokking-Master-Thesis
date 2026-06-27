---
tags: [concept, llm, generalization, in-context-learning, foundations]
---
↑ Parent: [[Decoder-Only Dominance]] · Related: [[Attention Mechanism]] · [[Grokking]] · [[Emergence]]

# Few-Shot Learning

## What Is It?

**Few-shot learning** is the ability of an AI model to solve a new task after seeing only a small number of examples — without any retraining or parameter updates.

You show the model a handful of examples inside the prompt. The model reads them, figures out the pattern, and applies it to a new input it has never seen.

> [!NOTE]
> "Few-shot" literally means "a few attempts." The model learns from a few examples, just as a human might.

There are three closely related versions of this idea:

- **Zero-shot** — The model gets no examples at all. You just describe the task in plain English and ask it to do it.
- **One-shot** — The model gets exactly one example.
- **Few-shot** — The model gets a small number of examples (typically 2–10).

All three are forms of **in-context learning** — the model learns from what is written in the prompt, not from changing its weights.

---

## Why Does It Exist?

### The Old Problem

Before few-shot learning existed, adapting an AI model to a new task was expensive and slow.

Here is what you had to do:

1. **Collect labelled examples.** A human had to manually label hundreds or thousands of examples for the new task.
2. **Design a new output layer.** The model needed a new "head" — a special component designed just for that task.
3. **Fine-tune the model.** You had to run training again for days or weeks.
4. **Deploy a separate model.** Every new task needed its own trained version of the model.

This meant that getting an AI to do something new was a project in itself — one that required time, data, compute, and engineering.

### The New Solution

Few-shot learning removes almost all of this. You give the model a few examples in plain text, and it figures out what to do. No retraining. No new output layer. No labelled dataset. No engineering.

This was the breakthrough that GPT-3 demonstrated in 2020 — and it changed how the entire field of AI thought about language models. See [[Decoder-Only Dominance]] for the full historical story.

---

## How Does It Work?

### Step by Step

**Step 1 — You write a prompt.**

The prompt contains:
- A short description of the task (optional but helpful).
- A few examples of inputs and correct outputs.
- The new input you want the model to handle.

**Step 2 — The model reads the whole prompt.**

The model processes everything in its **context window** — the full text of the prompt, from the first word to the last.

**Step 3 — The model recognises the pattern.**

By reading the examples, the model identifies the pattern: *"Given input of this shape, the correct output has this shape."*

**Step 4 — The model applies the pattern to the new input.**

It produces the output that fits the pattern — without any weights changing, without any retraining.

> [!NOTE]
> Nothing inside the model changes during few-shot learning. The model's weights stay exactly the same. The "learning" happens entirely inside the context window, not inside the model itself.

---

### The Mechanism: Induction Heads

How does the model actually recognise patterns in the prompt? The answer is **induction heads** — a type of attention circuit discovered inside transformer models.

An induction head does the following:

1. It notices when a pattern has appeared before in the context.
2. It predicts that the pattern will continue in the same way.

For example: if the prompt shows `A → B` three times, an induction head will notice *"every time I see A, I should predict B"* and apply this to the next occurrence of A.

This mechanism is built into the model through training — it is not specifically programmed. It emerges naturally from training on next-token prediction at scale.

See [[Attention Mechanism]] for a full explanation of how attention and induction heads work.

> [!TIP]
> Think of an induction head as a pattern-completion circuit. It is the mechanism that lets the model say: "I've seen this pattern before. I know how it ends."

---

## A Simple Example

Here is what a few-shot prompt actually looks like.

**Task: Sentiment classification (is a sentence positive or negative?)**

```
Sentence: "I loved this movie, it was fantastic."
Sentiment: Positive

Sentence: "The food was terrible and the service was rude."
Sentiment: Negative

Sentence: "This book changed my life."
Sentiment: Positive

Sentence: "I wasted two hours watching that film."
Sentiment:
```

The model reads the three examples and figures out the pattern: short descriptions of experiences map to either "Positive" or "Negative." It then applies that pattern to the fourth sentence and outputs: **Negative**.

No training on sentiment classification. No labelled dataset. Just three examples in a prompt.

---

### Zero-Shot Version of the Same Task

You can also skip the examples entirely:

```
Classify the sentiment of this sentence as Positive or Negative.

Sentence: "I wasted two hours watching that film."
Sentiment:
```

A large enough model will still answer correctly — because it has seen so much text during training that it already understands what sentiment classification means.

---

## Analogy

Imagine you are a new employee on your first day. Your manager shows you three completed invoices: how they are formatted, what goes in each field, and what a correct finished invoice looks like. Then they hand you a new invoice to complete.

You don't go back to school. You don't take a course. You just look at the examples, understand the pattern, and fill in the new invoice.

That is few-shot learning. The examples in the prompt are your training. The new input is your test. The output is your answer.

A zero-shot model would be like a new employee who has worked in so many offices before that they already know what an invoice looks like — without needing any examples at all.

---

## Why Did This Only Work with Large Models?

Few-shot learning did not work well with small models. Smaller models saw the examples but could not reliably recognise and apply the pattern.

This is an **emergent capability** — it appeared suddenly above a certain model size threshold. Models below this threshold performed near-randomly. Models above it performed impressively. There was no smooth transition.

This is directly related to [[Emergence]] and [[Phase Transition]]: the capability existed in neither small nor medium models, and then suddenly appeared in large ones — not as a gradual improvement, but as a jump.

The [[Neural Scaling Laws]] (Kaplan et al. 2020) describe how increasing model size, data, and compute leads to predictable improvement in next-token prediction. But few-shot capability is not just improvement — it is a qualitative jump that emerges from scale.

> [!WARNING]
> You cannot assume that because a small model fails at few-shot learning, a large model will also fail. Emergent capabilities do not follow the same smooth improvement curve as other metrics. This is one of the most surprising findings in modern AI research.

---

## Connection to Grokking

Few-shot learning and [[Grokking]] are deeply related. Both describe a model suddenly "getting" a rule from examples.

In **grokking**: the model sees many training examples of modular arithmetic. For thousands of steps, it only memorises them. Then suddenly, it discovers the underlying rule and generalises to examples it has never seen.

In **few-shot learning**: the model sees a handful of examples in the prompt. It immediately recognises the pattern and applies it to a new input.

Both are stories about a model extracting a general rule from a set of examples. Grokking is the slow, training-time version. Few-shot learning is the fast, inference-time version.

The mechanism underlying both is the same family of attention circuits — particularly induction heads. See [[Attention Mechanism]] for the mechanistic explanation, and [[Mechanistic Interpretability]] for the field that studies these circuits.

> [!TIP]
> One way to think about it: grokking is what happens when a model learns to do few-shot learning from scratch, during training. The model builds the circuits that enable pattern recognition — and once those circuits are in place, few-shot learning becomes possible.

---

## Connection to the Decoder-Only Revolution

Few-shot learning is only possible because of the decoder-only architecture and its training objective.

Here is why:

- **The causal language model** trains on predicting the next token. This means the model constantly practices: *"given everything I've seen so far, what comes next?"* — which is exactly what few-shot learning requires.
- **The context window** is where the examples live. A decoder-only model reads the full context window before producing each token, so it naturally processes all the examples you provide.
- **No fine-tuning needed** — the architecture already supports in-context adaptation through induction heads.

Encoder-only models like BERT cannot do few-shot learning in this sense. They produce a fixed-size embedding — not a sequence of tokens — so there is no natural way to give them examples and ask them to continue the pattern.

See [[Decoder-Only Dominance]] for why this architectural difference shaped the entire history of modern AI.

---

## What Came After Few-Shot Learning

Few-shot learning (GPT-3, 2020) opened the door to what came next:

- **Instruction tuning** — fine-tuning a model on thousands of task descriptions written in plain English, so that zero-shot performance improves dramatically. The model gets better at following instructions it has never seen.
- **[[RLHF|Reinforcement Learning from Human Feedback (RLHF)]]** — using human ratings of model outputs to further improve helpfulness, accuracy, and safety. This is what turned GPT-3 into ChatGPT.
- **Chain-of-thought prompting** — showing the model examples where the reasoning steps are written out explicitly, prompting the model to reason step by step rather than jumping straight to an answer.

All of these build on the core insight of few-shot learning: the model can adapt to new tasks through what you put in the prompt.

---

## Important Terms

| Term | Simple Definition |
|------|------------------|
| **Few-shot learning** | Solving a new task from a small number of examples in the prompt |
| **Zero-shot learning** | Solving a task with no examples at all — just a description |
| **One-shot learning** | Solving a task from exactly one example |
| **In-context learning** | The general ability to adapt from examples written in the prompt |
| **Prompt** | The text you give to the model as input |
| **Context window** | The full text the model can see at once before generating a response |
| **Induction head** | An attention circuit that recognises and completes repeating patterns |
| **Fine-tuning** | Retraining a model on new data to specialise it for a task |
| **Emergent capability** | An ability that appears suddenly above a scale threshold, not gradually |
| **Chain-of-thought** | A prompting technique where you show the model examples with step-by-step reasoning written out |

---

## Common Mistakes and Misconceptions

> [!WARNING]
> **"The model is learning from the examples."**
> Not in the usual sense. The model's weights do not change. It is not updating its parameters. It is pattern-matching inside its context window using circuits built during pre-training.

> [!WARNING]
> **"More examples always help."**
> Not always. Beyond a certain number of examples, performance can plateau or even degrade, especially if the examples are redundant or confusing. Quality and clarity of examples matters more than quantity.

> [!WARNING]
> **"Few-shot learning works the same at all model sizes."**
> No. It is an emergent capability. Small models get very little benefit from in-context examples. The ability only reliably appears at large scales.

---

## Key Takeaways

- Few-shot learning is the ability to solve a new task from a small number of examples in the prompt — **no retraining required**.
- It works through **induction heads** — attention circuits that recognise patterns in the context window and complete them.
- It is an **emergent capability** — it did not exist in small models and appeared suddenly in large ones.
- GPT-3 (2020) demonstrated this at scale, changing the entire economics of NLP: tasks that previously required labelled datasets and fine-tuning could now be solved with a short prompt.
- It is deeply connected to **[[Grokking]]**: both are stories about a model extracting a general rule from examples. Grokking is the training-time version. Few-shot learning is the inference-time version.
- Everything in modern AI that followed — instruction tuning, RLHF, ChatGPT — builds on this foundation.

---

## Related Notes

- [[Decoder-Only Dominance]] — why decoder-only models enabled few-shot learning
- [[Attention Mechanism]] — how induction heads work mechanistically
- [[Grokking]] — the training-time parallel to few-shot learning
- [[Emergence]] — few-shot learning as an emergent capability at scale
- [[Phase Transition]] — the sudden appearance of few-shot ability above a size threshold
- [[Neural Scaling Laws]] — the scaling laws that made few-shot learning predictable at large scale
- [[Mechanistic Interpretability]] — the field studying the circuits behind few-shot learning
- [[Generalization]] — few-shot learning as rapid generalisation from minimal evidence
- [[RLHF]] — the post-training technique that builds on the few-shot foundation
- [[Transformer]] — the architecture that makes in-context learning possible
