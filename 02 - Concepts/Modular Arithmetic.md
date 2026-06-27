---
tags: [concept, data, experiments, grokking]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[04 - Core Experimental Setup]]

# Modular Arithmetic

## Definition
**Modular arithmetic** is "clock arithmetic": arithmetic where numbers wrap around after reaching a fixed value $p$ (the modulus). Instead of the usual number line, you work on a cycle of $p$ elements $\{0, 1, \ldots, p-1\}$. The canonical grokking task is $(a + b) \bmod p$ with $p = 97$.

## The Formal Definition

For integers $a, b, p$ with $p > 0$:
$$a \bmod p = \text{the remainder when } a \text{ is divided by } p$$

So $(a + b) \bmod p = ((a \bmod p) + (b \bmod p)) \bmod p$.

Examples with $p = 97$:
- $(40 + 60) \bmod 97 = 100 \bmod 97 = 3$.
- $(0 + 0) \bmod 97 = 0$.
- $(96 + 1) \bmod 97 = 0$ (wraps around).
- $(50 + 50) \bmod 97 = 3$.

The output is always in $\{0, 1, \ldots, 96\}$ — 97 possible classes.

## In Plain Words
On a 12-hour clock, 4 hours after 9 o'clock is 1 o'clock (not 13). That wrap-around is "mod 12." Grokking experiments train a small network to predict, for every pair $(a, b)$ with $a, b \in \{0, \ldots, p-1\}$, what $(a + b) \bmod p$ equals. With $p = 97$, there are $97 \times 97 = 9409$ possible input pairs — a small, completely enumerable task.

## Why This Task Produces Grokking

Three key properties make modular arithmetic the perfect grokking testbed:

1. **Exact rule**: there is one correct answer for every input. Passing the test is a genuine generalisation check, not noise matching.
2. **Enumerability**: all $p^2 = 9409$ pairs can be listed. Train on 30%, test on 70%. The held-out test pairs are never seen during training — a clean [[Out-of-Distribution Generalization|out-of-distribution check]].
3. **Train fraction sensitivity**: use too much training data (>50%) and the model generalises immediately — no grokking. Use too little (<10%) and it never groks. A "grokking window" exists around 20–40% training data, where memorisation is easy but generalisation requires discovering the underlying rule ([[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]).

## The Fourier Circuit: What the Network Actually Learns

A grokked network does not memorise a table. It discovers that modular addition is **angle addition** on a circle. Specifically:

1. Represent each integer $k \in \{0, \ldots, p-1\}$ as a point on the unit circle at angle $\omega_k = 2\pi k / p$.
2. Note that $(a + b) \bmod p$ corresponds to the angle $\omega_a + \omega_b$ modulo $2\pi$.
3. Implement this via trigonometric identity: $\cos(\omega_k(a+b)) = \cos(\omega_k a)\cos(\omega_k b) - \sin(\omega_k a)\sin(\omega_k b)$.
4. Read off the result class from the resulting angular position.

This is the [[Fourier Features|Fourier circuit]] reverse-engineered by [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]. It is compact, exact, and has much lower weight norm than the memorisation solution — which is why [[Weight Decay]] eventually selects it.

## The Dataset Structure

With $p = 97$, 30% training split:

| Quantity | Value |
|---|---|
| All pairs $\{(a,b) : 0 \le a, b < 97\}$ | 9409 |
| Training pairs (30%) | 2794 |
| Test pairs (70%) | 6615 |
| Distinct output classes | 97 |
| Input vocabulary size | 98 (97 residues + 1 operator token) |

The task is presented as a sequence to the [[Transformer]]: `[a, +, b, =]` → predict the class label of $(a + b) \bmod 97$ via the final logit vector. Cross-entropy loss is used.

## Modular Arithmetic Variants

Grokking has been studied on several modular operations to test generality:

| Operation | Formula | Status |
|---|---|---|
| Addition | $(a+b)\bmod p$ | Core; most studied |
| Subtraction | $(a-b)\bmod p$ | Studied; grokking confirmed |
| Multiplication | $(a \times b)\bmod p$ | Studied; harder (fewer structured representations) |
| Division | $(a \div b)\bmod p$ (when defined) | Studied |
| Composition | $f(g(a,b))\bmod p$ | Studied in some papers |

Understanding whether predictors transfer across these variants is a key transferability question in the thesis (RQ3).

## Why p = 97?

97 is prime. This matters because:
- Every non-zero element has a multiplicative inverse ($a^{-1}$ exists for $a \ne 0$) — modular arithmetic is a *field*, with clean algebraic structure.
- The Fourier representation is exact: the characters $e^{2\pi i k/p}$ for $k=0,\ldots,p-1$ form a complete basis for functions on $\mathbb{Z}/p\mathbb{Z}$.
- The number 97 is large enough to make memorisation plausible but small enough to fit entirely in RAM and enumerate all pairs.

Non-prime moduli have more complex structure; primes give the cleanest connection between the task and the Fourier/angle representation.

## Key Insights
- The held-out pairs make the test a real [[Out-of-Distribution Generalization|generalisation]] check — not interpolation between seen examples.
- A grokked network solves it with **[[Fourier Features|Fourier-style circuits]]** (turning addition into adding angles).
- The **train fraction** matters: there is a grokking window (~20–40%) where memorisation is easy but generalisation requires the true rule.
- Variants (subtraction, multiplication) test whether findings are task-agnostic — key for [[Grokking Predictors|predictor transferability]] (thesis RQ3).
- $p$ being prime gives clean algebraic structure and makes the Fourier basis exact.

## Evidence
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]] — introduced grokking on modular arithmetic.
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — reverse-engineered the Fourier circuit.
- [[Varma - Explaining Grokking Through Circuit Efficiency]] — explained why the Fourier circuit wins.

## Relationship to Other Concepts
- The canonical setting for [[Grokking]] and [[Grokking Predictors]].
- Produces the [[Fourier Features|Fourier circuit]] via [[Mechanistic Interpretability]].
- Paired with [[04 - Core Experimental Setup]] and [[Common Datasets]].

## Open Questions
Do predictors tuned on modular addition transfer to other algorithmic tasks, including non-modular ones (thesis RQ4)? Does $p$ (prime or composite, size) affect grokking dynamics and predictor behaviour?

---
## Related Notes
- [[04 - Core Experimental Setup]] · [[Common Datasets]] · [[Grokking]] · [[Circuit Formation]]
- [[Fourier Features]] · [[Transformer]] · [[Out-of-Distribution Generalization]]
- [[Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]
- [[Varma - Explaining Grokking Through Circuit Efficiency]]
