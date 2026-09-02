# Detection Test Fixtures

Each detection has:

- `positive.json` — synthetic events that **must match** the canonical behavioral logic.
- `negative.json` — benign/control events that **must not match**.

These fixtures test semantic intent independently from vendor field mapping.

They are not malware samples and do not execute any offensive behavior.
