// CrowdStrike Falcon LogScale — CrowdStrike Query Language (CQL)
// Falcon process telemetry using ProcessRollup2.
#event_simpleName=ProcessRollup2 event_platform=Win ImageFileName=/\\schtasks\.exe$/i
| CommandLine=/\/create/i
| CommandLine=/(powershell|pwsh|cmd\s+\/c|mshta|rundll32|regsvr32|\\AppData\\|\\Temp\\)/i
| table([@timestamp, aid, ComputerName, UserName, ImageFileName, CommandLine], limit=1000)
