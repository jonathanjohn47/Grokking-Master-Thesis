---
tags: [literature, shortcut-learning, generalization, robustness, perspective]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Shortcut Learning]]

# Geirhos — Shortcut Learning in Deep Neural Networks

# Citation
Geirhos, R., Jacobsen, J.-H., Michaelis, C., Zemel, R., Brendel, W., Bethge, M., & Wichmann, F. A. (2020). *Shortcut learning in deep neural networks.* Nature Machine Intelligence, 2, 665–673.

# Research Question
Why do deep networks that score well on benchmarks so often fail in the real world? The authors argue that many separate-looking failures are really one problem: **shortcut learning**. A shortcut is a quick-and-dirty rule that works on the test set you happen to use, but breaks the moment the data changes a little.

# The Big Idea (in plain words)
A network is supposed to learn the *intended* rule (e.g. "tell a cow from a camel by its shape"). Instead it often learns a cheaper rule that just happens to work on the training photos (e.g. "cows appear on green grass, camels on sand"). On normal test photos the cheap rule looks great. Show it a cow on a beach and it fails. The network was never "wrong" by its own logic — it simply solved an easier problem than the one we cared about.

# Methodology
This is a **perspective / review paper**, not an experiment. It pulls together evidence from computer vision, language, reinforcement learning, and fairness, and borrows ideas from psychology and education to build a shared vocabulary. Its core tool is a simple **taxonomy of decision rules** (see below) and a toy star-vs-moon example showing a network that secretly classifies by *position* instead of *shape*.

# Key Findings
- **A ladder of solutions.** All possible rules → rules that fit the training data → rules that also work on similar (i.i.d.) test data → the intended rule. **Shortcuts sit on the second-to-last rung**: they pass the usual test but are not what we meant. See [[Out-of-Distribution Generalization]].
- **Shortcuts are everywhere.** Captioning models that never look at the image, X-ray models that read the hospital tag instead of the lungs, language models that latch onto the last sentence of a passage.
- **Why shortcuts happen.** Networks follow the *path of least resistance*: if a simple feature explains the training data, they take it. This is an [[Inductive Bias]] of the model plus dataset, not a bug in one network.
- **Biology does it too.** Rats "solving" mazes by smell, students passing exams by rote — the same gap between *intended* and *actual* learning.
- **Recommendations.** Test on **out-of-distribution** data, interpret the rule the model actually uses, and design harder benchmarks.

# Strengths
- Unifies a dozen scattered failure modes under one clear idea.
- Plain, intuitive framing (the decision-rule ladder) that travels across fields.
- Practical advice for benchmarking and interpretation.

# Limitations
- Conceptual, not a new method or theorem — it names and organises the problem rather than solving it.
- Mostly vision examples; less depth on language and RL.

# Relation to Other Papers
- The "many rules fit the training data, but they differ off-distribution" point is the *real-world* version of the **[[Memorization]] vs [[Generalization]]** tension grokking studies in miniature.
- Connects to [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]]: if a net can fit *anything*, what it actually fits depends on which rule is easiest — i.e. its shortcuts.
- The "intended vs cheap solution" framing mirrors **circuit efficiency** in grokking (memorising circuit = shortcut, generalising circuit = intended rule).

# Relevance to Thesis
Moderate–high (conceptual). Grokking is, in a sense, a network **starting on a shortcut (memorisation) and later switching to the intended rule (generalisation)**. Shortcut learning supplies the language for *why* a memorising solution can look perfect yet be wrong, and for why true generalisation must be tested off-distribution — directly relevant to how we define and measure a successful "grok."

# Key Quotes
> "Shortcuts are decision rules that perform well on standard benchmarks but fail to transfer to more challenging testing conditions."

> "Shortcut learning may be a common characteristic of learning systems, biological and artificial alike."

# Tags
#shortcut-learning #generalization #robustness #out-of-distribution #perspective

---
## Related Notes
- [[Shortcut Learning]] · [[Out-of-Distribution Generalization]] · [[Inductive Bias]]
- [[Memorization]] · [[Generalization]] · [[The Generalization Puzzle]]
