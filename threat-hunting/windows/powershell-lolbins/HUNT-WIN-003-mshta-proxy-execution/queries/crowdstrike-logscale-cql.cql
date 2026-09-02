// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:mshta\.exe)$/i OR ParentBaseFileName=/(?:winword\.exe|excel\.exe|outlook\.exe|powerpnt\.exe|chrome\.exe|msedge\.exe|firefox\.exe|wscript\.exe|cscript\.exe)$/i OR CommandLine=/(?:http://|https://|javascript:|vbscript:|\.hta|\.sct)/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
