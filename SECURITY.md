# Security Policy

## Reporting a Security Issue

Do not disclose a security-sensitive issue publicly if it could expose credentials, infrastructure details, exploitable configuration, or unsafe defensive logic.

When reporting an issue, include:

- affected file or component
- impact
- reproduction conditions
- safe proof of concept where applicable
- recommended remediation

## Repository Safety Principles

- No real credentials, tokens, secrets, internal IP addressing, or customer data.
- No production-sensitive evidence should be committed.
- Detection and response content must be reviewed before production deployment.
- Examples should use synthetic or sanitized data.
- Offensive techniques may be referenced only to support defensive detection, investigation, validation, or mitigation.

## Production Warning

Repository content is provided as engineering reference material. Validate in a lab or staging environment before production use and maintain a rollback path.
