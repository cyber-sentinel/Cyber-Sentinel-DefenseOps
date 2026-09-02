#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

errors = []
base = Path("threat-hunting/windows/powershell-lolbins")
required_queries = {
    "splunk-spl.spl",
    "microsoft-kql.kql",
    "elastic-kql.kql",
    "elastic-eql.eql",
    "elastic-esql.esql",
    "opensearch-query-dsl.json",
    "crowdstrike-logscale-cql.cql",
    "sentinelone-powerquery.powerquery",
    "google-secops-yara-l.yaral",
}
required_headings = {
    "## Hypothesis",
    "## Threat Context",
    "## Required Telemetry",
    "## Primary Signals",
    "## Hunt Procedure",
    "## Key Pivots",
    "## Evidence to Collect",
    "## Decision Criteria",
    "## Hunt → Detection Feedback",
    "## Limitations",
}

hunt_dirs = sorted(p for p in base.glob("HUNT-WIN-*") if p.is_dir())
if len(hunt_dirs) != 8:
    errors.append(f"{base}: expected 8 hunt directories, found {len(hunt_dirs)}")

for hunt in hunt_dirs:
    if not re.match(r"HUNT-WIN-00[1-8]-", hunt.name):
        errors.append(f"{hunt}: unexpected hunt naming")

    readme = hunt / "README.md"
    if not readme.exists():
        errors.append(f"{hunt}: missing README.md")
        continue

    text = readme.read_text(encoding="utf-8")
    for heading in required_headings:
        if heading not in text:
            errors.append(f"{readme}: missing heading {heading}")
    if "Microsoft Kusto Query Language (KQL)" not in text:
        errors.append(f"{readme}: Microsoft KQL label must be explicit")
    if "Elastic Kibana Query Language (KQL)" not in text:
        errors.append(f"{readme}: Elastic KQL label must be explicit")

    qdir = hunt / "queries"
    present = {p.name for p in qdir.iterdir()} if qdir.exists() else set()
    missing = sorted(required_queries - present)
    if missing:
        errors.append(f"{hunt}: missing query files: {', '.join(missing)}")

    dsl = qdir / "opensearch-query-dsl.json"
    if dsl.exists():
        try:
            data = json.loads(dsl.read_text(encoding="utf-8"))
            if "query" not in data:
                errors.append(f"{dsl}: missing query object")
        except Exception as exc:
            errors.append(f"{dsl}: invalid JSON: {exc}")

    yaral = qdir / "google-secops-yara-l.yaral"
    if yaral.exists():
        yt = yaral.read_text(encoding="utf-8")
        for token in ("rule ", "events:", "condition:", 'metadata.event_type = "PROCESS_LAUNCH"'):
            if token not in yt:
                errors.append(f"{yaral}: missing token {token}")

# Global ambiguity check under threat-hunting.
for p in Path("threat-hunting").rglob("*"):
    if p.is_dir() and p.name.lower() == "kql":
        errors.append(f"{p}: ambiguous directory name 'kql' is prohibited")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Threat hunting pack validation passed.")
