# Validation Guide

## Objective

Validate detection logic without introducing unsafe activity into production.

## Preferred Validation Order

### 1. Static Validation

- Sigma YAML parses successfully.
- Required fields are present.
- ATT&CK technique is documented.
- SPL/KQL syntax is reviewed for the target platform.

### 2. Synthetic Telemetry Replay

Preferred for potentially disruptive LOLBin use cases.

Create or replay sanitized process-creation events containing the expected:

- process image
- parent process
- command line
- user
- host
- timestamp

Confirm that the rule matches the synthetic event and does not match the negative-control event.

### 3. Controlled Lab Execution

Only in an isolated lab or authorized test endpoint.

Use benign commands or artifacts designed solely to produce the required telemetry. Avoid fetching or executing untrusted remote content.

### 4. Baseline / Shadow Mode

Run as a non-blocking detection first.

Measure:

- events per day
- distinct hosts
- distinct users
- parent processes
- software-management systems
- known administrative automation

### 5. Production Candidate

Promote only after:

- expected telemetry coverage is confirmed
- false positives are documented
- owner and response action are defined
- alert severity is justified
- rollback procedure is tested

## Rollback

If a rule causes excessive volume or operational impact:

1. Disable the alert or correlation search.
2. Preserve the last known-good rule version.
3. Export a sample of triggering events.
4. Tune only with evidence-based exclusions.
5. Re-test before re-enabling.
