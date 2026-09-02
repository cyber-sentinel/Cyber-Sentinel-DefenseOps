# HUNT-WIN-007 — Scheduled Task Persistence & Remote Task Execution

**Status:** Experimental Hunt
**Platform:** Windows
**ATT&CK:** [T1053.005 — Scheduled Task/Job: Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If an adversary creates or modifies a Windows scheduled task for persistence or execution, process and task telemetry should reveal unusual creators, actions, paths, remote targets, schedules, or follow-on execution.

## Threat Context

This hunt is designed to identify behavior that may be too broad, contextual, or environment-dependent for immediate alerting. It deliberately searches beyond the narrow detection rule and relies on analyst pivots, prevalence, parent/child relationships, identity context, and surrounding telemetry.

## Required Telemetry

Minimum:

- Process creation with full command line
- Parent process name and command line
- Host and user identity
- Reliable timestamps

Recommended:

- Sysmon Event ID 1 / Windows Security 4688
- EDR/XDR process telemetry
- Network connection telemetry
- DNS/proxy/firewall telemetry
- File creation and hash telemetry
- Authentication/logon telemetry
- Relevant Windows operational logs

## Primary Signals

- schtasks /create or /change
- Remote target via /s
- Action invoking interpreters/LOLBins
- Payload from user-writable directory
- Task created by unusual user or parent process

## Hunt Procedure

1. Run the broad query for a 7–14 day window where retention permits.
2. Establish prevalence by user, host, parent process, and command-line pattern.
3. Identify rare or first-seen combinations.
4. Pivot into child processes, network, files, identity, and peer-host activity.
5. Compare activity with known administrative tooling and change windows.
6. Preserve evidence for suspicious cases.
7. Classify the result as benign, suspicious, or incident candidate.
8. Feed stable findings back into detection engineering.

## Query Engines

| Query Artifact | Platform / Language |
|---|---|
| `queries/splunk-spl.spl` | Splunk Search Processing Language (SPL) |
| `queries/microsoft-kql.kql` | Microsoft Kusto Query Language (KQL) |
| `queries/elastic-kql.kql` | Elastic Kibana Query Language (KQL) |
| `queries/elastic-eql.eql` | Elastic Event Query Language (EQL) |
| `queries/elastic-esql.esql` | Elastic ES|QL |
| `queries/opensearch-query-dsl.json` | OpenSearch Query DSL |
| `queries/crowdstrike-logscale-cql.cql` | CrowdStrike Falcon LogScale CQL |
| `queries/sentinelone-powerquery.powerquery` | SentinelOne Singularity Data Lake PowerQuery |
| `queries/google-secops-yara-l.yaral` | Google Security Operations YARA-L 2.0 |

## Key Pivots

- Task name → Task Scheduler operational logs and XML definition
- Action path → file hash/signature and execution history
- Creator account → logon and privilege history
- Remote /s target → lateral movement scope
- Task execution time → child process/network activity

## Evidence to Collect

- schtasks command line
- Task name/path/XML
- Creator account
- Trigger and action
- Referenced executable/script
- Target host
- Task Scheduler event logs

## Decision Criteria

### Likely Benign

- Enterprise maintenance tasks
- Software updater tasks
- Backup/monitoring agents
- Approved administrative automation

### Suspicious

New/changed task invoking interpreters or user-writable paths, especially remotely or under privileged context.

### Incident Candidate

Task launches malicious content or is confirmed persistence/lateral movement on one or more hosts.

## Hunt → Detection Feedback

- Detect suspicious actions and remote /s usage
- Baseline enterprise task names/paths
- Correlate task creation with subsequent execution
- Require task XML collection in IR playbooks

Possible outcomes:

- new detection rule;
- tuning of an existing rule;
- new telemetry requirement;
- cyber-deception opportunity;
- IR/DFIR playbook update;
- architecture or control improvement.

## Limitations

- Field names and process schemas vary by vendor.
- Hunt queries require tenant-specific normalization before production use.
- Absence of a match does not prove absence of the behavior.
- Network/file pivots depend on telemetry retention and endpoint coverage.

## References

- https://attack.mitre.org/techniques/T1053/005/
- https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table
- https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax
