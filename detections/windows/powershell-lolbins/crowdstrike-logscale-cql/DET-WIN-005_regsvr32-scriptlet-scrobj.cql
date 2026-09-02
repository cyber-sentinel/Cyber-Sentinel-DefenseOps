// CrowdStrike Falcon LogScale — CrowdStrike Query Language (CQL)
// Falcon process telemetry using ProcessRollup2.
#event_simpleName=ProcessRollup2 event_platform=Win ImageFileName=/\\regsvr32\.exe$/i
| CommandLine=/scrobj\.dll/i
| CommandLine=/(\/i:|-i:)/i
| table([@timestamp, aid, ComputerName, UserName, ImageFileName, CommandLine], limit=1000)
