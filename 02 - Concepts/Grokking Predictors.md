---
tags: [concept, predictors, thesis-core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[11 - Predicting Grokking]] · Catalogue: [[The Nine Predictors]]

# Grokking Predictors

## What Are They?

**Grokking predictors** are internal measurements of a neural network that change during the [[Phase Transition|grokking plateau]] — before the test accuracy changes.

Think of them as early-warning signals.

They measure things *inside* the network that tell you: "Grokking is coming" or "Grokking is not coming."

The key insight: **the external accuracy looks completely flat during the plateau, but the inside of the network is changing dramatically.**

A good grokking predictor detects those internal changes before they show up in the test accuracy.

> [!EXAMPLE]
> During the plateau:
> - Test accuracy: 45% → 45% → 45% → (stuck for 10,000 steps)
> - Internal predictor: "Phase 1" → "Phase 2" → "Phase 2.5" → "Phase 3" → "Grokking happens next!"

---

## Why Do They Exist?

Imagine you are training a neural network and you reach the grokking plateau. The network looks stuck.

### The Problem: A Painful Decision

You cannot tell from the outside whether:
- Grokking is 5,000 training steps away (keep training)
- Grokking is 50,000 steps away (keep training even longer)
- The network will never grok (stop and save compute)

This is a real, practical problem researchers face every day.

Without guidance, teams either:
- **Stop too early:** Miss grokking by a few thousand steps. All that potential insight is lost.
- **Train forever:** Waste compute on networks that will never generalize. Money and time down the drain.

### The Solution: Look Inside

Grokking predictors solve this by looking **inside** the network, not just at external accuracy.

Even though test accuracy is flat, things are changing internally:
- Weight patterns are reorganizing
- Gradient flows are shifting
- Information structures are reforming
- The generalizing circuit is being constructed

The right internal measurements can detect these changes and give advance warning: "Keep training, something is happening."

---

## The Core Intuition: Internal vs External Signals

Think of monitoring a patient in a hospital.

### External Signals (Misleading During the Plateau)
The doctor watches whether the patient is conscious or not.
- Either awake (100%) or unconscious (0%)
- Binary information
- Does not change for hours

During this time, the doctor has no idea if the patient is recovering or getting worse.

### Internal Signals (Far More Informative)
The doctor measures:
- Heart rate (changing continuously)
- Blood pressure (rising or falling)
- Oxygen levels (improving or declining)
- Brain activity patterns (showing recovery)
- Inflammation markers (going up or down)

These measurements change continuously and give early warning before the external symptom (consciousness) changes.

### The Parallel

**Grokking predictors are the internal measurements for a neural network.**

- External signal = Test accuracy (binary-looking: near 0% or near 100%)
- Internal signals = Predictors (change continuously during the plateau)
- Early warning = "Grokking is coming" detected well before accuracy jumps

---

## The Nine Predictors

Nine different grokking predictors have been proposed by researchers around the world.

Each one measures something different inside the network. Each claims to be an early warning system for grokking.

Here is what each one does (in plain language):

### Predictor 1: Commutator Defect

**What it measures:** A specific property of how the network's gradients are organized.

**The intuition:** When the [[Circuit Formation|generalizing circuit]] is being built, the gradients follow a particular organizational pattern. This pattern is detectable — it changes in a specific, measurable way.

**When it works:** Good at detecting when the circuit is actively forming.

---

### Predictor 2: HTSR Alpha (Heavy-Tailed Self-Regularization)

**What it measures:** The statistical distribution of values in weight matrices.

**The intuition:** During memorization, weights are spread out randomly. During generalization, something interesting happens: the weights develop a "heavy-tailed" pattern.

This means:
- A few weights become very large
- Most weights stay very small
- It looks like wealth inequality: a few billionaires own most of the wealth, most people own very little

**The number:** Alpha (α) is a single number that describes how heavy-tailed the distribution is.

- Larger α = weights more evenly distributed = still memorizing
- Smaller α = heavier tail = closer to generalizing

**Why this matters:** See [[Heavy-Tailed Self-Regularization]] for the theory.

---

### Predictor 3: Correlation Traps

**What it measures:** A pathological pattern in weight matrices that signals failure.

**The intuition:** Sometimes, instead of grokking, the network can collapse into [[Anti-Grokking|anti-grokking]].

Correlation traps detect this by:
- Comparing the weight matrix to a randomly shuffled version of itself
- If they are suspiciously similar, the network has fallen into a trap
- It's "stuck memorizing" and won't escape

---

### Predictor 4: Weight-Space PCA

**What it measures:** The dimensionality (complexity) of the weight space.

**The intuition:** Imagine you have a dataset of color points in 3D space. If all points lie on a single line, the data is 1-dimensional even though space is 3D.

Similarly:
- During memorization: weight variation is high-dimensional and complex
- During generalization: weight variation becomes concentrated in a few key directions

**How it works:** [[Principal Component Analysis]] (PCA) finds these key directions. As generalization approaches, fewer directions capture all the important variation.

---

### Predictor 5: L2 Weight Norm

**What it measures:** The total size of all weights (sum of their squared values).

**The intuition:** This is the simplest predictor.

- Memorized solution = large weights (storing specific examples)
- Generalized solution = smaller weights (storing a simple rule)

As [[Weight Decay|weight decay]] acts on the network:
- The memorized solution (large weights) gradually shrinks
- The generalized solution (small weights) remains stable

So as training progresses: total weight size decreases → grokking is coming.

**Why use it?** Simple to compute, intuitive to understand.

---

### Predictor 6: Spectral Signature

**What it measures:** Specific patterns in weight matrices that appear early in training.

**The intuition:** Using tools from random matrix theory, certain spectral patterns emerge before grokking happens.

**What it promises:** The earliest possible warning signal.

**The challenge:** Requires deep mathematical knowledge to extract and interpret.

---

### Predictor 7: AGE (Absolute Gradient Entropy)

**What it measures:** The randomness of gradient signals during training.

**The intuition:** Entropy is a measure of disorder.

During memorization:
- Gradients are chaotic and random
- Entropy is high
- The network is "thrashing around"

During generalization:
- Gradients become organized and predictable
- Entropy becomes lower
- The network is "settling into a pattern"

As grokking approaches: gradient entropy decreases → organized circuit is forming.

---

### Predictor 8: Higher-Order Mutual Information

**What it measures:** How different parts of the network share information about the task.

**The intuition:** [[Information-Theoretic Measures|Mutual information]] measures relationships.

During memorization:
- Information is "synergistic" — you need multiple parts working together to store each example
- No part alone captures the pattern

During generalization:
- Information becomes "redundant" — many parts independently learn the same rule
- The rule is robust across the network

As grokking approaches: information structure reorganizes from synergistic to redundant.

---

### Predictor 9: Dropout Robustness

**What it measures:** How much the network breaks when you randomly disable connections.

**The intuition:** A truly general algorithm is robust — it still works even if some parts fail.

Think of two students:
- Student A memorized every exam answer (fragile) → if you ask one question differently, they fail
- Student B learned the underlying concept (robust) → they can answer variations and similar questions

Robustness test:
- Apply [[Dropout]] (randomly disable some connections)
- Measure performance drop
- A generalizing network is robust (small performance drop)
- A memorizing network is fragile (large performance drop)

As grokking approaches: robustness increases.

---

## The Four Qualities of a Good Predictor

Not all predictors are created equal.

A truly useful grokking predictor must have four key qualities:

### Quality 1: Accuracy

**What it means:** When the predictor says "grokking is coming," grokking actually comes.

**Why it matters:** A predictor that constantly gives false alarms is useless. You stop training early. You miss the grokking.

**The metric:** Low false alarm rate. AUC close to 1.0.

### Quality 2: Earliness

**What it means:** The predictor signals well before grokking actually happens.

**Why it matters:** Imagine two predictors:
- Predictor A: "Grokking is coming in 10 steps" (almost useless — by the time you react, it's done)
- Predictor B: "Grokking is coming in 5,000 steps" (very useful — time to make a decision)

The difference is enormous in practice.

**Good timing:** 1,000+ steps before grokking is useful. 100 steps before is not.

### Quality 3: Transferability

**What it means:** The predictor works on different tasks, not just the one it was trained on.

**Why it matters:** A predictor that only works on modular arithmetic but fails on language tasks is not useful. Science needs general predictions.

Example:
- Works on: Modular arithmetic tasks, permutation tasks, logic tasks
- Works on: Small image classification networks
- Bonus: Works on large language models

### Quality 4: Cheapness

**What it means:** Computing the predictor does not require huge computational overhead.

**Why it matters:** If checking the predictor takes longer than one training step, it is impractical.

Example:
- L2 Weight Norm: Dirt cheap (one calculation per step)
- Spectral Signature: Requires eigendecomposition (more expensive)

### The Trade-off Problem

These four qualities often conflict:

- The most **accurate** predictor might not be **early**
- The **earliest** predictor might not be **transferable**
- The **cheapest** predictor might not be **accurate**
- The **most transferable** predictor might be too expensive

> [!TIP]
> A good thesis asks: Which predictors achieve the best balance? Where are the trade-offs? What should practitioners actually use?

---

## Three Families of Predictors: How They Work

The nine predictors can be organized into three groups based on what they measure.

### Family 1: Spectral Predictors

**Members:** HTSR Alpha, Spectral Signature, Correlation Traps

**What they measure:** Mathematical patterns in weight matrices.

**Theoretical foundation:** [[Random Matrix Theory]] and the theory of self-regularization.

**Key advantage:** Require no data — only the weight matrices themselves.

**Key challenge:** Require mathematical sophistication to compute and interpret.

**Good for:** Early signals, low computational cost.

### Family 2: Geometric Predictors

**Members:** Weight-Space PCA, L2 Weight Norm

**What they measure:** The size and structure of the weight space.

**Theoretical foundation:** [[Neural Collapse]] dynamics and [[Weight Decay|weight decay]] mechanics.

**Key advantage:** Simple to compute, intuitive to understand.

**Key challenge:** May not capture early changes.

**Good for:** Practical use, easy implementation.

### Family 3: Information-Theoretic Predictors

**Members:** Higher-Order Mutual Information, AGE

**What they measure:** Information flow and gradient patterns.

**Theoretical foundation:** [[Information-Theoretic Measures]] and the reorganization of information during grokking.

**Key advantage:** Grounded in how information actually flows in the network.

**Key challenge:** Computationally expensive, harder to interpret.

**Good for:** Understanding the mechanism, capturing middle-phase changes.

---

## The Fair Comparison Problem

### Why No Comparison Has Happened Yet

Each of the nine predictors was proposed by a different research team.

Each team:
- Tested on their own specific tasks
- Used their own specific networks
- Compared against at most 2-3 other predictors
- Made claims like "our predictor is best"

**The result:** Chaos.

- Predictor A claims to be best on permutation tasks
- Predictor B claims to be best on modular arithmetic
- Predictor C claims to be best on transformers
- But nobody tested all nine predictors on all tasks using the same methods

There is no unified leaderboard. There is no standard way to compare. Every "best predictor" claim is made in isolation.

### What a Fair Comparison Requires

To fairly compare predictors, you need:
- **Same tasks:** All predictors tested on identical problems
- **Same networks:** Same architecture, same initialization, same training setup
- **Same measurement standards:** Accuracy, earliness, transferability, cost measured the same way
- **Same evaluation protocol:** Cross-validation, test/validation splits done identically
- **Statistical rigor:** Multiple runs, error bars, significance tests

### The Thesis Fills This Gap

This thesis is the first unified, fair comparison.

It tests all nine predictors under identical conditions and asks:

> Which predictors actually work best? Where do they fail? What should practitioners use?

---

## Each Predictor as an Order Parameter

From physics, we borrow the concept of an **order parameter**.

### What Is an Order Parameter?

An order parameter is a single number that tells you which phase a system is in.

**Example: Water freezing**

You could measure many things during freezing:
- Temperature
- Molecular motion
- Density
- Crystal structure
- Energy

But the order parameter — the quantity that most fundamentally distinguishes liquid from solid — is **density** (or equivalently, **crystal structure**).

- Liquid water: molecules random, density ~1.0 g/cm³
- Frozen ice: molecules in lattice, density ~0.92 g/cm³

The density sharply changes at the freezing point. It is the fundamental characteristic of the phase transition.

### For Grokking

Each proposed grokking predictor is claiming: "I am the order parameter for the grokking phase transition."

"I am the fundamental quantity that most clearly separates memorization from generalization."

- Memorization phase: specific value of predictor
- Generalization phase: different value of predictor
- The change happens sharply at grokking

### Which Is the True Order Parameter?

The thesis investigates:

Is there one true order parameter? Or do different predictors work for different reasons?

Are some predictors fundamental (measuring the same underlying change) while others are redundant?

Or do they all capture different aspects of a complex transition?

This is how we move from "nine competing claims" to "scientific understanding."

---

## Each Predictor as an Order Parameter

From the physics perspective, each grokking predictor is a proposed **order parameter** for the grokking phase transition.

An order parameter is a measurement that distinguishes the two phases: the memorisation phase and the generalisation phase. In water freezing, the order parameter is the density (or crystal structure) — very different in liquid and solid states.

For grokking, each predictor is claiming: "I am the quantity that most clearly distinguishes the memorisation phase from the generalisation phase."

The thesis tests which proposed order parameter is most reliable.

---

## Important Terms

### Grokking Predictor

An internal measurement of a neural network that changes during the plateau, before test accuracy does.

Not a single number — a whole family of different measurements, each proposing to detect the same phenomenon differently.

### Plateau

The long flat period during training where:
- Training accuracy stays high (near 100%)
- Test accuracy stays low (near 0%)
- Nothing appears to be changing
- But grokking might be coming

### Memorization vs Generalization

**Memorization:** The network stores specific training examples like a lookup table.
- Works on training data: 100%
- Works on test data: 0% (completely fails on new examples)

**Generalization:** The network learns the underlying rule or pattern.
- Works on training data: 100%
- Works on test data: 100% (works on new examples too)

### Entropy

A measure of randomness or disorder.

- High entropy = very random, chaotic, unpredictable
- Low entropy = very organized, ordered, predictable

Think of a room: high entropy is a messy room with stuff everywhere (random), low entropy is a perfectly organized room.

In networks: during memorization, gradients are chaotic (high entropy). During generalization, gradients become organized (low entropy).

### Heavy-Tailed Distribution

A statistical distribution where a few values are very large while most are small.

Real-world example: **Wealth distribution in society.**
- A few billionaires own enormous wealth
- Most people own very little
- The distribution has a long "tail" of small values and a few giant outliers

In networks: during generalization, weight values follow this pattern — a few giant weights and many tiny ones.

### Redundancy vs Synergy

**Synergistic information:** You need multiple parts working together.
- No part alone captures the pattern
- Like a puzzle where you need all pieces together

**Redundant information:** Many parts independently know the pattern.
- Each part could predict the answer alone
- Like multiple people who all independently memorized the answer

During grokking, information reorganizes from synergistic to redundant.

### Robustness

How well a system works even when something is broken or missing.

**Fragile system:** Breaks immediately if any part fails.
- A memorized network: remove one connection, lose one example

**Robust system:** Still works even if some parts fail.
- A generalized network: remove some connections, still knows the rule

### Dropout

A training technique that randomly disables (sets to zero) some connections during training.

- Applies during training to improve generalization
- Used in Predictor 9 as a test: "How robust is this network?"
- If performance drops a lot when you disable connections, the network is fragile (memorization)
- If performance barely drops, the network is robust (generalization)

### Principal Component Analysis (PCA)

A mathematical technique for finding the main directions of variation in data.

**Simple example:** If you plot students' heights and weights:
- Both vary, but they might vary together (correlated)
- PCA finds: "The main direction of variation is along the tall-and-heavy to short-and-light line"

Applied to networks: "What are the main directions in which weights vary?"

During generalization, variation becomes more concentrated — fewer directions capture most of the change.

### Mutual Information

A measure of how much knowing one thing tells you about another.

- High mutual information: Knowing A tells you a lot about B
- Low mutual information: A and B are independent

### False Alarm Rate

How often a predictor says "grokking is coming" when it is not.

- If you cry wolf too many times, people stop listening
- A predictor with high false alarm rate is not trusted
- Good predictors have low false alarm rate

### Order Parameter

A single measurement that fundamentally characterizes which phase a system is in.

Changes sharply at the phase transition (like a boundary between two countries).

In water: density changes sharply at the freezing point. Density is the order parameter.

In grokking: each predictor claims "I am the order parameter."

### Phase Transition

A sudden change from one state to another.

- Water freezing at 0°C: suddenly becomes solid
- Grokking: suddenly test accuracy jumps from ~0% to ~100%

The predictor's job: detect that a transition is coming before it happens.

### AUC (Area Under the Curve)

A standard statistical measurement of predictor quality.

- 1.0 = perfect predictor (always correct)
- 0.5 = no better than random guessing
- Higher is better

---

## Common Misconceptions

### Misconception 1: "A Predictor Must Work for All Networks"

Reality: Predictors have limited transferability. Some work great on modular arithmetic but fail on language tasks. This is normal.

The thesis investigates: Which predictors transfer best? Under what conditions?

### Misconception 2: "The Earliest Predictor Is the Best"

Reality: A predictor that signals 10,000 steps early but has lots of false alarms is useless. Accuracy matters too.

### Misconception 3: "Predictors Can Be Computed Instantly"

Reality: Some predictors require expensive operations like eigendecomposition. Their computational cost matters in practice.

### Misconception 4: "There Is One True Order Parameter"

Reality: There might be multiple order parameters capturing different aspects of the transition. Or they might all be approximations of the same underlying change.

---

## Why This Matters: The Practical Impact

### For Researchers

Understanding which predictor is best helps you:
- Know when to stop training
- Avoid wasting compute
- Run faster experiments
- Make better decisions during the plateau

### For Building Better AI

Predictors reveal what is happening inside the network during grokking.

Understanding this teaches us:
- How generalization actually works
- What causes [[Circuit Formation|circuits to form]]
- How to build more reliable training procedures
- Whether grokking is a useful phenomenon or just a quirk

### For Theory

Order parameters connect to fundamental physics concepts.

Finding the right order parameter means:
- Understanding the deep mechanisms
- Developing better theory
- Making predictions about other systems
- Solving other phase transition problems in learning

---

## Key Takeaways

**What they are:**
- Grokking predictors are internal measurements that change during the plateau before test accuracy changes

**Why they matter:**
- During the plateau, external scores are flat and give no information about whether grokking is coming
- Predictors solve a real practical problem: "Should I keep training or stop?"

**How many:**
- Nine different predictors have been proposed by different research teams

**How they organize:**
- Spectral predictors: analyze weight matrix patterns using random matrix theory
- Geometric predictors: measure weight space size and structure
- Information-theoretic predictors: analyze information flow and gradients

**What makes a good predictor:**
- Accuracy: correctly predicts grokking
- Earliness: signals far in advance
- Transferability: works on different tasks
- Cheapness: doesn't require excessive computation

**The deeper question:**
- Each predictor claims to be an order parameter for the grokking phase transition
- Which one is the true order parameter? Or are they all approximations?

**The research gap:**
- No fair, unified comparison of all nine predictors has been done
- That's what the thesis fills

---

## How This Connects to Learning

Understanding predictors requires understanding:

- [[11 - Predicting Grokking]] — The learning path for this entire topic
- [[Phase Transition]] — The sharp change from memorization to generalization
- [[Early Stopping]] — How to use predictions to decide when to stop training
- [[The Nine Predictors]] — The detailed catalogue of all nine

For theoretical depth:
- [[Heavy-Tailed Self-Regularization]] — Theory behind HTSR Alpha
- [[Information-Theoretic Measures]] — Theory behind information-theoretic predictors
- [[Neural Collapse]] — Theory behind geometric predictors
- [[Random Matrix Theory]] — Theory behind spectral predictors

For context on why this matters:
- [[05 - Thesis/The Nine Predictors]] — The core thesis topic
- [[Methodological Considerations]] — How to compare predictors fairly
- [[Competing Theories of Grokking]] — Different explanations of grokking

---

## Related Notes

**Core concepts:**
- [[The Nine Predictors]] — Detailed catalogue
- [[11 - Predicting Grokking]] — Learning path
- [[Methodological Considerations]] — How to compare them

**Predictor families:**
- [[Heavy-Tailed Self-Regularization]] — Spectral approach
- [[Information-Theoretic Measures]] — Information approach
- [[Neural Collapse]] — Geometric approach

**Consequences and applications:**
- [[Anti-Grokking]] — When predictors fail
- [[Early Stopping]] — Using predictions in practice
- [[Phase Transition]] — The underlying phenomenon

**Key papers:**
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]
