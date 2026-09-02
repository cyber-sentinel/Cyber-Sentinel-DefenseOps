# Lab Validation Standard

## Purpose

Q4 — **Lab Validated** means a detection or hunt has been exercised in a controlled, reproducible environment and produced the expected telemetry and result.

Q4 is stronger than syntax, parser, or synthetic-fixture validation. It must provide evidence that the behavior, telemetry pipeline, and defensive analytic work together.

## Required Lab Record

Every Q4 lab must document:

- Lab ID and linked detection/hunt IDs
- Objective and hypothesis
- Platform and operating-system version
- Telemetry source and version
- Collection configuration
- Engine/SIEM version
- Safe simulation method
- Exact expected events/fields
- Positive test
- Negative/control test
- Detection or hunt result
- False-positive observations
- Performance/volume observations where relevant
- Evidence artifacts
- Rollback/reset procedure
- Date and validator

## Safety Requirements

- Use controlled lab systems only.
- Use synthetic or benign simulations when they can reproduce the required telemetry.
- Do not use live credentials, production data, customer data, or uncontrolled malware.
- Network simulations must use reserved/test infrastructure or explicitly controlled destinations.
- Any destructive test requires an isolated disposable environment and documented reset procedure.

## Evidence Bundle

A Q4 evidence bundle should contain sanitized examples such as:

```text
labs/validation/<LAB-ID>/
├── README.md
├── environment.yaml
├── expected.md
├── telemetry/
│   ├── positive.json
│   └── negative.json
├── results/
│   ├── detection-output.txt
│   └── notes.md
└── reset.md
```

Do not commit secrets, real tokens, internal-only identifiers, or sensitive production telemetry.

## Promotion Gate: Q3 → Q4

A detection may be marked Q4 only when:

1. the simulation method is repeatable;
2. expected telemetry is actually observed;
3. the analytic matches the positive case;
4. the negative/control case does not produce an unacceptable result;
5. environment and engine versions are recorded;
6. evidence is retained in sanitized form;
7. limitations are documented.

## Q4 Is Not Q5/Q6

Lab validation does not make a detection universally production-ready.

Q5 additionally requires operational baseline, ownership, performance, response, and rollback planning.

Q6 is environment-specific production validation and must name the actual environment/version.
