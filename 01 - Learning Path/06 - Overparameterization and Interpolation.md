---
tags: [learning-path, theory, overparameterization]
---
← Previous: [[05 - Memorization vs Generalization]]  ↑ Parent: [[00 - Start Here]]  → Next: [[07 - Double Descent]]

# 06 - Overparameterization and Interpolation

## What Is This Note About?

Grokking only happens when a neural network has **far more capacity than it strictly needs**.

This sounds counterintuitive. Why would having too much capacity be a requirement for understanding something deeply?

This note explains what overparameterisation means, why it matters for grokking, and why having too many parameters is not always the disaster that classical statistics predicted.

---

## What Is Overparameterization?

**Overparameterisation** simply means: a model has more adjustable numbers (parameters) than it has training examples.

A simple analogy:
- Imagine you are trying to fit a curve through 5 points on a graph.
- A simple curve (few parameters) can only fit those 5 points approximately — it might not pass through any of them exactly.
- A very complex curve (many parameters) can be bent and twisted to pass through all 5 points exactly.
- A wildly complex curve (far too many parameters) can pass through the 5 points AND has huge amounts of extra flexibility left over.

A network is overparameterised when it is in that third category — it has so much flexibility that it can fit the training data perfectly, and then has capacity left over.

---

## What Is Interpolation?

**Interpolation** is a technical term for fitting your training data perfectly — achieving zero error on every single training example.

Think of it as the network "passing through" every point in the training data, like the complex curve above.

The number of parameters needed to just barely achieve this perfect fit is called the **interpolation threshold**. Models with fewer parameters than this threshold will not fit perfectly. Models past this threshold can fit perfectly and have spare capacity.

---

## The Classical Fear About Overparameterization

Classical statistics had a very clear prediction: if a model can fit the training data perfectly (and has spare capacity left over), it will simply memorise the training data and fail completely on new data.

The reasoning was:
- If you have more flexibility than you need, you will use that extra flexibility to fit noise and random quirks in the data.
- This is called **overfitting** — the model learns things specific to the training data that do not generalise.
- The result: perfect training score, terrible test score.

This was considered settled science. Almost every textbook taught it.

---

## Why This Classical Fear Turned Out to Be Wrong

Here is the surprising discovery: **past the interpolation threshold, adding more capacity often makes things better, not worse**.

Researchers found that in large neural networks, once the model can fit the training data perfectly AND has extra capacity, that extra capacity is often used in a beneficial way — to find simpler, smoother solutions that generalise well.

Several research teams proved this rigorously in different types of models:

- In a model called "random features regression," researchers derived an exact mathematical formula for how test error changes as model size increases. Past the interpolation threshold, test error goes **down** again, not up.
- In simple two-layer networks, researchers showed that the bias and variance (two kinds of error) behave very differently than classical theory predicted.
- In physical models, researchers found that crossing the interpolation threshold behaves like a physical phase transition — with a sharp, brief peak in error, followed by improvement.

---

## The Interpolation Threshold: A Critical Boundary

The interpolation threshold is the exact boundary where the model just barely becomes able to fit all the training data.

At this boundary, something unusual happens: test error peaks sharply. Models right at this boundary often perform **worse** than both smaller models and larger models.

Then, as you add more capacity past the threshold, test error falls again.

This produces a distinctive shape when you graph test error against model size — the shape looks like the letter U, followed by another descent. This is called **double descent**, described in detail in the next note.

---

## Why Overparameterization Matters for Grokking

Grokking requires overparameterisation. Here is why:

**A network at exactly the interpolation threshold** has just enough capacity to memorise the training data. It has no spare capacity. It is committed to the memorised solution and has nowhere else to go.

**A network well past the interpolation threshold** (overparameterised) has spare capacity. It can hold:
- The memorised solution
- AND a generalised solution simultaneously

This spare capacity is what allows the competition between memorisation and generalisation to happen at all. Without it, the network is forced to stay with whichever solution it found first — memorisation.

The long plateau in grokking is the period when the overparameterised network is slowly switching from the memorised solution to the generalised one. This switching only happens because there is spare capacity to hold both at once.

---

## An Everyday Analogy

Think of a restaurant that has room for exactly 10 people (the interpolation threshold). Every seat is taken by regular customers. There is no room for new customers, and no way to rearrange the seating.

Now think of a restaurant with room for 100 people but only 10 regular customers. There is enormous spare space. The owner can experiment with rearranging furniture, adding new tables, changing the layout — all without disrupting the existing customers. Eventually, the owner finds a much better arrangement.

In grokking, the training data is the 10 regular customers. The overparameterised network is the 100-seat restaurant. The spare capacity allows the network to find a better arrangement (the generalised solution) without immediately losing what it already has (the memorised solution).

> [!TIP]
> The key insight: **overparameterisation is not a flaw in the model. It is a feature.** The spare capacity is what allows the network to discover and switch to a better solution during the long plateau.

---

## Connecting to Training Time

The static (fixed) picture is: as you increase model size, test error forms a double descent curve.

The dynamic (over time) picture — which is grokking — is: as you increase training time, test error can initially rise (during memorisation), plateau, and then fall suddenly (at grokking).

These are two versions of the same story. In the static version, you change model size. In the dynamic version, you change training time. The same forces (capacity, efficiency, regularisation) drive both.

> [!NOTE]
> Some researchers describe grokking as "epoch-wise double descent" — double descent observed over training time rather than over model size. The static and dynamic pictures are deeply connected.

---

## Important Terms

**Overparameterization:** A model has more parameters (adjustable numbers) than it has training examples. Having "too many" parameters in classical terms, but often beneficial in practice.

**Parameters:** The adjustable numbers inside a neural network. During training, these are updated to improve performance.

**Interpolation threshold:** The exact model size at which the model can first fit all training data perfectly. Right at this threshold, test error often peaks before improving again.

**Interpolation:** Fitting training data with zero error — getting every training example exactly right.

**Overfitting:** When a model fits the training data so closely (including its quirks and noise) that it fails on new data. The classical fear with overparameterised models.

**Double descent:** The shape of the test error curve when plotted against model size. It goes down (classical regime), up (interpolation threshold), then down again (overparameterised regime). Explained in detail in [[07 - Double Descent]].

**Capacity:** How much a model can learn and represent. More parameters = more capacity.

---

## Key Takeaways

- Overparameterisation means a model has more parameters than training examples — more capacity than strictly needed.
- Classical theory predicted this would always cause overfitting. Modern research shows it often allows better generalisation.
- Past the interpolation threshold, extra capacity lets the network hold multiple solutions simultaneously — the memorised solution and the generalised solution.
- Grokking requires overparameterisation. Without spare capacity, the competition between memorisation and generalisation cannot happen.
- The long plateau in grokking is a direct consequence of overparameterisation: the network has room to slowly transition from one solution to another.

---

## Related Notes
- [[Overparameterization]] · [[Interpolation Threshold]]
- [[07 - Double Descent]] · [[08 - Phase Transitions in Learning]]
- [[Bias-Variance Tradeoff]] · [[Random Matrix Theory]]
