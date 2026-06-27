---
tags: [concept, mechanistic, interpretability]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Mechanistic Interpretability

## What Is It?

Mechanistic interpretability is the science of **opening up a trained neural network and understanding exactly how it solves a problem**.

Think of it this way: when you train a neural network, it learns some algorithm to solve a task. Mechanistic interpretability is the detective work of figuring out **what that algorithm is**.

It's not enough to say "the network learned something." We want to understand the actual computation. We want to see the steps. We want to be able to explain the algorithm to another person.

## Why Does It Exist?

Neural networks are black boxes. They learn very well, but we often don't know *how* they learned.

When a network solves a problem, the learning happens inside the weights — the parameters the network adjusted during training. Those weights are huge, complicated, and hard to understand.

Scientists created mechanistic interpretability because:

1. **Understanding is useful.** If we know how a network works, we can improve it, fix it, and trust it.
2. **Debugging is easier.** If something goes wrong, understanding the algorithm helps us fix it.
3. **Knowledge transfer.** Once we understand one network's algorithm, we might apply that knowledge elsewhere.
4. **Science.** We want to understand how intelligence works, not just that it works.

## Intuition First: The Gearing Analogy

Imagine a network learning to add two numbers together.

Memorization would work like this:
- The network learns a lookup table: "1 + 1 = 2, 2 + 2 = 4, 3 + 3 = 6" and so on.
- It just memorizes every answer.
- This works only for numbers it has seen before.

Understanding the algorithm would work like this:
- The network learns *how to add*.
- It understands the concept: "put the numbers on a balance, spin them around, and read the result."
- This works for any two numbers.

Mechanistic interpretability is asking: "Does the network memorize, or does it actually understand the algorithm?"

And for [[Grokking|grokking]], researchers found something beautiful: **the network actually learns a real algorithm using geometric tricks** — it rotates numbers like angles on a circle, adds them, and reads the result. It's like a set of interlocking gears doing math.

## Formal Definition

**Mechanistic interpretability** is the study of how a trained neural network solves problems by reverse-engineering the actual computations it performs.

More precisely: we try to identify human-understandable **[[Circuit Formation|circuits]]** — groups of neurons and connections that work together to compute something meaningful — and explain how these circuits are organized to produce the network's output.

The goal is not just explanation. The goal is **checkable, step-by-step understanding**.

## How Does It Work?

### Step 1: The Residual Stream Concept

To understand mechanistic interpretability, we first need to understand the [[Residual Stream]] (a more detailed concept).

The residual stream is a flowing river of information inside a [[Transformer]] model.

Here's the basic idea:

> In a transformer, information flows through a special structure called the **residual stream**. Every component in the network reads from this stream and writes back to it.

Think of it like a shared workspace:

- **Reading:** A component picks out the information it needs.
- **Writing:** A component adds its output to the stream.
- **Passing on:** The updated stream flows to the next component.

The key insight: **every component adds information; nothing erases what came before.**

This means we can understand the network by studying each component independently. Each component is responsible for one small piece of the algorithm.

### Step 2: Finding Components That Work Together

Different components in the network cooperate. They form **circuits** — groups that work together to solve a problem.

A circuit might:
- Take in raw information from earlier layers
- Process that information through several attention heads and neural networks
- Output something meaningful to later layers

For example, one circuit might recognize "this is a digit," while another circuit learns "this digit should be added to that digit."

### Step 3: Identifying Features

A **feature** is a human-understandable concept that the network has learned.

Examples of features:
- "This token is a noun"
- "This number is odd"
- "This sentence is about sports"
- "The word 'the' just appeared"

Features are not stored in single neurons. Instead, they live as **directions** — patterns across many neurons working together.

This is similar to how colors in a painting are not single pixels, but patterns of many pixels working together.

### Step 4: Understanding How Components Compose

Components can **build on each other's work**. One component writes a feature to the residual stream. Another component reads that feature and uses it for its own computation.

There are three main ways components interact:

| Name | What It Does |
|------|--------------|
| **Q-composition** | Head A writes information that Head B uses in its Query computation |
| **K-composition** | Head A writes information that Head B uses in its Key computation |
| **V-composition** | Head A writes information that Head B uses in its Value computation |

These names refer to parts of the [[Attention Mechanism]]. Don't worry if you don't know what Q, K, V mean yet — the key point is that components can pass information through the residual stream in different ways.

### Step 5: Using Tools to Understand

Mechanistic interpretability researchers use several techniques to understand networks:

| Technique | What It Does |
|-----------|--------------|
| **Activation patching** | Swap one network's internal computations into another network to see which parts "carry" important information |
| **Weight visualization** | Look directly at the weights to find patterns (like periodic structures) |
| **Logit lens** | Break down the final answer into contributions from each component |
| **Ablation studies** | Turn off components one by one and see what breaks |

These tools turn vague intuitions into concrete evidence.

## Worked Example: Modular Arithmetic

Let's use a real example: [[Grokking|grokking on modular arithmetic]].

A researcher trained a network to compute $(a + b) \bmod p$ — that's "add two numbers and divide by p, then report the remainder."

### What They Found

The network didn't memorize. Instead, it learned a beautiful geometric algorithm:

1. **Convert to angles:** The network converts each number into an angle on a circle. Think of a clock face — 12 o'clock is 0, 3 o'clock is 25% around, and so on.

2. **Add the angles:** It adds these angles together (like spinning the clock hand further).

3. **Read the result:** It reads where the final angle points to get the answer.

This is exactly like how a mechanical calculator works — gears spinning and meshing to produce an answer.

### Why This Matters

This is not a memorization table. This is an algorithm. And researchers could:

- Draw a picture of the algorithm
- Verify each step
- Explain why it worked
- Predict what would break it

This is mechanistic interpretability: **understanding the actual computation**. [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Nanda et al. (2023)]] showed that the grokked [[Transformer]] implements $(a+b)\bmod p$ via a [[Fourier Features|Fourier transform over rotation angles]] — see [[Circuit Formation]].

## Real-World Application: Grokking Prediction

This understanding led to something powerful: **progress measures**.

### The Problem

When a network is [[Grokking|grokking]], there's a long plateau where training accuracy is high but test accuracy stays low. Then suddenly, it jumps to high accuracy.

How can we predict when the jump will happen? Looking at test accuracy won't help — it's flat for most of the plateau.

### The Mechanistic Solution

By understanding the algorithm (the Fourier circuit), researchers found internal quantities that signal progress:

- "How much are the network's representations aligned with the Fourier basis?"
- "How much have the internal features clarified?"

These quantities **rise during the plateau, before test accuracy jumps**.

This transforms grokking from "magic that suddenly happens" to "a predictable progression we can measure internally."

This is why mechanistic interpretability is so useful: it reveals things we couldn't see from outside the network. [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Researchers defined internal metrics]] that rise monotonically during the plateau *before* test accuracy moves. This is the proof of concept for all [[Grokking Predictors|grokking predictors]].

Additionally, researchers found that the grokked solution is a minimal structure. It uses fewer parameters (lower norm) than memorisation, which is why [[Varma - Explaining Grokking Through Circuit Efficiency|Varma et al.]] can explain grokking through circuit efficiency.

## Analogy: A Restaurant Kitchen

Imagine a restaurant where you can't see the kitchen. You only see:
- Food coming out (outputs)
- Ingredients going in (inputs)
- How much food was used (training time)

Mechanistic interpretability is like opening the kitchen door and seeing:
- How the head chef coordinates with the line cooks (component composition)
- How each cook has a specialty (features)
- How techniques are combined (circuits)
- Why a dish turns out a certain way (algorithm)

Instead of wondering "how does the chef do this?" we can watch the process step-by-step.

## Important Terms

**Residual stream:**
The main pathway for information flow inside a [[Transformer]]. Every component reads from it and writes to it. Think of it like a shared blackboard where all parts of the network contribute.

**Circuit:**
A group of neurons and connections that work together to perform one piece of computation. Similar to how a circuit in an electrical system performs a specific function.

**Feature:**
A human-understandable concept that the network has learned to represent. Features are encoded as directions across many neurons, not single neurons.

**Attention head:**
A small component of the attention mechanism (one of the key parts of transformers) that focuses on specific parts of the input.

**Activation patching:**
Swapping internal computations between two networks to identify which components are essential for a specific behavior.

**Ablation:**
Turning off or removing a component to see what breaks. Like removing one ingredient from a recipe to understand its role.

**MLP (Multi-Layer Perceptron):**
A simple neural network component that processes vectors and usually applies non-linear transformations. It's one of the main building blocks alongside attention.

## Common Mistakes and Misconceptions

> [!WARNING]
> **Misconception 1:** "Mechanistic interpretability means understanding every neuron."
>
> **Reality:** We don't need to understand individual neurons. Features are encoded across *many* neurons working together. We look for patterns and directions, not single neurons.

> [!WARNING]
> **Misconception 2:** "If we find one circuit, we understand the whole network."
>
> **Reality:** Networks have many circuits working in parallel and building on each other. Understanding the network requires mapping all the interactions.

> [!WARNING]
> **Misconception 3:** "Mechanistic interpretability only works for toy problems."
>
> **Reality:** We've applied it successfully to real [[Transformer]] models like GPT. However, larger models are harder to fully understand. This is an active research challenge.

> [!WARNING]
> **Misconception 4:** "Once we understand the algorithm, the network is solved."
>
> **Reality:** Understanding how a network works is just the beginning. We then need to predict how changes affect behavior, generalize to new tasks, and improve the network based on this knowledge.

## Why It Matters

Mechanistic interpretability answers critical questions:

1. **What did the network actually learn?** Not "did it memorize" but "what algorithm did it discover?"

2. **How can we predict grokking?** By tracking internal progress measures (we cover this in [[Grokking Predictors]]), we can predict when sudden improvements will occur.

3. **Why does [[Weight Decay]] help grokking?** Because the efficient algorithm (discovered through mechanistic analysis) has lower norm — it uses simpler weights than memorization. Weight decay pushes the network toward the efficient solution.

4. **Can we trust the network?** If we understand how it works, we can predict when it might fail and build more reliable systems.

## Limitations

> [!NOTE]
> **Current Challenges:**
>
> - **Task-specific:** Mechanistic interpretability was developed using modular arithmetic problems. We don't yet know if other tasks have equally clear, interpretable circuits.
> - **Scalability:** Large models like GPT-3 are much harder to understand than small networks. The number of components grows exponentially.
> - **Generalization:** Can progress measures for one task predict grokking on completely different tasks?
>
> These are active research questions.

## Key Takeaways

1. **Mechanistic interpretability is detective work.** We reverse-engineer neural networks to understand their algorithms.

2. **The key insight: the residual stream.** In transformers, information flows through a shared structure. Every component reads and writes to it. This makes analysis possible.

3. **Networks learn real algorithms.** For grokking, networks don't memorize — they discover geometric algorithms (like spinning angles on a circle).

4. **Understanding enables prediction.** Once we understand the algorithm, we can predict when grokking will occur by tracking internal progress measures.

5. **It works for real models.** While it started with toy problems, mechanistic interpretability has been applied to real language models like GPT.

6. **It's not complete yet.** Understanding larger models and more complex tasks remains an open challenge.

---

## Evidence and Research

**Primary paper:** [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — this paper discovered the Fourier circuit in modular arithmetic and introduced progress measures.

**Related research:**
- [[Varma - Explaining Grokking Through Circuit Efficiency]] — explains grokking through the efficiency of learned circuits
- [[Papyan - Prevalence of Neural Collapse]] — related structure found in deep classifiers
- [[Xu - Dynamics in Deep Classifiers with the Square Loss]] — dynamics during the final training phases
- [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] — using information theory to detect grokking

## Related Notes

- [[Circuit Formation]] — how components organize into functional circuits
- [[Feature Learning]] — how networks learn human-understandable concepts
- [[Fourier Features]] — the specific mathematical trick grokked networks use
- [[Attention Mechanism]] — key component of transformers that mechanistic interpretability studies
- [[Residual Stream]] — the main information pathway in transformers
- [[Transformer]] — the model architecture being interpreted
- [[Grokking Predictors]] — using mechanistic understanding to predict when grokking occurs
- [[Weight Decay]] — why it's effective, explained through mechanistic understanding
- [[Mechanistic Explanations]] — synthesis note covering the full interpretability framework
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — the foundational paper
- [[Varma - Explaining Grokking Through Circuit Efficiency]] — alternative explanation of grokking

## Open Questions

- Do mechanistic progress measures work equally well for other tasks beyond modular arithmetic?
- Can we automatically detect circuits across different tasks?
- How does mechanistic interpretability scale to very large models?
- Are there universal features learned by all networks, or is every solution unique?

