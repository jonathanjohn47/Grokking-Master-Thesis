---
tags: [synthesis, causation, grokking]
---
↑ Parent: [[00 - Start Here]] · Related: [[Competing Theories of Grokking]]

# What Causes Grokking?

> [!note]
> This note explains **why** the sudden jump to understanding happens during grokking. It lays out the chain of events that leads to the moment of breakthrough.

---

## What Is It?

When a network groks, something dramatic changes inside it. But this change doesn't happen instantly — it's the result of a careful sequence of events. 

**What Causes Grokking** answers this question: *What events have to happen in order for that sudden jump to occur?*

The answer is not one single cause. Instead, it is a **chain of causes**: one thing leads to the next, which leads to the next, until finally the breakthrough moment arrives.

---

## Why Does This Question Matter?

Understanding what causes grokking is practical.

If you understand the causes, you might be able to:
- **Predict grokking** before it happens (so you know when to keep training)
- **Speed it up** (by strengthening the causal factors)
- **Prevent problems** (by avoiding conditions that block it)

This is why the [[Thesis Proposal Summary|thesis]] investigates this question — understanding the causes could help practitioners use grokking more effectively.

---

## The Intuition: Two Kinds of Solutions

Here is the core idea of grokking in one simple thought:

> When a network has learned all the training examples, there are **many ways** it could have done this. Some ways use simple, clever rules (like the actual addition formula). Other ways use **memorised shortcuts** (remembering every answer).

**Both kinds of solutions get 100% accuracy on the training data.**

The network needs to **choose** which kind to use. And [[Weight Decay]] is what does the choosing.

---

## The Step-by-Step Causal Chain

### Step 1: Overparameterization Creates Options

> [!tip]
> **What happens:** The network has more weights (knobs to turn) than it needs.
> **Why it matters:** This creates a huge space of different solutions — it's not forced into a single answer.

When you have more weights than training examples, the network is [[Overparameterization|overparameterized]].

This is actually a feature, not a bug. Why? Because overparameterization creates **multiple ways to solve the problem**.

Think of it like having too many paintbrushes: there are many ways to paint the same picture.

### Step 2: Memorization Is Reached First

> [!tip]
> **What happens:** The network discovers memorised solutions very quickly.
> **Why it matters:** Memorisation is a local "dead end" that makes generalisation hard to find.

The network will find a memorised solution before it finds the real rule.

Why? Because memorisation is **locally easy**. It's right in front of the network — it just stores the answers it sees. There's no puzzle to solve.

The real rule is much harder to discover. It requires understanding the underlying pattern.

So memorisation arrives first, and the network sits there with 100% training accuracy but 0% test accuracy.

### Step 3: Not All Solutions Are Created Equal

> [!warning]
> **Important:** Just because a solution memorises the training data perfectly does **not** mean all solutions are equally good.

The memorised solution and the real rule both achieve 100% training accuracy.

But they are **very different**:
- **Memorised solution:** Uses large, complicated weights. It's "heavy" in terms of weight magnitude.
- **Real rule:** Uses smaller, simpler weights. It's "light" in terms of weight magnitude.

One solution is essentially "bulky", and the other is "lean".

### Step 4: Weight Decay Applies Slow Pressure

> [!tip]
> **What happens:** The [[Weight Decay]] regulariser slowly reduces all the weights, pushing the network toward simpler solutions.
> **Why it matters:** This is the "choosing" mechanism — it slowly tips the balance away from memorisation.

Now here is the key mechanism: **[[Weight Decay]]**.

Weight decay is a simple rule:

> Make the weights smaller. Keep all the numbers in the network small.

The network has two solutions at 100% accuracy:
- The heavy, bulky memorised solution
- The light, simple real rule

Weight decay **slowly pushes against both**.

But here is what happens next: the heavy memorised solution **shrinks first and harder** because it has more to shrink. The light real rule **has less fat to trim**, so it survives longer.

Over thousands of steps, weight decay slowly shifts the balance. The memorised solution gets worse and worse (because its weights are being shrunk). The real rule gets better and better (because it survives the shrinking).

### Step 5: A Structured Circuit Forms Silently

> [!tip]
> **What happens:** While the loss looks flat, the network is **secretly reorganising** into a clean, structured solution.
> **Why it matters:** This reorganisation is necessary for the breakthrough moment.

During the plateau, something invisible is happening inside the network.

The network is not just shrinking weights randomly. It is **building a clean, organised circuit** — a structured pattern of weights and connections that implements the real rule.

This circuit forms slowly, step by step. You cannot see it in the loss curve. But it is happening.

### Step 6: The Transition Is Abrupt

> [!tip]
> **What happens:** Suddenly, once the circuit is strong enough, it **takes over** and produces all the predictions.
> **Why it matters:** This is why we see a sharp jump, not a gradual climb.

Here is the surprising part: even though the circuit forms slowly, the **switch happens suddenly**.

This is because [[Phase Transition|phase transitions]] work this way. A phase transition is an abrupt shift from one state to another, like water turning to ice.

Before the threshold:
- The memorised solution is still in charge
- Test accuracy stays at 0%

After the threshold:
- The new circuit is in charge
- Test accuracy jumps to 99%

The switch is sharp because once the circuit is **good enough**, it **completely takes over**.

---

## What Is Necessary vs. What Accelerates?

To grok, does every ingredient have to be present? Or do some just speed things up?

Here is what the literature suggests:

| Ingredient | Is It Required? | What It Does |
|-----------|---|---|
| **[[Overparameterization\|Overparameterization]]** | **Essential** | Creates the space of solutions. Without it, there's only one way to solve the problem. |
| **Small training set** | **Essential** | Creates the gap between memorisation and generalisation. If you train on everything, there's no real rule to find. |
| **Regularisation** (like [[Weight Decay]]) | **Drives the transition** | Applies the "keep it simple" pressure. Explicit weight decay speeds it up; implicit regularisation can work but very slowly. |
| **Long training time** | **Essential** | The process is slow. You need enough training steps for it to happen. |
| **A real, learnable rule** | **Essential** | There must actually be a real pattern to discover. If the task is truly random, grokking cannot happen. |

---

## A Concrete Example

Let's walk through a real grokking event step by step.

**Task:** Train a small [[Transformer]] to do clock math: $(a+b) \bmod 97$ (addition on a clock with 97 positions).

**Setup:**
- Show the network only 30% of the possible pairs.
- Use strong [[Weight Decay]] (weight decay = 1.0).
- Train for 50,000 steps.

**Step 1 (Steps 0–1,000): Memorisation**
- The network quickly learns the 30% of examples it sees.
- Training accuracy: 100%
- Test accuracy: ~1% (random guessing)
- **What's happening:** Memorised solution is in place.

**Step 2 (Steps 1,000–40,000): The Silent Plateau**
- The loss barely moves.
- Training accuracy: still 100%
- Test accuracy: still ~1%
- **What's happening:** Weight decay is slowly shrinking the memorised solution. Inside the network, a [[Fourier Features|circuit for clock math]] is slowly forming. But nothing shows in the loss.

**Step 3 (Steps 40,000–41,000): The Breakthrough**
- Suddenly the network tests its new circuit on an unseen example.
- The circuit works.
- Training accuracy: still 100%
- Test accuracy: jumps to ~99%
- **What's happening:** The new circuit has become strong enough to take over completely. The phase transition happens.

---

## A Real-World Analogy

Imagine a student learning music theory for a difficult exam.

**Week 1: Memorisation Phase**
- The student memorises every practice problem and answer.
- They get 100% on practice tests.
- But give them a new problem, and they fail. They don't understand the underlying theory.

**Weeks 2–12: The Plateau**
- The student keeps practising and studying.
- Their practice test score stays at 100% (they already memorised everything).
- Nothing seems to improve. They look "stuck".
- But inside their head, something is changing. They are slowly building deeper understanding of how music theory actually works.
- This happens **invisibly**. The practice tests do not show it.

**Week 13: The Breakthrough**
- Suddenly, the student **understands** music theory.
- They can now solve **new, unseen problems** that use the same principles.
- They score 99% on problems they have never seen before.

The key insight: **the understanding was forming the whole time** during weeks 2–12. But it was invisible until the moment it was complete enough to matter.

In the student story:
- **Overparameterization** = Studying more than necessary
- **Memorisation first** = Memorising the answers
- **Weight decay** = The internal drive to understand (not just memorise)
- **Silent reorganisation** = Building genuine understanding during the plateau
- **Abrupt transition** = The "aha!" moment when it all clicks

---

## Important Terms

**Overparameterization**
Having more knobs to turn (weights) than you strictly need to solve a problem. This creates multiple possible solutions.

**Zero-loss solutions**
Any solution that achieves 100% training accuracy. With overparameterization, there are many of these.

**Manifold**
Imagine all possible solutions as points in a high-dimensional space. The "manifold" is the surface or region where all the zero-loss solutions live.

**Weight Decay**
A regulariser that applies pressure to keep all weights small. It's like adding an invisible force that pushes against large weights.

**Norm** (or weight norm)
A measure of "how large" all the weights are. A solution with small weight norm is "lighter" than one with large weight norm.

**Circuit Formation**
The process by which a clean, organised pattern of weights emerges inside the network that implements the real rule.

**Phase Transition**
An abrupt shift from one state to another, like water turning to ice. In grokking, the shift from "memorised" to "generalising" is a phase transition.

---

## Common Misconceptions

**Misconception 1: "Grokking is just the network finally discovering the rule."**

Reality: The network **slowly builds** the rule throughout the plateau. By the time you see the jump in test accuracy, the rule was mostly already there — you just couldn't see it yet.

**Misconception 2: "Weight decay is definitely necessary for grokking to happen."**

Reality: Weight decay **accelerates** grokking dramatically. But grokking can happen without explicit weight decay — it just takes much longer because other, weaker forms of regularisation are working instead.

**Misconception 3: "The loss plateau means nothing is changing."**

Reality: The loss plateau is **deceptive**. The loss might stay flat while the internal structure of the network is completely reorganising. The external signal (loss) and the internal signal (circuit quality) are out of sync.

**Misconception 4: "All zero-loss solutions are equally good."**

Reality: Zero-loss solutions vary enormously in weight norm, structure, and generalisation ability. Weight decay naturally selects for the ones with smaller norms and better structure.

---

## Key Takeaways

Here is what you should remember:

1. **Grokking is not a single cause.** It is a chain: overparameterization → memorisation → weight decay pressure → silent circuit building → phase transition → breakthrough.

2. **Weight decay is the "choosing" mechanism.** It slowly tips the balance from memorised solutions toward generalising solutions.

3. **The plateau is real change happening invisibly.** The network is restructuring itself, but the loss curve doesn't show it.

4. **The breakthrough is sharp because it's a phase transition.** Once the generalising circuit is good enough, it completely takes over, producing a sudden jump.

5. **Multiple ingredients are required.** Overparameterization alone is not enough. You need the training data to be incomplete, you need regularisation pressure, and you need enough training time.

6. **This is still an active research question.** The exact balance between weight decay, dynamics, circuits, and geometry is not fully settled. See [[Competing Theories of Grokking]] for the different theories that coexist.

---

## Why This Matters For Your Thesis

Understanding the causal chain tells you what to **measure** during the plateau to predict grokking.

If the causal chain is correct, then good predictors should measure:
- How much circuit structure is forming
- How fast the memorised solution is being "de-selected"
- How close you are to the phase transition threshold

This is exactly what [[Grokking Predictors]] try to do. And this is what the [[Thesis Proposal Summary|thesis]] tests empirically.

---

## Related Notes

- [[Competing Theories of Grokking]] — Different theoretical perspectives on the same phenomenon
- [[Role of Weight Decay]] — Deep dive into what weight decay does and doesn't do
- [[Grokking]] — The foundational definition and phenomenology
- [[02 - The Grokking Training Dynamics]] — The detailed timeline of training
- [[Mechanistic Explanations]] — What the actual circuit looks like
- [[The Generalization Puzzle]] — The broader context of why this is hard to understand
