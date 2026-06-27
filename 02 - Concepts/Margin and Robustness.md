---
tags: [concept, margin, robustness, generalization]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[05 - Memorization vs Generalization]]

# Margin and Robustness

## Definition
The **classification margin** is the minimum distance from any training point to the model's decision boundary — a large margin means the decision is "confident and stable." **Robustness** is the model's insensitivity to small perturbations of the input — a robust model gives the same answer even when inputs are slightly corrupted. Together, large margin and high robustness are the distinguishing properties of a genuinely generalising solution, and they underlie the **Dropout Robustness** grokking predictor (Predictor #9 in [[The Nine Predictors]]).

## In Plain Words
**Margin** is how much breathing room there is between your examples and the line that separates the classes. A fat line divides two groups with lots of space; a razor-thin line barely separates them. **Robustness** means the answer doesn't flip when you nudge the input a little — the model's decision is stable, not brittle. Both are what set a genuinely good solution apart from one that merely memorises the training data.

## The Formal Picture

For a classifier $f: \mathbb{R}^d \to \mathbb{R}^K$ with decision boundary at $\{x : f_i(x) = f_j(x)\}$:

$$\text{margin}(x) = \min_{i \ne y} \left( f_y(x) - f_i(x) \right)$$

where $y$ is the true class. The **generalisation margin** (PAC-Bayes / Rademacher bounds) depends on:
- Minimum margin $\gamma = \min_{x_{\text{train}}} \text{margin}(x)$ 
- Model complexity (measured via spectral norm of weight matrices)

Specifically, [[Sokolić - Robust Large Margin Deep Neural Networks]] gives a width/depth-independent bound:
$$\mathcal{E}_{\text{test}} \le \mathcal{O}\!\left(\frac{\prod_l \|W_l\|_\sigma}{\gamma \sqrt{N}}\right)$$

where $\|W_l\|_\sigma$ is the spectral norm (largest singular value) of layer $l$'s weight matrix. The implication: **minimise spectral norms** (which [[Weight Decay]] does) and **maximise margin** → good generalisation bounds.

## Why Margin Distinguishes Memorisation from Generalisation

Both the memorising and generalising solutions achieve zero training error. Why does the generalising one have larger margin?

1. **Memorising solution**: fits training data by sharp, narrow decision boundaries near each training point — large logits for correct training labels, but tight boundaries elsewhere.
2. **[[Fourier Features|Fourier circuit]] (generalising)**: produces large logits for the correct class *for all inputs*, including test ones — a wide, smooth decision boundary.
3. The generalising solution has higher margin because its rule is *correct*, not just memorised — it confidently classifies the entire input space, not just the training points.

This is why the [[Simplex ETF]] geometry (which maximises class separation) is associated with both neural collapse and good generalisation: the ETF maximises the geometric margin.

## The Dropout Robustness Predictor

**Dropout robustness** (Predictor #9) operationalises margin as a grokking signal:
- At evaluation time (not training), apply dropout with a fixed rate $p$ to all activations.
- Measure test accuracy under this perturbation.
- A **grokked model's accuracy barely drops** under dropout — the Fourier circuit's multiple-head redundancy absorbs the perturbation.
- A **memorising model's accuracy collapses** under even small dropout — its sharp, specific activations are disrupted.
- The *dropout robustness gap* (post-dropout accuracy minus zero-dropout accuracy) is the predictor signal.

The intuition: the Fourier circuit implements the correct rule redundantly across multiple attention heads, so removing any one head only slightly degrades performance. The memorising solution has no such redundancy.

## Margin in the Context of Neural Collapse

The [[Simplex ETF]] geometry is a **maximum-margin** configuration. For $K$ classes represented by unit vectors:
- Any other configuration has some pair of class means closer together than the ETF minimum.
- The ETF's equal-angle structure maximises the minimum cosine distance between any two class means.
- This is why the ETF geometry (produced by [[Neural Collapse]]) is associated with the best generalisation bounds.

The grokking transition, in margin terms, is: the network moves from a low-margin memorising solution (tight, brittle boundaries) to a high-margin generalising solution (wide, robust boundaries).

## Measuring Margin as a Predictor

Beyond dropout robustness, several margin-adjacent signals can be monitored:
- **Logit margin**: the gap between the largest and second-largest logit for each test example.
- **Jacobian spectral norm**: the largest singular value of $\partial f/\partial x$ at test points — directly appears in [[Sokolić - Robust Large Margin Deep Neural Networks]]'s bound.
- **ETF deviation** ([[Simplex ETF]] note): how close the class-mean geometry is to the maximum-margin ETF.

Whether these signals fire before test accuracy (making them predictors with lead time) is the key empirical question for the thesis.

## Key Insights
- A bounded Jacobian spectral norm near training points gives width/depth-independent generalisation bounds ([[Sokolić - Robust Large Margin Deep Neural Networks]]).
- Among zero-loss interpolants, the **large-margin** one generalises; zero loss alone does not imply large margin ([[Xu - Dynamics in Deep Classifiers with the Square Loss]]).
- The **[[Simplex ETF]]** geometry is the maximum-margin configuration in its class ([[Papyan - Prevalence of Neural Collapse]]).
- Dropout robustness is a practical, model-agnostic proxy for margin: high robustness = high margin.
- Batch/weight normalisation improve generalisation through this margin/sensitivity lens ([[Sokolić - Robust Large Margin Deep Neural Networks]]).

## Evidence
[[Sokolić - Robust Large Margin Deep Neural Networks]], [[Xu - Dynamics in Deep Classifiers with the Square Loss]], [[Papyan - Prevalence of Neural Collapse]].

## Relationship to Other Concepts
- Selects the generalising solution in the [[Memorization]] vs [[Generalization]] race; driven toward by [[Weight Decay]].
- The robustness side grounds the **Dropout Robustness** entry in [[The Nine Predictors]].
- Geometric cousin of [[Neural Collapse]] and [[Neural Manifolds]] (manifold margin = distance between class manifolds).
- [[Simplex ETF]] is the maximum-margin geometry.

## Open Questions
Does margin (or Jacobian norm) increase sharply *at* the grokking transition, making it a usable predictor with lead time on algorithmic tasks? Is dropout-robustness a faithful proxy for the true geometric margin during training? Does the Fourier circuit's multi-head redundancy directly translate to high dropout robustness?

---
## Related Notes
- [[Sokolić - Robust Large Margin Deep Neural Networks]] · [[Neural Collapse]] · [[Simplex ETF]]
- [[The Nine Predictors]] · [[Generalization]] · [[Weight Decay]]
- [[Neural Manifolds]] · [[Fourier Features]] · [[Out-of-Distribution Generalization]]
