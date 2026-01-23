"""
Problem: normalize_events

You are given a list of event records coming from multiple backend systems.
Each record is expected to be a dictionary with the following keys:

- "id": non-empty string
- "timestamp": integer (Unix epoch, seconds)
- "value": integer or float
- "source": string identifier

The goal is to normalize these events into a canonical form while enforcing
strict correctness constraints.

The function must:
1. Discard invalid events (see invalidity rules below).
2. Deduplicate events by (id, timestamp).
3. Return events sorted by timestamp ascending.
4. Preserve numerical correctness of values (no implicit casting).

Invalidity rules:
- Missing required keys.
- timestamp <= 0
- value is NaN or infinite.
- id or source is empty or whitespace.
- Any event that is not a dict.

Edge cases to consider:
- Duplicate events differing only by value.
- Large input sizes.
- Mixed numeric types (int vs float).
- Non-deterministic ordering in input.

The function must be deterministic and side-effect free.
"""


from typing import List, Dict, Any


Event = Dict[str, Any]


def normalize_events(events: List[Any]) -> List[Event]:
    """
    Normalize a list of raw event records.

    Parameters:
        events: list of arbitrary objects (not guaranteed to be valid events)

    Returns:
        A list of normalized event dicts satisfying all invariants.

    Invariants:
        - Each event has keys: id, timestamp, value, source
        - Events are unique by (id, timestamp)
        - Events are sorted by timestamp ascending
        - Output is deterministic given the same input

    Notes:
        - This function should NOT raise on bad input.
        - Invalid events must be silently discarded.
        - Do not mutate the input list or its elements.
    """
    raise NotImplementedError("Specification only; implementation lives in solutions/")
