// CrowdStrike Falcon LogScale — CrowdStrike Query Language (CQL)
// Falcon process telemetry using ProcessRollup2.
#event_simpleName=ProcessRollup2 event_platform=Win ImageFileName=/\\wmic\.exe$/i
| CommandLine=/\/node:/i
| CommandLine=/process/i
| CommandLine=/call/i
| CommandLine=/create/i
| table([@timestamp, aid, ComputerName, UserName, ImageFileName, CommandLine], limit=1000)
