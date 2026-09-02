# HUNT-WIN-008 — PsExec / Service-Based Remote Execution

**Status:** Experimental Hunt
**Platform:** Windows
**ATT&CK:** [T1569.002 — System Services: Service Execution](https://attack.mitre.org/techniques/T1569/002/)
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If an adversary uses PsExec or temporary Windows services for remote execution, telemetry should show PsExec/PSEXESVC artifacts or services.exe spawning unusual command interpreters and payloads in a lateral-movement context.

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

- PsExec client or PSEXESVC process
- services.exe spawning cmd/PowerShell or uncommon payloads
- Remote service creation near administrative share access
- Privileged account used across multiple hosts
- Temporary service followed by payload execution

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

- Source user/host → authentication events and admin-share access
- Service name/image path → service creation telemetry
- services.exe child → command line, hash, network activity
- Account → spread across target hosts
- Target host → additional lateral movement or credential access

## Evidence to Collect

- PsExec/PSEXESVC process telemetry
- services.exe child process
- Service creation/configuration
- Source/target host
- User/logon data
- SMB/admin-share activity
- Payload hash/path

## Decision Criteria

### Likely Benign

- Approved systems administration
- Software deployment
- Remote support
- Authorized incident response

### Suspicious

Use from non-management hosts, unusual privileged identity, rare target set, or service spawning interpreters/payloads.

### Incident Candidate

Unauthorized service execution, compromised admin identity, or confirmed lateral movement/payload execution.

## Hunt → Detection Feedback

- Separate approved admin tooling by source/identity
- Correlate service creation + process execution + logon
- Detect services.exe spawning suspicious interpreters
- Add response playbook for credential containment and host isolation

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

- https://attack.mitre.org/techniques/T1569/002/
- https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table
- https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax
