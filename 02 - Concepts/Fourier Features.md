---
tags: [concept, mechanistic, circuits, grokking, fourier]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Fourier Features

## What Is It?

**Fourier features** are a way of representing numbers as positions on circles.

In the context of grokking, the network that has learned to do clock math (addition mod 97) has secretly invented a way of representing each number as a rotation angle — and then adds two numbers by adding their rotation angles.

This is the "algorithm" inside the grokked network. The network did not start with this algorithm. It invented it during the plateau, through the pressure of weight decay and the gradients from training.

---

## Why Does It Exist?

After grokking, researchers could see that the network was getting the right answers on new questions. But they wanted to know **how** it was computing those answers.

They reverse-engineered the trained network and found a beautiful, elegant algorithm based on angles and circles. This is the Fourier circuit.

The name "Fourier features" comes from Jean-Baptiste Joseph Fourier, a 19th-century mathematician who discovered that any repeating pattern can be described as a combination of waves of different frequencies. The clock math network's algorithm uses exactly this idea.

---

## The Clock Analogy

Before getting into the grokking specifics, here is the core idea using a real clock:

- Imagine a 12-hour clock. The position of the hour hand represents the time.
- 12 o'clock = pointing straight up (0 degrees)
- 3 o'clock = pointing right (90 degrees)
- 6 o'clock = pointing down (180 degrees)
- 9 o'clock = pointing left (270 degrees)

Now: what is 10 o'clock + 4 hours?
- 10 o'clock = 300 degrees
- 4 hours = 120 degrees
- Add the angles: 300 + 120 = 420 degrees
- 420 degrees wraps around to 60 degrees (420 - 360 = 60)
- 60 degrees = 2 o'clock

You have computed clock addition by adding angles! The modular wrap-around (going past 12 and starting again) happens automatically — the circle handles it.

The grokked network does exactly this, but with a clock that has 97 positions instead of 12.

---

## How the Grokking Network Uses This

For the clock-math task with 97 positions (addition mod 97), the grokked network uses multiple "clocks" running at different speeds simultaneously. Here is the step-by-step process:

**Step 1 — Encode each number as angles:**
Each input number (A and B) is converted to a set of rotation angles — one for each "clock speed." Using about 5 different clock speeds, the network creates a rich representation of each number as a combination of angular positions.

**Step 2 — Add the angles:**
The attention heads in the network compute what you get when you add the angles for A to the angles for B. There is a mathematical identity (from trigonometry) that lets you compute "the angle for A+B" if you know "the angle for A" and "the angle for B" separately.

In simple terms: instead of computing A+B directly, the network computes "what direction does A point, what direction does B point, and what direction does A+B point?"

**Step 3 — Read off the answer:**
The feed-forward network looks at the final combined angle and converts it back to the answer: which of the 97 positions is at that angle?

The result: the network can correctly compute A+B mod 97 for any A and B, even ones it has never seen during training. It is genuinely computing the answer, not looking it up.

---

## Why This Algorithm Won

The Fourier circuit won the competition against the memorised solution because it is **more efficient**.

**Memorised solution (lookup table):**
- Needs to store an answer for every training question separately.
- Requires large weights — many parameters with large values.
- Fails on new questions.

**Fourier circuit (angle algorithm):**
- Only needs to encode the rotation-angle representation and the addition rules.
- Requires small weights — a compact representation.
- Works on any question, including unseen ones.

Under weight decay (constant pressure to keep all weights small), the circuit with smaller total weight is favoured. Over the course of the plateau, weight decay gradually erodes the large lookup table while leaving the compact circuit relatively intact. Eventually, the circuit dominates — and grokking happens.

---

## Why This Is Remarkable

The network invented this algorithm on its own. Nobody told it to use rotations or angles or Fourier mathematics. The training process — minimising loss while weight decay kept weights small — led the network to rediscover an elegant mathematical approach to clock arithmetic.

When researchers first reverse-engineered the grokked network, they were surprised to find such a clean, interpretable algorithm inside it. Every weight in the circuit has a clear mathematical meaning.

This is what makes grokking scientifically valuable: it is a controlled, observable case where you can watch a network invent an algorithm and understand exactly what that algorithm is.

---

## Connection to Grokking Predictors

Because the Fourier circuit is what the network builds during the plateau, you can track circuit formation directly:

- Watch the embedding layer: when the numbers start being encoded as rotation angles, the circuit is forming.
- Watch the attention heads: when they start implementing the angle-addition computation, the circuit is maturing.

These measurements — tracking Fourier circuit formation — are among the most principled grokking predictors. They directly measure the phenomenon.

However, they require knowing what the circuit looks like (rotation angles, wave patterns). They are task-specific. One of the thesis's questions is: can task-agnostic signals (ones that do not require knowing the circuit structure) predict grokking just as well?

---

## An Everyday Analogy

Imagine learning to tell time on a 12-hour clock.

**Memorisation approach:** Memorise that at exactly 10:00, the hands look like [specific image]. At exactly 11:00, the hands look like [different image]. Memorise every hour. But if shown 10:30 — a time you haven't memorised — you fail.

**Fourier approach:** Learn that time is represented by angles. The hour hand points to 300 degrees at 10:00. Adding 30 minutes adds 15 degrees. You can now compute any time, not just the ones you memorised.

The Fourier circuit is the "learn the angle system" approach. The memorised solution is the "memorise every specific case" approach.

---

## Important Terms

**Fourier features:** A way of representing numbers as rotation angles on circles. Named after mathematician Fourier, who studied how patterns can be decomposed into waves.

**Rotation angle:** The angular position on a circle. Adding two rotations produces a new rotation — this is how the Fourier circuit adds numbers.

**Modular arithmetic (mod):** "Clock math." Addition that wraps around at a fixed point. (50 + 60) mod 97 = 13, because you go around the 97-position clock and land at 13.

**Trigonometric identity:** A mathematical rule about how angles combine. The key one here: the cosine of (A+B) can be computed from the cosines and sines of A and B separately. The attention heads implement this.

**Frequency:** In Fourier mathematics, different frequencies correspond to different "clock speeds." The grokked network uses about 5 different frequencies simultaneously.

**Circuit efficiency:** The property of producing correct outputs with less total weight. The Fourier circuit is more efficient than the lookup table.

---

## Key Takeaways

- The grokked network implements clock math by representing numbers as rotation angles and adding angles.
- This algorithm uses multiple "clocks" running at different speeds simultaneously.
- The algorithm was invented by the network through training — not programmed explicitly.
- It is more efficient (smaller total weight) than the memorised lookup table.
- Weight decay favours the efficient circuit over the bulky lookup table, causing the grokking transition.
- Tracking Fourier circuit formation provides the most direct predictor of grokking (but requires knowing the circuit structure).

---

## Related Notes
- [[Circuit Formation]] · [[Mechanistic Interpretability]] · [[Modular Arithmetic]]
- [[Attention Mechanism]] · [[Transformer]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] · [[Varma - Explaining Grokking Through Circuit Efficiency]]
- [[Weight Decay]] · [[Role of Weight Decay]]
