
Exploration focused on foundational mechanics of large language models at the system level. Emphasis was on how model capacity, tokenization, context windows, and API usage constraints shape behavior, cost, and perceived intelligence, with practical inspection via code rather than abstract theory.

Experiments / Clusters Touched

day4-transformers-parameters — scaling behavior and model size

tokenization-basics — tokens vs characters and words

tiktoken-inspection — programmatic tokenization analysis

illusion-of-memory — stateless API calls and conversational context

context-window-and-costs — limits, pricing, and inference constraints

Core Ideas Tested

Parameter count as a proxy for training-time capacity, not raw capability

Tokenization as a pragmatic compromise between characters and words

Distinction between token IDs, embeddings, and downstream vectors

Stateless inference as the root cause of “memory” being an illusion

Context window as a hard constraint on reasoning, retrieval, and cost

Inference-time scaling as orthogonal to training-time scaling

Decisions, Constraints, or Tradeoffs

Treating conversation history as explicit input rather than implicit state

Accepting higher token costs to preserve conversational coherence

Using subword tokenization to improve efficiency and generalization

Favoring smaller, cheaper models when context and reasoning depth allow

Framing cost analysis per million tokens to reason about scale effects

Failures, Limits, or Open Questions

No direct visibility into hidden reasoning tokens despite paying for them

Unclear upper bounds of parameter counts in current frontier models

Context window exhaustion as an unresolved bottleneck for long-running agents

Tokenization artifacts (numbers, code, rare words) still distort reasoning

Assumptions about parameter efficiency rely on incomplete public data

Notes for Future Reference

Always account for full conversation history in token budgeting

Context window must include both prompt and generated output

Cost variability increases with reasoning-heavy or agentic prompting

Token-to-word ratios break down in code, math, and technical text

Inference tricks can outperform raw model scaling in constrained settings