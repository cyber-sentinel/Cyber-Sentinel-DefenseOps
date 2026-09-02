# Cyber-Sentinel Product Roadmap

## Current

### Cyber-Sentinel-DefenseOps

- Multi-engine Windows PowerShell & LOLBins detection pack
- Threat hunting engineering pack
- Repository quality model
- Sigma/YARA/Suricata native validation
- Positive/negative detection fixtures
- Release candidate: `v0.1.0-rc.1`

## Next: DefenseOps v0.1.0

- finish release-candidate verification;
- improve native validation coverage where practical;
- formalize compatibility/version evidence;
- refine repository presentation;
- publish first stable release when quality gates are satisfied.

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
DefenseOps rename/reposition
        ↓
DefenseOps v0.1.0 hardening
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
