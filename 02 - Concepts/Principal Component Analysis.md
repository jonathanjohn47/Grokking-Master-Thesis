---
tags: [concept, mathematics, dimensionality-reduction]
---
↑ Parent: [[00 - Start Here]] · Applications: [[Grokking Predictors]] · Related: [[Feature Learning]]

# Principal Component Analysis (PCA)

## What Is It?

**Principal Component Analysis (PCA)** is a mathematical technique for finding the most important directions of variation in a dataset.

Imagine you have 100 different measurements but only a few of them actually matter. PCA finds the ones that matter most.

**In the context of grokking:**

[[Grokking Predictors|Predictor 4 (Weight-Space PCA)]] applies this to neural network weights. It measures: "How many important directions explain the weight changes?"

During generalization, the answer changes in a detectable way.

> [!NOTE]
> PCA does not remove data — it reorganizes data to reveal what is important.

---

## Why Does It Exist?

### The Original Problem: Too Many Dimensions

Real data is often complicated with many measurements:

**Example: Student dataset**
- Height
- Weight
- Age
- Test score
- Study hours
- Sleep hours
- Exercise frequency
- GPA
- Attendance rate
- Motivation level
- ... 100 more measurements

Human brains cannot visualize 100-dimensional space.

### The Challenge

Some measurements are:
- Redundant (height and weight are correlated)
- Noisy (small measurement errors)
- Irrelevant (left-handed vs right-handed might not matter)
- Highly correlated (rich families often have better test scores)

**Question:** What if we could reduce 100 measurements to just 2-3 that capture most of the information?

### Why This Matters

With fewer, more important dimensions:
- Easier to visualize
- Faster to compute
- Easier to understand patterns
- Better for machine learning
- Removes noise and redundancy

---

## Intuition: The Spotlight in Darkness

Imagine a dark room with 100 different colored lights, each varying in brightness.

Most people only care about a few of the brightest lights:
- Light 1 (very bright) — varies a lot
- Light 2 (very bright) — varies a lot
- Light 3 (very bright) — varies a lot
- Lights 4-100 (very dim) — barely change

**PCA finds:** "These three bright lights explain most of the action. The other 97 are noise."

### How It Works Conceptually

1. **Look at the data:** See which directions vary the most
2. **Find the main direction:** The direction where data changes the most
3. **Find the next direction:** Perpendicular to the first, with the most remaining variation
4. **Continue:** Find third direction, fourth, etc.
5. **Stop when:** Most of the variation is explained

### Visual Example

**Original data (messy):**
```
Scattered points in 2D, not aligned with axes
  •   •
    •
  •     •
    •
      •
  •       •
```

**After PCA rotation:**
```
Points aligned along one main direction
      •
    •
  •
  •
    •
      •
        •
```

The main direction (horizontal) explains most of the variation.

---

## How Does It Work?

### The Step-by-Step Process

**Step 1: Prepare the data**
- Collect all measurements
- Center the data (subtract the mean)
- Normalize if needed (scale to similar ranges)

**Step 2: Create the correlation matrix**
- Measure how much each variable correlates with every other variable
- High correlation = they change together
- Low correlation = they change independently

**Step 3: Find the principal components**
- Mathematics: compute eigenvalues and eigenvectors
- Intuition: find the directions where data varies most
- The first principal component explains the most variation
- The second explains the next most (perpendicular to the first)
- Continue until all variation is explained

**Step 4: Project onto principal components**
- Take original data
- Rotate to align with principal components
- Now data is expressed in these new directions

**Step 5: Keep the important ones**
- Plot variation explained by each component
- Usually first 2-3 components explain 80-95% of variation
- Discard the rest

### Mathematical Foundation

The correlation matrix $C$ has eigenvalues $\lambda_1, \lambda_2, \ldots$ and corresponding eigenvectors.

The eigenvalues represent how much variation each principal component explains.

$$\text{Variation explained by component } i = \frac{\lambda_i}{\sum_j \lambda_j}$$

The eigenvectors are the directions of these components.

---

## Worked Example: Student Data

### Setup

Imagine three student measurements:
- Study hours (0-10)
- Test score (0-100)
- Sleep hours (0-12)

Sample of 5 students:

| Study | Score | Sleep |
|-------|-------|-------|
| 2     | 40    | 5     |
| 4     | 60    | 6     |
| 6     | 80    | 8     |
| 8     | 95    | 9     |
| 10    | 100   | 10    |

### Observation

Looking at the data, study hours and score are highly correlated. Sleep hours also correlates but less strongly.

The points form a line (not a 3D cloud):
```
(2, 40, 5) → (4, 60, 6) → (6, 80, 8) → (8, 95, 9) → (10, 100, 10)
```

### PCA Result

The first principal component captures the main trend:
- "More study → better score → more sleep"
- Explains 95% of variation

The second principal component captures small deviations:
- Student A studies 2 hours but sleeps 5.5 (slightly unusual)
- Explains 4% of variation

The third principal component captures noise.

### After Reduction

Instead of three measurements, use just one principal component:
- First component captures 95% of the information
- Simpler, faster, cleaner

### At Test Time

New student: studies 7 hours.

Instead of predicting score using all three original variables (which are correlated anyway), predict using just the first principal component.

---

## Real-World Applications

### Image Compression

Original image: 1000 × 1000 pixels = 1,000,000 numbers.

PCA finds that most variation comes from a few principal components. Keep the top 10, discard the rest.

Result:
- 10 components instead of 1,000,000
- Image still looks almost identical
- 100,000× compression

### Face Recognition

Faces have consistent structure:
- Eyes in similar positions
- Nose in similar position
- Mouth in similar position

PCA finds the principal components of face variation:
- Component 1: How wide is the face?
- Component 2: How round is the face?
- Component 3: How dark is the skin?

New faces can be represented as combinations of these components.

### Gene Expression Analysis

Scientists measure expression of 20,000 genes in 100 patients.

PCA finds:
- A few gene patterns dominate variation
- Most genes don't vary much
- Focus analysis on the important genes

### In Grokking Research

[[Grokking Predictors|Predictor 4 (Weight-Space PCA)]] applies this to neural network weights:

**Question:** "During the plateau, how many important directions explain weight variation?"

**Prediction:**
- During memorization: weights vary in many directions (high-dimensional)
- During generalization: weights concentrate in fewer directions (low-dimensional)
- PCA detects this change

---

## Analogy: The Photo Album

Imagine a photo album with 1000 photos:

### Without Organization (All Dimensions)

Looking at all 1000 photos: confusing, hard to see patterns.

### With Organization (PCA)

Sort by principal components:
- **Component 1:** "Indoor vs Outdoor" (explains 40% of variation)
- **Component 2:** "Sunny vs Cloudy" (explains 25% of variation)
- **Component 3:** "People vs Landscapes" (explains 20% of variation)
- **Other:** (explains 15%)

**Result:** Just three categories explain most of the album structure.

Now you can quickly find any photo by checking: "Is it indoor? Is it sunny? Are there people?"

---

## Important Terms

### Principal Component

A new dimension (direction) in data that captures important variation.

Not the same as original measurements — it is a combination of many measurements.

**Example:** Instead of measuring separate ingredients, measure "overall tastiness" (a combination).

### Eigenvalue

A number representing how much variation a principal component explains.

- Large eigenvalue = important component (explains lots of variation)
- Small eigenvalue = unimportant component (explains little variation)

### Eigenvector

A direction in the original space that corresponds to a principal component.

Shows how to combine original measurements to get the principal component.

**Example:** "Combine 0.6 × height + 0.8 × weight to get the first principal component."

### Dimensionality

The number of independent measurements or directions.

- High dimensionality: many measurements
- Low dimensionality: few measurements

PCA reduces dimensionality by finding that fewer directions capture most information.

### Variance

A measure of how much something changes or varies.

High variance = big changes. Low variance = small changes.

PCA finds directions with high variance (important) versus low variance (noise).

### Correlation

A measure of how much two variables change together.

- High correlation: both increase together
- Low correlation: they vary independently

PCA uses correlations to group related measurements.

### Variance Explained

The percentage of total variation captured by a component.

If the first component explains 80% of variance, the other components explain 20%.

---

## Common Mistakes

### Mistake 1: PCA Removes Data

**Wrong:** "PCA deletes measurements I don't use."

**Why wrong:** PCA rotates data into a new coordinate system. Information is still there, just in a different form.

**Right:** PCA reorganizes data so important information is in the first few components and noise is in the later components. You can still use all of it if needed.

### Mistake 2: Principal Components Are Interpretable

**Wrong:** "The first principal component is always something I can name."

**Why wrong:** Principal components are mathematical combinations. Sometimes they don't correspond to anything meaningful.

**Example:** Component 1 might be 0.4 × height + 0.6 × income + 0.3 × age + ... (hard to name).

**Right:** Principal components are directions of variation, not necessarily meaningful concepts.

### Mistake 3: Keeping Too Few Components

**Wrong:** "Just use the first principal component."

**Why wrong:** You lose information. The second and third components might explain important variation.

**Right:** Plot the variance explained. Usually keep enough to explain 80-95% of variation.

### Mistake 4: Using PCA Without Centering

**Wrong:** "Apply PCA directly to data."

**Why wrong:** PCA assumes data is centered at the origin. Without centering, the first component just points to the mean.

**Right:** Always center data (subtract the mean) before PCA.

### Mistake 5: Comparing PCA Across Different Scales

**Wrong:** "Apply PCA to height (inches) and weight (pounds)."

**Why wrong:** Weight has larger numbers, so it dominates the analysis.

**Result:** PCA mostly focuses on weight variation, ignoring height.

**Right:** Normalize data to similar scales before PCA (usually by dividing by standard deviation).

---

## Key Takeaways

**What it is:**
- A technique to find the most important directions of variation
- Reduces dimensionality while keeping important information
- Reorganizes data to make patterns visible

**How it works:**
- Find correlations between measurements
- Identify directions with high variation (important)
- Identify directions with low variation (noise)
- Keep the important directions, discard the noise

**Why it matters:**
- Makes high-dimensional data understandable
- Speeds up computation (fewer dimensions)
- Removes correlations and redundancy
- Reveals underlying patterns

**The key insight:**
- Real data often varies in only a few important directions
- Most of the apparent complexity is redundancy or noise
- By finding these directions, you can understand data better

**In grokking research:**
- [[Grokking Predictors|Predictor 4 (Weight-Space PCA)]] measures weight-space dimensionality
- During memorization: high-dimensional (many directions matter)
- During generalization: low-dimensional (few directions matter)

---

## Mathematical Note

For those interested in the mathematics:

The covariance matrix $C$ of the data is computed. Its eigendecomposition is:

$$C = V \Lambda V^T$$

where:
- $V$ = matrix of eigenvectors (the principal component directions)
- $\Lambda$ = diagonal matrix of eigenvalues (variance explained by each component)

The data is then projected onto these eigenvectors:

$$X_{\text{new}} = X_{\text{centered}} \cdot V$$

The dimensionality reduction comes from keeping only the first $k$ columns of $V$ (corresponding to the $k$ largest eigenvalues).

---

## How It Connects to Learning

[[Grokking Predictors]] — Predictor 4 applies PCA to weight matrices:
- Measures how dimensionality changes during training
- Detects the transition from memorization to generalization

[[Feature Learning]] — Related to how networks learn representations:
- PCA finds important features in data
- Neural networks learn similar features

[[Representation Learning]] — Networks learn to represent data in useful ways:
- PCA is one simple way to find useful representations

---

## Related Notes

**Understanding PCA:**
- [[Feature Learning]] — How networks learn features
- [[Representation Learning]] — Learning useful data representations

**Statistical foundations:**
- [[Information-Theoretic Measures]] — Other ways to measure information
- [[Neural Collapse]] — Structure that emerges in networks

**In the thesis:**
- [[Grokking Predictors]] — Predictor 4 uses PCA
- [[05 - Thesis/The Nine Predictors]] — Full thesis topic
- [[Methodological Considerations]] — Measurement techniques