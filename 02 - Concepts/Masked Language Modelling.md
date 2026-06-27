---
tags: [concept, architecture, transformer, foundations, pretraining]
---
↑ Parent: [[00 - Start Here]] · Related: [[Transformer]] · [[Decoder-Only Dominance]]

# Masked Language Modelling (MLM)

## Definition
**Masked Language Modelling (MLM)** is a self-supervised pre-training objective in which a fraction of input tokens are randomly replaced with a special `[MASK]` token, and the model is trained to predict the original tokens at those positions. MLM is the pre-training task behind **BERT** (Devlin et al., 2018) and the entire encoder-only family of language models. It enables learning rich, **bidirectional** contextual representations — every token can attend to every other token, left *and* right — at the cost of being a proxy task rather than a direct measure of language understanding.

## In Plain Words
Imagine a fill-in-the-blank exam. You receive a sentence with some words blanked out — *"The cat [MASK] on the [MASK]"* — and your job is to recover the original words. To fill in *"sat"* and *"mat"*, you need to understand the entire sentence: what kind of thing a cat does, what follows "on the," and how the two blanks relate. This is MLM in a nutshell. The model trains on billions of such fill-in-the-blank problems and, in solving them, is forced to learn deep contextual meaning. Unlike next-token prediction (which only looks backward), MLM uses full bidirectional context — the model sees both sides of every blank.

## The Mechanics

### Step 1: Tokenise
The input sentence is converted to tokens (sub-word units), prepended with `[CLS]` and suffixed with `[SEP]`:

```
[CLS] The cat sat on the mat [SEP]
```

The `[CLS]` token's final representation is used as a summary embedding of the whole sentence (for classification tasks). `[SEP]` marks segment boundaries.

### Step 2: Mask
Approximately **15%** of all input tokens are selected at random. Of those selected:
- **80%** are replaced with `[MASK]`.
- **10%** are replaced with a random other token.
- **10%** are left unchanged.

This 80/10/10 split is deliberate. If every selected token were replaced with `[MASK]`, the model would never see real tokens at the positions it must predict at fine-tuning time — creating a **pre-training / fine-tuning mismatch**. The random-replacement and no-change cases force the model to maintain a good representation of *every* token, not just masked ones.

### Step 3: Predict
The model reads the masked sequence through a **bidirectional** [[Attention Mechanism]] (no causal mask — every token attends to every other token) and outputs a probability distribution over the vocabulary at each masked position:

$$\hat{y}_i = \text{softmax}(W_U \cdot h_i)$$

where $h_i$ is the contextual representation at position $i$ (from the final transformer layer) and $W_U$ is the unembedding / output matrix.

### Step 4: Compute loss
[[Cross-Entropy Loss]] is computed **only at the masked positions** — unmasked positions contribute nothing to the gradient:

$$\mathcal{L}_{\text{MLM}} = -\frac{1}{|\mathcal{M}|} \sum_{i \in \mathcal{M}} \log P(x_i^{\text{orig}} \mid \tilde{x})$$

where $\mathcal{M}$ is the set of masked positions and $\tilde{x}$ is the masked input.

## MLM vs Causal Language Modelling (Autoregressive)

| Property | MLM (BERT) | Causal LM (GPT/decoder-only) |
|---|---|---|
| **Direction** | Bidirectional — full context both ways | Left-to-right only — causal mask |
| **Training signals per $n$-token sequence** | ≈ $0.15n$ (only masked positions) | $n$ (every token predicts the next) |
| **Efficiency vs causal LM** | ~7× less[^mlm-efficiency] | Baseline |
| **Objective type** | Proxy task (fill in the blank) | Direct (predict what actually comes next) |
| **Generation ability** | None — produces embeddings, not tokens | Native — autoregressive sampling |
| **Best use** | Understanding, classification, retrieval | Generation, instruction following, in-context learning |
| **RLHF compatible?** | No — no token generation to evaluate | Yes |

See [[Decoder-Only Dominance]] for a detailed account of why this asymmetry caused encoder-only models to lose the architecture race.

## Why MLM Produces Powerful Representations

MLM forces the model into an extremely demanding [[Representation Learning|representation-learning]] problem. To recover the masked token `[MASK]` in:

```
The animal didn't cross the street because it was too [MASK]
```

the model must resolve the coreference ("it" → "animal"), understand that animals can be tired, and know that tiredness prevents crossing. This requires deep, structured contextual representations — ones that encode syntactic structure, semantic relationships, and world knowledge simultaneously. Every masked position is a tiny test of how well the model has encoded the context around it.

The result is a **contextual embedding**: the same word gets a different vector depending on the sentence it appears in. *"Bank"* in *"river bank"* and *"bank account"* produces different representations — unlike static word2vec embeddings where every word has exactly one vector. This contextual sensitivity is what made BERT representations dramatically better for downstream NLP tasks than earlier methods.

## MLM as an Inductive Bias

The masking strategy is itself an [[Inductive Bias|inductive bias]]:
- By masking uniformly at random, the model is pushed to treat all positions as equally important — no position is more "predictable" than any other by design.
- The 80/10/10 split biases the model to maintain high-quality representations of *every* token (not just masked ones), because it can never know which position will be evaluated.
- Bidirectionality biases the model toward using full context; the causal mask in decoder-only models biases toward left-context only.

This bidirectional bias is both a strength and a limitation. Bidirectionality gives richer understanding per token — but it makes the model structurally incapable of autoregressive generation, since generating token $t$ would require attending to future tokens $t+1, t+2, \ldots$ that don't yet exist.

## The Pre-training / Fine-tuning Paradigm

MLM (and BERT) popularised the now-standard **pre-train then fine-tune** workflow:

1. **Pre-train** on large unlabelled text via MLM (+ Next Sentence Prediction, NSP).
2. **Fine-tune** on a small labelled dataset for the target task (classification, NER, QA…) by adding a task-specific head on top of the `[CLS]` or token-level representations.

This paradigm was transformative: it showed that a single pre-trained model could be fine-tuned to state-of-the-art performance on dozens of different tasks. The pre-trained representations were general-purpose — they captured language structure, not task-specific patterns.

The paradigm carries a direct analogy to grokking: pre-training (memorising the form of language) precedes generalisation (learning to solve the task). The fine-tuning step can be seen as the generalisation event — the moment the model's representations are applied to a new structure.

## MLM and Grokking: Connections and Contrasts

MLM is less studied from a grokking perspective than causal LM, but several connections exist:

**Why MLM is less relevant to grokking experiments:**
- Canonical grokking experiments use **decoder-only transformers** on modular arithmetic — a causal, next-token-prediction setup.
- MLM requires padding and masking infrastructure that is unnecessary for the toy algorithmic tasks typically used for grokking.
- The 7× training-signal disadvantage means MLM-trained models generalise more slowly on a per-sequence basis, making grokking timescales harder to compare.

**Where MLM connects to grokking themes:**
- Both involve a model that first **memorises** (overfits) and must later **generalise** — the pre-training / fine-tuning split mirrors the grokking memorise/generalise split.
- The representations built by MLM are exactly what [[Representation Learning]] analyses focus on: rich contextual embeddings that encode structure rather than surface pattern — analogous to the Fourier circuit the grokked network builds (see [[Fourier Features]]).
- [[Shortcut Learning]] can occur in both: BERT can latch onto statistical co-occurrence cues in masked tokens rather than truly learning syntax, just as grokking models can latch onto memorisation before finding the underlying rule.
- [[Phase Transition|Phase transitions]] in fine-tuning performance as a function of pre-training data have been observed — an analogue of grokking in the large-scale regime.

## Key Insights
- MLM trains a model to fill in masked tokens using **bidirectional context** — the key innovation over earlier left-to-right language models.
- The 15% masking rate and 80/10/10 token replacement strategy are carefully tuned choices that constitute an inductive bias toward maintaining representations for every position.
- MLM produces $\approx 0.15n$ training signals per $n$-token sequence, vs $n$ for causal LM — a 7× efficiency gap that compounds enormously at scale.
- BERT's representations were contextual (same word, different embedding per context) — a breakthrough over static embeddings.
- MLM cannot natively generate text and is therefore incompatible with [[RLHF]] and instruction-tuning pipelines.
- The pre-training / fine-tuning paradigm MLM introduced shaped all subsequent LLM development, even though the objective itself was later displaced by causal LM.

## Evidence
- Devlin et al. (2018): "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" — the original MLM paper.
- Liu et al. (2019): "RoBERTa" — shows that removing NSP and training longer with larger batches dramatically improves BERT; pure MLM is sufficient.
- Clark et al. (2020): "ELECTRA" — replaces MLM with a discriminative objective (detect replaced tokens rather than predict masked ones) for better efficiency.

## Relationship to Other Concepts
- Contrasts with **causal language modelling** (next-token prediction) — see [[Decoder-Only Dominance]] for why causal LM ultimately won.
- Uses the full [[Attention Mechanism]] without causal masking — bidirectionality is what distinguishes encoder from decoder-only [[Transformer|transformers]].
- Is a [[Representation Learning]] objective: MLM forces the model to build contextual, structured representations that transfer to downstream tasks.
- Connects to [[Inductive Bias]]: the masking strategy and bidirectionality are both architectural biases about what structure matters.
- The training loss at masked positions is [[Cross-Entropy Loss]] — same objective as causal LM but applied to a subset of positions.
- Representations produced by MLM are used for [[Generalization]] on downstream tasks via fine-tuning, mirroring how grokking produces representations that generalise beyond the training set.
- [[Shortcut Learning]] risk: BERT can learn spurious correlations (e.g., predicting `[MASK]` from nearby punctuation) rather than true linguistic structure.
- MLM-trained models cannot do [[RLHF]] — generation is required for reward model evaluation. This is a primary reason the post-GPT-3 AI ecosystem moved to decoder-only.
- [[Feature Learning]] perspective: BERT learns to transform token IDs into rich contextual features — the same feature-learning question studied in grokking.

## Open Questions
Can MLM-trained encoder models exhibit grokking-like transitions during fine-tuning? What is the analogue of the Fourier circuit in BERT's contextual representations — can a similarly clean mechanistic account be found? Does the lower training-signal density of MLM change the *type* of representations learned, or only the *speed* at which they are acquired?

---
## Related Notes
- [[Transformer]] · [[Attention Mechanism]] · [[Decoder-Only Dominance]]
- [[Representation Learning]] · [[Feature Learning]] · [[Inductive Bias]]
- [[Cross-Entropy Loss]] · [[Generalization]] · [[Memorization]]
- [[Shortcut Learning]] · [[RLHF]] · [[Phase Transition]]
- [[Fourier Features]] · [[Grokking]]

[^mlm-efficiency]: **Why 7× less efficient?**

    A sequence of $n$ tokens gives the causal LM model exactly $n$ prediction targets — one per token, predicting the next. MLM selects only ~15% of tokens as masked targets, so a sequence of $n$ tokens gives approximately $0.15n$ prediction targets. The ratio is $n \div 0.15n = 1/0.15 \approx 6.67$, rounded to 7.

    To build intuition: a 100-word paragraph gives causal LM 100 training signals in one pass. MLM gets about 15. To see 100 training signals from the same paragraph, MLM would need to re-mask and re-run the same text roughly 7 times — extra compute for the same amount of learning. At the trillion-token scale of modern pre-training, this compounding inefficiency is enormous.

    Note also that the 10% "leave unchanged" fraction means some of the 15% budget is spent on positions that are trivially predictable (the model sees the original token). The *effective* number of hard prediction targets is even lower — closer to 12%. This widens the efficiency gap further.
