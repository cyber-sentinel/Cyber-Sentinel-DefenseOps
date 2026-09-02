# DefenseOps Stable Release Gates

This checklist defines the minimum evidence required before promoting Cyber-Sentinel-DefenseOps from a release candidate to a stable release.

## v0.1.0 Required Gates

### Repository Integrity

- [ ] Repository Hygiene passes on the release commit.
- [ ] No secret-bearing filenames or committed credentials.
- [ ] UTF-8 and trailing-whitespace checks pass.
- [ ] Canonical repository name and links use `Cyber-Sentinel-DefenseOps`.

### Detection Quality

- [ ] Detection pack structural validation passes.
- [ ] Sigma CLI / SigmaHQ strict validation passes.
- [ ] YARA compiles with `yarac`.
- [ ] Suricata accepts the network rules with `suricata -T`.
- [ ] Snort 3 accepts the Snort 3 rules with `snort -T`.
- [ ] Zeek loads the Zeek notice script with the pinned runtime.
- [ ] Positive/negative canonical fixtures pass for all eight current Windows detections.

### Hunting Quality

- [ ] Threat-hunting structural/content validation passes.
- [ ] Query language names are explicit; ambiguous `KQL` naming is prohibited.

### Evidence & Documentation

- [ ] Engine/runtime versions are recorded in `docs/compatibility-evidence.md`.
- [ ] Validation levels are consistent with `docs/quality-model.md`.
- [ ] Q4 lab-validation standard and reusable lab template exist.
- [ ] `CHANGELOG.md` describes the stable release delta.
- [ ] `VERSION` is updated to `0.1.0` only after all mandatory gates pass.

## Non-Blocking for v0.1.0

The following are intentionally not required for the first stable release:

- Q4 lab validation of every artifact;
- Q5 production-candidate status;
- Q6 production validation;
- tenant-native execution in every commercial SIEM/EDR platform.

Those validation levels must be earned and documented incrementally rather than implied.

## Stable Release Rule

If a mandatory gate fails, the release remains a release candidate.
