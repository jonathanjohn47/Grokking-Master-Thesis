---
tags: [learning-path, methodology, experiments]
---
← Previous: [[03 - Historical Background]]  ↑ Parent: [[00 - Start Here]]  → Next: [[05 - Memorization vs Generalization]]

# 04 - Core Experimental Setup

## What Is This Note About?

To study grokking scientifically, researchers needed a controlled experiment they could repeat reliably.

They designed an experiment that is deliberately **tiny and simple**. Small enough to run on a laptop. Simple enough that the correct answer to every question is known in advance.

This note explains the standard setup — what was used, why each choice was made, and what the knobs are that change the outcome.

---

## Why Use a Small, Controlled Experiment?

When studying a new phenomenon, it helps to start with the simplest possible case.

Imagine studying how fire behaves. You would not start with a forest fire. You would start with a candle. You can control everything about a candle: the wick length, the wax type, the wind. And you can observe it completely.

The grokking experiment is the candle version of studying generalisation.

---

## The Standard Grokking Experiment

### The Task: Clock Math

The most common task used in grokking experiments is **modular arithmetic** — specifically, addition on a "clock" with 97 positions instead of 12.

Here is how it works:
- Imagine a clock with positions 0 through 96 (that is 97 positions total).
- The task is: given two numbers *a* and *b*, what is *a + b* on this clock?
- For example: 50 + 60 = 110, but on a 97-position clock, 110 wraps around to 13 (because 110 - 97 = 13). So the answer is 13.

This is written as: (50 + 60) mod 97 = 13.

**Why this task?**
- There is an exact rule with a known correct answer for every possible question.
- If a network answers correctly on new questions, it *must* have learned the rule — there is no luck involved.
- It is simple enough that a tiny network with about 250,000 parameters can do it.

> [!NOTE]
> **Modular arithmetic** is the formal name for "clock math." The word "modular" refers to the idea of wrapping around. The number 97 is often used because it is a prime number, which has special mathematical properties that make the task clean and well-behaved.

---

### The Network: A Tiny Transformer

The experiments use a **transformer** — the same type of network used in large language models like ChatGPT, but tiny.

Specifically:
- 1 to 2 layers (large language models have dozens or hundreds)
- About 100,000 to 250,000 parameters (large models have billions)
- 4 attention heads (large models have many more)

**Why so small?**
- Small enough to fully observe. You can record every weight, every gradient, every activation at every training step.
- Small enough to run many experiments on a normal computer.
- Small enough that the cause of every behaviour can be traced.

A transformer reads the input as a sequence of tokens. For clock math, the input sequence is: [a, +, b, =]. The network reads this and predicts the answer at the "=" position.

> [!TIP]
> A **transformer** is a type of neural network that is very good at finding relationships between different parts of an input. Think of it as a network that can look at every word (or number) in a sequence and decide which other words are most relevant to understanding each word. It is the dominant architecture for modern AI systems.

---

### The Training Set: Deliberately Small

The researchers used only **30% of all possible questions** as training data. The remaining 70% were held out for testing.

This is unusual. Normally you want as much training data as possible. Here, the small training set is deliberate.

**Why use only 30%?**
- If you use too much training data, the network generalises immediately. There is no grokking — it just learns the rule from the start.
- If you use too little, the network can never generalise at all. There is not enough information.
- 30% is in the "grokking window" — just enough data that the network *can* eventually learn the rule, but the gap between memorisation and generalisation is long and observable.

---

### Training Duration: Very Long

The experiments run for 100,000 training steps or more.

This is important because grokking can happen anywhere from 10,000 to 100,000 steps after the training score hit 100%. You need patience.

---

### Weight Decay: The Main Knob

The single most important setting in the experiment is **weight decay** — a constant gentle pressure that keeps all the network's internal values (weights) small.

Experiments tested three levels of weight decay:
- **Zero weight decay (λ = 0):** Grokking often does not happen at all, or takes extremely long.
- **Low weight decay (λ = 0.01):** Grokking happens, but slowly.
- **High weight decay (λ = 1.0):** Grokking happens much faster. This became the standard setting.

> [!IMPORTANT]
> Weight decay is what makes grokking happen in a reasonable amount of time. It creates the pressure that slowly drives the network from the memorised solution to the generalised solution. Without it, the network can stay stuck in the memorised solution almost indefinitely.

---

## A Summary Table

| Setting | Typical Choice | Why |
|---------|---------------|-----|
| Task | Clock math (addition mod 97) | Exact rule, known correct answers, testable generalisation |
| Network | 1–2 layer transformer, ~250K parameters | Small enough to fully observe and run on a laptop |
| Training fraction | ~30% of all questions | Creates the grokking window: not too much, not too little |
| Training duration | 100,000+ steps | Grokking can take tens of thousands of steps after memorisation |
| Weight decay | 1.0 (high) | The main driver of grokking; without it, grokking may not happen |
| Optimiser | AdamW | A standard, well-understood training algorithm |

---

## Other Tasks Used

Researchers also tested grokking on other tasks to check if the findings are general:
- **Multiplication mod 97** (same clock, but multiplying instead of adding)
- **Parity** (given a list of numbers, is the count of odd numbers even or odd?)
- **XOR** (a simple logic operation)

These tasks let researchers check whether predictors and explanations work on many tasks, or only on the specific clock-addition task.

---

## What You Measure

**External measurements** (what you see from outside the network):
- Training accuracy (percentage of training questions answered correctly)
- Test accuracy (percentage of new questions answered correctly)
- Loss (a number measuring how wrong the network is)

**Internal measurements** (what you see by looking inside the network):
- The size of the weights (called the weight norm)
- Statistical patterns in the weight matrices (called spectral signatures)
- The randomness of gradient changes (called gradient entropy)
- How much information different layers share about the task (called mutual information)

The internal measurements are the key to predicting grokking, because the external measurements look flat during the plateau.

---

## Grokking Is Not Only in Transformers

One important discovery: grokking has been observed in systems that are **not** neural networks at all.

Researchers demonstrated grokking in **tensor networks** — a completely different type of mathematical model used in physics — on image classification tasks.

This shows that grokking is not a peculiarity of the transformer architecture. It is a more general property of how learning systems behave.

---

## Important Terms

**Modular arithmetic:** "Clock math." Adding or multiplying numbers on a number line that wraps around at a fixed point. (50 + 60) mod 97 = 13.

**Transformer:** A type of neural network that processes sequences by looking at relationships between all positions simultaneously. The dominant architecture in modern AI.

**Weight decay (λ):** A training technique that adds a gentle penalty for large weights. This keeps weights small and is the main driver of grokking.

**Training fraction:** The percentage of all possible questions used for training. In grokking experiments, this is deliberately kept small (around 30%).

**Spectral signatures:** Patterns found by analysing the mathematical properties of weight matrices. These can reveal information about a network's health and learning progress even when the accuracy scores are flat.

**Gradient entropy:** A measure of how random or predictable the gradient signals are. Can be used to detect changes in what the network is learning.

**Mutual information:** A measure of how much two things are related. In neural networks, it can measure how much information one layer is sharing with another about the task.

**Tensor network:** A mathematical model from physics, used to represent and compute with large amounts of information efficiently. Not a neural network, but capable of showing grokking.

---

## Key Takeaways

- The standard grokking experiment uses a tiny transformer doing clock math with 30% of possible questions as training data.
- The setup is deliberately small and controlled so every detail can be observed.
- Weight decay is the most important knob: without it, grokking often does not happen.
- The experiment uses 100,000+ training steps because grokking can take a very long time.
- Internal measurements (inside the network) are what reveal grokking is coming, not external scores.
- Grokking has been found in non-neural-network systems, showing it is a general learning phenomenon.

---

## Related Notes
- [[Common Datasets]] · [[Common Evaluation Metrics]]
- [[Experimental Designs Used in Literature]]
- [[Weight Decay]] · [[Grokking Predictors]]
