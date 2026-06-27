---
tags: [concept, optimization, training, neural-networks]
---
↑ Parent: [[Transformer]] · Learning path: [[04 - Core Experimental Setup]]

# Backpropagation

## What Is It?

**Backpropagation** is an algorithm for computing gradients (derivatives) of a loss function with respect to all weights in a neural network.

It works by applying the **chain rule** of calculus **backward** through the network:

1. Compute loss at the output.
2. Compute how loss changes with respect to the last layer's weights.
3. Propagate backward: compute how loss changes with respect to earlier layers.
4. Update all weights in the direction that reduces loss.

---

## Why Does It Exist?

### Problem: How to Train Neural Networks?

Neural networks have millions of parameters (weights). To train them:

1. You need to know: **"How much does each weight affect the loss?"**
2. Then: **"Update each weight to reduce loss."**

With millions of weights, computing derivatives manually is impossible.

### Solution: Backpropagation

Backpropagation efficiently computes all gradients in **one backward pass** using dynamic programming and the chain rule.

Without backpropagation, training deep neural networks would be computationally infeasible.

---

## Intuition

Imagine a line of dominoes:

```
You push domino A
  ↓
Domino B falls
  ↓
Domino C falls
  ↓
Domino D falls
```

**Backpropagation is reverse:**

```
Domino D is lying down (loss is high)
  ↑
How much did domino C contribute?
  ↑
How much did domino B contribute?
  ↑
How much did domino A contribute?
```

You trace backward to find the root cause of the loss, then fix it.

---

## How Does It Work?

### Forward Pass

Compute the loss by evaluating the network:

```
Input x
  ↓
[Layer 1: z₁ = W₁x + b₁]
  ↓
[Activation: a₁ = σ(z₁)]
  ↓
[Layer 2: z₂ = W₂a₁ + b₂]
  ↓
[Activation: a₂ = σ(z₂)]
  ↓
Loss = L(a₂, y)
```

### Backward Pass (Backpropagation)

Use chain rule to compute gradients starting from the loss:

$$\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2} \cdot \frac{\partial z_2}{\partial W_2}$$

$$\frac{\partial L}{\partial W_1} = \frac{\partial L}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2} \cdot \frac{\partial z_2}{\partial a_1} \cdot \frac{\partial a_1}{\partial z_1} \cdot \frac{\partial z_1}{\partial W_1}$$

**Key insight:** We **reuse** intermediate computations.

- $\frac{\partial L}{\partial a_2}$ computed once.
- $\frac{\partial a_2}{\partial z_2}$ computed once.
- Both reused for all weights in layer 1.

This is **dynamic programming** — avoid recomputing the same things.

### Weight Update

Once gradients are computed, update weights in the direction that reduces loss:

$$W_{\text{new}} = W - \text{lr} \times \frac{\partial L}{\partial W}$$

where lr = learning rate (step size).

---

## Example: Simple Network

**Network:**
```
Input x → W₁ → ReLU → W₂ → MSE Loss
```

**Forward pass (concrete numbers):**

```
x = 2
W₁ = 0.5,  b₁ = 0
z₁ = W₁ · x + b₁ = 0.5 · 2 + 0 = 1
a₁ = ReLU(z₁) = ReLU(1) = 1

W₂ = 0.3,  b₂ = 0
z₂ = W₂ · a₁ + b₂ = 0.3 · 1 + 0 = 0.3
ŷ = z₂ = 0.3

y_true = 5  (target)
Loss = (ŷ - y_true)² = (0.3 - 5)² = 22.09
```

**Backward pass:**

$$\frac{\partial L}{\partial ŷ} = 2(ŷ - y) = 2(0.3 - 5) = -9.4$$

$$\frac{\partial ŷ}{\partial W_2} = a_1 = 1$$

$$\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial ŷ} \cdot \frac{\partial ŷ}{\partial W_2} = -9.4 \cdot 1 = -9.4$$

$$\frac{\partial ŷ}{\partial a_1} = W_2 = 0.3$$

$$\frac{\partial a_1}{\partial z_1} = \text{ReLU}'(1) = 1$$

$$\frac{\partial z_1}{\partial W_1} = x = 2$$

$$\frac{\partial L}{\partial W_1} = -9.4 \cdot 0.3 \cdot 1 \cdot 2 = -5.64$$

**Weight updates (learning rate = 0.1):**

$$W_2^{\text{new}} = 0.3 - 0.1 \cdot (-9.4) = 0.3 + 0.94 = 1.24$$

$$W_1^{\text{new}} = 0.5 - 0.1 \cdot (-5.64) = 0.5 + 0.564 = 1.064$$

Both weights were updated to reduce loss.

---

## Why "Back"propagation?

The algorithm propagates errors **backward** from loss to early layers:

```
Output (loss computed)
  ↑
  ↑ Gradients flow backward
  ↑
Earlier layers
```

This is opposite to the **forward pass** where information flows forward.

---

## Computational Complexity

### Forward Pass
- Time: O(number of weights)
- Space: O(depth of network)

### Backward Pass
- Time: O(number of weights) — about 2-3× more computation than forward pass
- Space: O(depth of network) — need to store intermediate activations

**Total training cost:** ~3× more than just forward pass evaluation.

---

## Chain Rule in Detail

The chain rule is the foundation:

For a composition of functions $z = f(g(h(x)))$:

$$\frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dw} \cdot \frac{dw}{dx}$$

In neural networks:

$$\frac{\partial L}{\partial W_1} = \frac{\partial L}{\partial a_n} \cdot \frac{\partial a_n}{\partial z_n} \cdot \frac{\partial z_n}{\partial a_{n-1}} \cdots \frac{\partial z_1}{\partial W_1}$$

Each partial derivative is computed locally (at each layer), then multiplied together.

---

## Automatic Differentiation

Modern deep learning frameworks (**PyTorch**, **TensorFlow**) implement backpropagation automatically via **automatic differentiation (autodiff)**:

```python
import torch

x = torch.tensor(2.0, requires_grad=True)
W1 = torch.tensor(0.5, requires_grad=True)

z1 = W1 * x
a1 = torch.relu(z1)

W2 = torch.tensor(0.3, requires_grad=True)
y_pred = W2 * a1

loss = (y_pred - 5) ** 2

# Backpropagation (one line!)
loss.backward()

print(W1.grad)  # Gradient with respect to W1
print(W2.grad)  # Gradient with respect to W2
```

You just call `.backward()` and gradients are computed automatically!

---

## Backpropagation and Grokking

In grokking:

1. **Forward pass:** Compute predictions on training data.
2. **Compute loss:** Compare prediction to target.
3. **Backpropagation:** Compute gradients showing which weights caused errors.
4. **Weight update:** Adjust weights to reduce loss.

During **memorization phase:** Gradients directly optimize the loss.

During **jamming phase:** Gradients become small (loss plateaus) but backpropagation still occurs, driving internal reorganization.

During **generalization phase:** Gradients recover strongly as the model discovers the algorithm.

**Without backpropagation, none of this learning would happen.**

---

## Limitations

### Vanishing Gradients

In deep networks, gradients can become very small by the time they reach early layers. Early layers learn slowly or not at all.

**Solution:** [[Residual Connections]], [[Layer Normalization]]

### Exploding Gradients

Gradients can also grow exponentially, causing instability.

**Solution:** [[Gradient Clipping]]

### Memory Cost

Backpropagation requires storing intermediate activations from the forward pass. Large models need significant memory.

**Solutions:** Gradient checkpointing, mixed precision training.

---

## Analogy — Fixing a Broken Machine

Imagine a machine (the network) that's broken:

1. **Observe the problem:** Output is wrong (loss is high).
2. **Trace the cause backward:** Which part caused this?
3. **Find the root cause:** This component is broken.
4. **Fix it:** Replace or adjust the broken component.
5. **Test:** Does the output improve?

Backpropagation is the **systematic process** of tracing problems backward to their root causes and fixing them.

---

## Important Terms

**Backpropagation** — Algorithm computing gradients by propagating errors backward.

**Gradient** — Derivative of loss with respect to a parameter. Shows direction to reduce loss.

**Chain rule** — Calculus rule: $(f \circ g)' = (f' \circ g) \cdot g'$.

**Forward pass** — Computing output by evaluating the network forward.

**Backward pass** — Computing gradients by propagating errors backward.

**Automatic differentiation** — Computing gradients automatically without writing derivative code.

**Computational graph** — Abstract representation of the network used by autodiff systems.

---

## Common Mistakes

**Mistake 1:** "Backpropagation is only used in deep learning."

**Reality:** It's a fundamental optimization algorithm used in many fields (controls, robotics, etc.).

**Mistake 2:** "Backpropagation computes exact gradients."

**Reality:** It computes exact gradients (up to numerical precision). No approximation.

**Mistake 3:** "You need to implement backpropagation manually."

**Reality:** Modern frameworks (PyTorch, TensorFlow) do it automatically. Just call `.backward()`.

**Mistake 4:** "Backpropagation only works for neural networks."

**Reality:** It works for any differentiable computation. The network structure can be anything (as long as derivatives exist).

---

## Key Takeaways

- **Backpropagation** computes gradients efficiently using the chain rule.
- It propagates **errors backward** from loss to early layers.
- **Dynamic programming** avoids redundant computation.
- Essential for training neural networks efficiently.
- Modern frameworks implement it automatically (autodiff).
- Enables learning by updating weights to reduce loss.
- Fundamental to grokking: gradients drive memorization → generalization transition.

---

## Related Notes

- [[Gradient Flow]] — how gradients propagate through layers.
- [[Training Stability]] — backprop stability depends on gradient magnitudes.
- [[Gradient Clipping]] — technique to stabilize gradient magnitudes.
- [[Layer Normalization]] — helps maintain healthy gradients.
- [[Residual Connections]] — provide direct gradient paths.
- [[Transformer]] — trained using backpropagation.
