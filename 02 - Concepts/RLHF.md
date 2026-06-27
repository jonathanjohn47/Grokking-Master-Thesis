---
tags: [concept, training, alignment, llm, foundations]
---
↑ Parent: [[Decoder-Only Dominance]] · Related: [[Transformer]] · [[Mechanistic Interpretability]]

# RLHF (Reinforcement Learning from Human Feedback)

## Definition
**RLHF** is a post-training pipeline that steers a pretrained language model's output distribution toward human-preferred behaviour. The core idea: after pretraining on next-token prediction (which makes the model capable but not necessarily helpful or safe), use human judgments of response quality as a reward signal to fine-tune the model further via reinforcement learning.

The canonical formulation was introduced in InstructGPT (Ouyang et al., 2022) and is the pipeline underlying ChatGPT, Claude, Gemini, and virtually every deployed AI assistant.

## In Plain Words
Pretraining makes a model fluent — it can complete text. But "complete text plausibly" is not the same as "be helpful, harmless, and honest." A pretrained model is equally happy to write a great recipe or a convincing disinformation paragraph, because both are plausible continuations of the internet.

RLHF solves this by teaching the model *what humans prefer*. It works by asking humans to rank the model's own outputs, training a separate "preference model" on those rankings, then using that preference model as a reward signal to nudge the LM toward better behaviour.

## The Classic RLHF Pipeline

RLHF has three sequential stages:

### Stage 1 — Supervised Fine-Tuning (SFT)
Start with the pretrained model. Collect a dataset of (prompt, ideal response) pairs written by human contractors (e.g., "write a cover letter for a software engineer" → [example response]). Fine-tune the model to imitate these demonstrations via standard cross-entropy loss. This is ordinary supervised learning — it teaches the model *what good responses look like* but requires expensive human labour to produce each example.

### Stage 2 — Reward Model (RM) Training
For the same prompts, generate multiple model responses, then ask human raters: "which response is better?" — a comparison rather than an absolute rating. Comparing is much cheaper and more consistent than writing ideal responses from scratch.

Train a separate neural network (the **reward model**) to predict the human preference score for any (prompt, response) pair. The RM is usually initialised from the SFT model's weights (without the final language-modelling head), and a linear head is added to output a scalar score.

Formally, if a human prefers response $y_w$ over $y_l$ for prompt $x$, the RM is trained to satisfy:

$$r_\theta(x, y_w) > r_\theta(x, y_l)$$

using a Bradley-Terry pairwise loss.

### Stage 3 — RL Fine-Tuning (PPO)
Use the frozen RM as an environment. The LM is the **policy**: it receives a prompt (state), generates a response (action), and receives a reward $r_\theta(\text{prompt}, \text{response})$. Proximal Policy Optimization (PPO) updates the LM to maximise this reward.

A critical addition: a **KL penalty** keeps the updated model close to the SFT baseline:

$$\text{objective} = \mathbb{E}\left[ r_\theta(x, y) - \beta \cdot \text{KL}\!\left(\pi_\text{RL}(y|x) \,\|\, \pi_\text{SFT}(y|x)\right) \right]$$

Without the KL term, the model would find degenerate responses that score highly on the RM but are bizarre or incoherent — a phenomenon called **reward hacking**. The KL term says: "improve your reward, but don't stray too far from the SFT model."

## Key Variants

The classic PPO-based RLHF is computationally expensive and unstable. Several variants address this:

| Method | Key change | Paper |
|--------|-----------|-------|
| **DPO** (Direct Preference Optimization) | Eliminates the RM entirely; directly optimises the LM from preference pairs by treating the implicit reward analytically | Rafailov et al. (2023) |
| **Constitutional AI (CAI)** | Uses an AI (not humans) to critique and revise outputs according to a set of principles; greatly reduces human labelling | Anthropic (Bai et al., 2022) |
| **RLAIF** | General term for replacing human feedback with AI-generated feedback | Various |
| **KTO** (Kahneman-Tversky Optimisation) | Uses unpaired preference data (just "good" or "bad" labels, no comparisons) | Ethayarajh et al. (2024) |

**DPO** has largely supplanted PPO-based RLHF in practice because it is simpler, more stable, and achieves comparable results. The key insight: the optimal RL policy has a closed-form expression in terms of the preference data, so you can skip the RM and PPO entirely and directly minimise a single loss over preference pairs.

## Why Only Decoder-Only Models

RLHF is **only possible for generative (decoder-only) models**. The pipeline requires:

1. A model that generates a text *sequence* as output (not a single embedding vector).
2. A reward computed over that generated sequence.
3. Gradient flow back into the policy (the LM) to update it.

Encoder-only models (BERT, RoBERTa) produce a fixed-length embedding for a given input — they don't generate tokens sequentially. There is no "response" to evaluate, no sequence to reward, and no natural action space for RL. You cannot make BERT "helpful" via RLHF because there is nothing to prefer or compare.

This is a structural asymmetry — not a gap that better engineering could close — and it is one of the fundamental reasons the entire post-training ecosystem (RLHF, DPO, Constitutional AI, instruction tuning) was built on decoder-only models. See [[Decoder-Only Dominance]].

## What RLHF Changes in the Model

RLHF doesn't teach the model *new facts* — the world knowledge comes from pretraining. What it changes:

- **Format and style**: responses become more structured, direct, and appropriately scoped.
- **Safety**: harmful completions are suppressed.
- **Instruction-following**: the model stops completing text arbitrarily and starts interpreting prompts as instructions.
- **Calibration**: the model becomes more likely to say "I don't know" than to confabulate.

From a mechanistic interpretability perspective, RLHF shifts the activation distribution and likely reweights the contributions of certain attention heads and MLP layers — but exactly *which* circuits are modified by RLHF is an open research question (see [[Mechanistic Interpretability]]).

## Why This Matters for Grokking Research

The connection between RLHF and grokking is subtle but real:

**SFT parallels grokking setup.** The SFT stage is supervised training on a small, curated dataset — exactly the regime where grokking occurs. It is an open question whether the SFT model undergoes grokking-like dynamics (sudden transitions from memorisation to generalisation) when the demonstration dataset is small relative to model capacity.

**RLHF as a second training phase.** Grokking studies a model that transitions through phases (memorisation → plateau → generalisation). RLHF introduces a *second* training phase on top of a pretrained model. The dynamics of this second phase — whether the model re-enters something like a memorisation-generalisation cycle — are not well understood.

**Reward hacking as a generalisation failure.** Reward hacking (the model finds responses that score highly on the RM but are degenerate) is structurally similar to grokking's memorisation phase: the model exploits a proxy metric rather than learning the true underlying objective. The KL penalty is, in effect, a regulariser — analogous to weight decay in the grokking setup.

**Alignment and mechanistic interpretability.** Understanding what RLHF actually changes in model internals is a key alignment question. Mechanistic interpretability tools (residual stream decomposition, activation patching, circuit analysis — see [[Mechanistic Interpretability]]) are being applied to RLHF-trained models to understand what circuits are responsible for instruction-following vs. safety vs. helpfulness. Grokking's lesson — that interpretable circuits can be reverse-engineered — is directly relevant.

## Key Insights

- The three-stage pipeline (SFT → RM → PPO) makes human preference a tractable training signal for billion-parameter models.
- The KL penalty is structurally analogous to weight decay in grokking: both prevent the model from collapsing to a degenerate solution that exploits the training signal.
- DPO shows the RM and PPO are not strictly necessary — the preference signal can be incorporated directly, suggesting that RLHF's effect is more about the data than the RL algorithm.
- RLHF only works for generative models, which is why decoder-only architecture was a prerequisite for the aligned-AI-assistant era.
- RLHF does not teach facts; it reshapes *how* the model uses facts it already has.

## Evidence
- Ouyang et al. (2022): "Training Language Models to Follow Instructions with Human Feedback" (InstructGPT) — the canonical RLHF paper; demonstrates alignment on GPT-3.
- Bai et al. (2022): "Constitutional AI: Harmlessness from AI Feedback" (Anthropic) — CAI variant, AI-assisted feedback.
- Rafailov et al. (2023): "Direct Preference Optimization: Your Language Model is Secretly a Reward Model" — DPO, eliminates RM and PPO.
- Christiano et al. (2017): "Deep Reinforcement Learning from Human Preferences" — the original RLHF method, applied to Atari games and robotics before LLMs.
- Stiennon et al. (2020): "Learning to summarize with human feedback" — first significant RLHF application to an NLP task.

## Relationship to Other Concepts
- [[Decoder-Only Dominance]] — RLHF is only possible for generative/decoder-only models; it is one of the decisive reasons decoder-only architecture won.
- [[Transformer]] — RLHF is applied to a pretrained decoder-only transformer; the architecture is unchanged but the weight distribution shifts.
- [[Mechanistic Interpretability]] — understanding what RLHF modifies at the circuit level is an active interpretability research question; the residual stream framework and activation patching are the natural tools.
- [[Circuit Formation]] — grokking-style phase transitions may occur during SFT; reward hacking parallels memorisation; both require regularisation to resolve.
- [[Weight Decay]] — the KL penalty in RLHF plays an analogous role to weight decay in grokking: it prevents exploitation of the proxy objective.
- [[Phase Transition]] — the SFT and RLHF stages may involve phase-transition-like changes in model behaviour analogous to grokking.

## Open Questions
Do SFT models undergo grokking-like dynamics when the demonstration dataset is small? Which circuits in a pretrained model are actually modified by RLHF, and which remain unchanged? Is DPO finding a fundamentally different solution than PPO-based RLHF, or is the learned policy essentially the same? Can mechanistic interpretability tools identify when a model has "reward hacked" — and is this structurally the same as detecting the memorisation phase in grokking?

---
## Related Notes
- [[Decoder-Only Dominance]] · [[Transformer]] · [[Mechanistic Interpretability]]
- [[Circuit Formation]] · [[Weight Decay]] · [[Phase Transition]]
