# Cyber-Sentinel Product Roadmap

## Current

### Cyber-Sentinel-DefenseOps

- Multi-engine Windows PowerShell & LOLBins detection pack
- Threat hunting engineering pack
- Repository quality model
- Sigma/YARA/Suricata/Snort 3/Zeek native validation
- Positive/negative detection fixtures
- Stable baseline: `v0.1.0`

## Next: Cyber-Sentinel-Atlas Product Architecture

DefenseOps v0.1.0 is the validated engineering baseline. Major DefenseOps content expansion pauses while the Atlas product architecture and MVP foundation are designed.

## Strategic Product: Cyber-Sentinel-Atlas

Atlas is the planned signature project.

### Product goals

1. Internationally useful cyber defense reference and analyst platform.
2. Fast search across events, TTPs, technologies, artifacts and detections.
3. Modern and accessible UI.
4. Offline-first capability.
5. Structured source citations and update provenance.
6. Knowledge graph across ATT&CK, D3FEND, CAR, telemetry and detections.
7. API and CLI interfaces.
8. AI assistance that is grounded in source-backed content.

### Initial content domains

- Windows and Sysmon
- Active Directory
- PowerShell
- Exchange and SharePoint
- Linux
- Docker and Kubernetes
- AWS, Azure and Google Cloud
- SQL Server, MongoDB, MariaDB and other data platforms
- Detection Engineering
- Threat Hunting
- DFIR
- Incident Response

## Sequence

```text
DefenseOps identity stabilized
        ↓
DefenseOps v0.1.0 stable baseline
        ↓
Atlas product architecture
        ↓
Atlas MVP
        ↓
DefenseOps ↔ Atlas integration
        ↓
Atlas API / CLI
        ↓
Expand DFIR / IR / Deception / Cloud content
```
