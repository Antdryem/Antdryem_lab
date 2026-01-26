from typing import List, Dict, Any

Event = Dict[str, Any]


def normalize_events(events: List[Any]) -> List[Event]:
    """
    Normalize a list of raw event records.

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
    raise NotImplementedError
