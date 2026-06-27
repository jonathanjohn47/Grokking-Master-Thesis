---
tags: [concept, weight-decay, regularization, grokking]
---
↑ Parent: [[Regularization]] · Related: [[Role of Weight Decay]] · Concept: [[Weight Decay]]

# Will the Model Plateau Forever Without Weight Decay?

> [!summary]
> No. Models can eventually grok without explicit weight decay, but the timeline changes dramatically. Some form of regularization—explicit or implicit—is needed to escape [[Memorization|memorizing]] solutions. Weight decay acts as the primary speedup knob.

> [!question]
> This note answers a specific question: if we train without weight decay at all, will the model get stuck forever on the wrong solution?

---

## The short answer

**The model will not plateau forever.** But without explicit weight decay, grokking happens much more slowly (if at all within practical training budgets), relying on [[Heavy-Tailed Self-Regularization|implicit regularization]] effects built into gradient descent itself.

---

## Why implicit regularization matters

Even without an explicit weight decay penalty, three forces naturally push the model toward smaller, generalizing solutions:

### 1. Gradient descent's own conditioning

[[Gradient Descent]] has inherent regularizing effects. The way the optimizer moves through weight space naturally favors certain solutions over others—it gets "stuck" in lower-norm regions without being explicitly told to.

### 2. The frozen subspace effect

During training, some dimensions of the weight space freeze (stop changing). Gradient descent implicitly allocates exploration to the dimensions that matter most for training. This acts like a budget constraint without an explicit penalty.

### 3. Self-regularization emerges

As the network trains, weight spectra naturally develop **heavy tails**—a few large weights, many tiny weights. This spectrum itself provides regularization, even without an explicit decay term.

> [!tip]
> These three effects are called **implicit regularization**. They're free, but they work slowly.

---

## The explicit vs. implicit tradeoff

| Aspect | Explicit Weight Decay | Implicit Regularization |
|---|---|---|
| **Speed** | Fast plateau escape | Very slow plateau escape |
| **Mechanism** | Penalty term in loss | Built into gradient descent |
| **Control** | Tunable (decay coefficient) | Hard to control |
| **Cost** | Computational overhead (small) | None |
| **Necessity** | Accelerator, not requirement | Suffices if you wait long enough |

---

## What the research shows

### The case for explicit weight decay

- **Norm-based selection:** Among all solutions with zero training loss, decay picks the smallest-norm one—which is typically the [[Circuit Formation|generalizing circuit]].
- **Provable geometry:** Under certain losses, weight decay provably steers toward [[Neural Collapse|collapsed]] solutions with generalization guarantees.
- **Empirical dominance:** Stronger decay consistently shortens the memorization plateau in experiments.

### The case for implicit regularization

- **GD as regularizer:** Gradient descent itself provides conditioning and frozen-subspace effects that protect [[Generalization|generalization]] without a penalty term.
- **Self-regularization emerges:** Heavy-tailed weight spectra appear naturally during training, providing regularization as a byproduct.

---

## The synthesis: Weight decay as a timescale knob

> [!important]
> The best current explanation: **weight decay is not an on/off switch for grokking. It is a timescale knob.**
> 
> Some regularization (explicit or implicit) is *required* to move off the [[Memorization|memorizing]] solution. But explicit weight decay sets the *speed* at which this happens.

Think of it this way:

- **Zero explicit decay** → implicit regularization alone → grokking happens, but very slowly
- **Small decay** → much faster grokking
- **Large decay** → fast grokking, but risk of overshrinking (see [[Anti-Grokking]])
- **Too much decay** → weights shrink too aggressively → [[Anti-Grokking|test accuracy collapses]]

---

## Practical implications for your experiments

1. **Don't assume weight decay is required.** It's not necessary, just helpful.
2. **But expect slow training without it.** Implicit regularization works, but the timescale may be impractical.
3. **Decay is a primary experimental variable.** Small changes in decay coefficient dramatically change when grokking occurs.
4. **The optimal window is unknown.** Too much decay triggers [[Anti-Grokking]]; too little is slow. This is an open research question.

---

## Common mistakes

> [!warning]
> **Mistake 1:** "Without weight decay, grokking is impossible."
> 
> **Correction:** Grokking can happen without weight decay via implicit regularization. It's just slower.

> [!warning]
> **Mistake 2:** "Weight decay is the *cause* of grokking."
> 
> **Correction:** Weight decay is an *accelerator*. The underlying cause is the need to escape memorization solutions. Regularization (implicit or explicit) enables this escape.

> [!warning]
> **Mistake 3:** "More weight decay is always better."
> 
> **Correction:** Excessive decay triggers [[Anti-Grokking]], where test accuracy collapses. The optimal decay window is dataset- and model-dependent.

---

## Key takeaways

- Models won't plateau forever without explicit weight decay.
- Implicit regularization from gradient descent itself can drive generalization (very slowly).
- Weight decay acts as the primary speed control, not a requirement.
- Some regularization—explicit or implicit—is needed to escape memorization.
- Too much decay causes [[Anti-Grokking]]; the optimal range remains an open question.

---

## Related Notes

- [[Weight Decay]] · [[Role of Weight Decay]] · [[Regularization]]
- [[Heavy-Tailed Self-Regularization]] · [[Implicit Regularization]]
- [[Circuit Formation]] · [[Generalization]] · [[Memorization]]
- [[Anti-Grokking]] · [[Grokking]]
