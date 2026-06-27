---
tags: [learning-path, weight-decay, regularization]
---
← Previous: [[08 - Phase Transitions in Learning]]  ↑ Parent: [[00 - Start Here]]  → Next: [[10 - Mechanistic Explanations and Circuit Formation]]

# 09 - Weight Decay and Regularization

## What Is This Note About?

Weight decay is **the main switch for grokking**. Turn it on, and grokking eventually happens. Turn it off, and grokking often does not happen at all.

But why? What does weight decay actually do, and why does it have such a dramatic effect?

This note explains weight decay and the broader concept of regularisation — the family of techniques that prevent networks from memorising and instead push them toward genuine understanding.

---

## What Is Regularization?

**Regularisation** is any technique that prevents a neural network from memorising the training data too closely.

Think of it as a set of constraints or rules imposed on the network to encourage it to find simpler, more general solutions rather than specific, complex ones that only work on the training data.

Without regularisation, a network with enough capacity will simply memorise every training example. With regularisation, it is gently pushed toward finding the underlying pattern.

There are many types of regularisation. Weight decay is the most important one for grokking.

---

## What Is Weight Decay?

**Weight decay** is a simple regularisation rule applied at every single training step:

> "After every update, multiply all the weights by a number slightly less than 1."

For example, with a weight decay rate of 0.001, after each training step, every weight is multiplied by 0.999. This means every weight gets slightly smaller at every step.

The effect: the network is under constant pressure to keep all its internal values (weights) small.

---

## Why Does Keeping Weights Small Matter?

Here is the key insight:

**Different solutions to the same problem require different total amounts of weight.**

- The **memorised solution** (lookup table) needs large weights. To store an answer for every possible training question, the network needs large, complex internal representations. Think of it as needing a big database of many separate entries.

- The **generalised solution** (the actual rule) needs smaller weights. A rule can be expressed compactly. You do not need a separate entry for every question — you just need to capture the pattern. Think of it as a short formula instead of a big database.

When weight decay constantly presses all weights toward zero, it is equivalently pressing the network toward the solution that needs the **least total weight**. That solution is the generalised one.

---

## The Mechanism: Step by Step

Here is exactly what happens during grokking when weight decay is active:

**Step 1:** The network quickly memorises the training data. Training accuracy hits 100%. Test accuracy stays near 0%. The memorised solution is using large weights.

**Step 2:** Training loss is near zero. The gradient (the signal that normally drives learning) is also near zero. There is almost no normal learning signal left.

**Step 3:** But weight decay does not stop. It keeps pressing every weight slightly smaller at every step. This is the only active force now.

**Step 4:** The memorised solution — with its large weights — shrinks faster under this pressure. Its ability to produce correct outputs weakens.

**Step 5:** Meanwhile, the smaller generalised solution is also being shrunk, but it loses less because it was smaller to begin with.

**Step 6:** Eventually, the generalised solution becomes relatively stronger than the memorised solution. It starts producing larger, more confident outputs for the correct answers.

**Step 7:** The generalised solution takes over. Test accuracy suddenly jumps to near 100%. Grokking has happened.

> [!TIP]
> Think of two candles of different sizes. You put both in a steady wind (weight decay). The bigger candle burns down faster. The smaller candle lasts longer. Eventually, only the smaller one remains.

---

## How Weight Decay Rate Affects Grokking

Experiments compared different levels of weight decay:

**No weight decay (λ = 0):**
- After memorisation, the training gradient is near zero.
- There is almost no force pushing the network anywhere.
- The network stays in the memorised solution, possibly forever.
- Grokking does not happen (or takes an extremely long time).

**Low weight decay (λ = 0.01):**
- The pressure toward smaller weights is gentle.
- The transition from memorisation to generalisation happens, but slowly.
- Grokking occurs, but takes a very long time.

**High weight decay (λ = 1.0):**
- Strong pressure toward smaller weights.
- The memorised solution is eroded quickly.
- The transition happens much faster.
- Grokking occurs in a reasonable time.

**Too much weight decay:**
- The pressure becomes so strong that even the generalised solution cannot survive.
- The network collapses — it loses both memorisation AND generalisation.
- This is called **anti-grokking**: test accuracy briefly improves, then collapses again.

---

## Explicit vs. Implicit Regularisation

Weight decay is called **explicit regularisation** — it is a rule you deliberately add to the training process.

But researchers discovered there is also **implicit regularisation** — the training process itself tends to find simpler solutions, even without any explicit rule.

This happens because gradient descent (the training algorithm) tends to find solutions with smaller weights, even when you do not add weight decay. It is a subtle bias built into how the training algorithm works.

The practical consequence: grokking can happen even with zero explicit weight decay, but it happens much more slowly and less reliably. The implicit regularisation from the training process is weaker than explicit weight decay.

| Type | Source | Effect on Grokking |
|------|--------|--------------------|
| Explicit (weight decay) | A deliberate rule added to training | Main driver; controls the speed of grokking |
| Implicit (from training algorithm itself) | Built into gradient descent | Can cause grokking, but slowly and unreliably |

---

## How Weight Decay Connects to Structure

An important side effect of weight decay: it pushes the network's internal representations to become more organised and geometric.

Researchers found that networks trained with weight decay tend to develop very clean, symmetric arrangements in their internal representations. This is related to a phenomenon called **neural collapse** — where the network's hidden representations of different categories converge to a mathematically beautiful, maximally symmetric arrangement.

This structural organisation is connected to generalisation: a network with clean, symmetric representations generalises better. Weight decay drives the network toward these clean representations.

---

## The Practical Consequence

Because weight decay is the slow force driving the grokking transition, and because it operates silently while the training and test scores are both flat:

> **There is no external signal telling you how far along the transition is.**

You cannot look at the accuracy curves and tell if grokking is 1,000 steps away or 100,000 steps away. The curves look the same.

This is the core motivation for **grokking predictors** — internal measurements that track how far weight decay has eroded the memorised solution and how much the generalised solution has built up. These predictors aim to answer: "Is grokking nearly here, or is it still far away?"

---

## Important Terms

**Regularisation:** Any technique that discourages memorisation and encourages generalisation. Weight decay is one type of regularisation.

**Weight decay (λ):** A rule applied at every training step that multiplies all weights by a number slightly less than 1, keeping them small. Lambda (λ) is the symbol for how strong this pressure is.

**Weights:** The adjustable numbers inside a neural network. Training adjusts them to improve performance.

**Gradient:** The signal produced by the training process that tells each weight how to change. Near zero when the network already fits the training data well.

**Explicit regularisation:** Regularisation deliberately added by the researcher (like weight decay).

**Implicit regularisation:** Regularisation that happens naturally because of how the training algorithm works, without being explicitly added.

**Anti-grokking:** When weight decay is too strong, and the network collapses — losing generalisation after having briefly achieved it.

**Neural collapse:** A phenomenon where a network's internal representations of different categories converge to a maximally symmetric geometric arrangement. Connected to good generalisation. Occurs partly because of weight decay.

---

## Key Takeaways

- Weight decay is the primary driver of grokking. Without it, grokking often does not happen.
- It works by constantly pressing all weights smaller — favouring the solution that needs the least total weight (the generalised solution).
- The memorised solution needs large weights; the generalised solution needs small weights. Weight decay erodes the memorised solution and lets the generalised one take over.
- Too much weight decay causes anti-grokking — the network collapses entirely.
- Even the training process itself provides some implicit regularisation, but it is weaker than explicit weight decay.
- Because weight decay operates silently while scores are flat, internal predictors are needed to know if grokking is approaching.

---

## Related Notes
- [[Weight Decay]] · [[Role of Weight Decay]]
- [[Heavy-Tailed Self-Regularization]] · [[Neural Collapse]]
- [[10 - Mechanistic Explanations and Circuit Formation]]
