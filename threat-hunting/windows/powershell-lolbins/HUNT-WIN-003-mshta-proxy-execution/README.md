# HUNT-WIN-003 — Mshta Trusted Binary Proxy Execution

**Status:** Experimental Hunt  
**Platform:** Windows  
**ATT&CK:** [T1218.005 — System Binary Proxy Execution: Mshta](https://attack.mitre.org/techniques/T1218/005/)  
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If an adversary abuses mshta.exe to proxy script or HTA execution, telemetry should reveal remote/script-protocol arguments, unusual parents, network access, or follow-on processes inconsistent with legitimate HTA use.

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

- Remote URL or HTA path in mshta command line
- Inline javascript: or vbscript: protocol
- Office/browser/script-host parent process
- Outbound network communication from mshta
- Child process execution after mshta

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

- Mshta process → remote URL and network session
- Parent process → document/browser origin
- HTA/SCT artifact → file hash, YARA, script content
- Child process → PowerShell, cmd, rundll32, regsvr32, or payload execution
- Remote domain → other affected endpoints

## Evidence to Collect

- Mshta command line
- Parent process chain
- Remote URL/domain/IP
- HTA/SCT content if captured
- Child processes
- File writes
- User context

## Decision Criteria

### Likely Benign

- Legacy line-of-business HTA applications
- Approved internal HTA automation

### Suspicious

Remote HTA/script-protocol execution, unexpected user context, or uncommon parent/child relationships.

### Incident Candidate

Remote content is malicious, mshta launches a payload, or the infrastructure is linked to broader compromise.

## Hunt → Detection Feedback

- Detect remote/script-protocol mshta
- Baseline approved HTA paths/domains
- Correlate mshta network events and child processes
- Add YARA/network adjunct coverage

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

- https://attack.mitre.org/techniques/T1218/005/
- https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table
- https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax
