# Windows PowerShell & LOLBins Detection Pack v0.3

This pack provides multi-engine defensive detections for high-signal Windows command execution and LOLBin abuse patterns.

## Use Cases

| ID | Use Case | ATT&CK |
|---|---|---|
| DET-WIN-001 | PowerShell Encoded Command | T1059.001 |
| DET-WIN-002 | PowerShell Network Download Pattern | T1059.001 |
| DET-WIN-003 | Mshta Remote or Script-Protocol Execution | T1218.005 |
| DET-WIN-004 | Rundll32 Suspicious Script or Remote Execution | T1218.011 |
| DET-WIN-005 | Regsvr32 Scriptlet or Scrobj Abuse | T1218.010 |
| DET-WIN-006 | WMIC Remote Process Creation | T1047 |
| DET-WIN-007 | Suspicious Scheduled Task Creation | T1053.005 |
| DET-WIN-008 | PsExec or PSEXESVC Execution | T1569.002 |

## Engine Layout

### Portable / SIEM / Endpoint

- `sigma/` — Sigma YAML
- `splunk-spl/` — Splunk Search Processing Language (SPL)
- `microsoft-kql/` — Microsoft Kusto Query Language (KQL), targeting Defender XDR `DeviceProcessEvents`
- `microsoft-defender-custom-detection/` — Defender XDR custom-detection metadata referencing Microsoft KQL
- `elastic-kql/` — Elastic Kibana Query Language (KQL)
- `elastic-eql/` — Elastic Event Query Language (EQL)
- `elastic-esql/` — Elastic Elasticsearch Query Language (ES|QL)
- `elastic-query-dsl/` — Elasticsearch Query DSL
- `opensearch-query-dsl/` — OpenSearch Query DSL
- `crowdstrike-logscale-cql/` — CrowdStrike Falcon LogScale CQL
- `sentinelone-star/` — SentinelOne Singularity PowerQuery templates suitable for STAR promotion after validation
- `wazuh-xml/` — Wazuh XML custom rules
- `google-secops-yara-l/` — Google Security Operations YARA-L 2.0

### Artifact / Network / Runtime

- `yara/` — file/memory adjunct rules
- `suricata/` — network adjunct rules
- `snort3/` — Snort 3 network adjunct rules
- `zeek/` — Zeek network notices/scripts
- `falco/` — registered engine; N/A for this Windows process pack, used in Linux/container packs

See:

- [Engine Coverage](./engine-coverage.md)
- [Global Engine Registry](../../../docs/detection-engine-registry.md)
- [Naming Convention](../../../docs/detection-naming-convention.md)

## Telemetry

Recommended endpoint telemetry:

- Sysmon Event ID 1
- Windows Security Event ID 4688 with command-line auditing
- Microsoft Defender XDR `DeviceProcessEvents`
- Elastic Endpoint / ECS-compatible process events
- CrowdStrike Falcon process telemetry (`ProcessRollup2`)
- SentinelOne Singularity process-creation telemetry
- Wazuh-decoded Sysmon process telemetry

Network adjunct engines require network visibility and do not replace endpoint telemetry.

## Production Standard

Before promotion from `experimental` to a production candidate:

1. Validate syntax in the target engine.
2. Validate field/schema mappings in the actual tenant.
3. Replay synthetic or sanitized positive and negative telemetry.
4. Baseline event volume for 7–14 days where practical.
5. Document false positives and evidence-based exclusions.
6. Define alert ownership and response action.
7. Test rollback/disable procedures.
