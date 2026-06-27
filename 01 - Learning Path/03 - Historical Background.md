---
tags: [learning-path, history]
---
← Previous: [[02 - The Grokking Training Dynamics]]  ↑ Parent: [[00 - Start Here]]  → Next: [[04 - Core Experimental Setup]]

# 03 - Historical Background

## What Is This Note About?

Grokking did not appear out of nowhere in 2022.

For **decades** before the word "grokking" was even invented, researchers were puzzled by something strange: **why do large neural networks — networks with far more adjustable pieces than they should need — still manage to learn correctly on new data?**

This shouldn't work. According to basic statistics, it shouldn't. Yet it does.

This note tells the story of that mystery. It shows how grokking is just the latest, clearest example of a problem that has confused researchers for 30+ years.

---

## The Puzzle That Started Everything

Let me explain the puzzle with a simple rule from statistics:

> **If a model has more parameters than training examples, it will memorise the data and fail on anything new.**

This rule made sense. Think of it like this: if you give someone a photographic memory and only 50 photos to remember, they will remember them perfectly. But that doesn't mean they understood what's in the photos. Show them a new photo, and they fail.

Yet in the 2010s, something impossible happened. Researchers discovered that **huge neural networks with millions of parameters were memorising training data AND still succeeding on brand new data.**

How?

### A Famous Proof of the Puzzle

In 2017, researchers did a dramatic experiment:

They trained a neural network on **completely random labels**.

Imagine labelling 1000 dog photos with random fruits: apple, banana, pear, etc. The labels have nothing to do with the images. The network cannot possibly learn a real rule.

What happened?

The network **memorised every single random label perfectly**. 100% accuracy on training data.

But here's the bizarre part: the exact same type of network, trained on **real images with real labels**, also learned correctly on new images it had never seen.

> [!WARNING]
> How can the same network memorise nonsense perfectly, yet also learn meaningful patterns on real data? This is the paradox. Grokking research tries to solve it.

---

## Why This Puzzle Matters

The puzzle matters because it breaks a fundamental rule we thought was true.

If bigger networks always memorise instead of learn, then:
- Big language models should fail (they don't)
- Big image classifiers should fail (they don't)
- Deep learning shouldn't work at all (it does)

Something was wrong with our understanding. **Grokking is a controlled, miniature version of this same mystery**, which makes it perfect for investigation.

---

## Key Discoveries in the History (1991-2026)

Let me walk you through the major discoveries that led to understanding grokking. Each one added a piece to the puzzle.

---

### 1991 — The Hidden Plateau Effect

**Discovery:** Simple neural networks can have long "stuck" phases where nothing seems to happen, then suddenly improve.

**What it means:** Researchers studied the simplest possible networks (linear networks). They proved mathematically that these networks sometimes show:
- A flat performance plateau that lasts a long time
- Then a sudden jump in performance
- The network was building structure during the "stuck" phase, even though the scores weren't changing

**Why it matters:** This is the ancestor of grokking. It shows that stagnation doesn't mean the network is frozen. Something is happening underneath.

> [!ANALOGY]
> Like a student studying for a test. For weeks, practice tests show no improvement. Then one week, suddenly everything clicks. The student was building understanding the whole time.

---

### 2017 — The Memorisation Paradox (Zhang et al.)

**Discovery:** Large neural networks can memorise random data perfectly AND still learn real data correctly.

**The experiment:** Researchers took images and gave them random labels (no pattern). A network memorised these random labels to 100% accuracy. But the same network, trained on real images, also generalised to new images.

**Why it matters:** This broke the old rule. Big networks don't automatically memorise and fail. Something else is happening.

> [!TIP]
> Think of a student who can memorise a phone book word-for-word, yet still learns calculus correctly. The capacity to memorise doesn't prevent learning.

---

### 2017 — Phase Transitions in Learning (Physics Approach)

**Discovery:** Learning doesn't happen gradually. It happens in sharp jumps at critical points.

**What it means:** Researchers from physics noticed learning behaves like physical systems. Water freezes at a specific temperature — not gradually, but suddenly. Similarly:
- **Below** a threshold amount of training data, a network fails completely to learn
- **Above** that threshold, it suddenly succeeds
- There is no "gradual middle ground"

**Why it matters:** This shows grokking is not unique. Sharp jumps are built into how learning works.

---

### 2018 — Training Process Favours Simple Solutions (Implicit Regularisation)

**Discovery:** The training process itself (called [[Gradient Descent]]) automatically favours simpler solutions.

**What it means:** When you train a network, gradient descent doesn't find *any* solution that fits the data. It finds the **simplest** solution. It's like the network's teacher is saying: "Find a rule that works, but use the fewest resources possible."

**Why it matters for grokking:** The network starts with a memorised solution (complex, wasteful). But gradient descent keeps pushing it toward a simpler, rule-based solution. Eventually, the rule-based solution becomes more efficient than memorisation.

> [!EXAMPLE]
> Imagine two ways to remember a phone book:
> 1. Memorise every phone number exactly (complex, lots of memory)
> 2. Remember a pattern (simple, less memory)
> 
> A process that rewards efficiency will prefer option 2.

---

### 2018 — The Double Descent Phenomenon

**Discovery:** There is a critical size where networks transition from "too small to memorise" to "large enough to memorise."

**What it means:** As networks get bigger:
- Small network: cannot fit training data → fails on test data
- Medium network (critical boundary): **test error peaks sharply** ← odd behaviour
- Large network: fits training data → still succeeds on test data

**Why it matters:** Right at this critical boundary, something unusual happens. Test performance gets worse before it gets better. [[Double Descent]] is closely related to grokking's sudden jump.

---

### 2020 — Hidden Structure Keeps Forming After Perfect Accuracy (Neural Collapse)

**Discovery:** Even after a network memorises all training data perfectly, its internal hidden layer keeps reorganising.

**What it means:** Imagine the network has different "memory slots" for different types of data. After perfect memorisation:
- These slots don't stay random
- They gradually arrange into a beautiful, organised geometric pattern
- This keeps happening even though accuracy is already 100%

**Why it matters:** This proved the plateau is not empty. The network is actively reorganising itself. This reorganisation is what leads to [[Grokking]].

> [!NOTE]
> The plateau looks silent from the outside (accuracy not changing). But inside, the network is completely reorganising itself. This is crucial for understanding grokking.

---

### 2022 — Grokking Is Named and Studied (Power et al.)

**Discovery:** A specific, reproducible pattern in small neural networks training on simple arithmetic tasks.

**The pattern:**
1. Training accuracy jumps to 100% quickly (memorisation)
2. Test accuracy stays near 0% for a very long time (network is memorising)
3. Then test accuracy suddenly jumps to ~100% (the grokking moment)

**Why it matters:** This was the first **named, systematic study** of the phenomenon. It showed:
- Grokking is reproducible
- It can be studied scientifically
- It happens in simple, controllable settings

[[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets|The original grokking paper]] made this discovery.

---

### 2023 — Reverse-Engineering the Grokked Network (Nanda et al.)

**Discovery:** The network actually builds elegant, interpretable mathematical structures inside.

**What it means:** When researchers looked inside a grokked network, they found:
- A specific computational mechanism
- Using mathematical patterns (Fourier features, wave-like structures)
- Very different from a memorised solution

**Why it matters:** This showed grokking isn't magic. The network solves the problem using understandable math.

[[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Nanda's mechanistic interpretability study]] revealed what was actually happening.

---

### 2023 — Why Does the Network Choose the Rule? (Varma et al.)

**Discovery:** The rule-based solution becomes preferred because it is more efficient.

**What it means:** Compare two solutions:
- **Memorisation:** Remember every example individually (uses lots of network capacity)
- **Rule:** Learn the underlying pattern (uses little capacity)

Gradient descent naturally prefers the efficient solution.

**Why it matters:** This explains the *why* behind grokking. The network doesn't stay memorised because efficiency pressure pushes it toward rules.

[[Varma - Explaining Grokking Through Circuit Efficiency|Varma's circuit efficiency framework]] explained this mechanism.

---

## Timeline Summary

Here's the story at a glance:

| Year | What Happened |
|------|---------------|
| **1991** | Simple networks show long stuck phases that aren't really stuck — something building underneath |
| **2017** | Networks memorise random labels perfectly, yet learn real data correctly — the paradox |
| **2017** | Learning happens in sharp jumps at critical thresholds, not gradually |
| **2018** | Training automatically favours simple, efficient solutions |
| **2018** | Critical point between "too small" and "too large" networks shows strange double-descent behaviour |
| **2020** | Internal structure keeps reorganising even after perfect memorisation |
| **2022** | Grokking officially named and studied in detail (Power et al.) |
| **2023** | Grokked networks actually build interpretable mathematical circuits |
| **2023** | Circuit efficiency explains why networks prefer rules over memorisation |

---

## Understanding the Big Picture

Before grokking was named in 2022, researchers had been puzzling over one central question for 30+ years:

> **Why do large neural networks succeed at learning when statistics says they should fail?**

Each discovery in this timeline added a clue:
- Networks can have hidden plateaus (1991)
- Large networks memorise yet still learn (2017)
- Learning jumps rather than slides (2017)
- The training process favours efficiency (2018)
- Something weird happens at critical boundaries (2018)
- Internal reorganisation happens silently (2020)

**Grokking is the answer to all these clues.** It's a clean, simple setting where you can watch the whole process happen, understand it completely, and answer the 30-year-old question.

---

## Important Concepts and Terms

Let me define the key ideas in simple language:

**Overfitting**
When a network memorises specific examples instead of learning the general rule. Like a student who memorises past exams without understanding the material. Works perfectly on old exams, fails on new ones.

**Generalisation**
When a network learns the underlying rule or pattern. Like a student who understands the concept and can solve new problems they've never seen. This is what we actually want.

**Parameters**
The adjustable numbers inside a neural network. Think of them like dials you can turn. More parameters = more dials to turn = more flexibility. But more flexibility makes it easier to memorise than to understand.

**Gradient Descent**
The training process that adjusts all the parameters. Imagine you're standing on a hilly landscape in total darkness. Gradient descent repeatedly takes a small step downhill. Eventually, it reaches a valley. This valley is the trained network.

**Phase Transition**
A sudden shift in behaviour when a threshold is crossed. Examples:
- Water freezes at exactly 0°C (sudden, not gradual)
- A light switch turns on suddenly (not gradually)
- A network learning can jump from "cannot solve" to "can solve" suddenly

**Plateau**
A flat section. In grokking, test accuracy stays flat for a long time. It looks frozen, but the network is silently reorganising.

**Memorisation**
Remembering specific examples exactly, like recording a video. Doesn't require understanding the pattern.

**Rule Learning**
Finding the underlying pattern or formula. Like learning "add 1 each time" instead of memorising [1, 2, 3, 4].

---

## Why This History Matters

This history matters because it shows **grokking is not a quirk — it's a window into something fundamental.**

The 30-year puzzle is:
- **Why do big networks learn?** Classical statistics says they should memorise and fail.
- **When does learning happen in jumps?** Is it always sudden, or just sometimes?
- **What's happening during the stuck phase?** The network clearly *is* doing something.
- **What's the simplest system to study this?** We need something small enough to understand completely.

**Grokking answers all of these.** It's a perfect laboratory experiment:
- Small and simple
- Reproducible (happens reliably)
- Fully observable (we can look inside)
- Clean and clear

Grokking is like what happens in big, complex networks, but zoomed in and simplified so we can understand it.

---

## Key Takeaways

1. **Grokking is the latest chapter in a 30+ year mystery.** It didn't appear out of nowhere.

2. **The mystery is: why do large networks learn when they could memorise?** This should be impossible according to old statistics.

3. **Key discoveries built the picture:** Stuck plateaus, memorisation paradoxes, sharp transitions, efficiency pressure, internal reorganisation.

4. **Grokking is valuable because it makes the mystery visible and controllable.** We can watch it happen, understand it, and measure it.

5. **Understanding this history helps you see grokking as fundamental, not accidental.** It's not a bug. It's a feature of how neural networks actually work.

---

## Related Notes

Learn more about the concepts in this timeline:

- [[02 - The Grokking Training Dynamics]] — What grokking actually looks like
- [[04 - Core Experimental Setup]] — How grokking experiments are designed
- [[Double Descent]] — The strange boundary phenomenon
- [[Phase Transition]] — Sharp transitions in learning
- [[Generalization|The Generalization Puzzle]] — Why networks learn at all
- [[Research Timeline]] — Broader timeline of grokking research
- [[Evolution of Grokking Research]] — How understanding evolved
