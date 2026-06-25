# Incident Severity Classification Matrix

## Overview

Use this matrix to consistently classify incident severity. Severity drives response urgency, staffing requirements, communication scope, and escalation paths.

**Rule of thumb:** If any single dimension meets the criteria for a higher severity, classify at that higher severity. When in doubt, round up and reclassify down once impact is understood.

---

## Severity Definitions

### SEV-1: Critical

**Service is completely unavailable or a critical business function is non-operational for all or most users.**

| Dimension | Criteria |
|-----------|----------|
| **User Impact** | All or majority of users cannot complete core workflows. Service is fully unavailable or returning errors for primary functionality. |
| **Data Loss Risk** | Confirmed or highly probable data loss or data corruption. |
| **Revenue Impact** | Direct, measurable revenue loss occurring now (transactions failing, billing broken, customers churning in real-time). |
| **Expected Response Time** | Immediate. All-hands response within 15 minutes. |
| **Communication Requirements** | Internal: all engineering leadership notified immediately. External: status page updated within 10 minutes, executive briefing within 30 minutes, customer comms if duration > 30 minutes. |
| **Escalation Requirements** | Incident Commander required. Engineering Manager notified immediately. VP/CTO notified within 30 minutes. On-call from all affected teams paged. |

**Examples:**
- Production database is down and unrecoverable
- Authentication system is rejecting all login attempts
- Payment processing is failing for all transactions
- Confirmed data breach or security compromise

---

### SEV-2: Major

**A major feature is significantly degraded or unavailable. Large subset of users impacted. Workarounds may not exist or are unacceptable.**

| Dimension | Criteria |
|-----------|----------|
| **User Impact** | Significant portion of users (>10%) affected. Core functionality degraded but not completely unavailable. Some users cannot complete critical workflows. |
| **Data Loss Risk** | Possible but not confirmed. Data writes may be delayed or partially failing. |
| **Revenue Impact** | Probable revenue impact. Some transactions failing or delayed. Conversion rates likely affected. |
| **Expected Response Time** | Urgent. Primary responder engaged within 15 minutes. Full incident team assembled within 30 minutes. |
| **Communication Requirements** | Internal: engineering leadership notified within 15 minutes. External: status page updated within 15 minutes. Customer comms if duration > 1 hour. |
| **Escalation Requirements** | Incident Commander required. Engineering Manager notified within 15 minutes. Additional teams engaged as needed. |

**Examples:**
- API latency 10x normal causing timeouts for many users
- Search functionality completely broken
- Mobile app crashing on launch for one platform (iOS or Android)
- Third-party integration failure affecting a major workflow

---

### SEV-3: Minor

**A non-critical feature is impaired. Limited user impact. Workarounds available.**

| Dimension | Criteria |
|-----------|----------|
| **User Impact** | Small subset of users affected (<10%). Non-critical feature degraded. Reasonable workaround exists. |
| **Data Loss Risk** | No data loss. Data may be delayed but will be eventually consistent. |
| **Revenue Impact** | Minimal or no direct revenue impact. May affect user satisfaction but not transactions. |
| **Expected Response Time** | Within business hours. Acknowledged within 30 minutes. Work begins within 2 hours. |
| **Communication Requirements** | Internal: team channel notified. External: status page updated if user-visible. No executive notification unless duration > 4 hours. |
| **Escalation Requirements** | On-call engineer handles. Escalate to team lead if not resolved within 4 hours. No Incident Commander required (optional). |

**Examples:**
- Email notifications delayed by 30+ minutes
- Dashboard loading slowly but functional
- Export feature failing for specific file format
- Non-critical third-party integration intermittent

---

### SEV-4: Low

**Cosmetic issue, minor bug, or degradation with negligible user impact. No immediate action required.**

| Dimension | Criteria |
|-----------|----------|
| **User Impact** | Negligible. Fewer than handful of users affected, or impact is cosmetic only. No workflow is blocked. |
| **Data Loss Risk** | None. |
| **Revenue Impact** | None. |
| **Expected Response Time** | Handled during normal working hours. May be deferred to next sprint. |
| **Communication Requirements** | Internal: ticket created in backlog. No status page update. No stakeholder notification. |
| **Escalation Requirements** | None. Handled through normal ticket workflow. |

**Examples:**
- UI element misaligned in one browser
- Non-critical background job running slower than usual
- Informational log errors with no user impact
- Monitoring dashboard showing stale data for one non-critical metric

---

## Quick Reference Card

| | SEV-1 | SEV-2 | SEV-3 | SEV-4 |
|---|-------|-------|-------|-------|
| **Impact** | All users, core function | Many users, major feature | Few users, minor feature | Negligible |
| **Revenue** | Active loss | Probable loss | Minimal | None |
| **Data Risk** | Confirmed/likely | Possible | None | None |
| **Response** | Immediate (15 min) | Urgent (30 min) | Business hours (2 hr) | Normal workflow |
| **IC Required** | Yes | Yes | Optional | No |
| **Exec Notify** | Immediate | Within 30 min | If > 4 hours | Never |
| **Status Page** | Immediate | Within 15 min | If user-visible | No |
| **Customer Comms** | If > 30 min | If > 1 hour | Rarely | Never |

---

## Severity Reclassification

Severity can change as understanding improves:

**Upgrade when:**
- Impact is discovered to be wider than initially assessed
- Resolution is taking longer than expected and impact is growing
- Data loss or security implications emerge
- New symptoms indicate a deeper problem

**Downgrade when:**
- Mitigation reduces user impact significantly
- Affected user count is confirmed to be smaller than feared
- A workaround is identified that is acceptable to users

**Document all severity changes in the incident timeline with rationale.**

---

## Decision Tree

Use this when you are unsure of severity:

```
Is the service completely unavailable for all users?
├── Yes → SEV-1
└── No
    ├── Are >10% of users unable to complete core workflows?
    │   ├── Yes → SEV-2
    │   └── No
    │       ├── Is a non-critical feature impaired with workaround available?
    │       │   ├── Yes → SEV-3
    │       │   └── No → SEV-4
    │       └── Is there confirmed or likely data loss?
    │           ├── Yes → SEV-1
    │           └── No → Continue to next question
    └── Is there active, measurable revenue loss?
        ├── Yes → SEV-1 or SEV-2 based on scale
        └── No → SEV-3 or SEV-4 based on user impact
```

---

## Organizational Customization

Adapt this matrix to your context. Common customizations:

- **Add dimensions:** Compliance impact, contractual SLA implications, brand risk
- **Adjust thresholds:** User percentage thresholds depend on your user base size
- **Define "core workflows":** List your service's critical user journeys explicitly
- **Map to on-call tiers:** Define which on-call tier responds to which severity
- **Integrate with tooling:** Map severities to PagerDuty urgency levels, Slack channel routing, and status page component states
