# HUNT-WIN-004 — Rundll32 Proxy Execution & Suspicious DLL Invocation

**Status:** Experimental Hunt
**Platform:** Windows
**ATT&CK:** [T1218.011 — System Binary Proxy Execution: Rundll32](https://attack.mitre.org/techniques/T1218/011/)
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If rundll32.exe is abused for proxy execution, command lines, DLL paths, export syntax, parents, and follow-on activity should expose executions that differ from known operating-system and application baselines.

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

- Script protocol or remote content in command line
- DLL loaded from AppData/Temp/user profile
- Ordinal export execution such as ,#N
- Office/script-host parent process
- Rare DLL/export combination for the endpoint

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

- DLL path → hash, signature, reputation, YARA
- Parent → initial execution chain
- Child process → payload behavior
- Network activity → remote infrastructure
- Same DLL/export → prevalence across enterprise

## Evidence to Collect

- Full command line
- Referenced DLL/CPL path
- DLL hash/signature
- Parent/child process chain
- Network telemetry
- Module load telemetry when available

## Decision Criteria

### Likely Benign

- Control Panel operations
- Vendor software using signed DLLs
- Known application shell extensions

### Suspicious

User-writable DLL path, remote/script protocol, unusual parent, or rare export/ordinal invocation.

### Incident Candidate

Referenced module is malicious/untrusted or rundll32 is part of confirmed persistence, execution, or C2 activity.

## Hunt → Detection Feedback

- Create allowlists by signed DLL path/export, not by rundll32 alone
- Add module-load correlation
- Detect user-writable DLL execution and script-protocol variants

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

- https://attack.mitre.org/techniques/T1218/011/
- https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table
- https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax
