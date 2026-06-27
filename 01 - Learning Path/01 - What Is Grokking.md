---
tags: [learning-path, grokking, core]
---
← Previous: [[00 - Start Here]]  ↑ Parent: [[00 - Start Here]]  → Next: [[02 - The Grokking Training Dynamics]]

# 01 - What Is Grokking

## What Is It?

**Grokking** is a strange and surprising event that happens when you train a neural network.

Here is what happens, step by step:

1. You train a neural network on some examples.
2. The network quickly gets **all the training examples right** — it learns to answer the practice questions perfectly.
3. But if you test it on **new questions it has never seen**, it fails completely.
4. You keep training it, even though it already seems to know everything.
5. For a very long time — sometimes thousands of steps — **nothing seems to change**. The network looks stuck.
6. Then, suddenly and without warning, the network **starts getting the new questions right too**.

That sudden jump to understanding — after a long period of looking stuck — is called **grokking**.

> [!NOTE]
> The word "grokking" comes from a science fiction novel called *Stranger in a Strange Land* by Robert Heinlein. In the book, "to grok" something means to understand it so deeply that it becomes part of you. Researchers used this word because the network goes from knowing the surface answers to truly *understanding* the underlying rule.

---

## Why Is It Surprising?

Grokking breaks three rules that people expected to be true about how neural networks learn.

**Rule 1 that it breaks:** "If a network has already learned the training set perfectly, it should not get any better."

- In grokking, the network keeps improving on **new questions** even after it already has perfect scores on training questions.

**Rule 2 that it breaks:** "If the improvement curve looks flat, the network is done learning."

- In grokking, the curve looks completely flat for a very long time — but the network is secretly changing on the inside.

**Rule 3 that it breaks:** "More training past the point of perfect accuracy should make things worse, not better."

- In grokking, continuing to train is exactly what causes the network to eventually understand the rule.

> [!WARNING]
> If a researcher had used **early stopping** — a common technique where you stop training once the network seems stuck — they would have stopped too soon and missed the grokking moment entirely.

---

## A Simple Example

Imagine training a small network to do **clock math** — specifically, figuring out what time it is if you add two numbers on a clock with 97 positions (instead of 12).

- **Steps 0 to 1,000:** The network gets all the training problems right. But ask it a new problem it hasn't seen, and it answers randomly. It has memorised the answers, not learned the rule.
- **Steps 1,000 to 40,000:** Nothing seems to change. Both the training score and the test score stay exactly the same. A researcher might think the network is stuck and stop training.
- **Steps 40,000 to 41,000:** Suddenly, the network starts getting almost **every new question right**. It has figured out how clock math actually works.

This is grokking. The understanding arrived more than 40 times later than the memorisation did.

---

## A Real-World Analogy

Think about a student studying for a music exam.

- In the first week, the student **memorises** every question and answer from the practice tests. They score 100% on practice tests. But give them a question they've never seen, and they fail.
- For the next few months, the student keeps practising. Nothing seems to change. Their practice test score is already perfect, so progress looks flat.
- One day, something clicks. The student has actually **understood music theory** — not just memorised answers. Now they can answer any new question, including ones they've never seen before.

The moment of understanding came **long after** the memorisation. That is grokking.

---

## Why Is Grokking Worth Studying?

Grokking is valuable because it gives researchers a **simple, controlled place to study how networks go from memorising to understanding**.

In a large language model with billions of parameters, it is impossible to watch every step of this process. But in a tiny network doing clock math, you can watch it happen one step at a time.

By studying grokking, researchers can learn:
- Why do networks sometimes understand and sometimes just memorise?
- What is secretly happening inside a network during a long plateau?
- Can we detect that understanding is coming *before* it actually arrives?

---

## The Practical Problem This Creates

Here is the real-world challenge that grokking creates for AI researchers:

During the long plateau phase, there is **no way to tell from the outside** whether:
- The network will eventually grok (and you should keep training), or
- The network will stay stuck forever (and you should stop)

This is a serious problem. If you stop too early, you lose a model that would have understood the task. If you keep training when it will never understand, you waste time and computing power.

This is why researchers are trying to find **early warning signals** — measurements you can take inside the network during the plateau to predict whether grokking is coming.

Finding and comparing those signals is what the thesis in this vault is about.

---

## Important Terms

**Neural network:** A computer program loosely inspired by the human brain. It learns by adjusting millions of small numbers (called weights) based on examples.

**Training:** The process of showing a neural network many examples so it can learn from them.

**Training accuracy:** How well the network answers the questions it was trained on.

**Test accuracy:** How well the network answers new questions it has never seen before.

**Memorisation:** When a network learns the exact answers to the training questions without understanding the underlying rule. It only works on questions it has already seen.

**Generalisation:** When a network truly understands the rule behind the examples. It can correctly answer new questions it has never seen.

**Plateau:** A period during training when the network's scores seem to not change at all. In grokking, the plateau is deceptive — things are changing inside, just not visibly.

**Early stopping:** A technique where researchers stop training a network when its performance seems to stop improving. Grokking shows this can be a mistake.

---

## Key Takeaways

- Grokking is when a network first memorises the training data, then appears stuck, and then suddenly understands the underlying rule.
- It breaks the expectation that more training after perfect accuracy is useless or harmful.
- The long plateau is the most confusing part — the network looks stuck, but something is happening inside.
- Grokking is useful to study because it is a clean, small-scale example of the big question: how do networks go from memorising to understanding?
- The practical challenge is that you cannot tell from the outside whether the network will eventually grok or stay stuck — which motivates finding internal early-warning signals.

---

## Related Notes
- [[Grokking]] (concept hub)
- [[02 - The Grokking Training Dynamics]]
- [[Memorization]] · [[Generalization]]
- [[What Causes Grokking]]
