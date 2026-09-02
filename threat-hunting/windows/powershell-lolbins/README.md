# Windows PowerShell & LOLBins Threat Hunting Engineering Pack v0.1

This pack converts the eight Windows PowerShell/LOLBin detections into hypothesis-driven, multi-platform threat hunts.

## Hunts

| Hunt | Focus | ATT&CK |
|---|---|---|
| [HUNT-WIN-001](./HUNT-WIN-001-powershell-suspicious-execution/) | PowerShell Suspicious Execution & Post-Execution Activity | T1059.001 |
| [HUNT-WIN-002](./HUNT-WIN-002-powershell-network-retrieval/) | PowerShell Network Retrieval & Follow-on Execution | T1059.001 |
| [HUNT-WIN-003](./HUNT-WIN-003-mshta-proxy-execution/) | Mshta Trusted Binary Proxy Execution | T1218.005 |
| [HUNT-WIN-004](./HUNT-WIN-004-rundll32-proxy-execution/) | Rundll32 Proxy Execution & Suspicious DLL Invocation | T1218.011 |
| [HUNT-WIN-005](./HUNT-WIN-005-regsvr32-scriptlet-proxy/) | Regsvr32 Scriptlet / COM Proxy Execution | T1218.010 |
| [HUNT-WIN-006](./HUNT-WIN-006-wmi-remote-execution/) | WMI / WMIC Remote Process Execution | T1047 |
| [HUNT-WIN-007](./HUNT-WIN-007-scheduled-task-persistence/) | Scheduled Task Persistence & Remote Task Execution | T1053.005 |
| [HUNT-WIN-008](./HUNT-WIN-008-psexec-service-execution/) | PsExec / Service-Based Remote Execution | T1569.002 |

## Hunting Model

`Hypothesis → Broad Search → Baseline → Pivot → Evidence → Decision → Detection Feedback`

A hunt query is intentionally broader than an alert rule. It is designed to surface anomalies and relationships for analyst investigation rather than to immediately generate a high-confidence alert.

## Query Engines

Every hunt includes:

- Splunk SPL
- Microsoft Kusto Query Language (KQL)
- Elastic Kibana Query Language (KQL)
- Elastic Event Query Language (EQL)
- Elastic ES|QL
- OpenSearch Query DSL
- CrowdStrike Falcon LogScale CQL
- SentinelOne Singularity Data Lake PowerQuery
- Google Security Operations YARA-L 2.0

Other engines such as Sigma, Microsoft Defender XDR Custom Detection, Wazuh XML, YARA, Suricata, Snort, Zeek, and Falco are represented in the linked detection/adjunct layers where technically appropriate.

See [hunt-coverage.md](./hunt-coverage.md) and [hunt-to-detection-feedback.md](./hunt-to-detection-feedback.md).
