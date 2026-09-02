# Engine Validation Matrix

This matrix describes **validation capability**, not marketing coverage.

| Engine / Language | Repository Validation | Current Target | Production Caveat |
|---|---|---|---|
| Sigma | Sigma CLI / pySigma checks | Q2 | Backend field mappings still require deployment-specific validation |
| YARA | `yarac` compilation | Q2 | Artifact quality still requires representative samples |
| Suricata | `suricata -T` with repository rules | Q2 | Network visibility and protocol configuration vary |
| Snort 3 | Version-pinned native `snort -T` CI | Q1 → Q2 pending final pass | Q2 applies only after the pinned runtime accepts the repository rules |
| Zeek | Native script load with Zeek 8.0.9 | Q2 | Validate again when changing Zeek major/minor versions |
| Splunk SPL | Static/reviewed query | Q1 | Index, sourcetype, CIM, and field names vary |
| Microsoft Kusto Query Language (KQL) | Static/reviewed query | Q1 | Defender/Sentinel table and tenant schema validation required |
| Microsoft Defender XDR Custom Detection | Metadata + Microsoft KQL linkage | Q1 | Tenant execution and custom-detection constraints required |
| Elastic Kibana Query Language (KQL) | Static/reviewed query | Q1 | ECS/data-view mapping required |
| Elastic Event Query Language (EQL) | Static/reviewed query | Q1 | ECS and event category mapping required |
| Elastic ES|QL | Static/reviewed query | Q1 | Data stream/version validation required |
| Elasticsearch Query DSL | JSON structure validation | Q1 | Mapping/version validation required |
| OpenSearch Query DSL | JSON structure validation | Q1 | Mapping/version validation required |
| CrowdStrike Falcon LogScale CQL | Static/schema-aware template | Q1 | Falcon tenant schema validation required |
| SentinelOne STAR / PowerQuery | Static/schema-aware template | Q1 | Singularity tenant schema and STAR validation required |
| Wazuh XML Custom Rules | XML structure and custom-ID checks | Q1 | Wazuh manager/ruleset version validation required |
| Google SecOps YARA-L 2.0 | Static structure checks | Q1 | Google SecOps rule compiler/UDM validation required |
| Falco | N/A for current Windows pack | — | Used for Linux/container/runtime packs |

## Rule

A green GitHub Action badge means the repository quality gates passed. It does **not** mean every vendor-native rule has been executed in every commercial platform.
