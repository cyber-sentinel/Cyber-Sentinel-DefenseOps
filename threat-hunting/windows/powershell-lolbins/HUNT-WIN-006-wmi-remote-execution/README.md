# HUNT-WIN-006 — WMI / WMIC Remote Process Execution

**Status:** Experimental Hunt
**Platform:** Windows
**ATT&CK:** [T1047 — Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047/)
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If an adversary abuses WMI for local or remote execution, telemetry should expose wmic.exe remote process creation or suspicious children of WmiPrvSE.exe, including on systems where the legacy WMIC client is absent.

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

- wmic.exe with /node: and process call create
- Suspicious process spawned by WmiPrvSE.exe
- Remote administration outside approved management infrastructure
- Same user targeting multiple hosts
- Execution followed by discovery, credential access, or lateral movement

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

- Source user/host → authentication and remote-service telemetry
- WmiPrvSE child → command line, hash, network activity
- Target host → other lateral movement signals
- Account → privilege and logon history
- Remote execution time window → SMB/RPC/WinRM/DCOM telemetry

## Evidence to Collect

- WMIC command line where present
- WmiPrvSE child process
- Source/target host
- Account/logon context
- Remote services/RPC telemetry
- Child file/network activity

## Decision Criteria

### Likely Benign

- Legacy systems management
- Approved administration and inventory tools

### Suspicious

Remote WMI from non-management hosts, unusual account, or WmiPrvSE spawning interpreters/LOLBins.

### Incident Candidate

Remote WMI is unauthorized and tied to payload execution, credential compromise, or lateral movement.

## Hunt → Detection Feedback

- Do not depend only on wmic.exe
- Add WmiPrvSE child analytics
- Baseline management subnets/accounts
- Correlate logon + WMI + child process telemetry

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

- https://attack.mitre.org/techniques/T1047/
- https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table
- https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax
