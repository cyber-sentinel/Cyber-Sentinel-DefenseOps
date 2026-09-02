# HUNT-WIN-001 — PowerShell Suspicious Execution & Post-Execution Activity

**Status:** Experimental Hunt
**Platform:** Windows
**ATT&CK:** [T1059.001 — Command and Scripting Interpreter: PowerShell](https://attack.mitre.org/techniques/T1059/001/)
**Linked Detection Pack:** [Windows PowerShell & LOLBins Detection Pack](../../../detections/windows/powershell-lolbins/)

## Hypothesis

If an adversary abuses PowerShell for execution, obfuscation, download, or living-off-the-land activity, process telemetry should show anomalous command-line features, unusual parent processes, or follow-on child/network activity that deviates from the host and user baseline.

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

- Encoded or obfuscated PowerShell switches
- Execution-policy bypass or hidden-window execution
- Network retrieval primitives
- Office, script-host, browser, or LOLBin parent processes
- Unusual user/host combinations or first-seen command lines
- Follow-on child processes, file writes, or outbound connections

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

- ProcessUniqueId / PID → child processes and network connections
- Parent process → originating Office document, browser, script host, or LOLBin
- User → other PowerShell activity on the same and peer hosts
- Remote URL/IP → DNS, proxy, firewall, Zeek, Suricata, or EDR network telemetry
- Downloaded file hash/path → file creation, reputation, YARA, and execution

## Evidence to Collect

- Full PowerShell command line
- Parent and grandparent process
- ProcessUniqueId/PID and creation time
- User/logon context
- Network destinations and DNS
- Files created or modified
- PowerShell Script Block/Module logs when available

## Decision Criteria

### Likely Benign

- Enterprise administration scripts
- Configuration management
- Software deployment/bootstrap automation
- Signed internal PowerShell tooling

### Suspicious

Multiple suspicious command-line primitives, rare parent process, first-seen command, or unexpected external network activity.

### Incident Candidate

PowerShell plus confirmed malicious payload, credential access, persistence, lateral movement, or unapproved outbound communication.

## Hunt → Detection Feedback

- Promote stable command-line patterns to detection rules
- Add parent-child correlation
- Require Script Block Logging where coverage is weak
- Add network/file correlation for PowerShell retrieval
- Create allowlists only for validated automation identities and paths

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
