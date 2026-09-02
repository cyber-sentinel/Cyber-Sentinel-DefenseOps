#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import yaml

REQUIRED = {"title", "id", "status", "description", "author", "date", "logsource", "detection", "level", "tags"}
errors = []

# Sigma YAML validation.
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

# Elasticsearch Query DSL must be valid JSON and contain a query object.
for path in sorted(Path("detections").rglob("elastic-query-dsl/*.json")):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: JSON parse error: {exc}")
        continue
    if not isinstance(data, dict) or not isinstance(data.get("query"), dict):
        errors.append(f"{path}: Elasticsearch Query DSL file must contain a top-level query object")

# Elastic EQL basic static sanity.
for path in sorted(Path("detections").rglob("elastic-eql/*.eql")):
    text = path.read_text(encoding="utf-8").strip()
    if not text.startswith("process where "):
        errors.append(f"{path}: expected a process EQL query")

# YARA basic structural sanity. Full compilation can be added when a YARA binary is present in CI.
for path in sorted(Path("detections").rglob("*.yar")):
    text = path.read_text(encoding="utf-8")
    if "rule " not in text or "condition:" not in text:
        errors.append(f"{path}: missing YARA rule or condition section")

# Suricata basic SID uniqueness and structure. Full suricata -T testing belongs in a containerized CI stage.
sids = {}
for path in sorted(Path("detections").rglob("*.rules")):
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not stripped.startswith("alert "):
            errors.append(f"{path}:{lineno}: expected an alert rule")
        match = re.search(r"\bsid:(\d+);", stripped)
        if not match:
            errors.append(f"{path}:{lineno}: missing sid")
            continue
        sid = match.group(1)
        if sid in sids:
            errors.append(f"{path}:{lineno}: duplicate sid {sid}; first seen at {sids[sid]}")
        else:
            sids[sid] = f"{path}:{lineno}"

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Detection pack validation passed.")
