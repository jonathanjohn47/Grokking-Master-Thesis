---
tags: [concept, generalization, robustness]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Out-of-Distribution (OOD) Generalization

## Definition
**Out-of-distribution (OOD) generalisation** measures how well a model performs on data drawn from a *different distribution* than its training set. Its easier sibling is **in-distribution (i.i.d.) generalisation** — performance on data from the *same* distribution as training. Passing the OOD test is the gold standard of understanding; passing only the i.i.d. test proves only that the model handles more of the same.

## The Distinction in Plain Terms

Imagine a student trained on arithmetic problems from one textbook:
- **i.i.d. test**: more problems from the same textbook, same style, same difficulty. Easy.
- **OOD test**: problems from a different textbook, different notation, slightly different framing. Hard — and this is where shortcuts get exposed.

The student who memorised solution patterns will fail the OOD test. The student who understood the underlying rule will pass. Generalisation, properly defined, means passing the OOD test.

## Why Grokking is a True OOD Test

The canonical grokking setup uses a **random train/test split** of all $(a, b)$ pairs — 30% training, 70% test. This is not quite "OOD" in the sense of a different distribution, but it is **genuinely held-out**: the model never sees test pairs during training.

Crucially: if the model memorises the training pairs (lookup table), it achieves *exactly* chance test accuracy (~1/97 ≈ 1%) on the held-out pairs — because the rule "I've seen this exact pair before" fails completely on unseen pairs. The test set is not i.i.d. from the model's perspective; the memorising model assigns no probability to unseen patterns.

This is why test accuracy in grokking is a genuine generalisation signal, not i.i.d. noise: the two competing solutions (memorising and generalising) *disagree completely* on the held-out set.

## The i.i.d. / OOD Ladder

[[Geirhos - Shortcut Learning in Deep Neural Networks]] identified a hierarchy of decision rules that agree in-distribution but disagree out-of-distribution:

| Rule | Works i.i.d.? | Works OOD? |
|---|---|---|
| **Random label memorisation** | Yes (overfitting) | No |
| **Shortcut features** (texture, background) | Yes (in the training dataset) | No (new distribution) |
| **Partial rule** (correct feature, brittle) | Yes | Partially |
| **True rule** (correct, robust feature) | Yes | Yes |

Grokking is the network moving from the first row to the last — abandoning the memorising rule for the true rule.

## OOD Generalisation and Grokking Predictor Transferability

A key thesis question (RQ3, RQ4): do [[Grokking Predictors]] that work on modular addition *transfer* to other tasks? This is an OOD question about the predictors themselves:
- A predictor calibrated on $(a + b) \bmod 97$ should still fire (with similar timing and accuracy) on $(a \times b) \bmod 97$ or on XOR tasks.
- If it does, the predictor is truly detecting a general mechanism.
- If it doesn't, the predictor is a shortcut — it works by recognising a superficial property of modular-addition training dynamics, not the fundamental grokking mechanism.

This mirrors exactly the i.i.d./OOD distinction for models: a "shortcut predictor" would generalise only within the training task.

## Robustness and OOD Generalisation

[[Margin and Robustness]] connects directly to OOD performance: a model with high decision-boundary margin and low Jacobian sensitivity will maintain its predictions across distribution shifts. The [[Fourier Features|Fourier circuit]] is robust (multiple redundant heads, clean algebraic structure) and the memorising solution is brittle (specific pattern matching) — this is exactly why grokking improves OOD performance.

## Key Insights
- **Random train/test splits only measure i.i.d. performance** — by construction the two sets look alike.
- A model has many rules that fit the training data; they agree i.i.d. but **disagree OOD** — that's where shortcuts hide ([[Geirhos - Shortcut Learning in Deep Neural Networks]]).
- In grokking, the memorising solution achieves 1% test accuracy (chance), while the generalising solution achieves ~99% — maximum i.i.d./OOD disagreement.
- Predictor transferability (thesis RQ3) is an OOD generalisation question about the predictors themselves.
- Robust generalisation often requires the right [[Inductive Bias]], not just more data.

## Evidence
- [[Geirhos - Shortcut Learning in Deep Neural Networks]] — defines the i.i.d./OOD ladder of decision rules.
- [[Sokolić - Robust Large Margin Deep Neural Networks]] — larger margins give robustness to distribution shifts (a form of OOD stability).

## Relationship to Other Concepts
- The standard test for [[Generalization]]; the failure mode is [[Shortcut Learning]].
- Connected to [[Margin and Robustness]] (high margin → better OOD stability).
- [[Inductive Bias]] determines which solution is found — good bias → true rule → good OOD.
- Predictor transferability (thesis RQ3, RQ4) is an OOD generalisation question for the predictors themselves.

## Open Questions
Do grokking predictors that work on one task transfer to OOD tasks (thesis RQ3, RQ4)? Is a grokked circuit's robustness fully OOD, or does it depend on properties of the specific modular arithmetic family?

---
## Related Notes
- [[Shortcut Learning]] · [[Generalization]] · [[Margin and Robustness]] · [[Inductive Bias]]
- [[Geirhos - Shortcut Learning in Deep Neural Networks]] · [[Sokolić - Robust Large Margin Deep Neural Networks]]
- [[Grokking Predictors]] · [[Fourier Features]] · [[The Nine Predictors]]
