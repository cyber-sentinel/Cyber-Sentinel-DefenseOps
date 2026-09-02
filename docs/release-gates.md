# DefenseOps Stable Release Gates

This checklist defines the minimum evidence required before promoting Cyber-Sentinel-DefenseOps from a release candidate to a stable release.

## v0.1.0 Required Gates

### Repository Integrity

- [x] Repository Hygiene passes on the release commit.
- [x] No secret-bearing filenames or committed credentials.
- [x] UTF-8 and trailing-whitespace checks pass.
- [x] Canonical repository name and links use `Cyber-Sentinel-DefenseOps`.

### Detection Quality

- [x] Detection pack structural validation passes.
- [x] Sigma CLI / SigmaHQ strict validation passes.
- [x] YARA compiles with `yarac`.
- [x] Suricata accepts the network rules with `suricata -T`.
- [x] Snort 3 accepts the Snort 3 rules with `snort -T`.
- [x] Zeek loads the Zeek notice script with the pinned runtime.
- [x] Positive/negative canonical fixtures pass for all eight current Windows detections.

### Hunting Quality

- [x] Threat-hunting structural/content validation passes.
- [x] Query language names are explicit; ambiguous `KQL` naming is prohibited.

### Evidence & Documentation

- [x] Engine/runtime versions are recorded in `docs/compatibility-evidence.md`.
- [x] Validation levels are consistent with `docs/quality-model.md`.
- [x] Q4 lab-validation standard and reusable lab template exist.
- [x] `CHANGELOG.md` describes the stable release delta.
- [x] `VERSION` is updated to `0.1.0` only after all mandatory gates pass.

## Non-Blocking for v0.1.0

The following are intentionally not required for the first stable release:

- Q4 lab validation of every artifact;
- Q5 production-candidate status;
- Q6 production validation;
- tenant-native execution in every commercial SIEM/EDR platform.

Those validation levels must be earned and documented incrementally rather than implied.

## Stable Release Rule

If a mandatory gate fails, the release remains a release candidate.
