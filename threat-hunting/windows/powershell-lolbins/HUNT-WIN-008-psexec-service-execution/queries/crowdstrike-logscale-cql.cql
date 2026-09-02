// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:psexec\.exe|psexec64\.exe|psexesvc\.exe)$/i OR ParentBaseFileName=/(?:services\.exe)$/i OR CommandLine=/(?:psexec|psexesvc|cmd\.exe|powershell\.exe|pwsh\.exe|\\admin\$|\\ipc\$)/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
