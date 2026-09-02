# Contributing

Contributions should improve defensive value, reproducibility, technical accuracy, or operational usability.

## Contribution Requirements

A contribution should include:

- clear defensive objective
- prerequisites and telemetry requirements
- ATT&CK mapping where relevant
- validation steps
- false-positive / limitation analysis
- production impact
- rollback or disable guidance
- sanitized examples

## Naming

Use lowercase, descriptive, hyphen-separated filenames.

Example:

```text
detect-suspicious-powershell-child-process.yaml
```

## Review Standard

Content may be rejected if it:

- cannot be safely reproduced
- lacks defensive context
- contains sensitive data
- makes unsupported detection claims
- has no validation approach
- creates unacceptable production risk without controls
