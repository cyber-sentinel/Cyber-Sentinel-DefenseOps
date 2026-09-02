// CrowdStrike Falcon LogScale CQL — hunt query.
// Validate field names against the target Falcon dataset.
#event_simpleName=ProcessRollup2 event_platform=Win
| (ImageFileName=/(?:schtasks\.exe)$/i OR ParentBaseFileName=/(?:cmd\.exe|powershell\.exe|wmic\.exe|psexec\.exe|psexesvc\.exe|services\.exe)$/i OR CommandLine=/(?:/create|/change|/s |powershell|pwsh|cmd /c|mshta|rundll32|regsvr32|\\appdata\\|\\temp\\)/i)
| table([@timestamp, aid, ComputerName, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=2000)
