---
tags: [concept, generalization, core]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Memorization

## Definition
**Memorization** is fitting training labels without learning the underlying rule — effectively storing a lookup table. It yields zero training error but chance-level test accuracy on unseen data. Overparameterized networks can memorise even **random** labels and random-noise images ([[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]]).

## In Plain Words
Passing by rote: the network stores the answer to each training question without understanding why. It scores perfectly on what it has seen and fails on anything new. It is the quick, lazy solution a network reaches first — before (sometimes) grokking the real rule.

## What Memorization Looks Like in Practice

For a network trained on $(a+b)\bmod 97$ with 30% of all pairs as training data:

- **After memorisation:** the network produces the correct answer for each specific $(a,b)$ pair it was trained on — essentially by running a lookup in the weights. Ask it about an *unseen* pair and it guesses randomly (1/97 chance correct).
- **During the plateau:** it continues to memorise perfectly. From the outside, nothing appears to change.
- **After grokking:** the *same* training accuracy (100%) continues, but now via the [[Fourier Features|Fourier circuit]] — a compact algorithm that handles all pairs, seen and unseen.

Both states achieve zero training loss. Memorisation uses a fat, high-norm lookup structure; the grokked state uses a thin, low-norm, algorithmic circuit.

## Why Memorization Comes First

Memorisation is *locally easy*: fitting each example can be done independently, without shared structure. Finding the generalising rule requires coordinating across many examples simultaneously — a harder, slower process. Specifically:
- The memorising solution has **larger weight norm** and occupies a local minimum reached quickly.
- The generalising solution has **smaller weight norm** but is harder to reach — it requires assembling the [[Fourier Features|Fourier circuit]] across multiple layers simultaneously.
- [[Weight Decay]] slowly erodes the advantage of the memorising solution, eventually tipping the balance.

## Key Insights

- **Memorisation ≠ [[Overfitting]].** [[Rocks - Memorizing Without Overfitting]] showed explicitly that a model can memorise training data and still generalise — "memorising without overfitting." This happens because the test data is drawn from the same distribution as training data; memorisation of the training signal does not destroy the structure needed to generalise.
- **Norm gap.** Memorising solutions have larger weight norm than generalising ones. This is why the [[Grokking Predictors|L2-norm predictor]] tracks the transition — as norm drops under [[Weight Decay]], the network is moving from memorisation toward generalisation.
- **Not all interpolating solutions are equal.** [[Xu - Dynamics in Deep Classifiers with the Square Loss]] shows zero training loss does not imply large margin or good generalisation. The memorising solution is one of *many* zero-loss solutions; they differ in margin, norm, and test accuracy.
- **Random labels are memorised too.** [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] showed networks memorise even completely random labels (zero training loss) — proving memorisation capacity is far beyond what is "needed" for learning.

## Evidence
- [[Rocks - Memorizing Without Overfitting]] — bias/variance of interpolating models.
- [[Mei - Generalization Error of Random Features Regression]] — interpolators can generalise best.
- [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] — networks memorise random labels while generalising on real data.
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] — the Phase 1 (memorisation) observation.

## Relationship to Other Concepts
- The opposite of [[Generalization]], but both achieve zero training loss.
- Enabled by [[Overparameterization]] past the [[Interpolation Threshold]].
- The memorise→generalise handover is the subject of [[Circuit Formation]].
- Superficially resembles [[Overfitting]] (train 100%, test chance) but is not the same thing.
- The network exits memorisation via [[Weight Decay]] pressure (see [[Role of Weight Decay]]).
- The [[Early Stopping]] heuristic would mistakenly terminate here.

## Open Questions
What exactly distinguishes the memorising minimum geometrically from the generalising one, beyond norm? Is there always a margin gap that regularisation can exploit, or are there tasks where memorisation and generalisation have similar norm?

---
## Related Notes
- [[Generalization]] · [[Overfitting]] · [[Early Stopping]]
- [[Overparameterization]] · [[Weight Decay]] · [[Circuit Formation]]
- [[Zhang - Understanding Deep Learning Still Requires Rethinking Generalization]] · [[Rocks - Memorizing Without Overfitting]]
- [[05 - Memorization vs Generalization]] · [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]
