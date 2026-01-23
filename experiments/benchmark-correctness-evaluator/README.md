# Benchmark Correctness Evaluator (Python)

This repository contains a minimal, reproducible benchmark designed to evaluate **solution correctness**, **failure modes**, and **test rigor** in Python code using real-world constraints.

The goal is not performance tuning or algorithm novelty, but **validation discipline**:
- distinguishing partially-correct solutions from fully-correct ones
- exposing edge cases
- ensuring deterministic, reproducible evaluation

This mirrors how production-grade backend code is validated under adversarial conditions.

---

## Scope

The benchmark focuses on:

- Defining a **problem specification** with ambiguous and adversarial edge cases
- Providing multiple solution implementations:
  - naive (passes trivial cases, fails edge cases)
  - partially correct (handles common cases, misses invariants)
  - correct (fully compliant with specification)
- Evaluating solutions using **strict unit tests**
- Making failure modes explicit and reproducible

Machine Learning is intentionally excluded from the core logic.  
Any ML-related context is treated strictly as an operational constraint.

---

## Project Structure

