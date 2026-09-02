// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:regsvr32\.exe)$/i OR ParentBaseFileName=/(?:winword\.exe|excel\.exe|outlook\.exe|mshta\.exe|wscript\.exe|cscript\.exe|powershell\.exe|cmd\.exe)$/i OR CommandLine=/(?:scrobj\.dll|/i:|-i:|/u |http://|https://|\.sct|\\appdata\\|\\temp\\)/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
