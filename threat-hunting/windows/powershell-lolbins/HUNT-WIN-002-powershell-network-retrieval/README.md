# HUNT-WIN-002 — PowerShell Network Retrieval & Follow-on Execution

**Status:** Experimental Hunt
**Platform:** Windows
**ATT&CK:** [T1059.001 — Command and Scripting Interpreter: PowerShell](https://attack.mitre.org/techniques/T1059/001/)
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If PowerShell retrieves remote content for adversary execution, process telemetry should expose network-retrieval primitives and nearby network/file/process events that can reconstruct the download-to-execution chain.

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

- PowerShell retrieval cmdlets or .NET WebClient usage
- HTTP/HTTPS indicators embedded in the command line
- Suspicious parent process preceding retrieval
- Outbound network events initiated by PowerShell
- File creation followed by execution from user-writable paths

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

- PowerShell process → DeviceNetworkEvents / EDR network events
- Remote URL/domain → DNS, proxy, Zeek, Suricata, Snort
- Destination file → hash, signature, YARA, subsequent process creation
- Same user → other retrieval activity during the hunt window
- Same remote infrastructure → other hosts contacting the destination

## Evidence to Collect

- Command line
- Remote URL/domain/IP
- Destination file path and hash
- HTTP metadata when visible
- Parent process
- Child execution
- Proxy/DNS/firewall records

## Decision Criteria

### Likely Benign

- Software installation scripts
- Approved package/bootstrap scripts
- Administrative downloads from internal repositories

### Suspicious

PowerShell retrieves content from a rare or untrusted destination, especially from an unusual parent or into a user-writable location.

### Incident Candidate

Retrieved content is malicious or executed, or the destination is confirmed hostile/unapproved and scope extends to additional hosts.

## Hunt → Detection Feedback

- Add reputation/context enrichment
- Correlate process + network + file telemetry
- Create destination/path-based tuning criteria
- Add Suricata/Snort/Zeek adjunct detections where HTTP visibility exists

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

- https://attack.mitre.org/techniques/T1059/001/
- https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table
- https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax
