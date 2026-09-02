# Microsoft Defender XDR Custom Detections

Microsoft Defender XDR Custom Detection is a **platform-native detection mechanism**, not a separate query language.

The detection queries in this pack are written in **Microsoft Kusto Query Language (KQL)** and stored under `../microsoft-kql/`.

The manifest in this directory documents rule metadata, severity, ATT&CK mapping, and the query file used by each custom detection.

Before enabling a custom detection:

- run the Microsoft KQL query in Advanced Hunting;
- confirm `Timestamp`, `DeviceId`, and `ReportId` are returned for Defender for Endpoint telemetry;
- baseline alert volume;
- start alert-only;
- add automated response only after validation and rollback planning.
