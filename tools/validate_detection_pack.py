#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

REQUIRED = {"title", "id", "status", "description", "author", "date", "logsource", "detection", "level", "tags"}
errors = []

for path in sorted(Path("detections").rglob("*.yml")):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: YAML parse error: {exc}")
        continue

    if not isinstance(data, dict):
        errors.append(f"{path}: top-level YAML must be a mapping")
        continue

    missing = sorted(REQUIRED - set(data))
    if missing:
        errors.append(f"{path}: missing required keys: {', '.join(missing)}")

    tags = data.get("tags") or []
    if not any(str(tag).startswith("attack.t") for tag in tags):
        errors.append(f"{path}: missing ATT&CK technique tag")

    detection = data.get("detection")
    if not isinstance(detection, dict) or "condition" not in detection:
        errors.append(f"{path}: detection.condition is required")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Detection pack validation passed.")
