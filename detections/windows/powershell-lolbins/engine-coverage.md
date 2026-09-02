# Detection Engine Coverage Matrix

Legend:

- **Native** — the engine observes the primary behavior directly.
- **Adjunct** — useful supporting evidence, but not equivalent to the endpoint process detection.
- **N/A** — the engine is not a technically appropriate representation of that observable.

| ID | Sigma | Splunk SPL | Microsoft KQL | Elastic KQL | Elastic EQL | Elastic Query DSL | YARA | Suricata |
|---|---|---|---|---|---|---|---|---|
| DET-WIN-001 PowerShell Encoded Command | Native | Native | Native | Native | Native | Native | Adjunct | N/A |
| DET-WIN-002 PowerShell Network Download | Native | Native | Native | Native | Native | Native | Adjunct | Adjunct |
| DET-WIN-003 Mshta Remote/Script Protocol | Native | Native | Native | Native | Native | Native | Adjunct | Adjunct |
| DET-WIN-004 Rundll32 Suspicious Script/Remote | Native | Native | Native | Native | Native | Native | N/A | N/A |
| DET-WIN-005 Regsvr32 Scriptlet/Scrobj | Native | Native | Native | Native | Native | Native | Adjunct | Adjunct |
| DET-WIN-006 WMIC Remote Process Creation | Native | Native | Native | Native | Native | Native | N/A | N/A |
| DET-WIN-007 Suspicious Scheduled Task Creation | Native | Native | Native | Native | Native | Native | N/A | N/A |
| DET-WIN-008 PsExec/PSEXESVC Execution | Native | Native | Native | Native | Native | Native | N/A | N/A |

## Why YARA Is Not Universal

YARA scans files or process memory. It does not natively represent Windows process command-line telemetry, so a YARA rule for every LOLBin would create misleading coverage.

The YARA rules in this pack detect supporting script/file artifacts such as PowerShell retrieval primitives, HTA content, or scriptlet/scrobj content.

## Why Suricata Is Not Universal

Suricata observes network traffic. Local process creation, service execution, WMI, and scheduled-task creation are endpoint behaviors.

The Suricata rules in this pack therefore provide only supporting HTTP observables for PowerShell, HTA, and scriptlet retrieval patterns.
