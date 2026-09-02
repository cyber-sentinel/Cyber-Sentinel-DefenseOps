# Compatibility & Validation Evidence

This file records the concrete engine/runtime versions used to validate Cyber-Sentinel-DefenseOps artifacts.

## Release Candidate Baseline

| Component | Version / Channel | Validation |
|---|---|---|
| Snort 3 | 3.12.2.0 | Version-pinned native `snort -T` validation in `openeuler/snort3:3.12.2.0-oe2403sp4`; runtime version is asserted in CI |
| Zeek | 8.0.9 | Native script load/compile using pinned `zeek/zeek:8.0.9` image |
| Suricata | Ubuntu 24.04 packaged runtime | Native `suricata -T` validation |
| YARA | Ubuntu 24.04 packaged runtime | Native `yarac` compilation |
| Sigma | Sigma CLI + SigmaHQ validators | Strict rule/metadata validation |

## Evidence Policy

- Versions must be visible in CI logs or pinned in workflow definitions.
- A passing parser/compiler establishes Q2 only for the tested runtime/version.
- Vendor SaaS platforms remain tenant/schema dependent until tested against a compatible tenant.
- Compatibility claims must not be generalized beyond the recorded version family without evidence.

## Upgrade Procedure

When a validation engine changes major/minor version:

1. update the pinned version;
2. run all native validation jobs;
3. record breaking or behavior changes;
4. re-run positive/negative fixtures where applicable;
5. update the Engine Validation Matrix;
6. only then expand the compatibility claim.
