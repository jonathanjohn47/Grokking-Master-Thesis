---
tags: [concept, theory, representations]
---
↑ Parent: [[00 - Start Here]] · Learning path: [[10 - Mechanistic Explanations and Circuit Formation]]

# Feature Learning

## What Is It?

**Feature learning** is when a neural network actively changes how it represents information inside itself during training — not just what answer it gives, but how it "thinks about" the input.

When feature learning happens, the network does not just get better at answering questions. It fundamentally reorganises its internal representation of the world.

Grokking is one of the clearest demonstrations of feature learning in action.

---

## Why Does It Exist?

Neural networks process inputs by first converting them to internal representations (sometimes called "features" or "embeddings"). These internal representations are the network's "way of seeing" the input.

There are two very different ways a network can improve during training:

**The lazy way:** The network keeps the same internal representations it started with (from random initialisation). Only the final layer — the part that converts representations to outputs — adjusts. The network does not change how it "sees" the input; it only changes how it decides what answer to give based on its fixed view.

**The rich way (feature learning):** The network actively changes its internal representations. It learns to "see" the input differently — in a way that makes the task easier. The internal representation evolves throughout training.

The lazy way is mathematically simpler and was assumed by many early theories of neural networks. But the rich way — feature learning — is what actually happens in practice, and it is much more powerful.

---

## A Simple Analogy

Imagine two students learning to identify dogs.

**Lazy student:** Memorises a list of specific dog photos. When shown a new image, tries to match it against their memorised list. Their "feature" (what they look at) never changes — they always look at the whole image as a blur.

**Feature-learning student:** Initially looks at random things in the image. Over time, they learn to notice specific features: fur texture, ear shape, snout length. By the end, they have a rich, flexible representation — "features" — that lets them identify any dog, even ones they've never seen.

Feature learning is what turns the lazy approach into the powerful approach. The network develops a good way of seeing, not just a good list of answers.

---

## Two Stages of Feature Learning in Grokking

Grokking shows feature learning happening in two distinct stages:

**Stage 1 — Memorisation:**
The network learns shallow, brittle representations. Each training example is encoded separately. The "features" the network learns are essentially "which exact question is this?" — like filing each training example individually. This still counts as some kind of feature learning, but the features have no generalising structure.

**Stage 2 — The Grokking Transition:**
The network discards the filing-cabinet representations and builds a completely new kind of representation: the rotation-based circuit (see [[Fourier Features]]). Instead of encoding "which specific question is this?", it encodes "what are the rotation angles of these two numbers?" — a representation that captures the mathematical structure of the task.

This second stage is genuine, powerful feature learning. The network has found a way of representing inputs that makes the true rule transparent.

The transition between Stage 1 and Stage 2 is the grokking moment.

---

## Lazy vs Rich: Why It Matters Theoretically

For many years, theoretical analysis of neural networks used a framework called the **Neural Tangent Kernel (NTK)**.

NTK theory says: for very wide networks, the internal representations barely change during training. The network is in the "lazy" regime. This makes the mathematics very tractable — the network behaves like a linear model.

But NTK theory **cannot explain grokking**. Grokking requires the internal representations to change fundamentally — from filing-cabinet features to rotation-angle features. This means grokking experiments are firmly in the "rich" learning regime, outside what NTK theory covers.

This is actually important information: it tells researchers that the theoretical tools for lazy learning do not apply here. New tools are needed.

---

## What Good Features Look Like

When a network has learned good features, its internal representations of different categories have specific geometric properties:

**Low dimensionality:** The representations lie in a small subspace — many inputs map to nearby points in a compact region.

**Tight clusters:** Different examples of the same category are represented similarly to each other — they cluster together.

**Large separation:** Different categories are represented differently — they are far apart from each other.

After grokking, the clock-math network's representations of different answer classes (0 through 96) each form tight, well-separated clusters. Before grokking, the representations are scattered and overlapping.

The transition from scattered to clustered representations is exactly what feature learning produces.

---

## The Connection to Neural Collapse

At the extreme end of feature learning is a phenomenon called **neural collapse**: the representations become so well-organised that they achieve the most geometrically perfect arrangement possible — a shape called the Simplex ETF (Equiangular Tight Frame) where every category is exactly equidistant from every other.

Neural collapse is the completion of feature learning. The network has found the most efficient, most symmetric way to represent all the categories.

Feature learning during the plateau drives the network toward this perfect geometry.

---

## How to Detect Feature Learning

Because feature learning changes the internal representations, it can be detected by tracking those representations:

- **Dimensionality:** Does the effective dimension of representations decrease over training?
- **Cluster quality:** Are representations of the same category clustering together?
- **Margin:** Is there increasing separation between different categories?

These measurements change during the grokking plateau — before test accuracy does — making feature-learning-based measurements potential grokking predictors.

---

## Important Terms

**Feature learning:** The process by which a network changes its internal representations during training, not just its final-layer outputs.

**Features / embeddings:** The internal representations a network uses for inputs. A number like "37" in clock math is converted to an internal vector (list of numbers) — this vector is the feature or embedding.

**Lazy learning regime:** When representations barely change during training; only the final layer adapts. Predicted by NTK theory.

**Rich learning regime:** When representations actively change during training. Feature learning happens. Required for grokking.

**Neural Tangent Kernel (NTK):** A theoretical framework for analysing very wide neural networks in the lazy regime. Cannot explain grokking.

**Neural collapse:** The endpoint of feature learning — representations converge to the most symmetric possible geometric arrangement.

**Simplex ETF:** The specific symmetric arrangement that neural collapse produces.

**Dimensionality of representations:** How many independent dimensions of variation the internal representations span. Feature learning tends to reduce this, making representations more compact.

---

## Common Misconceptions

> [!WARNING]
> **Misconception:** "Feature learning happens only at the beginning of training."
> In grokking, the most important feature learning happens during the plateau — long after the initial training phase. The network is continuously reorganising its representations even when the accuracy scores look flat.

> [!WARNING]
> **Misconception:** "A network that memorises is not doing feature learning."
> It is doing some feature learning — just learning shallow, brittle features that do not generalise. Genuine feature learning produces compact, structured representations that enable generalisation.

---

## Key Takeaways

- Feature learning is when a network changes its internal representations during training, not just its final outputs.
- There are two regimes: lazy (representations barely change) and rich (representations actively change). Grokking is in the rich regime.
- In grokking, feature learning happens in two stages: first learning shallow memorisation features, then discarding them and building the efficient rotation-angle features.
- NTK theory (lazy learning) cannot explain grokking — grokking requires rich feature learning.
- After grokking, representations have good geometric properties: tight clusters, large separation, low dimensionality.
- Feature learning measurements can change during the plateau before test accuracy does — making them potential grokking predictors.

---

## Related Notes
- [[Neural Manifolds]] · [[Circuit Formation]] · [[Mean-Field Limit]] · [[Neural Tangent Kernel]]
- [[Neural Collapse]] · [[Fourier Features]] · [[Grokking Predictors]]
- [[Li - Representations and Generalization in Artificial and Brain Neural Networks]] · [[Mei - A Mean Field View of Two-Layer Neural Networks]]
