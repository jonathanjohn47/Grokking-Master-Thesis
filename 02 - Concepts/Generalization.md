---
tags: [concept, generalization, core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Generalization

## What Is It?

**Generalisation** is a model's ability to perform well on questions it has never seen before — not just the ones it was trained on.

A model that has generalised has learned the **underlying rule**. It can apply that rule to any input, not just the specific examples it was shown during training.

Grokking is the moment when a network suddenly achieves generalisation — after a long period of only memorising.

---

## Why Does It Exist? (What Problem Does It Solve?)

The whole point of training a machine learning model is that you want it to work on **new situations** — not just the exact situations it was trained on.

If your model only works on data it has already seen, it is useless in the real world. The world is full of new situations.

Generalisation is what makes a model useful beyond the training data.

---

## Two Examples: Generalisation vs. No Generalisation

**Clock Math Example:**

A model trained on 30% of possible clock-math questions (addition mod 97):

- **No generalisation (memorisation):** Gets 100% on the 30% of questions it trained on. Gets ~1% (random guessing) on the 70% it has never seen.

- **Generalisation (grokking):** Gets 100% on the 30% it trained on AND ~99% on the 70% it has never seen. It has learned the rotation-angle algorithm that works for any input.

Both models have identical training performance. Only the test performance reveals whether generalisation has happened.

**Student Example:**

- **No generalisation:** Student memorises 200 practice problems and can answer those 200 questions perfectly. Give them a new problem, and they fail.

- **Generalisation:** Student understands the mathematical rules. Can answer any new problem, not just the 200 they studied.

---

## Why Generalisation in Neural Networks Is Puzzling

Classical statistics had a clear prediction: if a model has more free parameters than training examples, it will not generalise. It will just memorise the training data and fail on everything else.

But modern neural networks routinely violate this prediction. Very large networks — with far more parameters than training examples — consistently generalise well.

This is the core mystery that grokking research is helping to solve. How do overparameterised networks generalise at all? What drives the shift from memorisation to generalisation?

Grokking is a controlled case study: the transition from memorisation to generalisation is slow enough to observe step by step, in a network small enough to inspect completely.

---

## What Good Generalisation Looks Like Inside the Network

Research has found that networks which generalise well share specific internal properties:

**Small weight norm:**
The generalising solution is compact — it does not need large weights. The weights required are smaller in total than those needed for the memorised solution.

**Large margin:**
The network's decision boundary is far away from the training examples — it is not squeezed tightly around specific training data.

**Low-rank representations:**
The internal representations lie in a small number of dimensions — they are compact and structured.

**Symmetric geometry (neural collapse):**
In the final stage of good generalisation, the internal representations of different categories converge to a maximally symmetric arrangement — each category is equally distant from all others.

All four of these properties emerge naturally from continued training with weight decay. All four are absent in the memorised solution.

---

## How to Predict Generalisation Without Test Data

Remarkably, researchers have found ways to predict whether a network will generalise **without looking at any test data**:

- **Weight matrix patterns:** The statistical distribution of values in the weight matrices (called "spectral" properties) correlates with generalisation quality. Networks that generalise well tend to show a specific "heavy-tailed" pattern in their weight matrix values.

- **Graph properties:** The structure of which network connections are active encodes information about final performance.

- **Representation geometry:** How compact and well-separated the internal representations are correlates with how well the network generalises.

These findings are exciting because they suggest generalisation is a measurable internal property of the network — not just something you discover after the fact by testing on new data.

---

## The Relationship Between Generalisation and Grokking

Grokking makes the transition to generalisation visible in a way that is usually invisible in larger models.

In a large language model, the transition from "not understanding something" to "understanding it" happens over huge training runs and cannot be pinpointed to specific training steps. In grokking, you can watch the exact moment when the network shifts from memorisation to genuine understanding.

This makes grokking an invaluable scientific tool: it is generalisation under a microscope.

---

## Generalisation Versus Related Concepts

**Generalisation vs. Memorisation:**
Both achieve perfect training accuracy. Generalisation additionally works on new data; memorisation does not. See [[Memorization]].

**Generalisation vs. Overfitting:**
Overfitting is when a model's test performance deteriorates because it memorised training data too specifically. Generalisation is the opposite — good test performance because the underlying rule was learned. See [[Overfitting]].

**Generalisation vs. Shortcut Learning:**
Shortcut learning is when a model appears to generalise but has actually found a spurious pattern that works on the test set but would fail in genuinely different contexts. True generalisation uses the actual underlying rule. See [[Shortcut Learning]].

---

## Important Terms

**Generalisation:** The ability to perform correctly on new data not seen during training. Requires learning the underlying rule.

**Training data:** The examples the network is trained on.

**Test data:** New examples the network has not seen during training. Used to measure generalisation.

**Weight norm:** The total size of all the weights in the network. Generalising networks tend to have smaller weight norms.

**Margin:** The distance between the network's decision boundary and the training examples. Larger margin tends to mean better generalisation.

**Neural collapse:** The maximally symmetric geometric arrangement of internal representations that emerges at the endpoint of good generalisation.

**Overfitting:** The failure mode where a network is too closely fitted to training data and fails on new data.

**Shortcut learning:** When a network learns a spurious pattern that happens to work on the test set, rather than the true underlying rule.

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "If a network has 100% training accuracy, it has learned the task."
> Training accuracy measures performance on training examples only. A network with 100% training accuracy may have just memorised those examples without learning anything transferable. Generalisation is measured by test accuracy on new examples.

> [!WARNING]
> **Misconception:** "Larger models cannot generalise because they overfit."
> Modern research, including grokking, shows that very large models can and do generalise — often better than smaller models. The classical overfitting concern does not apply straightforwardly to overparameterised models.

---

## Key Takeaways

- Generalisation is the ability to correctly answer new questions, not just memorised ones.
- A network has generalised when it has learned the underlying rule, not just stored the training answers.
- In grokking, generalisation arrives suddenly after a long plateau of memorisation.
- Generalising networks internally show small weight norms, large margins, and symmetric geometric arrangements.
- Generalisation can be predicted from internal network properties — without running on test data.
- Grokking is generalisation made visible and observable, at a scale where every step can be studied.

---

## Related Notes
- [[Memorization]] · [[Overfitting]] · [[Early Stopping]]
- [[Double Descent]] · [[Neural Manifolds]] · [[Feature Learning]]
- [[Out-of-Distribution Generalization]] · [[Shortcut Learning]]
- [[05 - Memorization vs Generalization]] · [[The Generalization Puzzle]]
