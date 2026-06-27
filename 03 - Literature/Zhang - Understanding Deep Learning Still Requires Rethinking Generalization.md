---
tags: [literature, generalization, memorization, foundational, primary-evidence]
---
↑ Parent: [[00 - Start Here]] · Hub: [[Memorization]] · [[Generalization]]

# Zhang — Understanding Deep Learning (Still) Requires Rethinking Generalization

# Citation
Zhang, C., Bengio, S., Hardt, M., Recht, B., & Vinyals, O. (2021). *Understanding deep learning (still) requires rethinking generalization.* Communications of the ACM 64(3). (Updates the 2017 ICLR paper.)

# The Gist (Plain Words)
The famous experiment showing networks can memorise completely random labels — so classic theories cannot explain why the same networks generalise on real data. We need to rethink generalisation.

# Research Question
Do classical explanations of generalization (model-family capacity, explicit regularization) actually explain why large neural networks generalize — and what does it mean that they can also **memorize** arbitrary data?

# Methodology
The **randomization test**: replace training labels (and even images) with random noise and retrain state-of-the-art CNNs. Plus a theoretical construction of finite-sample expressivity for depth-2 nets.

# Key Findings
- SOTA networks **fit random labels and random-noise inputs to zero training error** — so raw capacity cannot explain generalization.
- This is **qualitatively unaffected by explicit regularization** (weight decay, dropout, data augmentation) — regularization is neither necessary nor sufficient for generalization.
- Depth-2 nets have **perfect finite-sample expressivity** once parameters exceed data points.
- Traditional complexity measures (VC, Rademacher, uniform convergence) fail to be predictive.

# Strengths
- The defining empirical statement of the **generalization puzzle** that grokking dramatizes.
- Cleanly separates *ability to memorize* from *tendency to generalize*.

# Limitations
- Diagnostic/negative result — shows what *doesn't* explain generalization, not what does.
- Vision CNNs; not grokking or algorithmic tasks.

# Relation to Other Papers
- Sets up the puzzle answered dynamically by grokking and statically by [[Double Descent]] ([[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]]).
- "Memorize anything yet generalize" directly motivates [[05 - Memorization vs Generalization]] and the implicit-regularization view of [[Advani - High-dimensional Dynamics of Generalization Error]].
- Its "regularization isn't the whole story" stance informs the nuance in [[Role of Weight Decay]].

# Relevance to Thesis
High (foundational/framing). The canonical evidence that **memorization ≠ generalization** and that capacity/regularization alone don't explain generalization — the premise every grokking study builds on.

# Key Quotes
> "state-of-the-art convolutional networks ... easily fit a random labeling of the training data. This phenomenon is qualitatively unaffected by explicit regularization and occurs even if we replace the true images by completely unstructured random noise."

# Tags
#generalization #memorization #randomization-test #foundational #primary-evidence

---
## Related Notes
- [[Memorization]] · [[The Generalization Puzzle]] · [[05 - Memorization vs Generalization]] · [[Role of Weight Decay]]
