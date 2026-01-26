from typing import List, Dict, Any
import math

Event = Dict[str, Any]


def normalize_events(events: List[Any]) -> List[Event]:
    seen = set()
    output = []

    for e in events:
        if not isinstance(e, dict):
            continue

        try:
            eid = e["id"].strip()
            src = e["source"].strip()
            ts = int(e["timestamp"])
            val = float(e["value"])
        except Exception:
            continue

        if not eid or not src or ts <= 0:
            continue
        if math.isnan(val) or math.isinf(val):
            continue

        key = (eid, ts)
        if key in seen:
            continue

        seen.add(key)
        output.append(
            {"id": eid, "timestamp": ts, "value": val, "source": src}
        )

    return sorted(output, key=lambda x: x["timestamp"])
