// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:rundll32\.exe)$/i OR ParentBaseFileName=/(?:winword\.exe|excel\.exe|outlook\.exe|powerpnt\.exe|mshta\.exe|wscript\.exe|cscript\.exe|cmd\.exe|powershell\.exe)$/i OR CommandLine=/(?:javascript:|vbscript:|http://|https://|\\appdata\\|\\temp\\|,#|control_rundll|mshtml)/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
