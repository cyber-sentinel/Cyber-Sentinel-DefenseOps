// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:powershell\.exe|pwsh\.exe)$/i OR ParentBaseFileName=/(?:winword\.exe|excel\.exe|outlook\.exe|powerpnt\.exe|mshta\.exe|wscript\.exe|cscript\.exe|rundll32\.exe|chrome\.exe|msedge\.exe|firefox\.exe)$/i OR CommandLine=/(?:-encodedcommand| -enc |executionpolicy bypass|windowstyle hidden|invoke-webrequest|downloadstring|downloadfile|webclient|start-bitstransfer|invoke-expression| iex )/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
