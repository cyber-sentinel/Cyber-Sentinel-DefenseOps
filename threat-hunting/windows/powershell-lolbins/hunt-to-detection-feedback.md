# Hunt → Detection Feedback Loop

## Purpose

A mature threat-hunting program should improve permanent defensive controls.

```text
Hypothesis
   ↓
Broad Hunt
   ↓
Suspicious Pattern
   ↓
Evidence & Validation
   ↓
┌────────────────────────────────────────────┐
│ Detection Rule / Tuning                    │
│ Telemetry Requirement                      │
│ Cyber Deception Opportunity                │
│ IR / DFIR Playbook Update                  │
│ Architecture / Hardening Improvement       │
└────────────────────────────────────────────┘
   ↓
Measure & Re-hunt
```

## Promotion Criteria

Promote a hunt finding into a detection when:

- the observable is stable and measurable;
- telemetry coverage is sufficient;
- false positives can be bounded;
- severity and response ownership are defined;
- the detection can be validated with positive and negative tests;
- rollback/disable procedures are documented.

## Do Not Promote Yet When

- the signal requires heavy analyst interpretation;
- field coverage is inconsistent;
- legitimate prevalence is unknown;
- the observable is purely contextual;
- no safe response path exists.

## Output Types

Each hunt should finish with one or more of:

1. **No finding** — document coverage and blind spots.
2. **Baseline finding** — record expected administrative behavior.
3. **Detection candidate** — create/tune a rule.
4. **Telemetry gap** — request additional logging.
5. **Incident candidate** — escalate into THIR/DFIR.
6. **Deception candidate** — place a decoy/lure around the observed behavior.
7. **Architecture finding** — reduce attack surface or improve control design.
