---
tags: [learning-path, theory, double-descent]
---
← Previous: [[06 - Overparameterization and Interpolation]]  ↑ Parent: [[00 - Start Here]]  → Next: [[08 - Phase Transitions in Learning]]

# 07 - Double Descent

## What Is This Note About?

Classical statistics taught researchers that there is a "sweet spot" for model complexity. Make a model too simple, and it cannot learn. Make it too complex, and it memorises the data and fails on new examples.

This sweet spot idea was the foundation of machine learning for decades.

Then researchers discovered something that broke this idea completely: **double descent**.

This note explains what double descent is, why it matters, and how it connects to grokking.

---

## The Classical Idea: The U-Curve

The classical picture of how error changes with model complexity looks like a U-shaped curve.

- As you make a model more complex (add more parameters), error on new data initially decreases — the model learns more.
- At some point, the model becomes too complex. It starts memorising the training data instead of learning the pattern.
- After this "sweet spot," error on new data increases — the model overfits.

The advice was clear: find the sweet spot and use a model of that complexity.

---

## The Discovery: A Second Descent

In the late 2010s, researchers discovered that the U-curve was only half the story.

When you continue to increase model complexity past the "sweet spot," something unexpected happens:

1. Error rises to a peak (this is the classical overfitting region).
2. At a specific boundary — called the **interpolation threshold** — error reaches its maximum.
3. Then, as you continue to add more parameters, **error falls again** — often to levels better than the original sweet spot.

The error curve has two descents: one before the threshold, and one after. This is why it is called **double descent**.

```
Error on
new data
    |
    |  Classical       Second
    |  descent   Peak  descent
    |   .---.    /\    
    |  /     \  /  \_________
    | /       \/
    |/
    +--------------------------------> Model size
                   ^
              Interpolation
               threshold
```

---

## What Causes the Peak?

At the interpolation threshold, the model is "just barely" large enough to fit all the training data.

This is actually the worst place to be:
- The model is being squeezed to fit every single training example exactly, including any noise or unusual cases.
- It has no spare capacity to smooth things out.
- This forced, tight fit means the model is extremely sensitive to the training data — small changes in the training set would produce big changes in the model.

When you add more parameters past the threshold, the model has spare capacity. It no longer has to squeeze itself so tightly around the training data. It can find more relaxed, smoother solutions that generalise better.

> [!NOTE]
> Think of it like sewing a shirt. If you cut the fabric exactly to fit one specific person with no room to spare, the shirt is extremely uncomfortable and will tear easily. If you cut it a little bigger, there is room to breathe and the shirt is more comfortable and durable. The overparameterised model is the bigger shirt.

---

## Why the Second Descent Happens

When a model has more parameters than training examples, it has many possible ways to fit the data perfectly. 

Among all these ways, gradient descent tends to find solutions that are smoother and simpler. The extra capacity is not used to memorise noise — it is used to find a better overall fit.

Researchers have proven this in specific models. For example, in a model called "random features regression," the exact mathematical formula for test error was derived. It shows:
- Rising error as you approach the interpolation threshold
- A sharp peak at the threshold
- Falling error past the threshold, eventually better than the classical sweet spot

---

## Three Different Names for the Same Phenomenon

This phenomenon has been discovered independently by researchers from different fields, who gave it different names:

| Name | Field | Description |
|------|-------|-------------|
| Double descent | Machine learning | The two-descent curve over model size |
| Jamming transition | Statistical physics | The critical point where the model just barely fits the data |
| Phase transition | Information theory | A sharp change in learnability at the critical boundary |

All three describe the same underlying phenomenon: a sharp change in how error behaves right at the interpolation threshold.

---

## How Double Descent Connects to Grokking

Here is the key connection:

**Double descent is about model size.** As you increase the number of parameters, test error follows the double-descent curve.

**Grokking is about training time.** As you continue training a fixed model, test error follows a similar pattern:
1. It drops to near zero (memorisation, high training accuracy, low test accuracy)
2. It stays flat for a long time (the plateau)
3. It suddenly drops again (grokking — the test accuracy jumps)

The two phenomena are deeply related:
- In double descent, you are changing model size to find the generalised solution.
- In grokking, you are changing training time to find the generalised solution.
- The same forces are at work: capacity, efficiency, and the pressure of weight decay.

> [!IMPORTANT]
> Some researchers describe grokking as **"epoch-wise double descent"** — the same double-descent pattern, but played out over training steps instead of model size. The second descent in double descent is like the second phase of grokking: a better solution emerging after an initial period of worse performance.

---

## An Everyday Analogy

Imagine you are trying to predict tomorrow's weather.

**Too simple a model:** "It will be sunny every day." Easy, but wrong a lot.

**Sweet spot model (classical):** "Use temperature and humidity trends from the past week." Pretty good.

**Just-barely-complex model (interpolation threshold):** You have a model with so many parameters that it can memorise every past weather event exactly. But it is so tightly fitted to past quirks that it fails on genuinely new patterns. This is the worst performer.

**Overparameterised model (past threshold):** You have an extremely flexible model, but training finds a smooth, generalised solution that does not cling to past quirks. This often performs better than the "sweet spot" model.

---

## What This Means for Practice

The discovery of double descent changed how researchers think about model size:

**Old advice:** Never make your model bigger than necessary. Bigger models overfit.

**New advice:** Once you are safely past the interpolation threshold, adding more capacity often helps, not hurts. Very large models can be better than medium-sized ones.

This is part of why modern AI systems (like large language models) use billions of parameters — far more than the amount of training data would classically suggest.

---

## Important Terms

**Double descent:** The phenomenon where test error follows a curve that goes down, up (at the interpolation threshold), then down again as model size increases.

**Interpolation threshold:** The model size at which the model can just barely fit all training data perfectly. Error peaks here.

**Sweet spot (classical):** The model size that classical statistics predicted was optimal — before double descent was discovered.

**Variance:** One component of prediction error. Measures how much the model's predictions would change if you used a different training set. Variance peaks at the interpolation threshold because the model is squeezed tightly around the training data.

**Bias:** Another component of prediction error. Measures how far the model's average prediction is from the truth. Bias decreases as model complexity increases.

**Bias-variance tradeoff:** The classical idea that reducing bias requires increasing variance, and vice versa. Double descent breaks this classical tradeoff in the overparameterised regime.

**Epoch-wise double descent:** The same double-descent pattern observed over training time (epochs) rather than model size. Another name for what happens in grokking.

---

## Key Takeaways

- Classical statistics predicted a single sweet spot for model complexity. Double descent shows there is often a second, better region for very complex models.
- At the interpolation threshold, error peaks because the model is squeezed too tightly around the training data.
- Past the threshold, extra capacity allows the training process to find smoother, better-generalising solutions.
- Double descent (over model size) and grokking (over training time) are two versions of the same story.
- The lesson: very large models are not always worse. Sometimes they are better.

---

## Related Notes
- [[Double Descent]] · [[Interpolation Threshold]]
- [[Jamming Transition]] · [[Phase Transition]]
- [[Bias-Variance Tradeoff]]
- [[08 - Phase Transitions in Learning]]
