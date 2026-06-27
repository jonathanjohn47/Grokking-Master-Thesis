---
tags: [concept, neural-network, mathematics, non-linearity]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Activation Function

## What Is It?

An **activation function** is a mathematical operation applied to the output of a neuron (or layer) that introduces **non-linearity** into the model.

Without activation functions, neural networks would just be stacked linear transformations—equivalent to one giant linear function. They couldn't learn complex, non-linear patterns.

---

## Why Does It Exist?

### Problem: Linearity Is Limited

Imagine stacking linear transformations:

$$y = (W_3(W_2(W_1 x)))$$

This simplifies to:

$$y = (W_3 W_2 W_1) x = W x$$

No matter how many layers, it's still just one linear operation. You can't solve non-linear problems (like image recognition, language understanding).

### Solution: Non-Linearity

By inserting an activation function between layers:

$$y = W_2 \, \text{activation}(W_1 x)$$

The activation function **breaks linearity**. Now the model can learn curves, boundaries, and complex patterns.

---

## Intuition

Imagine a light switch (linear):

- **Off:** 0
- **On:** 1

You can only represent two states. Very limiting.

An activation function is like a **dimmer switch** (non-linear):

- Can output any value between 0 and 1 smoothly.
- Can express gradations.
- Much more expressive.

---

## Common Activation Functions

### ReLU (Rectified Linear Unit)

$$\text{ReLU}(x) = \max(0, x)$$

**Behavior:**
- If $x < 0$: output is 0.
- If $x \geq 0$: output is $x$ (linear).

**Pros:**
- Simple and fast.
- Works well in practice.
- Used in most deep networks.

**Cons:**
- Not differentiable at $x = 0$.
- Can cause "dead neurons" (neurons that output 0 forever).

**Example:**

```
ReLU([1, -0.5, 2, -3]) = [1, 0, 2, 0]
```

### GELU (Gaussian Error Linear Unit)

$$\text{GELU}(x) = x \cdot \Phi(x)$$

where $\Phi(x)$ is the cumulative standard normal distribution.

**Behavior:**
- Smooth approximation to ReLU.
- Outputs vary continuously between 0 and 1.

**Pros:**
- Smoother than ReLU.
- Avoids dead neurons.
- Better for transformer models.

**Cons:**
- Slightly slower to compute.

**Modern transformers (GPT-2+) use GELU.**

### Sigmoid

$$\text{Sigmoid}(x) = \frac{1}{1 + e^{-x}}$$

**Behavior:**
- Smooth S-shaped curve.
- Outputs between 0 and 1.

**Pros:**
- Interpretable as probability.
- Smooth gradient everywhere.

**Cons:**
- Slow to compute.
- Gradients vanish at extremes.
- Rarely used in modern deep networks.

### Tanh (Hyperbolic Tangent)

$$\text{Tanh}(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

**Behavior:**
- S-shaped curve centered at 0.
- Outputs between -1 and 1.

**Pros:**
- Symmetric around 0.
- Zero-centered (better for optimization).

**Cons:**
- Vanishing gradient problem.

---

## Where Are They Used?

### In Feedforward Networks

```
Input x (dimension 128)
  │
  ▼
[Dense: 128 → 512]
  │
  ▼
[Activation: ReLU or GELU]   ← applies activation function
  │
  ▼
[Dense: 512 → 128]
  │
  ▼
Output
```

### In Transformers

[[Feed-Forward Network (MLP)]] uses an activation function between the two dense layers:

```
[Up-projection: 128 → 512]
  │
  ▼
[GELU activation]
  │
  ▼
[Down-projection: 512 → 128]
```

---

## Example: Why Activation Matters

Suppose we have two layers without activation:

$$z = W_2(W_1 x)$$

If $W_1 = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$ and $W_2 = \begin{bmatrix} 0.5 & 0 \\ 0 & 0.5 \end{bmatrix}$:

$$z = \begin{bmatrix} 0.5 & 0 \\ 0 & 0.5 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} x = I \cdot x = x$$

Just the identity! No learning.

With ReLU:

$$z = W_2 \text{ReLU}(W_1 x)$$

Now the network can learn non-linear patterns by using ReLU to create different behavior in different regions.

---

## Why ReLU and GELU?

### Computational Efficiency

ReLU is literally `if x > 0 then x else 0`. Very fast.

### Gradient Flow

In backpropagation, gradients need to flow backward. ReLU has a simple gradient:

$$\frac{d}{dx} \text{ReLU}(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x < 0 \end{cases}$$

This keeps gradients strong (= 1) for active neurons, preventing vanishing gradients.

---

## Analogy — Camera Lenses

A **linear function** is like a transparent window:
- Light passes straight through.
- No distortion, no focus.
- Everything is flat.

An **activation function** is like a camera lens:
- It bends and focuses light.
- Creates depth and structure.
- Makes images sharp and interesting.

Without activation functions, neural networks would be like transparent windows—no learning happens.

---

## Important Terms

**Non-linearity** — A function that is not a straight line. Essential for learning complex patterns.

**Saturated region** — Where the activation function's gradient becomes very small (e.g., extreme values in sigmoid).

**Dead neurons** — Neurons that always output the same value (especially 0), so they never learn.

**Smoothness** — How continuous and differentiable the activation function is. Smoother = better gradients.

---

## Common Mistakes

**Mistake 1:** "Activation functions are just scaling or shifting values."

**Reality:** They introduce fundamental non-linearity. Without them, the entire network is linear and useless.

**Mistake 2:** "Any activation function works the same."

**Reality:** Different activations have different properties. ReLU is fast; GELU is smooth; sigmoid is interpretable but slower.

**Mistake 3:** "We need many different activation functions in one model."

**Reality:** Modern models typically use one activation (e.g., GELU everywhere) for consistency.

---

## Key Takeaways

- **Activation functions** introduce non-linearity, enabling neural networks to learn complex patterns.
- **ReLU** is fast and widely used in deep networks.
- **GELU** is smooth and preferred in modern transformers.
- Without activation functions, neural networks would be just linear combinations—unable to learn.
- The choice of activation affects training speed, stability, and final performance.

---

## Related Notes

- [[Feed-Forward Network (MLP)]] — uses activation functions between dense layers.
- [[Transformer]] — contains activation functions in the FFN.
- [[Gradient Flow]] — how activation functions affect gradient flow during backpropagation.
- [[Training Stability]] — activation functions impact how stable training is.
