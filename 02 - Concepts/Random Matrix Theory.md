---
tags: [concept, theory, spectral, physics]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[06 - Overparameterization and Interpolation]]

# Random Matrix Theory (RMT)

## Definition
**Random Matrix Theory (RMT)** is a branch of mathematics that studies the statistical properties of large matrices with random entries. In deep learning, it provides exact asymptotic results for the eigenvalue distributions of weight matrices, data covariance matrices, and Hessians — enabling precise, non-asymptotic results about generalisation error, spectral dynamics, and model quality.

## In Plain Words
A weight matrix has thousands of entries — seemingly random numbers after random initialisation, evolving toward structured patterns during training. RMT provides the mathematical tools to characterise these patterns. The key insight: many properties of a large random matrix can be predicted exactly from just a few summary statistics (size, variance, correlation structure), and deviations from these predictions reveal structure that training has introduced. Those deviations are the signal — they tell you the model has learned something.

## The Marchenko-Pastur Distribution: The Baseline

For a matrix $W$ of shape $n \times m$ filled with i.i.d. entries of variance $\sigma^2/m$, the empirical spectral density (ESD) of $\frac{1}{n}W^TW$ converges (as $n, m \to \infty$ with ratio $c = n/m$) to the **Marchenko-Pastur distribution**:

$$\rho_{MP}(\lambda) = \frac{1}{2\pi\sigma^2} \frac{\sqrt{(\lambda_+ - \lambda)(\lambda - \lambda_-)}}{\lambda c}$$

where $\lambda_\pm = \sigma^2 (1 \pm \sqrt{c})^2$ are the distribution's support boundaries.

**Why this matters:** A freshly initialised weight matrix has a Marchenko-Pastur ESD. After training, its ESD *departs* from Marchenko-Pastur. The departure is the signal:
- **Eigenvalues escaping the MP bulk** → the corresponding directions have been learned (signal has separated from noise).
- **Heavy tail** extending far beyond $\lambda_+$ → the [[Heavy-Tailed Self-Regularization|HTSR]] signature of a well-trained layer.
- **Rank-one outliers** above the Tracy-Widom edge → correlation traps ([[Anti-Grokking]] signature).

## Tracy-Widom Law: Outlier Detection

The **Tracy-Widom distribution** describes the fluctuations of the *largest eigenvalue* of a random matrix. Under the Marchenko-Pastur ensemble, the largest eigenvalue concentrates near $\lambda_+$. If a real weight matrix has eigenvalues significantly exceeding this bound, they are **not random** — they are learned signal. This is used by [[Heavy-Tailed Self-Regularization|WeightWatcher]] to separate structured (learned) from noise (random) components.

## Key Results Used in This Vault

| Result | What it says | Used in |
|---|---|---|
| **Marchenko-Pastur** | ESD of a random rectangular matrix | [[Heavy-Tailed Self-Regularization]] baseline |
| **Tracy-Widom** | Largest-eigenvalue fluctuations in random matrices | Outlier detection for HTSR / correlation traps |
| **Stieltjes transform / replica method** | Exact generalisation error for high-dimensional linear models | [[Mei - Generalization Error of Random Features Regression]] |
| **Semicircle law** | ESD of a symmetric random matrix → semicircle | [[Advani - High-dimensional Dynamics of Generalization Error]] |
| **Power-law tail fitting** | ESD with $p(\lambda) \sim \lambda^{-(\alpha+1)}$ = heavy-tailed | HTSR Alpha predictor |

## RMT and Generalisation Error

The most powerful use of RMT in this vault: computing **exact generalisation error curves** in high dimensions. [[Mei - Generalization Error of Random Features Regression]] and [[Advani - High-dimensional Dynamics of Generalization Error]] use the replica method (from statistical physics) to derive the full [[Double Descent]] curve analytically — including the exact location and height of the [[Interpolation Threshold]] peak.

This makes RMT the rigorous foundation for understanding *why* double descent has the shape it does.

## RMT and HTSR

The transition from Marchenko-Pastur bulk to power-law tail is quantified by the exponent $\alpha$:
- Random (untrained) matrix: $\alpha \to \infty$ (exponential cutoff, not a true power law).
- Weakly trained: $\alpha \approx 6$–$8$ (mild tail, some signal).
- Well-trained: $\alpha \approx 2$–$4$ (heavy tail, strong regularisation signal).
- Over-regularised: $\alpha < 2$ (tail so heavy it indicates rank collapse).

[[Martin - Predicting Trends in Neural Network Quality]] validated this across hundreds of pre-trained models: $\alpha$ in the 2–4 range correlates with best downstream performance, across architectures and datasets.

## RMT and Grokking Dynamics

During the grokking plateau, the weight spectra evolve slowly:
- MP bulk narrows as [[Weight Decay]] shrinks overall weight scale.
- Structured eigenvalues (corresponding to the forming [[Fourier Features|Fourier circuit]]) migrate further from the bulk.
- At the grokking transition, the structured eigenvalues spike — the circuit "crystallises" spectral mass.

This is the basis for the **HTSR Alpha** and **Spectral Signature** predictors (Predictors #2 and #6 in [[The Nine Predictors]]).

## Key Insights
- Generalisation-error dynamics and the [[Double Descent]] peak follow from the spectrum of the data/feature matrix ([[Advani - High-dimensional Dynamics of Generalization Error]], [[Mei - Generalization Error of Random Features Regression]]).
- Departures from Marchenko-Pastur bulk toward **heavy tails** signal learning and self-regularisation ([[Martin - Predicting Trends in Neural Network Quality]]).
- The **speciation** time of diffusion models is read from the data-correlation spectrum ([[Biroli - Dynamical Regimes of Diffusion Models]]).
- RMT converts high-dimensional deep learning into tractable math — it is the language in which exact results are possible.

## Evidence
[[Advani - High-dimensional Dynamics of Generalization Error]], [[Mei - Generalization Error of Random Features Regression]], [[Martin - Predicting Trends in Neural Network Quality]], [[Biroli - Dynamical Regimes of Diffusion Models]].

## Relationship to Other Concepts
- Mathematical foundation for [[Heavy-Tailed Self-Regularization]] and [[Spectral Bias]].
- Tool for analysing [[Double Descent]], [[Phase Transition]], and [[Neural Tangent Kernel]].
- Provides the Marchenko-Pastur baseline for [[Grokking Predictors|spectral predictors]].
- The Stieltjes/replica method gives rigorous derivations of [[Interpolation Threshold]] behaviour.

## Open Questions
Can RMT predict the *timing* of grokking from the evolving weight spectrum — not just static quality? Is the grokking transition observable as a Tracy-Widom edge event (a sudden new outlier appearing)?

---
## Related Notes
- [[Heavy-Tailed Self-Regularization]] · [[Double Descent]] · [[Spectral Bias]]
- [[Interpolation Threshold]] · [[Grokking Predictors]] · [[Anti-Grokking]]
- [[Advani - High-dimensional Dynamics of Generalization Error]] · [[Mei - Generalization Error of Random Features Regression]]
- [[Martin - Predicting Trends in Neural Network Quality]] · [[Biroli - Dynamical Regimes of Diffusion Models]]
