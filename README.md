# Cyber-Sentinel-DefenseOps

**Open Cyber Defense Operations Engineering**

[![Repository Hygiene](https://github.com/cyber-sentinel/Cyber-Sentinel-DefenseOps/actions/workflows/repository-hygiene.yml/badge.svg)](https://github.com/cyber-sentinel/Cyber-Sentinel-DefenseOps/actions/workflows/repository-hygiene.yml)
![Stable Release](https://img.shields.io/badge/release-v0.1.0-success)
![ATT&CK Mapped](https://img.shields.io/badge/MITRE%20ATT%26CK-mapped-informational)
![Multi-Engine](https://img.shields.io/badge/detection-multi--engine-informational)

[Cyber-Sentinel Profile](https://github.com/cyber-sentinel)

Cyber-Sentinel-DefenseOps is the open engineering core of the Cyber-Sentinel ecosystem, focused on reusable, testable, production-aware detections, hunts, validation assets, response content, and defensive automation.

## Mission

Turn cyber defense knowledge into engineering artifacts that can be reviewed, tested, measured, automated, and operationalized.

## Ecosystem Position

```text
Cyber-Sentinel
├── DefenseOps  → open defensive engineering content, validation, hunts, detections and automation
└── Atlas       → planned global cyber defense intelligence, search and analyst platform
```

DefenseOps is intentionally content- and engineering-first. Cyber-Sentinel-Atlas will consume curated DefenseOps knowledge through web, offline, API, and CLI interfaces rather than duplicating it.

## Current Stable Release

`v0.1.0`

The first stable baseline establishes a formal quality and validation model:

- native Sigma validation with Sigma CLI;
- native YARA compilation with `yarac`;
- native Suricata configuration/rule validation;
- native Snort 3.12.2.0 rule validation;
- native Zeek 8.0.9 script validation;
- positive and negative synthetic detection fixtures;
- explicit engine-validation maturity levels;
- CI enforcement for detection and hunting packs.

See:

- [Quality Model](./docs/quality-model.md)
- [Engine Validation Matrix](./docs/engine-validation-matrix.md)
- [Changelog](./CHANGELOG.md)

## Validation Snapshot

| Capability | Current Evidence | Quality Level |
|---|---|---:|
| Sigma rules | Sigma CLI / SigmaHQ strict validation | Q2 |
| YARA rules | Native `yarac` compilation | Q2 |
| Suricata rules | Native `suricata -T` validation | Q2 |
| Zeek scripts | Native Zeek 8.0.9 script load validation | Q2 |
| Snort 3 rules | Native Snort 3.12.2.0 `snort -T` validation | Q2 |
| Canonical Windows detection behavior | Positive + negative synthetic fixtures | Q3 |
| Threat-hunting content | Repository structural/content validation | Q1 |
| Vendor-specific SIEM/EDR queries | Static/schema-aware review | Q1 |

> CI green means repository quality gates passed. It does not imply universal production validation across every vendor tenant or deployment.

## Core Domains

- Security Operations & SOC
- Threat Hunting & Incident Response (THIR)
- Detection Engineering & Cyber Deception
- Digital Forensics & Incident Response (DFIR)
- Security Architecture
- AppSec & DevSecOps
- AI Security & Automation

## Detection Engineering Standard

Cyber-Sentinel-DefenseOps uses explicit engine/language names. Ambiguous labels such as **KQL** by itself are not used.

See [Detection Engine & Language Registry](./docs/detection-engine-registry.md).

## Detection Packs

- [Windows PowerShell & LOLBins Detection Pack v0.3](./detections/windows/powershell-lolbins/) — multi-engine coverage across Sigma, Splunk SPL, Microsoft KQL, Microsoft Defender XDR Custom Detections, Elastic KQL/EQL/ES|QL/Query DSL, OpenSearch Query DSL, CrowdStrike Falcon LogScale CQL, SentinelOne STAR templates, Wazuh XML, Google SecOps YARA-L, YARA, Suricata, Snort 3, and Zeek where technically applicable.

## Threat Hunting Packs

- [Windows PowerShell & LOLBins Threat Hunting Engineering Pack v0.1](./threat-hunting/windows/powershell-lolbins/) — 8 hypothesis-driven hunts with Splunk SPL, Microsoft KQL, Elastic KQL/EQL/ES|QL, OpenSearch Query DSL, CrowdStrike Falcon LogScale CQL, SentinelOne PowerQuery, Google SecOps YARA-L, investigation pivots, evidence collection, and Hunt → Detection feedback.

## Engineering Standard

Every substantive artifact should document:

1. Objective and defensive use case
2. Threat or ATT&CK context
3. Required telemetry / prerequisites
4. Engine, platform, and language
5. Detection, hunt, deception, or response logic
6. Validation level and evidence
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
