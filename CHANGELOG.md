# Changelog

All notable changes to Cyber-Sentinel-DefenseOps are documented here.

The project follows a release-candidate-first model: a green CI run is necessary but does not automatically imply production readiness.

## [Unreleased]

### Planned

- reproducible Q4 lab-validation evidence;
- broader platform coverage;
- additional vendor-native validation where compatible test environments exist.

## [0.1.0] — 2026-09-02

### Stable Baseline

- all mandatory DefenseOps v0.1.0 release gates satisfied;
- Repository Hygiene passes;
- Sigma CLI / SigmaHQ strict validation passes;
- YARA native compilation passes;
- Suricata native `-T` validation passes;
- Snort 3.12.2.0 native `snort -T` validation passes;
- Zeek 8.0.9 native script validation passes;
- positive/negative fixtures pass for all eight current Windows detections;
- threat-hunting validation passes;
- compatibility evidence and Q4 lab-validation standards are documented.

### Scope Boundary

Stable means the repository's defined v0.1.0 quality gates are satisfied. It does not imply Q5/Q6 or universal validation in every vendor tenant.

## [0.1.0-rc.2] — 2026-09-02

### Added

- native Zeek 8.0.9 validation;
- version-pinned Snort 3.12.2.0 validation workflow;
- compatibility/version evidence;
- Q4 lab-validation standard and reusable lab template;
- explicit stable-release gates.

### Changed

- corrected Snort 3 rule-file comment syntax after native engine validation exposed the issue;
- optimized native engine validation to use version-pinned runtimes.

### Status

- Zeek: Q2 Engine Validated.
- Snort 3: Q2 Engine Validated after version-pinned `snort -T` pass.

## [0.1.0-rc.1] — 2026-09-02

### Added

- formal Q0–Q6 repository quality model;
- engine validation matrix;
- positive and negative synthetic fixtures for all eight Windows PowerShell/LOLBin detections;
- canonical fixture test harness;
- Windows PowerShell & LOLBins multi-engine detection pack;
- Windows PowerShell & LOLBins threat-hunting engineering pack;
- explicit Microsoft KQL vs Elastic KQL naming;
- Cyber-Sentinel DefenseOps / Atlas brand architecture and roadmap.

### Validation

- Sigma CLI / SigmaHQ strict validation;
- YARA compilation with `yarac`;
- native Suricata `-T` rule validation;
- detection-pack structural validation;
- threat-hunting structural validation;
- UTF-8 and trailing-whitespace repository hygiene checks.

### Changed

- repository identity repositioned from Cyber-Sentinel-Forge to Cyber-Sentinel-DefenseOps;
- Sigma rule filenames and ATT&CK tactic metadata aligned with SigmaHQ validation expectations;
- public documentation now distinguishes static, engine, fixture, lab, and production validation.

### Notes

Vendor-native content for Microsoft Defender XDR, SentinelOne, CrowdStrike, Google SecOps, Wazuh, Elastic, OpenSearch, and similar platforms remains deployment/schema dependent until validated against a compatible runtime or tenant.
