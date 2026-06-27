---
tags: [concept, scaling-laws, spectral, theory]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[12 - Modern Developments]]

# Neural Scaling Laws

## What Is It?

A **neural scaling law** is a simple rule that describes how well an AI model performs as you give it more resources.

The rule says: **the more resources you give a model, the better it gets — and the improvement follows a predictable mathematical pattern.**

The three main resources are:

- **Parameters ($N$)** — the number of adjustable numbers inside the model. More parameters = a bigger, more capable model.
- **Data ($D$)** — the number of training examples (for language models, measured in tokens — individual words or word pieces).
- **Compute ($C$)** — the total amount of computational work used for training, measured in floating-point operations (FLOPs).

The key finding: if you double the number of parameters, or double the training data, the model's error drops by a predictable amount — not randomly, not unpredictably, but according to a reliable mathematical formula.

> [!NOTE]
> "Empirical" means these laws were discovered by running experiments, not derived from pure theory. Researchers trained hundreds of models of different sizes and measured what happened. The smooth, consistent pattern they found is the scaling law.

---

## Why Does It Exist?

### The Problem It Solves

Training large AI models is extraordinarily expensive. A single training run for a large language model can cost millions of dollars and take months. You cannot just try random configurations and hope for the best.

Before scaling laws, researchers had no reliable way to answer questions like:

- *"If I make my model 10× bigger, how much better will it get?"*
- *"Should I spend my compute budget on more parameters or more training data?"*
- *"Is it worth training for longer?"*

Scaling laws gave researchers a **roadmap**. By fitting a formula to small experiments, they could predict what would happen at large scale — before spending millions of dollars. They could plan investments in AI the same way an engineer plans the construction of a bridge: with reliable formulas, not guesswork.

---

## How Does It Work?

### The Basic Idea

Run an experiment: train many models of different sizes on different amounts of data. Measure how accurate each model is at the end. Plot the results.

What you find is that the relationship between resources and performance follows a **power law**.

A power law is a relationship where doubling one thing doesn't double another, but it consistently multiplies it by some factor. For example: every time you double the number of parameters, the error might drop by about 10%. Every time you double the data, the error might drop by about 8%.

The formula discovered by Kaplan et al. (2020) and refined by Hoffmann et al. (2022, "Chinchilla") is:

$$L(N, D) \approx \frac{A}{N^\alpha} + \frac{B}{D^\beta} + L_\infty$$

In plain English:
- $L$ is the model's **loss** (its error — lower is better).
- $N$ is the number of **parameters**.
- $D$ is the amount of **training data** (in tokens).
- $\alpha$ and $\beta$ are small numbers (roughly 0.076 and 0.095) that describe how quickly the error drops as you scale up.
- $L_\infty$ is the **irreducible loss** — the minimum possible error, even with infinite resources. Some tasks are just hard; no model can be perfect.

> [!TIP]
> Don't worry about memorising the formula. The intuition is what matters: **both parameters and data matter, and each has diminishing returns** — doubling them helps, but the improvement gets smaller each time.

---

### The Two Bottlenecks

The formula has two separate terms — one for parameters, one for data. This reveals two separate bottlenecks:

**Bottleneck 1: Too few parameters.**
If your model is too small, it simply doesn't have enough capacity to represent what it has learned. No matter how much data you show it, it can't improve beyond a ceiling set by its size.

**Bottleneck 2: Too little data.**
If your model is large but trained on too little data, it memorises the small dataset and never learns to generalise. More parameters won't help if there isn't enough variety in what the model sees.

The critical insight from the Chinchilla paper (2022): **these two bottlenecks need to be balanced**. For a fixed compute budget, the best model is not the biggest one — it is the one where parameters and data are properly matched. Many earlier models (including the original GPT-3) were over-parameterised relative to how much data they were trained on.

---

### The Four Regimes

[[Bahri - Explaining Neural Scaling Laws]] gave a deeper theoretical explanation with four distinct regimes, depending on which resource is the current bottleneck:

| Regime | What Is Limiting? | What Happens to Loss | Why |
|---|---|---|---|
| **Parameter-limited** | Model too small | Loss $\propto N^{-\alpha}$ | Model can't represent complex patterns |
| **Data-limited** | Too little training data | Loss $\propto D^{-\beta}$ | Model overfits, can't generalise |
| **Resolution-limited** | Both are fine; task is hard | Loss $\propto D^{-\gamma}$ | High-frequency task features require lots of data to learn |
| **Variance-limited** | Near-infinite data | Slow scaling with $N$ | Model expressiveness becomes the ceiling |

The **resolution-limited** regime is especially interesting: it connects to [[Spectral Bias]] — the idea that models naturally learn smooth, simple patterns before learning complex, jagged ones. Tasks that are structured and smooth are easier to scale; tasks that are complex and irregular require much more data to improve.

---

## Simple Example

Imagine you are running a translation company, and you want to know how to improve your AI translator.

You run experiments:

- A model with 1 million parameters trained on 1 billion words achieves 20% error.
- A model with 10 million parameters trained on 1 billion words achieves 16% error.
- A model with 100 million parameters trained on 1 billion words achieves 13% error.
- A model with 100 million parameters trained on 10 billion words achieves 10% error.

You notice a pattern: each 10× increase in parameters drops error by about 3–4 points. Each 10× increase in data also drops error by a similar amount.

You now have a formula. You can extrapolate: *"A model with 1 billion parameters trained on 100 billion words should achieve roughly 6% error."* You can decide whether that improvement is worth the cost before building it.

That is what scaling laws do.

---

## Analogy

Think of training an AI model like filling a library.

- The **parameters** are the **number of shelves**. More shelves means you can store more knowledge.
- The **training data** is the **number of books** you fill the shelves with.
- The **loss** is how often the librarian gives you the wrong book.

The scaling law says:
- A bigger library (more shelves) makes the librarian better at their job — but only if you have enough books to fill it.
- More books help — but only if you have enough shelves to organise them.
- If you have a huge library with almost no books, the shelves are wasted. If you have a mountain of books but only a few shelves, they pile up uselessly on the floor.

The Chinchilla insight: don't build a giant library and fill it sparsely. Match the shelves to the books.

And the irreducible loss ($L_\infty$) is like the fact that some books are just badly written — no matter how organised your library is, some questions will never have a great answer.

---

## Scaling Laws vs Grokking: Two Very Different Stories

This is important for understanding the vault. Scaling laws and [[Grokking]] are almost opposites:

| | **Scaling Laws** | **Grokking** |
|---|---|---|
| What changes? | Model size, data, compute | Training time (model size stays fixed) |
| How does performance change? | Smoothly, predictably | Flat for a long time, then a sudden jump |
| Can you predict it? | Yes — reliable power-law formula | Hard — the jump is unpredictable without internal signals |
| What drives it? | Gradual compression of patterns across the data | Sudden formation of a generalisation circuit |

Scaling laws describe the **average, smooth improvement** you get by spending more resources. Grokking describes a **hidden, abrupt transition** that happens inside a single training run.

> [!TIP]
> A useful way to think about it: a scaling law tells you where a model will end up after training. Grokking describes what happens *during* training on the way there — which is often far stranger than the smooth curve suggests.

---

## Emergent Capabilities: When Scaling Laws Break Down

Scaling laws predict smooth improvement. But researchers have observed **emergent capabilities** — abilities that appear suddenly in large models, with almost no warning from the smooth curve.

Wei et al. (2022) documented many such examples: arithmetic, multi-step reasoning, code generation. Small models could not do these things at all. Then, above a certain size, they could — not gradually, but almost overnight.

Some researchers (Schaeffer et al., 2023) argued these jumps are measurement artefacts — an artefact of how performance is measured, not a genuine discontinuity.

The grokking perspective offers a third explanation: **emergent capabilities may be grokking events happening at large scale**.

The idea: inside a large model, a specific circuit for a capability (like multi-step arithmetic) forms suddenly, just as the Fourier circuit forms suddenly in a small grokking experiment. This jump is invisible in aggregate loss metrics — which average over thousands of tasks — but becomes visible when you test the specific capability directly.

If this is right, scaling laws describe the average, but the per-capability dynamics inside the model are governed by grokking-like circuit formation. See [[Emergence]] and [[Phase Transition]] for more on this idea.

---

## Why Scaling Laws Connect to Grokking Research

The tools used to understand scaling laws and the tools used to understand grokking overlap significantly:

- **[[Spectral Bias]]** — models learn low-frequency (smooth) patterns before high-frequency (complex) ones. This explains both why scaling laws have the shape they do and why grokking takes so long before the generalising circuit forms.
- **[[Random Matrix Theory]]** — a mathematical framework for understanding the properties of large weight matrices. It applies to both the theory of scaling laws and the analysis of what happens inside a model during grokking.
- **[[Feature Learning]]** — both scaling laws and grokking are ultimately about how a model learns to represent the features of its task. Scaling laws describe this at a macro level; grokking reveals it at the level of individual circuits.

The smooth scaling story and the abrupt grokking story are not contradictions — they are two regimes of the same underlying framework.

---

## Common Mistakes and Misconceptions

> [!WARNING]
> **"Bigger is always better."**
> Only if you also have enough data to match the size. A huge model trained on too little data is wasteful. Chinchilla showed that many famous models were under-trained relative to their size.

> [!WARNING]
> **"Scaling laws predict everything."**
> They predict smooth, average improvement in loss. They do not predict emergent capabilities, grokking events, or the behaviour of specific circuits inside the model.

> [!WARNING]
> **"The irreducible loss means scaling is useless beyond a point."**
> Not quite. The irreducible loss $L_\infty$ is the theoretical floor for a given task with a given training distribution. It does not mean progress stops — it means you may need better data or a better task formulation, not just more compute.

---

## Important Terms

| Term | Simple Definition |
|------|------------------|
| **Scaling law** | A mathematical rule describing how model performance improves with more resources |
| **Power law** | A relationship where doubling one thing multiplies another by a fixed factor (not doubles it) |
| **Parameters ($N$)** | The adjustable numbers inside a neural network — more parameters = bigger model |
| **Training tokens ($D$)** | The amount of text (or data) the model was trained on |
| **Compute ($C$)** | The total computational work used for training, in FLOPs |
| **Loss ($L$)** | A measure of the model's error — lower is better |
| **Irreducible loss ($L_\infty$)** | The minimum possible error, even with unlimited resources |
| **Bottleneck** | The resource that is currently limiting performance — fixing it gives the most improvement |
| **Chinchilla** | The 2022 paper (Hoffmann et al.) that showed parameters and data must be balanced |
| **Emergent capability** | An ability that appears suddenly above a scale threshold, not gradually |
| **FLOPs** | Floating Point Operations — the standard unit for measuring computational work |

---

## Key Takeaways

- Neural scaling laws describe a **predictable, smooth relationship** between model resources (parameters, data, compute) and model performance (loss).
- Performance follows a **power law**: each doubling of resources gives a consistent, diminishing improvement.
- There are **two bottlenecks** — too few parameters and too little data — and they must be balanced. The Chinchilla paper (2022) showed many famous models were oversized relative to their training data.
- Scaling laws are **smooth and predictable**. Grokking is **abrupt and surprising**. They describe the same system at different levels: the macro-average vs. the per-capability training dynamics.
- **Emergent capabilities** — sudden jumps in ability at large scale — may be grokking events hidden inside the smooth scaling average.
- The same theoretical tools ([[Spectral Bias]], [[Random Matrix Theory]]) explain both scaling laws and grokking, connecting the two phenomena at a deep level.

---

## Evidence

- Kaplan et al. (2020): "Scaling Laws for Neural Language Models" — the original power-law discovery.
- Hoffmann et al. (2022): "Training Compute-Optimal Large Language Models" (Chinchilla) — optimal parameter/data balance.
- Wei et al. (2022): "Emergent Abilities of Large Language Models" — documented sudden capability jumps.
- Schaeffer et al. (2023): challenged whether emergent capabilities are genuine discontinuities or metric artefacts.
- [[Bahri - Explaining Neural Scaling Laws]] — theoretical framework explaining *why* scaling laws have the shape they do.

---

## Relationship to Other Concepts

- [[Phase Transition]] and [[Grokking]] — the abrupt counterpart to smooth scaling.
- [[Double Descent]] — another non-monotonic surprise in how loss behaves with scale.
- [[Spectral Bias]] — explains the shape of scaling-law exponents via the data manifold spectrum.
- [[Neural Manifolds]] — the geometric view of what the model is learning as it scales.
- [[Random Matrix Theory]] — mathematical tools for analysing large weight matrices during scaling.
- [[Emergence]] — emergent capabilities at scale as potential grokking events.
- [[Feature Learning]] — what the model actually learns as resources increase.
- [[Decoder-Only Dominance]] — scaling laws were a key driver of decoder-only model dominance.
- [[Few-Shot Learning]] — few-shot ability is one of the emergent capabilities that appears with scale.

---

## Open Questions

- Is grokking a breakdown of smooth scaling — a hidden transition inside a scaling regime?
- Could emergent capabilities in large models be grokking-at-scale rather than smooth scaling?
- What determines the crossover between smooth scaling and abrupt grokking for a given task?
- Do scaling laws eventually plateau — and if so, does the path forward require qualitatively new architectures or just more data?

---

## Related Notes

- [[Bahri - Explaining Neural Scaling Laws]] · [[Spectral Bias]] · [[Double Descent]] · [[Phase Transition]]
- [[Emergence]] · [[Random Matrix Theory]] · [[Feature Learning]] · [[Grokking]]
- [[12 - Modern Developments]] · [[Future Directions]]
- [[Decoder-Only Dominance]] · [[Few-Shot Learning]]
