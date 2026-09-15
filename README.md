# Cyber-Sentinel-DefenseOps

**Open Cyber Defense Operations Engineering — DEFEND**

[![Repository Hygiene](https://github.com/cyber-sentinel/Cyber-Sentinel-DefenseOps/actions/workflows/repository-hygiene.yml/badge.svg)](https://github.com/cyber-sentinel/Cyber-Sentinel-DefenseOps/actions/workflows/repository-hygiene.yml)
![Stable Release](https://img.shields.io/badge/release-v0.1.0-success)
![ATT&CK Mapped](https://img.shields.io/badge/MITRE%20ATT%26CK-mapped-informational)
![Multi-Engine](https://img.shields.io/badge/detection-multi--engine-informational)

[Cyber-Sentinel Profile](https://github.com/cyber-sentinel)

Cyber-Sentinel-DefenseOps is the **DEFEND** layer of the Cyber-Sentinel ecosystem: a defensive-engineering repository focused on reusable, testable, production-aware detections, threat hunts, validation assets, response engineering, DFIR/IR material, deception-oriented content, and defensive automation.

> **Repository visibility:** Private during active development. The word “Open” describes the vendor-neutral engineering approach; repository visibility alone does not grant a public license.

## Mission

Turn cyber-defense knowledge into engineering artifacts that can be reviewed, tested, measured, validated, automated, and operated in real environments.

**Core question:** *What can we detect, validate, hunt, and defend?*

## Product Position

DefenseOps is **not**:

- the canonical knowledge graph or analyst knowledge platform — that is Atlas;
- the repository for reusable operational procedures and playbooks — that is Skills;
- a dump of unvalidated detection rules;
- a SIEM-specific content collection;
- a claim that CI-green content is automatically production-safe everywhere.

DefenseOps owns the engineering lifecycle around defensive content: telemetry requirements, detection logic, hunting logic, validation evidence, response engineering, production constraints, rollback, reproducibility, and measurement.

## Cyber-Sentinel Ecosystem

Cyber-Sentinel is intentionally a **contract-separated ecosystem** with three current project layers:

```text
Cyber-Sentinel
├── Atlas       — KNOW   → Connect • Search • Investigate • Explain
├── DefenseOps  — DEFEND → Detect • Hunt • Validate • Respond • Automate
└── Skills      — APPLY  → Execute • Review • Reuse • Govern
```

### Atlas — KNOW

[Cyber-Sentinel-Atlas](https://github.com/cyber-sentinel/Cyber-Sentinel-Atlas) owns governed cyber-defense knowledge, canonical relationships, deterministic retrieval, provenance, investigation context, offline knowledge delivery, and analyst-facing product interfaces.

DefenseOps can provide controlled defensive content to Atlas, but repository origin alone never grants canonical authority. Atlas applies its own ingestion, provenance, licensing, validation, promotion, and release boundaries before any DefenseOps-derived content becomes trusted Atlas knowledge.

### DefenseOps — DEFEND

DefenseOps owns defensive engineering artifacts and their validation lifecycle:

- detections and detection packs;
- threat-hunting content;
- validation assets and synthetic fixtures;
- response engineering;
- DFIR/IR engineering material;
- cyber-deception content;
- security automation;
- engine-aware implementation guidance;
- production constraints, rollback, and measurement.

### Skills — APPLY

[Cyber-Sentinel-Skills](https://github.com/cyber-sentinel/Cyber-Sentinel-Skills) owns reusable, vendor-neutral operational procedures and playbooks for humans and AI agents.

Skills may operationalize DefenseOps artifacts as repeatable procedures, but it does not replace the underlying detection, hunt, validation, or response engineering owned here.

### Ecosystem Operating Loop

```text
Authoritative Sources / Telemetry / Security Knowledge
                         │
                         ▼
                  ATLAS — KNOW
        Connect • Search • Investigate • Explain
                         │
             evidence / defensive context
                         ▼
               DefenseOps — DEFEND
       Detect • Hunt • Validate • Respond • Automate
                         │
              repeatable operating method
                         ▼
                  Skills — APPLY
          Execute • Review • Reuse • Govern
                         │
                         ▼
          VALIDATE → AUTOMATE → EVOLVE
                         │
                         └──────────────↺
                    feedback into knowledge,
                 engineering and procedures
```

`VALIDATE`, `AUTOMATE`, and `EVOLVE` are operating outcomes and feedback stages, not separate repositories.

`KNOW → DEFEND → APPLY → VALIDATE → AUTOMATE → EVOLVE`

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

```text
Design → Review → Test → Validate → Deploy → Measure → Tune → Retire
```

The lifecycle is evidence-driven. A rule or query becoming syntactically valid is not equivalent to production validation.

## Safety

This repository is intended for authorized defensive security engineering, controlled laboratories, detection validation, incident response, and security research.

Do not deploy untested content directly to production environments.

---

**Maintainer:** Ali RahimDabagh  
**Profile:** `cyber-sentinel`  
**Focus:** Information Security Management & Cyber Defense Architecture
