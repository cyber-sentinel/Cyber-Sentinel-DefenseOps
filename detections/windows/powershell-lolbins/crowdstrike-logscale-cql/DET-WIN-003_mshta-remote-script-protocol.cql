// CrowdStrike Falcon LogScale — CrowdStrike Query Language (CQL)
// Falcon process telemetry using ProcessRollup2.
#event_simpleName=ProcessRollup2 event_platform=Win ImageFileName=/\\mshta\.exe$/i
| CommandLine=/(https?:\/\/|javascript:|vbscript:)/i
| table([@timestamp, aid, ComputerName, UserName, ImageFileName, CommandLine], limit=1000)
