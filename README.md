# Cyber-Sentinel-Forge

**Flagship Cyber Defense Engineering Lab**

[![Repository Hygiene](https://github.com/cyber-sentinel/Cyber-Sentinel-Forge/actions/workflows/repository-hygiene.yml/badge.svg)](https://github.com/cyber-sentinel/Cyber-Sentinel-Forge/actions/workflows/repository-hygiene.yml)
![Release Candidate](https://img.shields.io/badge/release-v0.1.0--rc.1-informational)
![ATT&CK Mapped](https://img.shields.io/badge/MITRE%20ATT%26CK-mapped-informational)
![Multi-Engine](https://img.shields.io/badge/detection-multi--engine-informational)

[Cyber-Sentinel Profile](https://github.com/cyber-sentinel)

Cyber-Sentinel-Forge is a practical cyber defense engineering repository focused on building reusable, testable, and production-aware defensive security content.

## Mission

Turn cyber defense knowledge into engineering artifacts that can be reviewed, tested, measured, and operationalized.

## Current Release Candidate

`v0.1.0-rc.1`

The release candidate introduces a formal quality model:

- native Sigma validation with Sigma CLI;
- native YARA compilation with `yarac`;
- native Suricata configuration/rule validation;
- positive and negative synthetic detection fixtures;
- explicit engine-validation maturity levels;
- CI enforcement for detection and hunting packs.

See:

- [Quality Model](./docs/quality-model.md)
- [Engine Validation Matrix](./docs/engine-validation-matrix.md)

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
