# Windows PowerShell & LOLBins Detection Pack v0.2

This pack provides multi-engine defensive detections for high-signal Windows command execution and LOLBin abuse patterns.

## Coverage

| ID | Use Case | ATT&CK |
|---|---|---|
| DET-WIN-001 | PowerShell Encoded Command | T1059.001 |
| DET-WIN-002 | PowerShell Network Download Pattern | T1059.001 |
| DET-WIN-003 | Mshta Remote or Script-Protocol Execution | T1218.005 |
| DET-WIN-004 | Rundll32 Suspicious Script or Remote Execution | T1218.011 |
| DET-WIN-005 | Regsvr32 Scriptlet / Scrobj Abuse | T1218.010 |
| DET-WIN-006 | WMIC Remote Process Creation | T1047 |
| DET-WIN-007 | Suspicious Scheduled Task Creation | T1053.005 |
| DET-WIN-008 | PsExec / PSEXESVC Execution | T1569.002 |

## Detection Engines

The pack intentionally separates query languages that are often conflated:

- `sigma/` — portable Sigma process-creation rules
- `splunk/` — Splunk SPL
- `kql/` — Microsoft Kusto Query Language for Microsoft Defender XDR / Sentinel-style telemetry
- `elastic-kql/` — Kibana Query Language against ECS process fields
- `elastic-eql/` — Elastic Event Query Language against ECS process events
- `elastic-query-dsl/` — Elasticsearch Query DSL JSON
- `yara/` — file or memory artifact detection only where YARA is technically meaningful
- `suricata/` — network adjunct detections only where an HTTP/network observable exists

See [engine-coverage.md](./engine-coverage.md) for the per-use-case matrix.

## Telemetry

Recommended endpoint telemetry sources:

- Sysmon Event ID 1 (Process Create)
- Windows Security Event ID 4688 with command-line auditing enabled
- Microsoft Defender XDR `DeviceProcessEvents`
- Elastic Endpoint / ECS-compatible process telemetry
- Other EDR/XDR process telemetry with full command line

Network adjunct rules require:

- Suricata HTTP visibility
- plaintext HTTP or an architecture that provides decrypted HTTP visibility
- appropriate `HOME_NET` / `EXTERNAL_NET` definitions

## Validation Model

Rules are intentionally marked `experimental` until tuned against a target environment.

Before production deployment:

1. Validate required fields and field mappings.
2. Replay synthetic or sanitized telemetry.
3. Measure baseline frequency for at least 7–14 days where practical.
4. Identify administrative tooling and software-distribution exceptions.
5. Add narrow environment-specific filters.
6. Validate alert routing and response ownership.
7. Keep a rollback path to disable or restore the previous rule.

See [validation.md](./validation.md).

## Production Warning

Do not copy rules directly into production without field normalization and baseline tuning. SPL index/sourcetype conventions, Elastic ECS mappings, Microsoft table availability, and Suricata visibility vary by deployment.
