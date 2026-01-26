from typing import List, Dict, Any

Event = Dict[str, Any]


def normalize_events(events: List[Any]) -> List[Event]:
    valid = []
    for e in events:
        if not isinstance(e, dict):
            continue
        if "id" in e and "timestamp" in e and "value" in e and "source" in e:
            valid.append(e)
    return sorted(valid, key=lambda x: x["timestamp"])
