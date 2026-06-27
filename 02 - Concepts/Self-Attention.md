---
tags: [concept, architecture, transformer, foundations, attention]
---
↑ Parent: [[Attention Mechanism]] · Related: [[Transformer]] · [[Masked Language Modelling]] · [[Decoder-Only Dominance]]

# Self-Attention

## Definition
**Self-attention** is the specific variant of the attention mechanism in which a sequence attends to *itself* — every position in the input simultaneously queries, probes, and reads from every other position in the same sequence. It is the defining computation inside every [[Transformer]] and is what replaces the sequential processing of RNNs with a single parallelisable operation over the full input. "Self" is the operative word: no second sequence is involved; the model routes information within one sequence.

## In Plain Words
Consider the sentence *"The animal didn't cross the street because it was too tired."* A human reading this knows "it" refers to "animal," not "street." To make that connection, you need to look back: you check "animal" and "street," compare them, decide which one being "tired" makes more sense, and route that meaning into your representation of "it." Self-attention formalises exactly this: every word simultaneously asks "who should I be informed by?" and every other word simultaneously answers "here is what I contain." The answers are aggregated, weighted by how well the questions and answers matched. The result is a new representation for each word — one that has been contextualised by the whole sequence.

In the grokking experiments, the "words" are numbers like `[37, +, 61, =]`. Self-attention lets the `=` position look back at `37` and `61` simultaneously, compute their interaction, and use that interaction to predict the output — which is exactly what the [[Fourier Features|Fourier circuit]] needs to do.

## The Mechanism in Full

### Step 1: Three Linear Projections

Given an input sequence as a matrix $X \in \mathbb{R}^{n \times d_{\text{model}}}$ (one row per token, $d_{\text{model}}$-dimensional):

$$Q = XW_Q, \quad K = XW_K, \quad V = XW_V$$

where $W_Q, W_K, W_V \in \mathbb{R}^{d_{\text{model}} \times d_k}$ are learned weight matrices. These produce three parallel copies of the sequence — one playing the role of "questioner" (Query), one of "answerer" (Key), one of "content" (Value).[^qkv-intuition]

### Step 2: Attention Score Matrix

Compute a raw score for every (position $i$, position $j$) pair:

$$\text{score}(i, j) = \frac{Q_i \cdot K_j}{\sqrt{d_k}}$$

This is a dot product between the query at position $i$ and the key at position $j$. A high dot product means "position $i$ is looking for something like what position $j$ has." Dividing by $\sqrt{d_k}$ is critical for numerical stability.[^scaling]

All $n^2$ scores are assembled into a matrix $S \in \mathbb{R}^{n \times n}$, where $S_{ij}$ is how much position $i$ attends to position $j$.

### Step 3: Softmax Normalisation

Convert scores to probabilities along each row:

$$A_{ij} = \frac{\exp(S_{ij})}{\sum_{j'} \exp(S_{ij'})}$$

Row $i$ of $A$ is now a probability distribution: the attention weights from position $i$ over all positions. They sum to 1. Positions with high scores get most of the weight; positions with low scores are nearly ignored.

### Step 4: Weighted Sum of Values

$$\text{Output}_i = \sum_j A_{ij} \cdot V_j$$

Position $i$'s output is a weighted combination of all Value vectors, where high-weight positions contribute more. In matrix form:

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

The output has the same shape as the input: $n \times d_k$. It is then projected back to $d_{\text{model}}$ via an output matrix $W_O$ and **added** to the residual stream (see [[Transformer]]).

## Why "Self" — Attending Within One Sequence

In the original encoder-decoder transformer (Vaswani et al. 2017), the decoder used **cross-attention**: the decoder's Query vectors probed the encoder's Key and Value vectors — one sequence attending to a different sequence (e.g., the English source sentence and the French translation being generated).

**Self-attention** is a special case where $Q$, $K$, and $V$ all come from the same sequence. This makes the operation closed: the sequence reads itself. All three modern transformer families use self-attention as their core operation:

- **Encoder-only (BERT):** bidirectional self-attention — every position attends to every other (see [[Masked Language Modelling]]).
- **Decoder-only (GPT, Claude, LLaMA):** causal self-attention — every position attends only to itself and earlier positions, enforced by masking (see [[Decoder-Only Dominance]]).
- **Encoder-decoder (T5):** self-attention in each component, plus cross-attention in the decoder.

## Causal vs. Bidirectional Self-Attention

The only structural difference between encoder and decoder self-attention is the **mask** applied before softmax.

**Bidirectional (encoder-only):** No mask. Every position can attend to every other. The attention score matrix $S$ is fully populated. Richer contextual representations per token, but structurally incapable of generation (you cannot generate position $t$ while attending to positions $t+1, t+2, \ldots$ that haven't been produced yet).

**Causal (decoder-only):** Future positions are masked to $-\infty$ before softmax, so they receive zero attention weight:

$$S_{ij} \leftarrow \begin{cases} S_{ij} & \text{if } j \le i \\ -\infty & \text{if } j > i \end{cases}$$

After softmax, the attention weight matrix is strictly lower-triangular. Position $i$ can only draw information from positions $\le i$. This is what makes autoregressive generation valid: the model never "sees the answer" when computing the prediction at any position.

In grokking experiments, the model is decoder-only. The `=` token (position 3 in `[a, ◦, b, =]`) attends to `a`, `◦`, and `b` but not to future positions (none exist). The Fourier circuit uses this single attention over `a` and `b` to compute their sum.

## Permutation Equivariance and Positional Encodings

Self-attention has no built-in sense of order. Swap "cat sat on the mat" to "mat the on sat cat" — the attention weight matrix $A$ changes (different words produce different Q/K matches), but the *formula* treats all positions identically. There is no term in $QK^T / \sqrt{d_k}$ that depends on absolute position $i$ or $j$.[^perm-equivariance]

This **permutation equivariance** is both a strength (attention patterns are determined by content, not position) and a limitation (the model has no way to know token order without external help).

**Positional encodings** break the symmetry by adding a position-dependent vector to each token's embedding before the first layer:

$$x_i \leftarrow x_i + P_i$$

where $P_i$ encodes position $i$. This makes the input to the first attention layer position-dependent, so Q/K dot products implicitly reflect token order. Common choices:

| Encoding | Used in | Properties |
|---|---|---|
| Sinusoidal | Original Transformer (2017) | Fixed, deterministic; generalises to unseen lengths |
| Learned absolute | GPT-2 | Flexible; does not generalise beyond training length |
| Rotary (RoPE) | LLaMA, Mistral, Gemini | Encodes *relative* positions via rotation of Q/K vectors; extrapolates better to long contexts |
| ALiBi | MPT, BLOOM | Adds position-dependent bias to attention scores; extrapolates to long contexts at inference |

In grokking experiments, learned positional embeddings are standard (the four positions `a`, `◦`, `b`, `=` each get their own learned vector added at the embedding stage).

## Multi-Head Self-Attention

Instead of one set of Q/K/V projections, use $h$ independent **heads**, each with its own $W_Q^{(i)}, W_K^{(i)}, W_V^{(i)}$:

$$\text{head}_i = \text{Attention}(XW_Q^{(i)}, XW_K^{(i)}, XW_V^{(i)})$$

$$\text{MultiHead}(X) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h) W_O$$

Each head operates in a lower-dimensional subspace ($d_k = d_{\text{model}} / h$), so total compute is similar to a single full-size head. The benefit is that different heads can specialise: one might track syntactic dependencies, another semantic similarity, another copying relationships.[^head-specialisation]

In grokking experiments (GPT-2 Small variant), the typical setup is 4 heads over a 128-dimensional model, so each head works in a 32-dimensional subspace. Nanda et al. found that specific heads specialise to specific Fourier frequencies of the modular arithmetic circuit.

## Computational Complexity

Self-attention is $O(n^2 d)$ in time and $O(n^2)$ in memory, where $n$ is sequence length and $d$ is model dimension. The $n^2$ comes from the score matrix $S \in \mathbb{R}^{n \times n}$: computing and storing it requires $n^2$ operations and $n^2$ entries.

For grokking experiments ($n = 4$ tokens), this is trivial. For LLMs with $n = 100$k+ tokens, this quadratic scaling is the primary bottleneck and the reason for research into approximate attention (Longformer, Flash Attention, linear attention). The per-layer FFN is $O(n \cdot d^2)$, so the dominant cost depends on the ratio of $n$ to $d$.

## Self-Attention in the Residual Stream Framework

From the [[Mechanistic Interpretability]] perspective, each attention head reads from the residual stream and writes back to it additively:

$$x_\ell = x_{\ell-1} + \sum_{h=1}^{H} \text{head}_h(\text{LayerNorm}(x_{\ell-1})) \cdot W_O^{(h)}$$

The critical insight: because all contributions are **additive**, each head's output can be analysed independently. The head at layer $\ell$, head $h$ contributes a specific rank-$d_v$ update to the residual stream, and this update can be decomposed into Q-composition, K-composition, and V-composition terms (how much each head reads from directions written by earlier components).

This additivity is what makes mechanistic interpretability tractable: you can attribute each logit contribution back to specific heads and layers. In [[Circuit Formation|the grokking circuit]], the key attention heads contribute the trig-identity computation $\cos(\omega_k(a+b))$ directly, and this contribution can be isolated and tracked across training.

## Connection to Grokking

The grokking circuit for $(a+b) \bmod p$ is largely an attention story. As [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability|Nanda et al. (2023)]] showed:

1. The embedding matrix encodes each input number as a rotation vector — sines and cosines of key Fourier frequencies.
2. **Attention heads compute dot products between these rotation vectors**, which implements the trig identity $\cos(\omega(a+b)) = \cos\omega a \cos\omega b - \sin\omega a\sin\omega b$. The attention score $Q_i \cdot K_j$ between position `=` (which queries) and positions `a` and `b` (which answer) is precisely this product.
3. The FFN then reads the resulting $\cos(\omega(a+b))$ signal and maps it to the correct output class.

Understanding self-attention is therefore not optional for understanding grokking: the Fourier circuit *is* a self-attention computation. The grokking transition corresponds to attention heads converging on the correct Fourier-structured pattern from initially random weights.

More broadly, grokking can be seen as the model discovering the right **inductive use of self-attention** — moving from attention weights that implement a memorisation lookup table to attention weights that implement a general algebraic algorithm. See [[Circuit Formation]] and [[Fourier Features]].

## Key Insights
- Self-attention computes all pairwise relationships in a sequence in one parallel operation — replacing recurrence with simultaneous global communication.
- The Q/K dot product is a learned similarity function; the V projection is learned content; $W_O$ is a learned routing back into the residual stream.
- Scaling by $\sqrt{d_k}$ prevents softmax saturation and keeps gradients flowing.
- Permutation equivariance means positional encodings must be injected externally — self-attention itself has no sense of order.
- Causal masking is the only difference between encoder (bidirectional) and decoder (left-to-right) self-attention.
- Multi-head attention lets different heads specialise to different relationship types, including different Fourier frequency components in the grokking circuit.
- Additive residual updates make each head's contribution independently decomposable — the basis of mechanistic interpretability.

## Evidence
- Vaswani et al. (2017): "Attention Is All You Need" — introduces self-attention as the replacement for recurrence.
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]] — shows self-attention heads compute the Fourier trig identity in the grokked circuit.
- Olsson et al. (2022): "In-context Learning and Induction Heads" — shows attention heads form specialised circuits (induction, previous-token, copying).
- Clark et al. (2019): "What Does BERT Look At?" — shows different BERT attention heads specialise to syntactic structure, coreference, punctuation.

## Relationship to Other Concepts
- Operationalises the [[Attention Mechanism]] — self-attention is the form attention takes when a single sequence reads itself.
- The core computation inside every [[Transformer]] block; sits inside the residual stream framework.
- **Bidirectional** self-attention is the engine of [[Masked Language Modelling]]; **causal** self-attention is the engine of [[Decoder-Only Dominance|decoder-only generation]].
- Permutation equivariance is an [[Inductive Bias]] — it forces all positional information to come from added encodings rather than the operation itself.
- The Fourier trig identity computed by attention heads in grokking connects directly to [[Fourier Features]] and [[Circuit Formation]].
- Each head's additive residual contribution is the object analysed by [[Mechanistic Interpretability]].
- The output representations produced by self-attention are the contextual embeddings studied in [[Representation Learning]].
- Weight matrices $W_Q, W_K, W_V, W_O$ are the matrices whose eigenvalue spectra are measured by [[Heavy-Tailed Self-Regularization]] and [[Random Matrix Theory]].

## Open Questions
Do different attention heads specialise to different Fourier frequency components of the grokking circuit, and if so, do they form at different speeds during the plateau? Does the causal masking structure in decoder-only grokking experiments qualitatively change the kind of circuit that forms, compared to a hypothetical bidirectional setup? Can the formation of the correct self-attention pattern (the Fourier dot product) be directly used as an early grokking predictor, before test accuracy moves?

---
## Related Notes
- [[Attention Mechanism]] · [[Transformer]] · [[Masked Language Modelling]]
- [[Decoder-Only Dominance]] · [[Inductive Bias]] · [[Representation Learning]]
- [[Circuit Formation]] · [[Fourier Features]] · [[Mechanistic Interpretability]]
- [[Heavy-Tailed Self-Regularization]] · [[Random Matrix Theory]]
- [[Nanda - Progress Measures for Grokking via Mechanistic Interpretability]]

[^qkv-intuition]: **Why three separate projections — Q, K, and V?**

    At first it seems odd to make three copies of the same input. The reason is that Q, K, and V play structurally different roles, and the model benefits from learning them independently.

    **Query (Q):** "What am I looking for?" Each position projects its current representation into a query vector — a direction in $d_k$-dimensional space that encodes the kind of information it needs. The `=` token in a grokking input might learn a query direction that matches patterns relevant to computing the sum.

    **Key (K):** "What do I contain?" Each position also projects itself into a key vector — a direction in the same $d_k$-dimensional space encoding what it offers. The `a` position might learn a key direction that represents "I contain the first operand."

    **Value (V):** "What do I actually pass on?" The value projection is what gets *received* by attending positions. It is separate from K because what a position advertises (key) can differ from what it delivers (value). For example, a head might advertise its syntactic role via K (so it gets attended to by the right queries) while delivering semantic content via V.

    The separation lets the model learn three independent transformations simultaneously: a "what to look for" space (Q/K), and a "what to carry" space (V). Without separation, these constraints would be entangled: the model could not independently choose what to advertise vs. what to deliver.

    In mechanistic interpretability, the "OV circuit" ($W_V W_O$) and the "QK circuit" ($W_Q W_K^T$) are analysed separately. The QK circuit determines *where* attention is placed; the OV circuit determines *what information* is moved. This decomposition is central to how circuits are reverse-engineered in [[Circuit Formation]] and [[Mechanistic Interpretability]].

[^scaling]: **Why divide by $\sqrt{d_k}$?**

    The dot product $Q_i \cdot K_j = \sum_{m=1}^{d_k} Q_{im} K_{jm}$.

    If each element of $Q_i$ and $K_j$ is independently drawn from a distribution with mean 0 and variance 1 (a reasonable assumption after initialisation), then the dot product has mean 0 and variance $d_k$ — the variance scales linearly with the dimension. With $d_k = 64$, a dot product has standard deviation $\sqrt{64} = 8$; with $d_k = 512$, it has standard deviation $\approx 22$.

    Large raw scores are catastrophic for softmax. Softmax computes $\exp(s_j) / \sum \exp(s_{j'})$ — if $s_j$ is 22 and $s_{j'}$ is 20 for all other $j'$, the softmax output is approximately $[1, 0, 0, \ldots]$: the model attends essentially to one position only. This is called **softmax saturation**: the output is nearly a one-hot vector, and the gradient through a saturated softmax is near zero (the exponential function is very flat at extreme values). Training stalls.

    Dividing by $\sqrt{d_k}$ normalises the scores back to unit variance: $\text{Var}(Q_i \cdot K_j / \sqrt{d_k}) = d_k / d_k = 1$. Scores are now of order 1 regardless of $d_k$, and softmax outputs are well-distributed, keeping gradients healthy throughout training.

    The $\sqrt{d_k}$ choice is specifically derived from this variance calculation — it is not a hyperparameter to tune but a mathematically motivated normalisation.

[^perm-equivariance]: **What permutation equivariance actually means and why it forces positional encodings.**

    A function $f$ is **permutation equivariant** if shuffling its inputs shuffles its outputs in the same way: $f(\sigma(X)) = \sigma(f(X))$ for any permutation $\sigma$. In plain terms: rearranging the input rearranges the output identically, but does not otherwise change the computation.

    Self-attention without positional encodings is permutation equivariant. To see why: the attention score between position $i$ and position $j$ is $Q_i \cdot K_j / \sqrt{d_k}$. This depends only on the *content* of positions $i$ and $j$ — their token embeddings — not on their indices $i$ and $j$. If you swap the `a` and `b` tokens in `[a, ◦, b, =]`, the attention weights between `a` and `b` remain the same (the dot product of their embeddings does not change), and the only difference is that the positions of `a` and `b` in the output are swapped.

    For a language model, this is a problem. "The cat chased the dog" and "The dog chased the cat" have the same words but opposite meanings. Without positional encodings, a permutation-equivariant model cannot distinguish them. The word embeddings for "cat" and "dog" are the same regardless of position, and the attention weights are symmetric (they depend only on content similarity, not position). The model's output for both sentences would be identical except for permuted positions — so "who chased whom" could not be resolved.

    Positional encodings break this symmetry. By adding a distinct vector $P_i$ to every token at position $i$ before the first layer, the effective embedding becomes $e_i + P_i$ — now the content of token $i$ is *mixed* with position $i$. The Q/K dot products then implicitly encode both content and position: $Q_i \cdot K_j = (e_i + P_i) W_Q \cdot (e_j + P_j) W_K^T$, which includes cross-terms between token embeddings and position encodings. The model can now compute attention patterns that depend on both what a token is and where it is.

    The choice of positional encoding scheme shapes what position information the model can extract. Sinusoidal encodings (Vaswani et al.) allow the model to compute relative positions via the trig identity $\sin(a+b) = \sin a \cos b + \cos a \sin b$ — this is not coincidental and connects directly to how position-sensitive patterns emerge in attention heads. Rotary encodings (RoPE) encode relative positions by rotating the Q and K vectors by angle $\theta_i - \theta_j$, so the dot product $Q_i \cdot K_j$ naturally depends only on the relative offset $i - j$, giving clean relative-position sensitivity.

[^head-specialisation]: **How multi-head attention allows specialisation.**

    With a single attention head, the model has one set of Q/K/V matrices to learn all useful relationships in the input simultaneously. These constraints are entangled: a head that learns to track syntactic subject-verb agreement may not simultaneously be able to track coreference or semantic similarity, because the Q/K/V matrices are shared.

    With $h$ heads, each head has its own $W_Q^{(i)}, W_K^{(i)}, W_V^{(i)}$. Head 1 can freely specialise to syntactic relationships; head 2 to semantic similarity; head 3 to copying patterns; head 4 to long-range coreference. The specialisation is *learned* — it is not designed in — but it emerges reliably because different types of information are useful for next-token prediction and gradient descent discovers that separate heads for separate types is efficient.

    Each head operates in a $d_k = d_{\text{model}} / h$ dimensional subspace. With $d_{\text{model}} = 512$ and $h = 8$, each head works in 64 dimensions. The outputs of all heads are concatenated (giving $h \cdot d_k = d_{\text{model}}$ dimensions) and projected by $W_O$ back to $d_{\text{model}}$.

    In the grokking circuit, Nanda et al. found that different heads specialise to different Fourier frequency components of the modular arithmetic solution. A model using 4 heads over 5 key frequencies distributes the computation naturally — each head handles a subset of the algebraic structure.

    Clark et al. (2019) systematically characterised BERT attention heads and found interpretable specialisation: certain heads consistently attended to adjacent tokens, others to coreferent noun phrases, others to verbs' direct objects. This head-level specialisation is the empirical basis for the circuit-finding methodology in [[Circuit Formation]] — you can analyse each head's QK pattern and OV circuit independently.
