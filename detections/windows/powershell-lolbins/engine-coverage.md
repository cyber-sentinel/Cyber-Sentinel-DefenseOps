# Detection Engine Coverage Matrix — v0.3

## Endpoint / SIEM / Platform-Native Engines

| Engine | Current Pack Status |
|---|---|
| Sigma | Native — 8/8 |
| Splunk SPL | Native — 8/8 |
| Microsoft Kusto Query Language (KQL) | Native — 8/8 |
| Microsoft Defender XDR Custom Detection | Native wrapper over Microsoft KQL — 8/8 metadata |
| Elastic Kibana Query Language (KQL) | Native — 8/8 |
| Elastic Event Query Language (EQL) | Native — 8/8 |
| Elastic ES|QL | Native — 8/8 |
| Elasticsearch Query DSL | Native — 8/8 |
| OpenSearch Query DSL | Native, mapping-dependent — 8/8 |
| CrowdStrike Falcon LogScale CQL | Native, Falcon schema-dependent — 8/8 |
| SentinelOne STAR / Singularity PowerQuery | Native template, tenant-schema validation required — 8/8 |
| Wazuh XML Custom Rules | Native for Sysmon Event ID 1 — 8/8 |
| Google SecOps YARA-L 2.0 | Native UDM process-event rules — 8/8 |

## Artifact / Network / Runtime Engines

| Engine | Status | Rationale |
|---|---|---|
| YARA | Adjunct | Detects supporting files/memory artifacts, not Windows command-line telemetry itself |
| Suricata | Adjunct | HTTP/network visibility for selected retrieval patterns |
| Snort 3 | Adjunct | HTTP/network visibility for selected retrieval patterns |
| Zeek | Adjunct | HTTP behavioral notices for selected retrieval patterns |
| Falco | N/A in this pack | Windows process pack; Falco belongs in Linux/container/runtime packs |

## Design Rule

Coverage count is never prioritized over technical correctness. An engine is omitted or marked N/A when it cannot observe the behavior faithfully.
