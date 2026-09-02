# Cyber-Sentinel-DefenseOps Architecture

## Role in the Cyber-Sentinel Ecosystem

Cyber-Sentinel-DefenseOps is the **open defensive engineering layer**.

Cyber-Sentinel-Atlas is planned as the **global knowledge, search, investigation and analyst-experience layer**.

```text
                  Cyber-Sentinel
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
     DefenseOps                    Atlas
 Open Engineering Core      Intelligence / UX Platform
          │                           │
          ├─ Detections               ├─ Global Search
          ├─ Threat Hunts             ├─ Knowledge Graph
          ├─ Validation               ├─ Investigation Workspace
          ├─ DFIR                     ├─ Offline/PWA/Desktop
          ├─ Incident Response        ├─ AI-assisted navigation
          ├─ Deception                ├─ API
          └─ Automation               └─ CLI
```

## Design Goals

DefenseOps is organized by defensive capability rather than vendor. This prevents the repository from becoming a product-specific collection and keeps artifacts portable across security stacks.

## Capability Model

```text
Threat / Risk
    ↓
Telemetry & Intelligence
    ↓
Detect ── Deceive ── Hunt
    ↓         ↓        ↓
Triage ─ Investigate ─ Respond
    ↓
Lessons Learned
    ↓
Architecture / Detection / Automation Improvement
```

## Separation of Concerns

- **Domains** describe professional security capabilities.
- **Technologies** are implementation mechanisms.
- **Artifacts** are reproducible engineering outputs.
- **Labs** validate assumptions before production adoption.
- **DefenseOps** owns open defensive content and validation evidence.
- **Atlas** will own discovery, navigation, knowledge relationships, analyst workflows, offline access, API and CLI experiences.
