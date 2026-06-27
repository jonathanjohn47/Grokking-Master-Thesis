---
tags: [concept, training-strategy, learning-methodology]
---
↑ Parent: [[00 - Start Here]] · Related: [[Early Stopping]] · Applications: [[Grokking Predictors]]

# Curriculum Learning

## What Is It?

**Curriculum learning** is a training strategy where you teach a neural network in a specific order: start with easy examples, gradually progress to harder ones.

Instead of showing the network random examples throughout training, you organize them by difficulty.

Easy examples first → Medium examples → Hard examples → Final examples

This is the same strategy humans use in education.

> [!NOTE]
> Curriculum learning is not about changing the network architecture. It is about changing the order and selection of training examples.

---

## Why Does It Exist?

### The Original Problem: Random Order

Standard neural network training shows examples in random order:

```
Step 1: Hard example
Step 2: Easy example
Step 3: Hard example
Step 4: Easy example
```

The network sees everything mixed together from day one.

### Why This Can Be Inefficient

Humans don't learn this way. A child doesn't:
- Read Shakespeare on day 1
- Learn to read basic words on day 2
- Read Shakespeare again on day 3

Instead, humans follow a curriculum:
- Learn letters (A, B, C, ...)
- Learn simple words (cat, dog, run, ...)
- Learn to read sentences
- Learn to read stories
- Eventually read Shakespeare

**The insight:** Learning is faster and more effective when you start simple and gradually increase difficulty.

### Why Curriculum Learning Helps Neural Networks

Networks benefit from the same principle:

1. **Initial learning:** Easy examples allow the network to learn basic patterns quickly
2. **Foundation building:** Simple examples establish useful representations
3. **Progressive difficulty:** Hard examples refine and extend learning
4. **Efficiency:** Less wasted training effort on premature hard examples
5. **Convergence:** Network reaches good solutions faster

---

## Intuition: Teaching a Child to Play Basketball

### Without Curriculum (Random Order)

You give a 5-year-old these tasks in random order:
- Make a three-pointer from 25 feet
- Dribble around cones
- Make a layup from 2 feet
- Pass accurately to a moving target
- Play full-court defense
- Shoot free throws

Result: Frustration, confusion, slow learning.

### With Curriculum (Ordered by Difficulty)

Week 1: **Very easy**
- Dribble while standing still
- Pass to stationary target
- Shoot from 2 feet (very close)

Week 2: **Easy**
- Dribble slowly in a straight line
- Pass to moving target (slow)
- Shoot from 5 feet

Week 3: **Medium**
- Dribble through cones
- Pass quickly to moving target
- Shoot from 10 feet
- Practice free throws

Week 4: **Hard**
- Dribble while being lightly defended
- Make layups at game speed
- Shoot from 15 feet

Week 5: **Very hard**
- Full-court defense
- Make three-pointers
- Play actual game

Result: Smooth progression, faster skill development, more confidence.

### How It Applies to Neural Networks

The network needs the same progression:

**Phase 1: Easy examples**
- Simple patterns, clear signals
- Network learns foundations quickly
- Builds basic representations

**Phase 2: Medium examples**
- Moderate complexity
- Network refines existing knowledge
- Extends understanding

**Phase 3: Hard examples**
- Complex patterns, subtle details
- Network applies and combines learned concepts
- Achieves expert-level understanding

---

## How Does It Work?

### Step 1: Organize Examples by Difficulty

First, you need a **difficulty metric** — a way to measure how hard an example is.

Examples:

**For image classification:**
- Easy: high-contrast, clear objects
- Hard: low-contrast, ambiguous objects

**For modular arithmetic:**
- Easy: operations with small numbers
- Hard: operations with large numbers

**For language:**
- Easy: short, simple sentences
- Hard: long, complex sentences with rare words

### Step 2: Create Training Batches by Difficulty

Organize training data into phases:

```
Phase 1 (Steps 0-1000):     Only easy examples
Phase 2 (Steps 1000-3000):  Mix easy + medium
Phase 3 (Steps 3000-5000):  Mix medium + hard
Phase 4 (Steps 5000+):      All examples equally
```

### Step 3: Train with Progressive Difficulty

Train as normal, but examples are presented in curriculum order instead of random order.

### Step 4: Monitor Learning Progress

Watch for:
- Training accuracy on phase 1 examples (should be near 100% quickly)
- Training accuracy on phase 2, 3, 4 examples (should improve over time)
- When to transition to next phase

### Transition Strategies

**Strategy 1: Fixed schedule**
- Phase 1: first 1000 steps
- Phase 2: next 2000 steps
- Phase 3: next 2000 steps
- Decided in advance

**Strategy 2: Performance-based**
- Stay in Phase 1 until accuracy > 95%
- Then move to Phase 2
- Move to Phase 3 when Phase 2 accuracy > 90%

**Strategy 3: Mixed**
- Follow schedule, but also check performance
- If accuracy is too low, stay longer in current phase

---

## Worked Example: Learning Modular Arithmetic

### Setup

Task: Learn modular arithmetic (e.g., 5 + 3 mod 7 = 1)

Difficulty metric: Size of numbers involved

### Standard Training (No Curriculum)

Random examples throughout:
- Step 1: (17 + 23) mod 97 = ?
- Step 2: (2 + 1) mod 5 = ?
- Step 3: (81 + 19) mod 53 = ?
- Step 4: (1 + 1) mod 3 = ?

Network sees everything mixed up. Slow learning.

### Curriculum Learning Training

**Phase 1 (Steps 0-500): Easy** — Numbers 1-10
- (2 + 1) mod 5 = 3
- (3 + 4) mod 7 = 0
- (5 + 1) mod 8 = 6
- Only small numbers

Result: Network quickly learns basic mod arithmetic (90% accuracy by step 300).

**Phase 2 (Steps 500-1500): Medium** — Numbers 1-50
- (15 + 23) mod 31 = 7
- (44 + 12) mod 37 = 19
- Network applies learned rules to larger numbers

Result: Accuracy grows to 85% on medium examples.

**Phase 3 (Steps 1500-3000): Hard** — Numbers 1-200
- (127 + 89) mod 157 = 59
- (199 + 43) mod 181 = 61
- Scaling to much larger numbers

Result: Accuracy reaches 95% on hard examples.

**Phase 4 (Steps 3000+): All mixed**
- Random examples from all difficulties
- Network maintains and refines knowledge

### Comparison

| Metric | No Curriculum | With Curriculum |
|--------|---------------|-----------------|
| Steps to 90% accuracy on easy | 400 | 300 |
| Steps to 80% accuracy on hard | 5000 | 2500 |
| Final accuracy (all) | 92% | 96% |
| Convergence speed | Slow | Fast |

Curriculum learning is 2× faster in this example.

---

## Real-World Applications

### Computer Vision: Image Classification

**Easy examples:**
- High-resolution images
- Objects centered
- Simple backgrounds
- Clear lighting
- Single object per image

**Hard examples:**
- Low-resolution images
- Objects at edges
- Cluttered backgrounds
- Poor lighting
- Multiple objects

Training with curriculum: network learns general shapes first, then fine details.

### Natural Language Processing: Machine Translation

**Easy examples:**
- Short sentences (5-10 words)
- Common words
- Simple grammar
- English-to-Spanish (similar languages)

**Hard examples:**
- Long sentences (50+ words)
- Rare words
- Complex grammar
- English-to-Chinese (very different languages)

### Speech Recognition

**Easy examples:**
- Clear, slow speech
- No background noise
- Native speakers
- Standard pronunciation

**Hard examples:**
- Fast speech
- Background noise
- Non-native speakers
- Regional accents
- Mumbled speech

### Object Detection

**Easy examples:**
- Large objects
- Clear objects
- Well-lit scenes

**Hard examples:**
- Small objects (tiny dots in image)
- Partially occluded objects
- Poor lighting

---

## Connection to Grokking

### How Curriculum Learning Affects Grokking

Curriculum learning can interact with [[Grokking]] in interesting ways:

**Observation 1: Faster Initial Learning**
With curriculum, the network memorizes easy examples quickly.

**Observation 2: Delayed Generalization**
But generalization to hard examples might take longer or not occur.

**Observation 3: Different Grokking Patterns**
The grokking plateau might look different with curriculum:
- Easy examples: grok early
- Medium examples: grok later
- Hard examples: might not grok at all

### Measuring with Predictors

[[Grokking Predictors]] might behave differently with curriculum:

- [[Grokking Predictors|Dropout Robustness]]: Network might memorize easy examples (fragile) for longer before becoming robust
- [[Grokking Predictors|Weight-Space PCA]]: Dimensionality might stay high longer because different example subsets need different solutions
- [[Grokking Predictors|HTSR Alpha]]: Heavy-tailed distribution might emerge at different times for different difficulties

---

## Analogy: Building a House

### Without Curriculum

You hire a construction company and give them a random task list:

```
Step 1: Install electrical wiring
Step 2: Pour foundation
Step 3: Paint walls
Step 4: Install roof
Step 5: Build walls
```

Nonsense. Nothing works because the order is wrong.

### With Curriculum

The construction company follows a proper curriculum:

```
Phase 1: Foundation
- Prepare ground
- Pour concrete
- Let it set

Phase 2: Structure
- Build walls
- Install roof
- Install basic utilities (rough-in)

Phase 3: Systems
- Install electrical wiring
- Install plumbing
- Install HVAC

Phase 4: Finishing
- Paint walls
- Install fixtures
- Decorate
```

Each phase builds on the previous. Progress is smooth and efficient.

### Neural Networks Learn Similarly

A network needs the same structured progression, building each layer of understanding on previous knowledge.

---

## Important Terms

### Curriculum

A structured sequence of training examples, ordered by difficulty.

Not a random shuffle — a deliberate progression.

### Difficulty Metric

A way to measure how hard an example is.

- Could be human-assigned (e.g., "easy," "medium," "hard")
- Could be computed automatically (e.g., distance from class centroid)
- Could be based on model prediction (e.g., examples the network gets wrong)

### Easy Example

An example that the network can learn quickly.

Characteristics:
- Clear signal
- Unambiguous label
- Similar to examples network has seen
- Helps build foundations

### Hard Example

An example that challenges the network.

Characteristics:
- Subtle signal
- Ambiguous or complex
- Novel or unusual
- Requires advanced understanding

### Warm-up

An initial period of training with easy examples only.

Helps the network establish basic representations before seeing complexity.

### Transfer

The ability to apply knowledge from easy examples to solve hard examples.

Goal of curriculum learning: ensure transfer occurs smoothly.

### Self-paced Learning

A variant where the network chooses which examples to see (or how to weight them) based on its own learning progress.

Related to curriculum learning but more dynamic.

### Mining

Selecting particularly informative examples (often hard examples) to train on.

The opposite of curriculum learning in some ways — focuses on hard examples.

---

## Common Mistakes

### Mistake 1: Curriculum Learning Always Helps

**Wrong:** "Use curriculum learning for all problems."

**Why wrong:** Curriculum learning isn't always beneficial.

**When it doesn't help:**
- Very simple tasks (dataset so easy that random order is fine)
- When examples are naturally ordered (time series)
- When difficulty metric is hard to define
- Small datasets where reordering matters less

**Right:** Use curriculum learning when you have complex tasks and can meaningfully define difficulty.

### Mistake 2: Starting Too Easy

**Wrong:** "Only train on the 10 easiest examples first."

**Why wrong:** The network might never learn to generalize beyond these easy cases.

**Result:** Poor performance on harder examples.

**Right:** Balance — include some medium examples early to promote generalization.

### Mistake 3: Not Transitioning Gradually

**Wrong:** "Train on easy examples until 99% accuracy, then switch to hard."

**Why wrong:** Sudden jump in difficulty causes a learning cliff. The network struggles to adapt.

**Result:** Performance dips, slower overall learning.

**Right:** Gradually mix in harder examples — transition smoothly.

### Mistake 4: Using Random Difficulty Metric

**Wrong:** "Assign difficulty labels randomly."

**Why wrong:** The curriculum is not actually ordered by difficulty. It is just random with labels.

**Right:** Use a principled difficulty metric based on task properties or model performance.

### Mistake 5: Forgetting to Test on All Examples

**Wrong:** "Train with curriculum, but only evaluate on easy examples."

**Why wrong:** You don't know if the network actually learned to solve hard examples.

**Right:** Evaluate regularly on all difficulties to monitor generalization.

---

## Key Takeaways

**What it is:**
- A training strategy that presents examples in difficulty order
- Start with easy examples, progress to hard ones
- Gradual curriculum design instead of random order

**Why it helps:**
- Networks learn faster with simple examples first
- Foundation building improves overall learning
- Smooth progression reduces training difficulty
- Better convergence to good solutions

**How it works:**
1. Define a difficulty metric for examples
2. Organize training examples into difficulty phases
3. Train with examples in order (or gradually mix in harder ones)
4. Monitor learning progress across difficulty levels

**The key insight:**
- Just like humans learn best with structured progression, neural networks benefit from curriculum
- Random order wastes training time on inappropriately difficult examples early on

**In grokking research:**
- Curriculum learning can interact with grokking phenomena
- Different difficulties might grok at different times
- Predictors might behave differently with curriculum

---

## How It Connects to Training

[[Early Stopping]] — Curriculum learning can change when to stop:
- With curriculum, easy examples might converge quickly
- But hard examples need more time
- Stopping early might miss generalization on hard examples

[[Grokking Predictors]] — Different predictors might signal grokking at different times:
- Easy examples: early grokking signal
- Hard examples: delayed signal
- Overall predictor must account for this

[[Regularization]] — Curriculum learning is a form of implicit regularization:
- Starting simple prevents overfitting to complex patterns
- Gradual increase in difficulty improves generalization

[[Generalization]] — The ultimate goal of curriculum learning:
- Ensure network learns patterns, not memorization
- Extend learning from easy to hard examples

---

## Related Notes

**Understanding curriculum learning:**
- [[Grokking]] — Phenomenon that curriculum learning can affect
- [[Memorization]] — Curriculum learning helps prevent this
- [[Generalization]] — What curriculum learning promotes

**Related training strategies:**
- [[Early Stopping]] — When to stop training
- [[Weight Decay]] — Another form of regularization
- [[Dropout]] — Another technique to prevent overfitting

**In research:**
- [[Grokking Predictors]] — How curriculum affects predictors
- [[05 - Thesis/Experimental Designs Used in Literature]] — Training methodology
- [[Methodological Considerations]] — How to design fair comparisons

**Key concepts:**
- [[Feature Learning]] — What happens during curriculum
- [[Representation Learning]] — How representations develop
- [[Phase Transition]] — Curriculum can affect phase transitions