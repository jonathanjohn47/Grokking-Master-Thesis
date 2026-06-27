---
tags: [literature, grokking, founding-paper, primary-evidence, algorithmic-tasks]
aliases: ["Power et al. 2022", "Grokking Paper"]
---

> [!NOTE]
> This is an alias note. The full literature review for this paper lives at:
> [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]

---

# Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets

**Authors:** Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin, Vedant Misra
**Year:** 2022
**ArXiv:** 2201.02177

---

## What Is This Paper?

This is the **founding paper** of the grokking phenomenon.

It describes something surprising: a small [[Transformer|transformer]] trained on modular arithmetic tasks first memorises all the training answers, then appears stuck for a very long time — and then, suddenly, learns the actual rule and generalises perfectly to unseen examples.

The authors named this "**grokking**" — after Robert Heinlein's term for deep, complete understanding.

> [!TIP]
> This paper is the starting point for everything in this vault. If you are new to the topic, begin here:
> [[01 - What Is Grokking]]

---

## One-Line Summary

> A tiny transformer can dramatically delay generalisation far past the point of memorisation — and then suddenly snap into full generalisation — when trained with weight decay on small algorithmic datasets.

---

## Why It Matters

Before this paper, it was generally assumed that:

* Once a model reaches 100% training accuracy, training is effectively over.
* Continued training past that point does little meaningful.

This paper showed that assumption is **wrong** — at least for certain settings.

The model can memorise first, then **later** discover the true underlying rule. The gap between memorisation and generalisation can be **hundreds of thousands of gradient steps**.

This opened an entirely new research direction asking: *why does delayed generalisation happen, and can we predict or control it?*

---

## Key Facts

| Item | Detail |
|---|---|
| Task | Modular arithmetic: $a \circ b \pmod{p}$ |
| Architecture | 1–2 layer transformer, ≤ 250K parameters |
| Training split | ~30% train, ~70% test |
| Optimiser | [[AdamW]] with [[Weight Decay\|weight decay]] |
| Key finding | Delayed generalisation: memorisation first, generalisation later |
| Key variable | Weight decay — larger weight decay → shorter delay |

---

## Key Finding

After reaching 100% training accuracy, test accuracy may stay near chance for **thousands or tens of thousands of steps** — then suddenly rise to near 100%.

```
Training accuracy:  ████████████████████████████████ 100% (early)
Test accuracy:      ░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓████ 100% (much later)
                    ←──── very long gap ────→ ↑ grokking
```

---

## What the Paper Does Not Explain

Power et al. **observe and name** the phenomenon but do not explain it mechanistically.

The explanation came later:

* **Mechanism:** [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — discovered the internal [[Fourier Features|Fourier circuit]] the network builds.
* **Cause:** [[Varma - Explaining Grokking Through Circuit Efficiency]] — explained *why* the generalising solution eventually wins.

---

## Full Literature Note

→ [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]

---

## Related Notes

- [[Grokking]] — the concept this paper introduced
- [[01 - What Is Grokking]] — beginner introduction
- [[02 - The Grokking Training Dynamics]] — detailed explanation of what happens during training
- [[04 - Core Experimental Setup]] — the specific setup used in this paper
- [[Weight Decay]] — the key variable that controls grokking
- [[Modular Arithmetic]] — the tasks used in the experiments
- [[Transformer]] — the architecture used
- [[Memorization]] — the first phase of training
- [[Generalization]] — the delayed second phase
- [[Phase Transition]] — how grokking resembles physical phase transitions
