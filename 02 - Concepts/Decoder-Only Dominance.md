---
tags: [concept, architecture, transformer, foundations, llm]
---
↑ Parent: [[Transformer]] · Related: [[Attention Mechanism]] · [[Neural Scaling Laws]] · [[Few-Shot Learning]]

# Why Decoder-Only Models Won

## What Is It?

A **decoder-only transformer** is a type of AI model that works by predicting the next word — one word at a time — to produce text.

Models like GPT, Claude, LLaMA, Mistral, and Gemini are all decoder-only.

Today, decoder-only models are the most popular and powerful design for AI language systems. They have taken over from two older designs:

- **Encoder-only models** (like BERT, RoBERTa) — good at *understanding* text, but cannot *generate* it.
- **Encoder-decoder models** (like T5, BART) — can both understand and generate, but are more complex.

This didn't happen overnight. BERT was the best model in the world for two years. But over time, decoder-only models proved to be simpler, more flexible, and much easier to scale up.

> [!NOTE]
> "Decoder-only dominance" means: one design style has become so successful that almost all modern AI language systems now use it.

---

## Why Does It Exist?

### The Problem It Solves

Before 2020, AI researchers used different types of models for different tasks:

- A model for **translation**.
- A different model for **question answering**.
- Another model for **summarisation**.
- Yet another for **classification**.

Each task needed its own specially trained model. This was expensive, slow, and complicated.

Decoder-only models solved this by doing something radical: **framing every task as text generation**.

Instead of building a special model for each task, you just ask one model to *write* the answer. Want a translation? Ask the model to write it. Want a summary? Ask the model to write it. Want a classification? Ask the model to write the label.

One model. Every task.

---

## How Did This Happen? A Simple History

| Year | What Happened | Why It Mattered |
|------|--------------|----------------|
| 2017 | "Attention Is All You Need" paper | Invented the transformer architecture |
| 2018 | BERT released by Google (encoder-only) | Best model in the world; "understanding" was king |
| 2018 | GPT-1 released by OpenAI (decoder-only) | Decent results; mostly ignored |
| 2019 | GPT-2 | Impressive text generation; people were surprised |
| 2020 | GPT-3 (175 billion parameters) | Could solve new tasks with just a few examples in the prompt — no training needed. **Everything changed.** |
| 2022 | InstructGPT / ChatGPT | Combined decoder-only with human feedback → consumer AI |
| 2023 | LLaMA, Mistral, Gemini, Claude | All decoder-only. Encoder-only models pushed to the sidelines. |

---

## The 8 Reasons Decoder-Only Models Won

### Reason 1 — Training on Free Data

Decoder-only models are trained on **next-token prediction**. This means: given the words so far, predict the next word.

Here is why this is powerful: **the answer is always already in the text**.

If the training sentence is *"The cat sat on the mat"*, then when the model reads *"The cat sat on the"* — the answer, *"mat"*, is right there in the next position. No human has to label anything. The text labels itself.

This means you can train on every book, article, and webpage ever written — for free.[^decoder-only-training]

Also: a sentence of $n$ words gives the model $n$ separate learning opportunities in one pass. BERT (encoder-only) uses **[[Masked Language Modelling|Masked Language Modelling (MLM)]]**, which only gives about $0.15n$ learning signals — roughly **7× fewer** per sentence.[^mlm-explained]

> [!TIP]
> Think of it this way: a decoder-only model learns something from every single word in every sentence. BERT only learns from about 1 in 7 words.

---

### Reason 2 — One Simple Goal

Decoder-only models have a single job: **predict the next word**.

BERT needed two goals at the same time — predict masked words *and* decide if two sentences were related. Two goals made it harder to scale and harder to improve.

One goal is simpler to train, simpler to debug, and much simpler to scale up.

---

### Reason 3 — Every Task Becomes Writing

This is the most important insight. **Any language task can be turned into a text-generation task**.

Here are some examples:

- **Classification** → *"The sentiment of this review is ___"*
- **Translation** → *"Translate to French: 'Hello' →"*
- **Question answering** → *"Q: What is the capital of France? A:"*
- **Summarisation** → *"Summarise the following article: ..."*
- **Code** → *"Write a Python function that..."*

Encoder-only models **cannot do this**. They produce a single summary vector — a compressed number — not a sequence of words. To do any task, they need a special "head" (an extra piece added on top) designed just for that task.

Decoder-only models can do everything encoder-only models do — plus generate text. Encoder-only models cannot return the favour.

---

### Reason 4 — No Training Needed for New Tasks

In 2020, GPT-3 showed something remarkable: **you could solve a new task just by describing it in the prompt**.

Give the model three examples of translating English to French. Then give it a new English sentence. It translates it — without any training on translation, without any parameter updates.

This is called [[Few-Shot Learning]] or **in-context learning**.

With encoder-only models, every new task required:
1. Collect labelled examples.
2. Design a special output head.
3. Fine-tune the model for days.
4. Deploy a separate model.

With a large decoder-only model:
1. Describe the task in the prompt.
2. Done.

The mechanism behind this is called **induction heads** — special attention circuits that recognise repeating patterns in the context and complete them. See [[Attention Mechanism]] for more detail.

> [!NOTE]
> This connects to grokking: the model learns to recognise a rule from examples in the prompt. Grokking is the same thing happening during training — the model suddenly recognises the underlying pattern after long exposure to examples.

---

### Reason 5 — Human Feedback Training Requires Generation

Once a model can generate text, you can improve it using **[[RLHF|Reinforcement Learning from Human Feedback (RLHF)]]**.

The idea: human raters read the model's outputs and say which ones are better. The model learns to produce outputs humans prefer.

This only works if the model actually *produces* text. Encoder-only models output a number vector, not words. There is no natural way to ask a human "which embedding is better?" The entire field of model alignment — instruction tuning, [[RLHF]], DPO, Constitutional AI — only exists because decoder-only models can produce text that humans can read and rate.

---

### Reason 6 — Scaling Laws

Researchers discovered that decoder-only model performance improves in a **predictable, reliable way** as you increase compute, data, and model size. This is described by the **[[Neural Scaling Laws]]** (Kaplan et al. 2020, Hoffmann et al. 2022 — "Chinchilla").

This was a big deal. It meant labs could plan: *"If we use 10× more compute, we will get roughly this much better."* There was a reliable roadmap.

No equivalent roadmap was found for encoder-only models. Their training objective (masked word prediction) is a proxy — getting better at it doesn't cleanly translate to being more capable on real tasks.

The Chinchilla result also showed that data efficiency matters enormously at scale. The decoder-only approach — $n$ learning signals per sentence — means every extra token of training data is used much more efficiently.

---

### Reason 7 — Emergent Abilities

As decoder-only models grew larger, they started doing things nobody programmed them to do:

- Multi-step arithmetic.
- Chain-of-thought reasoning.
- Code generation.
- Analogical reasoning.

These abilities appeared **suddenly** above certain scales — not gradually. Small models couldn't do them. Large models could.

This is called **[[Emergence]]** — and it connects directly to grokking. In grokking, a model suddenly learns to generalise after long training. In large models, a capability suddenly appears above a size threshold. Both are **phase transitions** — sudden jumps rather than smooth improvements. See [[Phase Transition]].

No equivalent emergent abilities were documented for encoder-only models at scale.

---

### Reason 8 — Long Contexts and Flexible Output

Encoder-only models (like BERT) were originally limited to **512 tokens** — about 400 words. Every input had to fit in that window.

Decoder-only models, by design, generate outputs of **any length**. Researchers built new techniques (like RoPE — Rotary Positional Encoding, and sliding window attention) to push their context windows to 128,000 tokens and beyond.

These improvements happened because there was a huge incentive — long-context generation is genuinely useful. No equivalent ecosystem developed for encoder-only models because there was no equivalent need.

---

## Where Encoder-Only Models Still Win

Encoder-only models are not useless — they just have a narrower role now:

- **Semantic search and retrieval** — producing a single dense vector to find similar documents.[^embedding-retrieval]
- **Fast classification** — BERT-family models are smaller and faster when you just need a quick yes/no label.
- **Specialised domains** — clinical NLP, legal document classification, where you have labels and don't need generation.

These are niches, not the mainstream. The general-purpose AI landscape belongs to decoder-only.

---

## Why This Matters for Grokking Research

The grokking experiments in this vault use a **decoder-only transformer** — the same architecture as GPT, Claude, and LLaMA. This is not a coincidence.

- The **next-token prediction** objective that drives LLM capabilities is the same objective under which grokking occurs.
- **In-context learning** (driven by induction heads — see [[Attention Mechanism]]) and **grokking** (sudden generalisation after long training) are both sudden phase-transition-like events coming from the same training dynamics.
- Understanding grokking in a small toy setting may explain why large decoder-only models develop emergent capabilities. Both stories are about a model discovering a compressed, general rule after initially memorising the training data.

See [[Emergence]] and [[Phase Transition]] for the cross-scale connection.

---

## Simple Example

Imagine you want to build an AI that can:
- Answer questions.
- Translate sentences.
- Summarise articles.
- Write code.

**Old approach (encoder-only):** Build four separate models. Train each one on labelled data. Maintain four systems.

**New approach (decoder-only):** Build one model. Ask it to write the answer. One system handles everything.

The decoder-only model wins because writing is a superset of understanding.

---

## Analogy

Think of an encoder-only model as a **brilliant reader** who can understand any book deeply — but is completely mute. They can tell you whether a sentence is positive or negative (by writing a score on paper), but they cannot speak a sentence themselves.

A decoder-only model is a **writer** who can also read. They understand text deeply *because* they have learned to generate it. And they can do anything: summarise, translate, answer, explain — all by writing.

For a long time, people thought the reader was smarter. Then they realised: a good enough writer is also a good reader — and the writer can do things the reader simply cannot.

---

## Important Terms

| Term | Simple Definition |
|------|------------------|
| **Decoder-only model** | An AI that generates text one word at a time by predicting what comes next |
| **Encoder-only model** | An AI that reads and understands text but cannot generate it |
| **Next-token prediction** | The training task: given the words so far, predict the next word |
| **Masked Language Modelling (MLM)** | BERT's training task: randomly hide some words and predict them |
| **Few-shot learning** | Solving a new task from just a few examples in the prompt, no training needed |
| **In-context learning** | The ability to follow instructions and examples given in the prompt |
| **Induction heads** | Attention circuits inside the model that detect repeating patterns |
| **Emergent ability** | A capability that suddenly appears at large scale but was absent at small scale |
| **Scaling laws** | Mathematical rules describing how model performance improves with more compute/data |
| **RLHF** | Reinforcement Learning from Human Feedback — training a model to be more helpful using human ratings |
| **Embedding / dense vector** | A compressed list of numbers that represents the meaning of a piece of text |

---

## Key Takeaways

- Decoder-only models are trained on next-token prediction — a task where **every word in every sentence is a free training label**.
- They produce **$n$ learning signals per sentence**, compared to only ~$0.15n$ for BERT. That is a 7× efficiency advantage that compounds enormously at scale.
- **Any language task can be framed as text generation** — decoder-only models can do everything encoder-only models can do, plus generate text.
- GPT-3's **few-shot learning** showed that large decoder-only models can solve new tasks from prompt examples alone — no fine-tuning, no labelled data.
- The entire **post-training ecosystem** ([[RLHF]], instruction tuning, alignment) is built on decoder-only generation.
- **Scaling laws** are cleaner for decoder-only models, giving a reliable improvement roadmap.
- **Emergent capabilities** at large scale mirror **grokking** at small scale — both are sudden phase transitions in generalisation.

---

## Evidence

- Kaplan et al. (2020): "Scaling Laws for Neural Language Models" — decoder-only scaling laws.
- Hoffmann et al. (2022): "Training Compute-Optimal Large Language Models" (Chinchilla) — data efficiency.
- Brown et al. (2020): "Language Models are Few-Shot Learners" (GPT-3) — the in-context learning paradigm shift.
- Ouyang et al. (2022): "Training Language Models to Follow Instructions with Human Feedback" (InstructGPT) — RLHF on decoder-only.
- Olsson et al. (2022): "In-context Learning and Induction Heads" — the mechanistic basis of few-shot learning.

---

## Relationship to Other Concepts

- [[Transformer]] — the architecture; decoder-only is now its dominant variant.
- [[Attention Mechanism]] — causal masking (decoder-only) vs. bidirectional (encoder-only); induction heads as the mechanistic basis of in-context learning.
- [[Neural Scaling Laws]] — the scaling laws that made decoder-only dominance predictable in hindsight.
- [[Emergence]] — emergent capabilities at scale are the large-scale analogue of grokking.
- [[Phase Transition]] — scaling laws produce phase-transition-like capability jumps; grokking is the same in miniature.
- [[Mechanistic Interpretability]] — the field that explains *why* decoder-only models generalise, via induction heads and the residual stream framework.

---

## Open Questions

- Will decoder-only models continue to dominate, or will hybrid architectures (mixture-of-experts, state-space models like Mamba) eventually challenge them?
- Do the scaling laws plateau? And if so, does the advantage of the causal LM objective diminish?
- Is emergent capability in large language models mechanistically the same phenomenon as grokking?

---

## Related Notes

- [[Transformer]] · [[Attention Mechanism]] · [[Neural Scaling Laws]]
- [[Emergence]] · [[Phase Transition]] · [[Mechanistic Interpretability]]
- [[Grokking]] · [[Circuit Formation]] · [[RLHF]]
- [[Few-Shot Learning]]

---

[^decoder-only-training]: Three claims unpacked:

    **1. "Next-token prediction (causal language modelling)"** — The model sees a partial sequence and predicts the next word. Given *"The cat sat on the"*, it learns to predict *"mat."* The word *causal* means it can only look backwards — each prediction uses only the tokens that came before it, never the ones ahead.

    **2. "The training signal is free"** — To understand this, first consider how most supervised machine learning works. In image classification, a human must look at thousands of photos and manually write labels: *"this is a cat," "this is a dog."* That labelling is expensive, slow, and bottlenecks how much data you can train on. The label is the *training signal* — the thing the model compares its prediction against in order to learn.

    Now consider a sentence: *"The cat sat on the mat."* The model's job is to predict the next token at each position. When it predicts what comes after *"The cat sat on the"*, the correct answer is *"mat"* — and that answer was already sitting right there in the original text. No human needed to write it. The text itself supplies the label for free.

    This means every book, article, webpage, and forum post on the internet is a ready-made training dataset — no annotation, no labelling pipeline, no human in the loop. You just feed raw text in, and the next word is always the answer. The "cost" of obtaining labelled data — which limits almost every other ML task — simply does not exist here. That is what "free" means: the supervision signal is already embedded in the structure of language itself.

    **3. "An $n$-token sequence produces $n$ training examples simultaneously"** — Consider the six-word sentence *"The cat sat on the mat."* In a single forward pass, the model makes five predictions at once: *"The" → "cat"*, *"The cat" → "sat"*, *"The cat sat" → "on"*, and so on. Every token position is a separate training example, all computed in parallel. By contrast, a labelled image dataset gives one training example per image. This parallelism is why causal LM is so data-efficient at scale.

    To see why this matters, think about what a "forward pass" is. The model reads the entire sentence in one go. At every single position, it simultaneously asks: *"given everything up to here, what comes next?"* Position 1 asks what follows *"The."* Position 2 asks what follows *"The cat."* Position 3 asks what follows *"The cat sat."* And so on — all at the same time, in one pass through the network.

    Each of those questions is a fully independent training example with its own prediction and its own error signal. A six-token sentence therefore hands the model five separate learning opportunities in one shot. A document with 1,000 tokens hands it 999.

    Now compare to an image classifier. You feed in one image, get one prediction, compute one error, update the model once. To get 999 learning updates, you need 999 separate images. For a language model, you need one document of 1,000 tokens.

    This is the compounding advantage at scale. Modern LLMs train on trillions of tokens. Every single one of those tokens is both an input *and* a label for the token before it. The dataset is simultaneously enormous and fully labelled — at zero extra cost.

[^embedding-retrieval]: **What "producing a single dense vector for semantic search" actually means.**

    **The core idea.** Imagine you have a library of one million documents and a user types a query: *"How do transformer attention heads work?"* You need to find the most relevant documents — fast. The classical approach is keyword matching: find documents containing the words "transformer," "attention," "heads." But keyword matching is brittle. A document that uses *"[[self-attention mechanisms in neural networks]]"* is highly relevant but shares few exact words with the query.

    Semantic search solves this by mapping every document — and every query — to a point in a high-dimensional vector space, where **meaning determines proximity**. Two sentences that mean the same thing should land near each other; two that mean different things should be far apart. The distance between vectors is the measure of semantic similarity.

    **What "dense vector" means.** A *sparse* vector for a 50,000-word vocabulary would be 50,000 numbers long, nearly all zeroes — one slot per vocabulary word, non-zero only when that word appears. TF-IDF and BM25 (classic IR systems) work this way. A *dense* vector is far shorter — typically 384, 768, or 1536 numbers — and every slot is a non-zero floating-point value encoding some abstract semantic feature. Dense vectors pack more meaning into fewer dimensions because the model has learned to compress semantics during training, not just record word occurrence.

    **How an encoder-only model produces one.** A sentence like *"Attention heads detect syntactic structure"* enters the encoder as a sequence of tokens. Bidirectional attention lets every token attend to every other token simultaneously — the word "heads" sees both "Attention" (to its left) and "detect" (to its right) at the same time. After $L$ transformer layers, each token has a rich contextual representation. To collapse this sequence into a single vector, two strategies are common:

    - **[CLS] pooling**: BERT prepends a special `[CLS]` token to every sequence. After the forward pass, the hidden state of `[CLS]` is used as the sentence-level embedding. In theory, because every token attends to `[CLS]` and vice versa throughout all layers, `[CLS]` accumulates a global summary of the whole input.
    - **Mean pooling**: average the hidden states of all non-padding tokens. In practice, `sentence-transformers` found this often outperforms `[CLS]` pooling, especially after fine-tuning on semantic similarity datasets.

    Either way, the output is a single vector — one point in the embedding space — representing the entire input sentence.

    **Why encoder-only is well-suited here.** Bidirectional attention is the key advantage. When encoding a query or document, you already have the full text — there is nothing to generate, so there is no need for causal masking. Seeing the whole sentence from both directions lets the encoder build richer contextual representations per token than a left-to-right decoder would. The resulting embedding is more informationally dense.

    **What `sentence-transformers` does.** Raw BERT embeddings are surprisingly poor for semantic similarity out of the box. The `[CLS]` token was trained under MLM, not under any sentence-similarity objective, so geometrically similar sentences do not necessarily land near each other in embedding space. `sentence-transformers` (Reimers & Gurevych, 2019) fine-tunes a BERT-like model using **Siamese network training**: pairs of semantically similar sentences are pushed closer together; dissimilar pairs are pushed apart. After this fine-tuning, the embedding space has the structure you actually want for retrieval — proximity = semantic similarity.

    **The retrieval pipeline.** At index time, you run every document through the encoder and store its embedding in a vector database (e.g., FAISS, Pinecone, Weaviate). At query time, you encode the query with the same model, then compute approximate nearest neighbours in the embedding space — typically via cosine similarity or dot product. The top-$k$ results are the most semantically similar documents. Because the search is over fixed-length vectors rather than variable-length text, it can be made extremely fast with approximate nearest-neighbour indices, even at million-document scale.

    **Why decoder-only models are less natural here.** A decoder-only model produces a new token at each step; it does not have a built-in mechanism for collapsing a sequence into a single summary vector. You can extract the hidden state of the last token as an approximation, but because causal masking means early tokens cannot attend to later tokens, the final token carries most of the contextual weight and early tokens are underrepresented. Decoder-only embeddings are improving (e.g., E5-Mistral, LLM2Vec), but they require careful fine-tuning to overcome the structural mismatch between autoregressive generation and fixed-vector retrieval. Encoder-only models have the architectural alignment: one forward pass, full bidirectional context, one vector out.

[^mlm-explained]: **How MLM works — a simple breakdown.**

    **What "masking" means.** Take a sentence: *"The cat sat on the mat."* MLM randomly picks about 15% of the tokens — say, *"sat"* and *"mat"* — and replaces them with a special placeholder called `[MASK]`. The sentence becomes: *"The cat [MASK] on the [MASK]."* The model's job is to recover the original words at those two positions, using the surrounding context.

    **Why only 15%?** If you masked every token, there would be nothing left to read — the model would have no context to predict from. If you masked almost nothing, training signals would be extremely sparse. 15% is the experimentally-found sweet spot: enough masked positions to learn from in each sentence, but enough visible context to make sensible predictions.

    **The 80/10/10 split — and why it matters.** Of the ~15% of tokens chosen for masking, not all of them actually get replaced with `[MASK]`. The breakdown is:
    - **80%** → replaced with `[MASK]`. This is the main training case.
    - **10%** → replaced with a *random* other word (e.g., the word "banana" appears where "sat" should be). This forces the model to not trust that every token is correct — it must verify even unmasked positions.
    - **10%** → left *completely unchanged*. The model still has to predict the original token, but it sees the real word. This prevents the model from learning to treat `[MASK]` tokens as the only ones that matter.

    Without the 10/10 trick, the model would "switch off" for unmasked positions and only pay attention when it saw `[MASK]`. After pre-training, there are no `[MASK]` tokens during fine-tuning — so a model that ignored non-masked tokens would perform badly. The 80/10/10 split prevents this mismatch.

    **Why it's only $0.15n$ training signals.** A sentence of $n$ tokens gives $0.15 \times n$ masked positions. The model only computes a loss — and therefore only learns — at those masked positions. The other $0.85 \times n$ positions contribute nothing to the gradient update. In contrast, causal LM computes a loss at every single position (each token predicts the next), giving $n$ training signals from the same sentence. That is the origin of the ~7× inefficiency: $n \div 0.15n \approx 6.7$.

    **What "bidirectional" means and why it matters.** When filling in *"The cat [MASK] on the mat,"* you can look at words both before *and* after the blank — you use *"The cat"* (left context) and *"on the mat"* (right context) together. This is **bidirectional** attention. Causal (decoder-only) models are **unidirectional**: when predicting the next word, they can only see what came before, never what comes after. Bidirectionality gives MLM a richer understanding of each token — but it means the model structurally cannot generate text, because generating word $t$ would require attending to future words $t+1, t+2, \ldots$ that haven't been generated yet.

    **Why MLM is called a "proxy task."** Next-token prediction is a direct objective: *predict what actually comes next in the text*. MLM is indirect: *predict words we randomly chose to hide*. The signal is useful, but it is a human-designed approximation of language understanding rather than language understanding itself. At large scales, this distinction matters: optimising a proxy well does not guarantee you are optimising the true objective well. Next-token prediction has no such gap — predicting the next token *is* the task.
