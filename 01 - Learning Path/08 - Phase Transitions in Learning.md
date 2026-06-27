---
tags: [learning-path, theory, phase-transition]
---
← Previous: [[07 - Double Descent]]  ↑ Parent: [[00 - Start Here]]  → Next: [[09 - Weight Decay and Regularization]]

# 08 - Phase Transitions in Learning

## What Is This Note About?

Grokking is not just a curiosity about neural networks. It is an example of a much broader phenomenon found throughout science: **phase transitions**.

Understanding phase transitions — what they are, why they happen, and how to detect them — gives us powerful tools for understanding and predicting grokking.

This note explains phase transitions in plain terms and shows how they connect to learning in neural networks.

---

## What Is a Phase Transition?

A **phase transition** is when a system abruptly switches from one state to another as a single condition crosses a threshold.

The most familiar example: water and temperature.

- At 1°C, water is liquid.
- At 0°C, water starts to freeze.
- At -1°C, water is solid ice.

One degree of change causes a complete transformation of the material. The water does not gradually become "a bit more ice-like." It flips.

This abrupt, threshold-driven change is a phase transition.

---

## Why Phase Transitions Are Interesting to Scientists

Phase transitions are studied because they are universal — the same mathematics describes them across completely different systems:
- Water freezing (physics)
- A magnet losing its magnetism when heated (physics)
- Populations of bacteria suddenly dying when resources run out (biology)
- Financial markets crashing (economics)

In each case, a single "control parameter" (temperature, resource level, market pressure) crosses a threshold, and the system abruptly changes state.

The key tools for studying phase transitions are:
1. The **control parameter** — the thing you change that eventually triggers the transition.
2. The **order parameter** — a measurement that is near zero in one phase and clearly nonzero in the other. This is how you detect which phase the system is in.

---

## Grokking as a Phase Transition

Grokking fits this pattern perfectly.

- The system: a neural network during training.
- The control parameter: training time (number of steps).
- The two phases:
  - **Memorisation phase:** Network answers new questions randomly (test score near 0%).
  - **Generalisation phase:** Network answers new questions correctly (test score near 100%).
- The transition: the sudden jump in test accuracy — the grokking moment.

Just like water freezing, the jump from memorisation to generalisation is abrupt. There is no smooth, gradual transition. The network is in one state, then it is in another.

---

## Order Parameters: The Key to Detection

If grokking is a phase transition, then finding the right **order parameter** is the central challenge.

An order parameter is a measurement that:
- Is near zero in the memorisation phase
- Becomes clearly nonzero as generalisation approaches
- Changes *before* the obvious symptom (test accuracy) does

Why does this matter? Because during the grokking plateau, test accuracy is stuck at near 0%. You cannot use test accuracy to tell if grokking is coming. You need a measurement that starts changing *during the plateau*, before the jump happens.

This is exactly what grokking predictor research is about: **finding the right order parameter for the grokking phase transition**.

---

## Examples of Proposed Order Parameters

Researchers have proposed several measurements as order parameters for grokking:

**1. Weight norm (total size of all weights)**
- During memorisation: weight norm is large (the memorised solution needs large values).
- As generalisation approaches: weight norm decreases.
- Signal: a drop in weight norm during the plateau.

**2. Spectral power-law exponent (a measure of weight matrix patterns)**
- During memorisation: weight matrices show a certain pattern.
- As generalisation approaches: the pattern changes in a specific, measurable way.
- Signal: the power-law exponent changes before test accuracy does.

**3. Entanglement entropy (used in non-neural-network systems)**
- In a non-neural-network learning system, a quantity called "entanglement entropy" was found to spike sharply right at the grokking transition.
- This is like an order parameter that jumps from one value to another at the exact moment of grokking.

**4. Information measures (how much information different parts of the network share)**
- During memorisation: information inside the network is organized in one way (called "synergistic").
- At grokking: it reorganises to a different way (called "redundant").
- Signal: this reorganisation can be detected before test accuracy jumps.

> [!NOTE]
> The thesis in this vault is specifically about comparing these proposed order parameters — finding out which one reliably predicts grokking earliest, across different tasks and network sizes. See [[The Nine Predictors]] and [[11 - Predicting Grokking]].

---

## Phase Transitions in the Research Literature

Researchers from physics have found phase transitions in many learning problems. Here are examples from the papers in this vault:

| Paper | What changes (control parameter) | What transition was found |
|-------|----------------------------------|--------------------------|
| Barbier et al. | Number of training examples | Sharp boundary: below it, the model cannot learn; above it, it succeeds completely |
| Spigler et al. | Number of parameters vs. constraints | At the interpolation threshold, a sharp "jamming" transition occurs |
| Biroli et al. | Denoising time in diffusion models | Two distinct transitions: one where the model identifies the category, one where it collapses to specifics |
| Pomarico et al. | Training time | A sharp entanglement transition coincides with grokking |

All of these are examples of the same underlying mathematical structure: a control parameter crossing a threshold, causing an abrupt change in the system's behaviour.

---

## Sharp vs. Gradual Transitions

Not all transitions are equally abrupt.

In physics, there are two types:
- **First-order transitions:** Very sharp and abrupt (like water freezing — ice and water coexist only briefly at exactly 0°C).
- **Second-order transitions:** More gradual (like a magnet losing its magnetism — it happens smoothly as temperature rises).

Grokking appears to be more like a first-order transition — very sharp. The jump in test accuracy happens over just a few hundred training steps, even after 40,000+ steps of plateau. This abruptness is part of what makes grokking so striking.

During the plateau, the network is in a **metastable state** — like water cooled below 0°C that has not yet started to freeze. It can exist in this state for a long time, but eventually the transition happens, and when it does, it happens fast.

---

## Why the Physics Perspective Is Useful

Bringing physics tools to learning research provides:

1. **Mathematical rigour:** The physics tools (called replica method, random matrix theory, message passing) allow exact calculation of where transitions happen, not just approximate simulation.

2. **Universal insights:** Because the same mathematics describes transitions in many systems, insights from one system can transfer to another.

3. **The concept of order parameters:** This gives researchers a clear framework for what they are looking for when they study grokking predictors. An order parameter is not just a useful measurement — it is a theoretically meaningful quantity that characterises the phase.

---

## The Connection Between Grokking Predictors and Order Parameters

> [!IMPORTANT]
> Every grokking predictor is, in essence, a proposed order parameter for the grokking phase transition.
>
> When researchers propose a new predictor (like weight norm, or spectral patterns, or information measures), they are saying: "I think this is the quantity that characterises which phase the network is in."
>
> The thesis tests which proposed order parameter is most reliable — which one fires earliest, most consistently, and across the most different situations.

---

## Important Terms

**Phase transition:** An abrupt change in a system's behaviour as a control parameter crosses a critical threshold. Examples: water freezing, a magnet demagnetising, a network going from memorisation to generalisation.

**Control parameter:** The quantity you change that eventually triggers the phase transition. In grokking, this is training time.

**Order parameter:** A measurement that is near zero in one phase and clearly nonzero in the other. Used to detect which phase the system is in.

**Metastable state:** A state that looks stable but is not truly stable. Like supercooled water — it has not frozen yet, but it is ready to freeze at any moment. The plateau in grokking is a metastable state.

**Entanglement entropy:** A measure used in quantum physics to describe how entangled (correlated) different parts of a system are. Found to be an order parameter for grokking in tensor-network systems.

**Synergistic information:** Information that only makes sense when multiple parts are considered together — more than the sum of the parts.

**Redundant information:** Information that is shared and repeated across multiple parts. At grokking, the network's internal information reorganises from synergistic to redundant.

**First-order transition:** A sharp, abrupt phase transition. Grokking appears to be first-order.

**Second-order transition:** A gradual phase transition.

---

## Key Takeaways

- A phase transition is an abrupt change from one state to another as a single parameter crosses a threshold.
- Grokking is a phase transition: the network abruptly switches from the memorisation phase to the generalisation phase.
- Finding the right order parameter — a measurement that changes before test accuracy does — is the central challenge of grokking prediction research.
- The physics framework (phase transitions, order parameters) provides both mathematical tools and conceptual clarity for understanding grokking.
- Every grokking predictor is a proposed order parameter. The thesis compares them to find which is most reliable.

---

## Related Notes
- [[Phase Transition]] · [[Jamming Transition]]
- [[Phase Transitions Across Models]] (synthesis)
- [[Grokking Predictors]]
- [[09 - Weight Decay and Regularization]]
