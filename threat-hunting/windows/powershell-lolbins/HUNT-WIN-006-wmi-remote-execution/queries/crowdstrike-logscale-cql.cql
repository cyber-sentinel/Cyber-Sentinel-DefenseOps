// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:wmic\.exe)$/i OR ParentBaseFileName=/(?:wmiprvse\.exe)$/i OR CommandLine=/(?:/node:|process call create|process | call | create )/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
