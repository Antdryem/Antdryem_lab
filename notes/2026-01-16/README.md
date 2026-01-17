# README.md

## Context

Exploration of applied LLM workflows focused on chaining model calls to achieve a concrete commercial objective.
Work operated at the boundary between conceptual understanding and practical system assembly, emphasizing prompt design, structured outputs, and agent-like composition.

## Experiments / Clusters Touched

* Day5_BrochureGenerator — multi-call LLM pipeline for content synthesis
* Day5_LinkSelection — relevance filtering via JSON-constrained outputs
* Day5_Streaming — token-level streaming for user-facing UX
* Day5_BusinessApplications — framing LLM workflows as products

## Core Ideas Tested

* Chaining LLM calls produces qualitatively different capabilities than single prompts
* Prompt structure acts as a control surface for model behavior
* JSON and markdown align with model training priors for reliability
* Relevance classification is feasible via language understanding rather than rules
* Streaming exposes the true token-by-token nature of generation
* Verticalized tools retain value even if underlying models are commoditized

## Decisions, Constraints, or Tradeoffs

* Used notebooks to maximize iteration speed over production rigor
* Accepted partial scraping and truncation to control cost and latency
* Split tasks across models to balance reasoning cost and generation speed
* Preferred prompt iteration over hard-coded heuristics
* Allowed creative freedom in generation at the expense of factual strictness

## Failures, Limits, or Open Questions

* Outputs can hallucinate culture, values, or slogans when prompts allow creativity
* Relevance judgments are probabilistic and vary run to run
* No automatic validation of scraped content accuracy
* Scaling beyond small websites may hit context and cost limits
* Transition path from notebook prototype to production system remains undefined

## Notes for Future Reference

* Prompt examples and counterexamples materially shift output quality
* JSON-constrained responses reduce downstream parsing complexity
* Agentic workflows emerge naturally from simple function wrapping
* Streaming requires UI-aware handling when rendering markdown
* Model choice materially affects latency and cost characteristics
