#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET
import yaml

errors = []
REQUIRED = {"title", "id", "status", "description", "author", "date", "logsource", "detection", "level", "tags"}

# Prohibit ambiguous KQL folder names.
for p in Path("detections").rglob("*"):
    if p.is_dir() and p.name.lower() == "kql":
        errors.append(f"{p}: ambiguous directory name 'kql' is prohibited; use microsoft-kql or elastic-kql")

# Sigma.
for path in sorted(Path("detections").rglob("sigma/*.yml")):
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

# JSON query formats.
for pattern in ("elastic-query-dsl/*.json", "opensearch-query-dsl/*.json"):
    for path in sorted(Path("detections").rglob(pattern)):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path}: JSON parse error: {exc}")
            continue
        if not isinstance(data, dict) or not isinstance(data.get("query"), dict):
            errors.append(f"{path}: query DSL file must contain a top-level query object")

# Elastic EQL / ES|QL.
for path in sorted(Path("detections").rglob("elastic-eql/*.eql")):
    if not path.read_text(encoding="utf-8").strip().startswith("process where "):
        errors.append(f"{path}: expected an Elastic process EQL query")
for path in sorted(Path("detections").rglob("elastic-esql/*.esql")):
    text = path.read_text(encoding="utf-8")
    if "FROM " not in text or "| WHERE " not in text:
        errors.append(f"{path}: expected Elastic ES|QL FROM and WHERE commands")

# Wazuh XML.
wazuh_ids = set()
for path in sorted(Path("detections").rglob("wazuh-xml/*.xml")):
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: XML parse error: {exc}")
        continue
    for rule in root.findall(".//rule"):
        rid = int(rule.attrib.get("id", "0"))
        if not 100000 <= rid <= 120000:
            errors.append(f"{path}: Wazuh custom rule id {rid} is outside 100000-120000")
        if rid in wazuh_ids:
            errors.append(f"{path}: duplicate Wazuh rule id {rid}")
        wazuh_ids.add(rid)

# CrowdStrike CQL.
for path in sorted(Path("detections").rglob("crowdstrike-logscale-cql/*.cql")):
    text = path.read_text(encoding="utf-8")
    if "#event_simpleName=ProcessRollup2" not in text:
        errors.append(f"{path}: expected Falcon ProcessRollup2 source filter")

# SentinelOne PowerQuery templates.
for path in sorted(Path("detections").rglob("sentinelone-star/*.powerquery")):
    text = path.read_text(encoding="utf-8")
    if "event.type='Process Creation'" not in text and 'event.type = \'Process Creation\'' not in text:
        errors.append(f"{path}: expected SentinelOne process-creation event filter")

# Google SecOps YARA-L.
for path in sorted(Path("detections").rglob("google-secops-yara-l/*.yaral")):
    text = path.read_text(encoding="utf-8")
    for token in ("rule ", "meta:", "events:", "condition:", 'metadata.event_type = "PROCESS_LAUNCH"'):
        if token not in text:
            errors.append(f"{path}: missing YARA-L token {token}")

# YARA basic structure.
for path in sorted(Path("detections").rglob("*.yar")):
    text = path.read_text(encoding="utf-8")
    if "rule " not in text or "condition:" not in text:
        errors.append(f"{path}: missing YARA rule or condition")

# Suricata/Snort SID uniqueness within each family.
for family, pattern in (("Suricata", "suricata/*.rules"), ("Snort3", "snort3/*.rules")):
    sids = {}
    for path in sorted(Path("detections").rglob(pattern)):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith("(") or stripped.startswith(")"):
                continue
            match = re.search(r"\bsid:(\d+);", stripped)
            if match:
                sid = match.group(1)
                if sid in sids:
                    errors.append(f"{path}:{lineno}: duplicate {family} sid {sid}; first seen at {sids[sid]}")
                sids[sid] = f"{path}:{lineno}"

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Detection pack validation passed.")
