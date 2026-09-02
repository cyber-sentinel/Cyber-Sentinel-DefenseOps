# Detection Engine & Language Registry

This document is the naming authority for Cyber-Sentinel-DefenseOps.

## Rule

Never write an ambiguous engine label such as **KQL** by itself.

Always identify both the platform/vendor context and the language or rule format.

## Registered Engines and Languages

| Canonical Label | Platform / Engine | Language / Format | Primary Use |
|---|---|---|---|
| Sigma | Portable | Sigma YAML | Cross-SIEM behavioral detection |
| Splunk SPL | Splunk | Search Processing Language (SPL) | SIEM search/detection |
| Microsoft Kusto Query Language (KQL) | Microsoft Defender XDR / Sentinel | Kusto Query Language | Hunting and analytics |
| Microsoft Defender XDR Custom Detection | Microsoft Defender XDR | Microsoft KQL + detection metadata | Scheduled/NRT custom detections |
| Elastic Kibana Query Language (KQL) | Elastic / Kibana | Kibana Query Language | Filtering/search |
| Elastic Event Query Language (EQL) | Elastic | EQL | Event/sequence detection |
| Elastic ES|QL | Elastic | Elasticsearch Query Language (ES|QL) | Piped analytics/search |
| Elasticsearch Query DSL | Elasticsearch | JSON Query DSL | Native search/detection backend |
| OpenSearch Query DSL | OpenSearch | JSON Query DSL | OpenSearch search/detection |
| CrowdStrike Falcon LogScale CQL | CrowdStrike Falcon LogScale | CrowdStrike Query Language (CQL) | Search/detection analytics |
| SentinelOne STAR Custom Rule | SentinelOne Singularity | Singularity Data Lake PowerQuery / STAR | Endpoint custom detection/response |
| Wazuh XML Custom Rule | Wazuh | XML ruleset | HIDS/XDR custom detection |
| Google SecOps YARA-L 2.0 | Google Security Operations | YARA-L 2.0 | SIEM detection/correlation |
| YARA | YARA engine | YARA rule | File/memory artifact detection |
| Suricata | Suricata | Suricata rule syntax | Network IDS/IPS |
| Snort 3 | Snort | Snort 3 rule syntax | Network IDS/IPS |
| Zeek Notice/Script | Zeek | Zeek scripting language | Network analytics/notices |
| Falco | Falco | Falco YAML rules | Linux/container/runtime detection |

## Applicability Principle

Not every use case must have every engine.

Use:

- **Native** when the engine directly observes the behavior.
- **Adjunct** when the engine contributes supporting evidence.
- **Template / Schema-dependent** when vendor field schemas or tenant versions must be validated before production use.
- **N/A** when translation would be technically misleading.
