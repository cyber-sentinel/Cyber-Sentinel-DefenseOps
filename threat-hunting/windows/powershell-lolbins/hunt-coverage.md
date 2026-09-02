# Threat Hunting Engine Coverage

## Primary Hunt Query Engines

| Engine / Language | Coverage | Notes |
|---|---:|---|
| Splunk SPL | 8/8 | Generic Windows process-field normalization; adapt index/sourcetype |
| Microsoft Kusto Query Language (KQL) | 8/8 | Microsoft Defender XDR `DeviceProcessEvents` |
| Elastic Kibana Query Language (KQL) | 8/8 | ECS process fields |
| Elastic Event Query Language (EQL) | 8/8 | ECS process events |
| Elastic ES|QL | 8/8 | Endpoint process data streams; adjust source pattern |
| OpenSearch Query DSL | 8/8 | ECS-style mapping assumed |
| CrowdStrike Falcon LogScale CQL | 8/8 | `ProcessRollup2`; schema validation required |
| SentinelOne Singularity PowerQuery | 8/8 | Tenant/schema validation required |
| Google SecOps YARA-L 2.0 | 8/8 | Broad UDM process-launch event filters |

## Adjunct / Conversion Engines

| Engine | Role in Hunting |
|---|---|
| Sigma | Hunt finding → portable detection candidate |
| Microsoft Defender XDR Custom Detection | Microsoft KQL hunt → scheduled/NRT detection |
| Wazuh XML | Hunt finding → Wazuh custom detection |
| YARA | File/memory artifact pivot |
| Suricata / Snort 3 | Network pivot and supporting detection |
| Zeek | Network behavioral pivot/notices |
| Falco | Used when hunts target Linux/container/runtime telemetry |

## Rule

Hunt coverage is based on observability, not on maximizing the number of translated files.
