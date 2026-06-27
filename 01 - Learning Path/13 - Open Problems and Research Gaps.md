---
tags: [learning-path, gaps, thesis-core]
---
← Previous: [[12 - Modern Developments]]  ↑ Parent: [[00 - Start Here]]  → Next: [[Vault Overview]]

# 13 - Open Problems and Research Gaps

## What Is This Note About?

Grokking research has made impressive progress since 2022. We understand the basic phenomenon, have several theories for why it happens, and have proposed multiple early-warning signals.

But many important questions remain unanswered.

This note lists the open problems — the things we still do not know — and explains where the thesis fits in addressing them.

---

## The Biggest Gap: No Fair Comparison Exists

The most important unresolved problem is simple to state:

> **No one has compared the nine grokking predictors fairly against each other.**

Each predictor was:
- Proposed by a different research team
- Tested on that team's own task and network setup
- Compared against at most two or three other predictors, sometimes none

This means:
- We do not know which predictor is most accurate overall.
- We do not know which fires earliest, giving the most lead time.
- We do not know which transfers best to different tasks and network sizes.
- We do not know whether any predictor works for detecting anti-grokking.
- We do not know if combining multiple predictors works better than any single one.

There is no "leaderboard" or standard benchmark. Researchers cannot look up which predictor to use when facing grokking in a new context.

This is the gap the thesis closes — by building the first unified benchmark with standardised rules, where only the signal quality differs between predictors.

---

## Open Scientific Question 1: What Causes Grokking?

Several competing theories explain why grokking happens. They are not mutually exclusive, but they are not fully unified either.

The main theories are:

**Theory 1 — Weight decay and circuit efficiency:** The generalised solution (a compact algorithm) needs less weight than the memorised solution (a lookup table). Weight decay eventually favours the more efficient solution. (Supported by Varma et al., 2023)

**Theory 2 — Slow-mode dynamics:** The training process has "fast" directions (where the network learns quickly) and "slow" directions (where learning takes much longer). Generalisation lives in the slow direction. The plateau is simply the time it takes for the slow direction to develop. (Supported by Advani et al., 2017)

**Theory 3 — Mechanistic circuit formation:** A specific algorithm (rotation-based arithmetic) is assembled inside the network. Grokking happens when this circuit becomes complete and takes over the outputs. (Supported by Nanda et al., 2023)

**Theory 4 — Information reorganisation:** The internal information of the network shifts from a "synergistic" pattern to a "redundant" pattern. This reorganisation is the grokking event. (Supported by Pomarico et al., 2025)

**Theory 5 — Geometric convergence:** The network's internal representations converge to a highly symmetric geometric arrangement. This convergence is the generalised solution. (Supported by Papyan et al., 2020)

**Open question:** Do these theories all describe different aspects of the same mechanism? Or do different tasks and networks produce grokking through different mechanisms?

---

## Open Scientific Question 2: Is There a Universal Order Parameter?

An order parameter is a measurement that changes sharply at the grokking transition and can serve as a reliable predictor.

Several candidates have been proposed. But no one has shown that any single measurement works reliably across:
- Different tasks (clock math, parity, image classification)
- Different network architectures (different depths, widths, numbers of heads)
- Different training algorithms (AdamW, Muon)

**Open question:** Does a universal order parameter exist — a single measurement that reliably detects grokking in all settings? Or do different settings require different predictors?

---

## Open Scientific Question 3: Does Prediction Transfer?

All grokking predictors were developed and tested primarily on clock-math tasks (addition mod 97).

But do they work when the task changes? Specifically:
- Do predictors calibrated on clock math work on parity tasks?
- Do they work on image classification?
- Do they work on language tasks?

**Open question:** Which predictors are task-specific, and which are genuinely general? Transferability is a key criterion for practical usefulness.

---

## Open Scientific Question 4: Grokking vs. Anti-Grokking

Grokking (sudden generalisation after memorisation) and anti-grokking (collapse of generalisation after it has occurred) are related phenomena. But they may require completely different detection methods.

Current evidence suggests:
- The signals that predict grokking may not predict anti-grokking.
- Anti-grokking may require its own dedicated detectors (like correlation traps).

**Open question:** Are grokking and anti-grokking governed by the same internal signals, or do they require fundamentally different approaches?

---

## Open Scientific Question 5: Does Grokking Scale?

Almost all grokking research uses tiny networks (100,000 to 250,000 parameters) on simple tasks (clock math, parity).

But modern AI systems are enormous (billions or trillions of parameters) trained on vast amounts of data.

Does grokking happen in large models? Do the same predictors work? If so, the lessons from grokking research could inform how we train and monitor large language models.

**Open question:** Does grokking occur in large-scale models? Do grokking predictors transfer to the large-model setting?

---

## Open Scientific Question 6: Bridging Theory and Dynamics

There is rigorous mathematical theory for "static" phenomena like double descent and phase transitions at fixed model sizes.

There is a good descriptive understanding of "dynamic" grokking (what the curves look like, what happens inside the network over time).

But there is not yet a rigorous mathematical bridge between the two:
- Can we derive exactly *when* grokking will happen from the model size, dataset size, and weight decay settings?
- Can we prove that specific predictors will always fire at a specific number of steps before grokking?

**Open question:** Can the static mathematical theory of generalisation be extended to make quantitative predictions about dynamic grokking?

---

## Methodological Gaps

In addition to the scientific questions above, there are also practical problems with how grokking research has been conducted:

**Inconsistent definitions:** Different research teams define "grokking" differently. Some say grokking happens when test accuracy exceeds 95%. Others use 90%. Others use a sharp rate of change. Without a shared definition, comparisons are meaningless.

**No standard calibration:** Different teams use different thresholds for deciding when a predictor "fires." Without shared calibration, a predictor that fires at a low threshold looks better than one that fires at a high threshold, even if both have the same underlying quality.

**Survivor bias:** When a predictor is tested on a set of experiments, teams often only report experiments where grokking happened. Experiments where the network never grokked are dropped. This makes predictors look more reliable than they are.

These methodological issues are addressed directly in the thesis design.

---

## Where the Thesis Fits

The thesis addresses the biggest gap: the missing fair comparison.

It builds a unified benchmark that:
- Uses the same definition of grokking across all experiments
- Uses the same calibration for all predictors
- Includes both grokking and non-grokking cases (no survivor bias)
- Tests all nine predictors on the same tasks and architectures
- Tests at least one predictor on anti-grokking detection

The result will be the first fair leaderboard of grokking predictors — telling practitioners which predictor to use and researchers which order parameter best characterises the grokking transition.

---

## Important Terms

**Open problem:** A question that has not yet been definitively answered by the scientific community.

**Universal order parameter:** A single measurement that reliably characterises the grokking transition across all tasks, architectures, and training settings.

**Transferability:** Whether a predictor or theory developed for one setting works in a different setting.

**Anti-grokking:** When a network that has achieved generalisation later loses it — the collapse of generalisation. The reverse of grokking.

**Survivor bias:** A methodological flaw where only successful cases are reported. In grokking research: only including experiments where grokking happened, ignoring cases where it did not.

**Calibration:** The process of choosing a threshold for when a predictor "fires." Without shared calibration, comparisons between predictors are unfair.

**Benchmark:** A standardised test used to compare different methods fairly. The thesis creates the first grokking predictor benchmark.

---

## Key Takeaways

- The biggest gap is the absence of a fair comparison between all nine grokking predictors.
- Open scientific questions include: what causes grokking? Is there a universal order parameter? Do predictors transfer to new tasks? How do grokking and anti-grokking relate? Does grokking happen at scale?
- Methodological problems (inconsistent definitions, different calibrations, survivor bias) make existing comparisons unreliable.
- The thesis fills the biggest gap by building the first standardised, fair benchmark of all nine predictors.
- This is both a practical contribution (a usable tool for practitioners) and a scientific one (a rigorous test of which order parameter best characterises the grokking transition).

---

## Related Notes
- [[Research Gaps]] · [[Future Directions]] · [[Potential Thesis Questions]]
- [[Competing Theories of Grokking]]
- [[Thesis Proposal Summary]]
