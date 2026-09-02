# Validation Labs

This directory stores reproducible evidence used to promote Cyber-Sentinel-DefenseOps artifacts toward Q4 — Lab Validated.

## Naming

Use:

`LAB-<PLATFORM>-<NNN>`

Examples:

- `LAB-WIN-001`
- `LAB-LINUX-001`
- `LAB-AZURE-001`
- `LAB-K8S-001`

## Standard

Follow:

- [`docs/lab-validation-standard.md`](../../docs/lab-validation-standard.md)
- [`lab-validation-template.md`](./lab-validation-template.md)

## Evidence Rules

- Commit only synthetic or sanitized evidence.
- Never commit production credentials, secrets, tokens, internal-only IP inventories, or customer data.
- Record exact platform, telemetry, and engine versions.
- Include both positive and negative/control behavior when feasible.
- Preserve reset/rollback instructions.
