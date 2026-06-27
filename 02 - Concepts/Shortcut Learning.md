---
tags: [concept, generalization, robustness]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Shortcut Learning

## Definition
**Shortcut learning** is when a network learns a spurious rule that happens to work on the specific training and test distribution it sees, but fails when data changes. The network has found an easy feature that correlates with the label in the training set — a "shortcut" that avoids learning the intended rule. It looks like generalisation but is brittle to distribution shift.

## In Plain Words
You want a model to recognise cows by their shape. Instead it notices cows usually stand on grass, so it learns "green background = cow." It aces the normal test (cows really *are* on grass in that dataset) and flops on a cow at the beach. It found an easier rule than the intended one — a shortcut.

## The Grokking Connection

In grokking, the **memorising phase is a shortcut**:
- The network learns to predict training labels correctly by storing (input, label) associations.
- This is a shortcut because it matches the training set *exactly* — but the rule is "I've seen this exact pair before," not "I understand modular arithmetic."
- Crucially, on the held-out test pairs the shortcut fails completely: these pairs were never seen, so the lookup-table rule produces chance accuracy.
- Grokking is the network **abandoning the shortcut** and discovering the real rule: [[Fourier Features|Fourier angle-addition]].

This makes grokking a uniquely clean case study of shortcut abandonment:
1. We can diagnose the shortcut precisely (memorisation = lookup table).
2. We know the intended rule (Fourier circuit).
3. We can watch the transition happen by monitoring internal signals.

## Taxonomy of Shortcuts (Geirhos et al.)

[[Geirhos - Shortcut Learning in Deep Neural Networks]] identified three levels:

| Level | What the network uses | Example |
|---|---|---|
| **Texture** shortcuts | Surface statistics rather than shape | Classifying a cat from fur texture, not outline |
| **Background/context** shortcuts | Background scene rather than object | "Cow" because of grass background |
| **Dataset** shortcuts | Biases specific to the dataset (e.g. camera angle, watermarks) | Always "cat" for images with specific aspect ratio |

For algorithmic tasks like modular arithmetic, the analogue is **position shortcuts**: the network may learn to predict the right answer for specific $(a, b)$ pairs without learning the underlying structure — the modular-arithmetic equivalent of a texture shortcut.

## Why Shortcuts Are Easy to Take

Shortcuts are the path of least resistance for an [[Inductive Bias|inductive bias]] that doesn't perfectly align with the task structure:
- In the training set, shortcuts and the true rule both produce the correct label.
- Shortcuts are often *simpler* (lower norm, faster to learn) than the true rule.
- The network takes whatever gives correct predictions fastest.

This is exactly why the memorising solution forms first in grokking — it is the fastest shortcut available: memorise each pair explicitly. Only [[Weight Decay]] pressure eventually makes the *true rule* preferable.

## Detecting Shortcut vs True Rule

The only reliable way to detect shortcuts is to test on data that breaks the shortcut:
- **Distribution shift**: test on data from a different distribution than training.
- **Adversarial examples**: find inputs that break the shortcut while preserving the true label.
- **Mechanistic inspection**: check *what the network actually computes* (see [[Mechanistic Interpretability]]).

For grokking, the held-out test pairs serve as the distribution-shift check — they are never seen during training, so the memorising shortcut immediately fails on them.

## Shortcut Learning as Predictor Failure Mode

A key concern for [[Grokking Predictors]]: if a predictor fires based on a shortcut feature of the training dynamics, it may give false positives. For example:
- If weight norm drops early due to a network compressing its memorising solution (not because the generalising circuit is forming), the L2-norm predictor would fire incorrectly.
- Ensuring predictors track genuine generalising circuit formation — not compression of shortcuts — is a methodological challenge.

## Key Insights
- Models take the **path of least resistance**: if a simple feature explains the training data, they use it ([[Inductive Bias]]).
- A shortcut passes the usual (i.i.d.) test but fails **out-of-distribution** — see [[Out-of-Distribution Generalization]].
- The only reliable way to catch a shortcut is to **test on data that differs** from training, or inspect the rule the model actually uses ([[Mechanistic Interpretability]]).
- Grokking is shortcut *abandonment*: the memorising solution is the shortcut, and grokking is the network discovering the true rule.

## Evidence
- [[Geirhos - Shortcut Learning in Deep Neural Networks]] — comprehensive analysis of shortcut types and their causes.
- [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] — networks can memorise random labels, confirming shortcuts are the default.
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — shows exactly when the shortcut (memorising circuit) is abandoned and the true rule (Fourier circuit) forms.

## Relationship to Other Concepts
- The real-world face of the [[Memorization]] vs [[Generalization]] split.
- Tied to [[Inductive Bias]] (determines which shortcuts are preferred) and [[Out-of-Distribution Generalization]] (the test of whether learning was genuine).
- In grokking: memorising circuit = shortcut; [[Circuit Formation|Fourier circuit]] = intended rule.
- [[Mechanistic Interpretability]] is the tool for determining whether a network is using a shortcut or the true rule.

## Open Questions
Can a "shortcut score" act as an early signal during the grokking plateau — detecting that the memorising shortcut is still dominant? Do predictors that detect grokking also detect when a model is *still* on a shortcut vs has begun the transition to the true rule?

---
## Related Notes
- [[Geirhos - Shortcut Learning in Deep Neural Networks]] · [[Out-of-Distribution Generalization]] · [[Inductive Bias]]
- [[Generalization]] · [[Memorization]] · [[Mechanistic Interpretability]]
- [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]]
- [[Grokking Predictors]] · [[Circuit Formation]] · [[Fourier Features]]
