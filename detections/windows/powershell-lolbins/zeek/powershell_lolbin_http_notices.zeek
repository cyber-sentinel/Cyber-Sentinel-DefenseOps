@load base/frameworks/notice

module CyberSentinel;

export {
    redef enum Notice::Type += {
        PowerShell_HTTP_User_Agent,
        HTA_HTTP_Retrieval,
        SCT_HTTP_Retrieval,
    };
}

event http_header(c: connection, is_orig: bool, original_name: string, name: string, value: string)
    {
    if ( is_orig && name == "USER-AGENT" && /[Pp]ower[Ss]hell/ in value )
        NOTICE([$note=PowerShell_HTTP_User_Agent,
                $msg=fmt("PowerShell-like HTTP User-Agent from %s to %s", c$id$orig_h, c$id$resp_h),
                $src=c$id$orig_h,
                $dst=c$id$resp_h]);
    }

event http_request(c: connection, method: string, original_URI: string, unescaped_URI: string, version: string)
    {
    if ( /\.[Hh][Tt][Aa]([?#].*)?$/ in unescaped_URI )
        NOTICE([$note=HTA_HTTP_Retrieval,
                $msg=fmt("HTA retrieval over HTTP: %s", unescaped_URI),
                $src=c$id$orig_h,
                $dst=c$id$resp_h]);

    if ( /\.[Ss][Cc][Tt]([?#].*)?$/ in unescaped_URI )
        NOTICE([$note=SCT_HTTP_Retrieval,
                $msg=fmt("SCT scriptlet retrieval over HTTP: %s", unescaped_URI),
                $src=c$id$orig_h,
                $dst=c$id$resp_h]);
    }
