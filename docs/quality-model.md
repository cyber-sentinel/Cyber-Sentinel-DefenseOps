# Cyber-Sentinel Repository Quality Model

## Purpose

Cyber-Sentinel content must distinguish between **authored**, **statically checked**, **engine validated**, and **production validated** artifacts.

A rule existing in the repository does not imply that it has been proven in every vendor tenant or production environment.

## Validation Levels

| Level | Label | Meaning |
|---|---|---|
| Q0 | Draft | Content exists but has not passed repository checks. |
| Q1 | Static Validated | Syntax/schema/metadata checks pass in repository CI. |
| Q2 | Engine Validated | The native engine/compiler/parser accepts the artifact. |
| Q3 | Fixture Validated | Positive and negative synthetic fixtures behave as expected. |
| Q4 | Lab Validated | Reproducible execution in a controlled lab produces the expected telemetry and result. |
| Q5 | Production Candidate | Baseline, false positives, ownership, performance, and rollback are documented. |
| Q6 | Production Validated | Validated in a specific production environment. This label must name the environment/version and must never be implied globally. |

## Current Policy

- Sigma, YARA, and Suricata should reach Q2 where CI can run the native tooling.
- Canonical behavioral logic should reach Q3 with synthetic positive/negative fixtures.
- Microsoft Defender XDR, SentinelOne, CrowdStrike, Google SecOps, Wazuh, Elastic, and OpenSearch artifacts may require tenant/version-specific validation before claiming Q2/Q4.
- Vendor-specific content must state schema assumptions.
- No artifact may be called production-ready solely because CI is green.

## Evidence Required for Promotion

### Q1 → Q2

- Native parser/compiler/engine command runs successfully.
- Tool version is visible in CI logs.

### Q2 → Q3

- Positive fixture matches.
- Negative control does not match.
- Test is reproducible in CI.

### Q3 → Q4

- Lab architecture is documented.
- Telemetry source and version are documented.
- Expected event fields are captured.
- Test procedure is safe and repeatable.

### Q4 → Q5

- False-positive baseline is documented.
- Severity and response ownership are defined.
- Operational impact is assessed.
- Rollback/disable path is tested.
