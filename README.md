# Cyber-Sentinel-Forge

**Flagship Cyber Defense Engineering Lab**

[Cyber-Sentinel Profile](https://github.com/cyber-sentinel) • `Bootstrap v0.1`

Cyber-Sentinel-Forge is a practical cyber defense engineering repository focused on building reusable, testable, and production-aware defensive security content.

## Mission

Turn cyber defense knowledge into engineering artifacts that can be reviewed, tested, measured, and operationalized.

## Core Domains

- Security Operations & SOC
- Threat Hunting & Incident Response (THIR)
- Detection Engineering & Cyber Deception
- Digital Forensics & Incident Response (DFIR)
- Security Architecture
- AppSec & DevSecOps
- AI Security & Automation

## Detection Engineering Standard

Cyber-Sentinel-Forge uses explicit engine/language names. Ambiguous labels such as **KQL** by itself are not used.

See [Detection Engine & Language Registry](./docs/detection-engine-registry.md).

## Detection Packs

- [Windows PowerShell & LOLBins Detection Pack v0.3](./detections/windows/powershell-lolbins/) — multi-engine coverage across Sigma, Splunk SPL, Microsoft KQL, Microsoft Defender XDR Custom Detections, Elastic KQL/EQL/ES|QL/Query DSL, OpenSearch Query DSL, CrowdStrike Falcon LogScale CQL, SentinelOne STAR templates, Wazuh XML, Google SecOps YARA-L, YARA, Suricata, Snort 3, and Zeek where technically applicable.

## Engineering Standard

Every substantive artifact should document:

1. Objective and defensive use case
2. Threat or ATT&CK context
3. Required telemetry / prerequisites
4. Engine, platform, and language
5. Detection, hunt, deception, or response logic
6. Validation procedure
7. Expected false positives / limitations
8. Production considerations
9. Rollback or disable procedure
10. References and version history

## Content Lifecycle

`Design → Review → Test → Validate → Deploy → Measure → Tune → Retire`

## Safety

This repository is intended for authorized defensive security engineering, controlled laboratories, detection validation, incident response, and security research.

Do not deploy untested content directly to production environments.

---

**Maintainer:** Ali RahimDabagh
**Profile:** `cyber-sentinel`
**Focus:** Information Security Management & Cyber Defense Architecture
