/*
  Cyber-Sentinel-Forge
  Windows PowerShell & LOLBins artifact adjunct rules.
  These rules scan files or memory artifacts; they do not replace endpoint process telemetry.
*/

rule CyberSentinel_PowerShell_Encoded_Command_Artifact
{
    meta:
        author = "Ali RahimDabagh (Cyber-Sentinel)"
        description = "Detects script or memory artifacts containing encoded PowerShell execution and decoding primitives."
        attack = "T1059.001"
        status = "experimental"

    strings:
        $enc1 = "-EncodedCommand" ascii wide nocase
        $enc2 = "-enc " ascii wide nocase
        $b64_1 = "FromBase64String" ascii wide nocase
        $b64_2 = "[Convert]::" ascii wide nocase
        $exec1 = "Invoke-Expression" ascii wide nocase
        $exec2 = "IEX(" ascii wide nocase

    condition:
        filesize < 5MB and
        (1 of ($enc*) and 1 of ($b64*)) and
        (1 of ($exec*) or 2 of ($b64*))
}

rule CyberSentinel_PowerShell_Network_Retrieval_Artifact
{
    meta:
        author = "Ali RahimDabagh (Cyber-Sentinel)"
        description = "Detects PowerShell script or memory artifacts containing multiple network retrieval primitives."
        attack = "T1059.001"
        status = "experimental"

    strings:
        $net1 = "Invoke-WebRequest" ascii wide nocase
        $net2 = "DownloadString" ascii wide nocase
        $net3 = "DownloadFile" ascii wide nocase
        $net4 = "System.Net.WebClient" ascii wide nocase
        $net5 = "Start-BitsTransfer" ascii wide nocase
        $exec1 = "Invoke-Expression" ascii wide nocase
        $exec2 = "IEX(" ascii wide nocase

    condition:
        filesize < 5MB and
        2 of ($net*) and
        (1 of ($exec*) or 3 of ($net*))
}

rule CyberSentinel_HTA_Script_Execution_Artifact
{
    meta:
        author = "Ali RahimDabagh (Cyber-Sentinel)"
        description = "Detects HTA-like script artifacts containing script-host and shell execution indicators."
        attack = "T1218.005"
        status = "experimental"

    strings:
        $hta = "<hta:application" ascii wide nocase
        $activex = "ActiveXObject" ascii wide nocase
        $wscript = "WScript.Shell" ascii wide nocase
        $shell = "Shell.Application" ascii wide nocase
        $powershell = "powershell" ascii wide nocase

    condition:
        filesize < 5MB and
        $hta and $activex and
        1 of ($wscript, $shell, $powershell)
}

rule CyberSentinel_Scriptlet_Scrobj_Artifact
{
    meta:
        author = "Ali RahimDabagh (Cyber-Sentinel)"
        description = "Detects scriptlet/scrobj-style artifacts that can support regsvr32 proxy execution."
        attack = "T1218.010"
        status = "experimental"

    strings:
        $scriptlet = "<scriptlet" ascii wide nocase
        $registration = "<registration" ascii wide nocase
        $scrobj = "scrobj.dll" ascii wide nocase
        $jscript = "JScript" ascii wide nocase
        $vbscript = "VBScript" ascii wide nocase

    condition:
        filesize < 5MB and
        2 of ($scriptlet, $registration, $scrobj) and
        1 of ($jscript, $vbscript)
}
