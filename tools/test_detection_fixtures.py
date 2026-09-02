#!/usr/bin/env python3
from pathlib import Path
import json
import sys

BASE = Path("tests/fixtures/detections")

def low(value):
    return str(value or "").lower()

def image_name(event):
    return low(event.get("Image")).replace("/", "\\").rsplit("\\", 1)[-1]

def command(event):
    return low(event.get("CommandLine"))

def match(det_id, event):
    image = image_name(event)
    cmd = command(event)

    if det_id == "DET-WIN-001":
        return image in {"powershell.exe", "pwsh.exe"} and any(x in cmd for x in (
            " -enc ", " -encodedcommand ", " /enc ", " -e "
        ))

    if det_id == "DET-WIN-002":
        return image in {"powershell.exe", "pwsh.exe"} and any(x in cmd for x in (
            "invoke-webrequest", "downloadstring", "downloadfile", "webclient", "start-bitstransfer"
        ))

    if det_id == "DET-WIN-003":
        return image == "mshta.exe" and any(x in cmd for x in (
            "http://", "https://", "javascript:", "vbscript:"
        ))

    if det_id == "DET-WIN-004":
        return image == "rundll32.exe" and any(x in cmd for x in (
            "javascript:", "vbscript:", "http://", "https://"
        ))

    if det_id == "DET-WIN-005":
        return (
            image == "regsvr32.exe"
            and "scrobj.dll" in cmd
            and ("/i:" in cmd or "-i:" in cmd)
        )

    if det_id == "DET-WIN-006":
        return (
            image == "wmic.exe"
            and "/node:" in cmd
            and "process" in cmd
            and "call" in cmd
            and "create" in cmd
        )

    if det_id == "DET-WIN-007":
        return (
            image == "schtasks.exe"
            and "/create" in cmd
            and any(x in cmd for x in (
                "powershell", "pwsh", "cmd /c", "mshta", "rundll32",
                "regsvr32", "\\appdata\\", "\\temp\\"
            ))
        )

    if det_id == "DET-WIN-008":
        return image in {"psexec.exe", "psexec64.exe", "psexesvc.exe"}

    raise KeyError(det_id)

errors = []
det_dirs = sorted(p for p in BASE.glob("DET-WIN-*") if p.is_dir())

if len(det_dirs) != 8:
    errors.append(f"Expected 8 detection fixture directories, found {len(det_dirs)}")

for det_dir in det_dirs:
    det_id = det_dir.name
    pos = json.loads((det_dir / "positive.json").read_text(encoding="utf-8"))
    neg = json.loads((det_dir / "negative.json").read_text(encoding="utf-8"))

    if not pos or not neg:
        errors.append(f"{det_id}: positive and negative fixture sets must be non-empty")
        continue

    for i, event in enumerate(pos, 1):
        if not match(det_id, event):
            errors.append(f"{det_id}: positive fixture #{i} did not match")

    for i, event in enumerate(neg, 1):
        if match(det_id, event):
            errors.append(f"{det_id}: negative fixture #{i} unexpectedly matched")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Detection fixture validation passed: 8 detections, positive and negative controls.")
