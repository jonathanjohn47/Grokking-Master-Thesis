---
tags: [concept, grokking, core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[01 - What Is Grokking]]

# Grokking

## Definition
**Grokking** is delayed generalisation: a neural network reaches perfect training accuracy quickly while test accuracy stays at chance, then — after a long plateau and far more training — abruptly generalises to near-perfect test accuracy. Generalisation arrives *long after* the network has interpolated (memorised) the training set. Coined by Power et al. (2022); the word is from Heinlein, meaning to understand something completely.

## In Plain Words
A network "gets it," but late. It nails the practice questions almost instantly, then looks completely stuck for a very long time, and then suddenly aces the real test out of nowhere. The understanding shows up long after it seemed to stop learning.

## A Concrete Example

Training a small [[Transformer]] on $(a+b)\bmod 97$ with a 30% train split and [[AdamW]] (weight decay = 1.0):

- **Step 0–1,000:** Train accuracy reaches 100%. Test accuracy stays near 1% (chance for 97 classes). The network has memorised the 30% of number pairs it saw.
- **Steps 1,000–40,000:** Both curves stay flat. Loss barely moves. A practitioner with [[Early Stopping]] would stop here, concluding the network is useless on test data.
- **Steps 40,000–41,000:** Test accuracy jumps from ~1% to ~99% in a few hundred steps.

The network has "grokked" — it discovered the **[[Fourier Features|Fourier circuit]]** for modular addition and can now compute the answer for any pair, not just the ones it memorised.

## Why It Is Surprising

> [!important]
> Three classical expectations all break:
> - **Generalisation should not lag memorisation by 100×.** [[Early Stopping]] would have discarded the model.
> - **A flat loss plateau usually means "done."** Here it hides a reorganisation in progress.
> - **More training past zero train-loss should overfit, not help.** Instead the *terminal phase* is where generalisation is born (compare [[Neural Collapse]]).

## What makes grokking valuable to study

Grokking is a **clean, reproducible microcosm of generalisation**. Because it happens in tiny models on tasks with a known ground-truth rule, you can watch the transition from [[Memorization]] to [[Generalization]] step by step — something impossible in a billion-parameter LLM. It connects directly to [[Double Descent]], [[Phase Transition|phase transitions]], [[Weight Decay|regularisation]], and [[Mechanistic Interpretability]].

## The Five Accounts of Why Grokking Happens

The **regularisation / circuit-efficiency** view ([[Varma - Explaining Grokking Through Circuit Efficiency]]): the generalising [[Fourier Features|Fourier circuit]] has lower weight norm than memorisation; [[Weight Decay]] slowly tips the balance. The **slow-mode** view ([[Advani - High-dimensional Dynamics of Generalization Error]]): GD has fast and slow eigenmodes; generalisation lives in the slow ones. The **mechanistic** view ([[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]): a specific algorithm (Fourier trig identities) forms gradually. The **information-theoretic** view ([[Pomarico - Transfer Entropy and O-Information to Detect Grokking]]): internal information reorganises from synergistic to redundant. The **geometric** view ([[Neural Collapse]]): representations tighten into a low-rank, collapsed, high-margin shape. See [[Competing Theories of Grokking]].

## The Practical Hook (Why the Thesis Exists)

During the plateau there is **no external signal** telling you whether the model will eventually grok or stay stuck forever. Practitioners either stop too early (losing a model that would have grokked) or run forever (wasting compute). This motivates **[[Grokking Predictors|internal early-warning signals]]** — the subject of [[Thesis Proposal Summary|the thesis]].

## Key Evidence in This Vault

- The founding paper: [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] — original discovery on [[Modular Arithmetic]] with [[Transformer|transformers]].
- The mechanism: [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — Fourier-circuit reverse-engineering.
- Beyond neural networks: [[Pomarico - Transfer Entropy and O-Information to Detect Grokking]] — grokking in tensor networks with an entanglement order parameter.
- Static analogues: [[Mei - Generalization Error of Random Features Regression]], [[Rocks - Memorizing Without Overfitting]].

## Relationship to Other Concepts
- Tension between [[Memorization]] and [[Generalization]].
- Lives in the [[Overparameterization]] regime, past the [[Interpolation Threshold]].
- Predicted by [[Grokking Predictors]]; its failure mode is [[Anti-Grokking]].
- A time-domain instance of the [[Phase Transition]] family; the static analogue is [[Double Descent]].
- The [[Transformer]] architecture (trained with [[AdamW]]) is the canonical experimental substrate.

## Open Questions
Single cause or many ([[Competing Theories of Grokking]])? A universal order parameter? Does it scale to large models? See [[13 - Open Problems and Research Gaps]].

---
## Related Notes
- [[01 - What Is Grokking]] · [[What Causes Grokking]] · [[Anti-Grokking]] · [[The Nine Predictors]]
- [[Weight Decay Necessity]] — does grokking require weight decay?
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
- [[Fourier Features]] · [[Transformer]] · [[AdamW]]
