---
tags: [learning-path, core, generalization]
---
← Previous: [[04 - Core Experimental Setup]]  ↑ Parent: [[00 - Start Here]]  → Next: [[06 - Overparameterization and Interpolation]]

# 05 - Memorization vs Generalization

## What Is This Note About?

At the heart of grokking is a competition between two completely different ways of getting the right answer.

Both ways score 100% on training questions. But only one of them works on new questions.

Understanding this competition — what each solution looks like, why one wins first and the other wins later — is essential to understanding grokking.

---

## Two Ways to Get the Right Answer

### Way 1: Memorisation

Imagine you are given 1,000 maths questions to study for an exam. One approach is to simply memorise every question and its answer.

You write them all down:
- Question 37 → Answer is 14
- Question 52 → Answer is 71
- Question 88 → Answer is 3
- ... and so on for all 1,000 questions.

On exam day, you score 100%. But if any question is slightly different — if question 37 is phrased differently, or if a new question appears — you fail. You never learned *how* to do maths. You just stored the answers.

This is memorisation. In a neural network:
- The network stores the answers for every training question.
- It gets 100% on training data.
- It cannot answer anything new.
- The memorised solution tends to be **large and complex** — like a big filing cabinet full of stored answers.

---

### Way 2: Generalisation

Another approach to the same 1,000 maths questions: actually learn how to do the maths.

You understand the rules. On exam day, you can answer any question — including new ones you have never seen. You might even do better on new questions than on the ones you studied, because you understand the underlying logic.

This is generalisation. In a neural network:
- The network discovers the underlying rule.
- It can answer any question correctly, including ones it has never seen.
- The generalised solution is **smaller and more efficient** — like a compact formula instead of a filing cabinet.

---

## The Key Insight: Both Solutions Score 100% on Training Data

Here is the crucial point that makes grokking puzzling and interesting:

> **Both the memorised solution and the generalised solution achieve perfect scores on the training data.**

A network with enough capacity can *always* memorise the training data. But it can also *potentially* learn the rule. Both approaches look identical from the outside during training.

The difference only shows up when you test on new data:
- Memorised solution → Fails on new questions (test score near 0%)
- Generalised solution → Succeeds on new questions (test score near 100%)

> [!IMPORTANT]
> This is why the training score alone tells you nothing about whether a network has learned to generalise. You must look at the test score. And in grokking, the test score stays at 0% for a very long time — which is why the plateau is so deceptive.

---

## Why Memorisation Wins First

The memorised solution wins first because it is **easier to reach**.

Think of it like finding your way in the dark. You could search for the best possible path. Or you could just grab the first path you find. The first path is probably not the best one, but you found it quickly.

The memorised solution is the "first path you find." It is:
- Easy to reach quickly
- Does not require discovering any pattern
- Works by storing each example independently

The generalised solution is the "best path." It is:
- Harder to reach — it requires discovering the actual rule
- More efficient once found
- Smaller and more compact

Gradient descent (the training process) finds the memorised solution first simply because it is closer and easier.

---

## Why Generalisation Eventually Wins

This is where **weight decay** comes in.

Weight decay is a rule applied at every training step: "keep the weights small." It adds a constant gentle pressure to reduce the size (norm) of all the network's internal values.

The memorised solution has **large** internal values (it needs big values to store many separate answers). Under weight decay pressure, these large values are gradually eroded.

The generalised solution has **small** internal values (it just needs to encode the rule efficiently). It survives weight decay much better.

So during the plateau:
- Weight decay is slowly eroding the large memorised solution.
- The smaller, more efficient generalised solution is gradually building up.
- Eventually, the generalised solution becomes strong enough to take over the outputs.

That takeover is grokking.

> [!TIP]
> Think of it like two businesses competing. The memorised solution is like a big, expensive store with a huge inventory. The generalised solution is like a small, lean startup with a smart algorithm. Both serve customers initially, but the startup's efficiency eventually wins when costs are cut (weight decay applies pressure).

---

## What the Competition Looks Like Inside the Network

Researchers have shown that during the plateau, the two solutions coexist inside the network at the same time.

The memorised solution is actively producing outputs. The generalised solution is being slowly assembled in the background.

As weight decay erodes the memorised solution and the generalised solution grows stronger, there comes a tipping point — and the generalised solution suddenly takes over. This is the sudden jump in test accuracy we see in grokking.

---

## The Role of Network Size

This competition only happens in networks that have **enough capacity to hold both solutions at once**.

If the network is too small, it cannot memorise all the training data. It is forced to generalise immediately (no grokking).

If the network is large enough to memorise the training data, it can afford to spend time on the memorised solution first, while slowly building the generalised one in the background. This is what produces the long plateau.

> [!NOTE]
> Having "more capacity than you need" is called being **overparameterised**. Grokking only happens in overparameterised networks. The next note explains this concept in detail: [[06 - Overparameterization and Interpolation]].

---

## The Weight Norm as a Signal

Because the memorised solution has larger weights than the generalised solution, the **total size of all weights** (called the weight norm) decreases as the network transitions from memorisation to generalisation.

This means the weight norm can be used as an early-warning signal for grokking: if you watch the total weight norm drop during the plateau, that is a sign that the memorised solution is being eroded and the generalised solution is taking over.

This is the simplest of the nine grokking predictors studied in the thesis.

---

## How This Connects to the Bigger Picture

The memorisation vs. generalisation tension in grokking is a small, observable version of a question that haunts all of machine learning:

- Will a model learn the true pattern, or just memorise the training data?
- How do we know if a model has genuinely understood something?
- What forces a model toward understanding rather than memorisation?

Grokking lets researchers study these questions in a tiny, controllable setting where all the answers are known. The lessons may apply to much larger models.

---

## Important Terms

**Memorisation:** Learning by storing specific examples and their answers, without understanding the rule. Works only on examples that were stored. Tends to require large, complex internal representations.

**Generalisation:** Learning by understanding the underlying rule. Works on any new example, not just stored ones. Tends to require small, efficient internal representations.

**Weight norm:** The total "size" of all the weights in a network, measured by adding up their squares (or a similar measure). A large weight norm means the network has large internal values; a small weight norm means smaller, more compact values.

**Capacity:** How much a network can learn and store. A network with many parameters has more capacity — it can memorise more examples and/or learn more complex rules.

**Overparameterised:** A network that has more capacity (parameters) than it strictly needs to fit the training data. Grokking only happens in overparameterised networks.

**Tipping point:** The moment when the generalised solution becomes strong enough to take over from the memorised solution. This is the grokking moment.

---

## Key Takeaways

- Memorisation and generalisation are two different solutions to the same problem — both score 100% on training data.
- Memorisation wins first because it is easier to reach; generalisation wins eventually because it is more efficient.
- Weight decay is the pressure that erodes the memorised solution and lets the generalised solution take over.
- The tipping point when generalisation takes over is the grokking moment — the sudden jump in test accuracy.
- The weight norm (total size of all weights) is a useful signal for tracking this competition.

---

## Related Notes
- [[Memorization]] · [[Generalization]]
- [[Neural Collapse]] · [[Circuit Formation]]
- [[06 - Overparameterization and Interpolation]]
- [[What Causes Grokking]]
