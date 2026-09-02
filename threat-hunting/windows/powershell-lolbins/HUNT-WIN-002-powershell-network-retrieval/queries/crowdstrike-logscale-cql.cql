// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:powershell\.exe|pwsh\.exe)$/i OR ParentBaseFileName=/(?:winword\.exe|excel\.exe|outlook\.exe|mshta\.exe|wscript\.exe|cscript\.exe|cmd\.exe)$/i OR CommandLine=/(?:invoke-webrequest|downloadstring|downloadfile|system\.net\.webclient|start-bitstransfer|curl |wget |http://|https://)/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
