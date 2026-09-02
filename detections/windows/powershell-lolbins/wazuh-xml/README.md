# Wazuh XML Custom Rules

These rules target **Sysmon Event ID 1 process-creation telemetry** decoded by Wazuh.

Key assumptions:

- parent group: `sysmon_event1`
- image field: `win.eventdata.image`
- command-line field: `win.eventdata.commandLine`
- custom rule IDs use the Wazuh-recommended custom range `100000–120000`

Production procedure:

1. Validate on a test Wazuh manager.
2. Use `wazuh-logtest` with sanitized events.
3. Confirm field names against the deployed Wazuh version/ruleset.
4. Deploy to a staging rule file under `/var/ossec/etc/rules/`.
5. Restart the manager only after syntax validation and keep a rollback copy.
