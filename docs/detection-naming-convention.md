# Detection Naming Convention

## Folder Names

Use explicit platform/language names:

- `sigma/`
- `splunk-spl/`
- `microsoft-kql/`
- `microsoft-defender-custom-detection/`
- `elastic-kql/`
- `elastic-eql/`
- `elastic-esql/`
- `elastic-query-dsl/`
- `opensearch-query-dsl/`
- `crowdstrike-logscale-cql/`
- `sentinelone-star/`
- `wazuh-xml/`
- `google-secops-yara-l/`
- `yara/`
- `suricata/`
- `snort3/`
- `zeek/`
- `falco/`

## Prohibited Ambiguity

Do not use:

- `kql/`
- “KQL rule”
- “EQL rule” without Elastic context when context is unclear
- “CQL” without CrowdStrike Falcon LogScale context in user-facing documentation

Preferred wording:

- **Microsoft Kusto Query Language (KQL)**
- **Elastic Kibana Query Language (KQL)**
- **Elastic Event Query Language (EQL)**
- **CrowdStrike Falcon LogScale CQL**
