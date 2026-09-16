# Cyber-Sentinel-DefenseOps

**Production-Aware Cyber Defense Engineering — DEFEND**

[![Repository Hygiene](https://github.com/cyber-sentinel/Cyber-Sentinel-DefenseOps/actions/workflows/repository-hygiene.yml/badge.svg)](https://github.com/cyber-sentinel/Cyber-Sentinel-DefenseOps/actions/workflows/repository-hygiene.yml)
![Stable Release](https://img.shields.io/badge/release-v0.1.0-success)
![ATT&CK Mapped](https://img.shields.io/badge/MITRE%20ATT%26CK-mapped-informational)
![Multi-Engine](https://img.shields.io/badge/detection-multi--engine-informational)

[Cyber-Sentinel Ecosystem](https://github.com/cyber-sentinel)

Cyber-Sentinel-DefenseOps is the **DEFEND** layer of the Cyber-Sentinel ecosystem: a defensive-engineering product repository for building, validating, operating, and improving detections, threat hunts, response content, DFIR/IR material, deception-oriented controls, and security automation.

It is designed for security teams that need defensive content to be **reviewable, testable, evidence-backed, engine-aware, production-conscious, and reusable** rather than accumulated as isolated rule files.

> **Current maturity:** Stable baseline `v0.1.0`
> **Repository visibility:** Private during active development
> **Primary audience:** SOC, Detection Engineering, Threat Hunting, DFIR/IR, Security Engineering, Purple Team, and security platform teams
> **Operating posture:** Defensive use, controlled validation, explicit production constraints
> **Licensing note:** Repository visibility does not itself grant public reuse or redistribution rights

## Why DefenseOps Exists

Defensive content often fails between research and production: telemetry assumptions are undocumented, query languages are ambiguous, rules are copied without validation evidence, rollback is omitted, and syntactic correctness is mistaken for operational readiness.

DefenseOps addresses that gap by treating defensive content as an **engineering lifecycle** rather than a rule collection.

**Core question:** *What can we detect, validate, hunt, and defend — and what evidence supports that claim?*

## Product Value

DefenseOps is intended to help security teams:

- standardize Detection-as-Code and Hunt-as-Code practices;
- make telemetry prerequisites and coverage assumptions explicit;
- validate content with native engines where practical;
- separate syntax validation from behavioral validation and production validation;
- preserve false-positive, tuning, rollback, and deployment context;
- maintain portable, vendor-aware defensive engineering across multiple platforms;
- turn incident and hunting findings into measurable defensive improvements;
- provide controlled engineering content to the broader Cyber-Sentinel ecosystem.

## What DefenseOps Owns

DefenseOps owns the engineering lifecycle around:

- **detections** and detection packs;
- **threat hunts** and investigation queries;
- **validation assets**, fixtures, and conformance evidence;
- **response engineering** and operational control content;
- **DFIR/IR engineering material**;
- **cyber-deception content**;
- **security automation** and defensive workflow assets;
- **engine-aware implementation guidance**;
- **production constraints, rollback, reproducibility, and measurement**.

DefenseOps is **not**:

- the canonical cyber-defense knowledge graph or analyst knowledge platform — that is ATLAS;
- the repository for reusable operating procedures and playbooks — that is Skills;
- an unvalidated rule dump;
- a claim that CI-green content is automatically production-safe in every environment;
- a replacement for tenant-specific telemetry validation, change control, or analyst judgment.

## Current Stable Release

### `v0.1.0`

The current stable baseline establishes a formal quality and validation model across multiple defensive engines.

Validated baseline capabilities include:

- native Sigma validation with Sigma CLI;
- native YARA compilation with `yarac`;
- native Suricata configuration/rule validation;
- native Snort `3.12.2.0` rule validation;
- native Zeek `8.0.9` script validation;
- positive and negative synthetic detection fixtures;
- explicit engine-validation maturity levels;
- CI enforcement for detection and hunting packs.

Reference documentation:

- [Quality Model](./docs/quality-model.md)
- [Engine Validation Matrix](./docs/engine-validation-matrix.md)
- [Detection Engine & Language Registry](./docs/detection-engine-registry.md)
- [Changelog](./CHANGELOG.md)

## Validation Model

| Capability | Current Evidence | Quality Level |
|---|---|---:|
| Sigma rules | Sigma CLI / SigmaHQ strict validation | Q2 |
| YARA rules | Native `yarac` compilation | Q2 |
| Suricata rules | Native `suricata -T` validation | Q2 |
| Zeek scripts | Native Zeek `8.0.9` script load validation | Q2 |
| Snort 3 rules | Native Snort `3.12.2.0` `snort -T` validation | Q2 |
| Canonical Windows detection behavior | Positive + negative synthetic fixtures | Q3 |
| Threat-hunting content | Repository structural/content validation | Q1 |
| Vendor-specific SIEM/EDR queries | Static/schema-aware review | Q1 |

> **Quality gates are evidence, not universal deployment guarantees.** A passing repository check confirms the defined validation contract; it does not prove that every rule will behave identically across every customer tenant, data model, sensor version, or operating environment.

## Detection & Hunting Coverage

### Detection Packs

- [Windows PowerShell & LOLBins Detection Pack v0.3](./detections/windows/powershell-lolbins/) — multi-engine coverage across Sigma, Splunk SPL, Microsoft KQL, Microsoft Defender XDR Custom Detections, Elastic KQL/EQL/ES|QL/Query DSL, OpenSearch Query DSL, CrowdStrike Falcon LogScale CQL, SentinelOne STAR templates, Wazuh XML, Google SecOps YARA-L, YARA, Suricata, Snort 3, and Zeek where technically applicable.

### Threat Hunting Packs

- [Windows PowerShell & LOLBins Threat Hunting Engineering Pack v0.1](./threat-hunting/windows/powershell-lolbins/) — eight hypothesis-driven hunts with Splunk SPL, Microsoft KQL, Elastic KQL/EQL/ES|QL, OpenSearch Query DSL, CrowdStrike Falcon LogScale CQL, SentinelOne PowerQuery, Google SecOps YARA-L, investigation pivots, evidence collection, and Hunt → Detection feedback.

## Engineering Standard

Every substantive artifact should document, as applicable:

1. Objective and defensive use case
2. Threat or ATT&CK context
3. Required telemetry and prerequisites
4. Engine, platform, and query/rule language
5. Detection, hunt, deception, or response logic
6. Validation level and supporting evidence
7. Expected false positives, blind spots, and limitations
8. Production considerations and operational dependencies
9. Rollback, disable, or recovery procedure
10. References, attribution, and version history

The repository uses explicit engine and language names. Ambiguous labels such as **KQL** by itself are avoided because Microsoft Kusto Query Language, Elastic KQL, and other query dialects are not interchangeable.

## Content Lifecycle

```text
Design → Review → Test → Validate → Deploy → Measure → Tune → Retire
```

The lifecycle is evidence-driven. A syntactically valid rule is not automatically behaviorally validated, and a behaviorally validated rule is not automatically production-approved for every environment.

## Core Security Domains

DefenseOps is structured to support engineering work across:

- Security Operations & SOC
- Detection Engineering
- Threat Hunting
- Incident Response
- Digital Forensics & Incident Response
- Cyber Deception
- Security Architecture
- AppSec & DevSecOps
- AI Security & Defensive Automation

## Cyber-Sentinel Ecosystem

Cyber-Sentinel uses three contract-separated layers:

```text
Cyber-Sentinel
├── ATLAS       — KNOW   → Connect • Search • Investigate • Explain
├── DefenseOps  — DEFEND → Detect • Hunt • Validate • Respond • Automate
└── Skills      — APPLY  → Execute • Review • Reuse • Govern
```

### ATLAS — KNOW

[Cyber-Sentinel-Atlas](https://github.com/cyber-sentinel/Cyber-Sentinel-Atlas) owns governed cyber-defense knowledge, canonical relationships, deterministic retrieval, provenance, investigation context, verified offline knowledge delivery, and analyst-facing product interfaces.

DefenseOps may provide controlled defensive engineering content to ATLAS, but repository origin never grants canonical authority. ATLAS applies its own ingestion, provenance, licensing, validation, promotion, trust, and release boundaries.

### DefenseOps — DEFEND

DefenseOps owns the engineering artifacts used to detect, hunt, validate, respond, automate, and continuously improve defensive controls.

### Skills — APPLY

[Cyber-Sentinel-Skills](https://github.com/cyber-sentinel/Cyber-Sentinel-Skills) owns reusable operating procedures and playbooks for consistent execution by humans and, where appropriate, AI agents.

Skills may operationalize DefenseOps content, but it does not replace or silently redefine the detection, hunt, validation, or response engineering owned here.

### Operating Loop

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

## Security, Safety & Deployment Boundaries

This repository is intended for **authorized defensive security engineering, controlled validation, incident response, threat hunting, and security research**.

Before production deployment:

- validate telemetry availability and field mappings;
- review engine and platform versions;
- test expected positive and negative behavior;
- estimate false-positive and performance impact;
- define rollback or disable procedures;
- use normal organizational change control.

Do not treat repository content as automatic authorization to make production changes.

## Product Direction

The near-term direction is to expand evidence-backed defensive engineering while preserving the distinction between:

- portable defensive logic;
- engine-specific implementation;
- validation maturity;
- production readiness;
- operational procedure ownership.

The objective is a defensible engineering system that can support enterprise security operations without hiding assumptions behind vendor-specific syntax or undocumented analyst knowledge.

---

**Maintainer:** Ali RahimDabagh  
**Profile:** `cyber-sentinel`  
**Ecosystem role:** `DEFEND`  
**Focus:** Security Leadership • Cyber Defense Architecture • Detection Engineering • Threat Hunting • DFIR • Defensive Automation
