# Threat Hunting Engineering Standard

## Core Principle

A detection asks: **Should this event alert?**

A hunt asks: **What evidence would exist if this behavior were occurring, and what relationships distinguish malicious activity from normal operations?**

## Lifecycle

`Hypothesis → Scope → Query → Baseline → Pivot → Validate → Conclude → Improve Controls`

## Query Naming

Never use ambiguous language labels.

Examples:

- Microsoft Kusto Query Language (KQL)
- Elastic Kibana Query Language (KQL)
- Elastic Event Query Language (EQL)
- Elastic ES|QL
- CrowdStrike Falcon LogScale CQL

## Hunt Classification

- **Exploratory** — broad behavioral search.
- **Targeted** — threat/TTP-specific search.
- **Triggered** — initiated from an alert, intelligence, or incident.
- **Validation** — tests whether telemetry/detections cover a behavior.

## Required Hunt Outputs

- findings;
- evidence;
- scope;
- confidence;
- blind spots;
- detection opportunities;
- telemetry gaps;
- IR/DFIR escalation criteria.
