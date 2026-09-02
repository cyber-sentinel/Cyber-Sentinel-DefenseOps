# HUNT-WIN-005 — Regsvr32 Scriptlet / COM Proxy Execution

**Status:** Experimental Hunt  
**Platform:** Windows  
**ATT&CK:** [T1218.010 — System Binary Proxy Execution: Regsvr32](https://attack.mitre.org/techniques/T1218/010/)  
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If regsvr32.exe is abused to proxy code or scriptlet execution, telemetry should show suspicious /i or /u usage, scrobj.dll, remote SCT content, unusual DLL paths, or network/module activity inconsistent with routine registration.

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

- scrobj.dll with /i or -i arguments
- Remote .sct or URL argument
- DLL/OCX from temporary or user-writable locations
- Unusual parent process
- Outbound network activity by regsvr32

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

- Remote SCT/URL → network and DNS telemetry
- DLL/OCX → hash, signature, YARA, module load
- Parent process → initial access/execution chain
- COM registration/persistence → registry telemetry
- Same command line or artifact → enterprise prevalence

## Evidence to Collect

- Regsvr32 command line
- Parent process
- Referenced SCT/DLL/OCX
- Network destinations
- Module loads
- Registry modifications
- File hashes/signatures

## Decision Criteria

### Likely Benign

- Software installation and COM registration
- Approved application maintenance

### Suspicious

Remote scriptlet, scrobj.dll, unusual /i usage, or unsigned content from non-standard paths.

### Incident Candidate

Malicious scriptlet/DLL is confirmed or regsvr32 activity is linked to persistence, C2, or payload execution.

## Hunt → Detection Feedback

- Correlate process + module load + network
- Baseline legitimate registration paths
- Add registry follow-up analytics
- Preserve high-severity remote scriptlet detection

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

- https://attack.mitre.org/techniques/T1218/010/
- https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table
- https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax
