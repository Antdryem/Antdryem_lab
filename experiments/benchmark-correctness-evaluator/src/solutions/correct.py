from typing import List, Dict, Any
import math
import copy

Event = Dict[str, Any]


def normalize_events(events: List[Any]) -> List[Event]:
    seen = {}
    result = []

    for e in events:
        if not isinstance(e, dict):
            continue

        if not all(k in e for k in ("id", "timestamp", "value", "source")):
            continue

        eid = e["id"]
        src = e["source"]
        ts = e["timestamp"]
        val = e["value"]

        if not isinstance(eid, str) or not isinstance(src, str):
            continue
        if not eid.strip() or not src.strip():
            continue
        if not isinstance(ts, int) or ts <= 0:
            continue
        if not isinstance(val, (int, float)):
            continue
        if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
            continue

        key = (eid, ts)
        if key not in seen:
            seen[key] = copy.deepcopy(e)

    result = list(seen.values())
    result.sort(key=lambda x: x["timestamp"])
    return result
