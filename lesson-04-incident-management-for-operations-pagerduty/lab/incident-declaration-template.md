# Incident Declaration Template

Use this template when declaring a new incident. Fill in all fields at the time of declaration; update as information becomes available.

---

## Incident Declaration

| Field | Value |
|-------|-------|
| **Incident ID** | INC-________ (auto-assigned or sequential) |
| **Declared At** | YYYY-MM-DD HH:MM UTC |
| **Declared By** | |
| **Severity** | SEV-1 / SEV-2 / SEV-3 / SEV-4 |

---

## Impact

| Field | Value |
|-------|-------|
| **Affected Service(s)** | |
| **Affected Region(s)** | |
| **User Impact** | |
| **Estimated Users Affected** | |
| **Revenue Impact** | None / Estimated $____ per hour / Unknown |
| **Data Loss Risk** | None / Possible / Confirmed |

---

## Incident Team

| Role | Name | Contact |
|------|------|---------|
| **Incident Commander** | | |
| **Operations Lead** | | |
| **Communications Lead** | | |
| **Subject Matter Expert(s)** | | |
| **Scribe** | | |

---

## Coordination

| Field | Value |
|-------|-------|
| **War Room** | [Link to video call / Slack channel] |
| **Incident Channel** | #inc-________ |
| **Status Page** | [Link if applicable] |
| **Tracking Document** | [Link to live incident doc] |

---

## Initial Assessment

**What is happening?**

(Describe the observed symptoms in 2-3 sentences)

**When did it start?**

YYYY-MM-DD HH:MM UTC

**What changed recently?**

- [ ] Deployment (what, when, by whom)
- [ ] Configuration change
- [ ] Infrastructure change
- [ ] Traffic pattern change
- [ ] External dependency issue
- [ ] Unknown

**Initial Hypothesis:**

---

## Timeline (started at declaration, updated throughout)

| Time (UTC) | Event |
|------------|-------|
| | Incident declared |
| | |
| | |
| | |

---

## Checklist at Declaration

- [ ] Severity assigned
- [ ] Incident Commander identified
- [ ] War room opened
- [ ] Incident channel created
- [ ] Stakeholders notified (per severity matrix)
- [ ] Status page updated (if customer-facing)
- [ ] Timeline logging started

---

## Quick Reference: Severity Definitions

| Severity | Criteria |
|----------|----------|
| **SEV-1** | Complete service outage or data loss; revenue-impacting; all customers affected |
| **SEV-2** | Major feature unavailable; significant user impact; partial degradation |
| **SEV-3** | Minor feature impacted; workaround available; limited user impact |
| **SEV-4** | Cosmetic issue or low-impact degradation; no immediate user impact |

---

## Escalation

If the incident requires escalation beyond the initial team:

| Escalation Level | Contact | When to Escalate |
|-----------------|---------|------------------|
| Engineering Manager | | SEV-1/SEV-2 not resolved in 30 min |
| VP Engineering | | SEV-1 not resolved in 1 hour |
| Executive Team | | SEV-1 with customer/revenue impact > 2 hours |
| Legal/Compliance | | Data breach suspected |
| PR/Communications | | Media attention likely |
