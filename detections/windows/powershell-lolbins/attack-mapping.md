# MITRE ATT&CK Mapping

| Detection | Technique | Defensive Rationale |
|---|---|---|
| DET-WIN-001 | T1059.001 PowerShell | Detect encoded PowerShell execution frequently used to obscure command content. |
| DET-WIN-002 | T1059.001 PowerShell | Detect PowerShell command lines containing common network retrieval primitives. |
| DET-WIN-003 | T1218.005 Mshta | Detect trusted mshta.exe used with remote URLs or script protocols. |
| DET-WIN-004 | T1218.011 Rundll32 | Detect rundll32.exe with script-protocol or remote-content indicators. |
| DET-WIN-005 | T1218.010 Regsvr32 | Detect regsvr32 scriptlet/scrobj patterns associated with proxy execution. |
| DET-WIN-006 | T1047 Windows Management Instrumentation | Detect WMIC remote process creation through `/node:` and process call create. |
| DET-WIN-007 | T1053.005 Scheduled Task | Detect task creation with suspicious interpreters or user-writable paths. |
| DET-WIN-008 | T1569.002 Service Execution | Detect PsExec/PSEXESVC process execution consistent with remote service execution. |

## Notes

ATT&CK mapping describes adversary behavior, not proof of malicious intent. A match must be triaged with user, host, parent-process, asset criticality, and surrounding telemetry.
