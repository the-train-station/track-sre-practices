# Blameless Postmortem Template

## Incident Metadata

| Field | Value |
|-------|-------|
| **Incident ID** | INC-________ |
| **Date** | YYYY-MM-DD |
| **Duration** | HH:MM - HH:MM UTC (total: ___) |
| **Severity** | SEV-1 / SEV-2 / SEV-3 / SEV-4 |
| **Incident Commander** | |
| **Postmortem Author** | |
| **Postmortem Reviewer(s)** | |
| **Review Meeting Date** | |
| **Status** | Draft / In Review / Complete |

---

## Incident Summary

(Write 3-5 sentences summarizing what happened, who was affected, and how it was resolved. This should be understandable by someone with no context.)

---

## Impact

| Metric | Value |
|--------|-------|
| **Duration of user impact** | |
| **Number of users affected** | |
| **Number of failed requests** | |
| **Error budget consumed** | ___% of monthly budget |
| **Revenue impact** | |
| **Support tickets created** | |
| **SLA breach** | Yes / No |
| **Data loss** | Yes / No (details: ___) |

---

## Timeline

All times in UTC.

| Time | Event |
|------|-------|
| | First sign of problem (monitoring/alert/user report) |
| | Incident detected by team |
| | Incident declared (severity assigned) |
| | Initial investigation began |
| | Root cause identified |
| | Mitigation applied |
| | Service restored for users |
| | Incident closed |

**Detection time** (first sign to team awareness): ________ minutes

**Time to mitigate** (team awareness to user impact resolved): ________ minutes

---

## Root Cause Analysis

### What happened

(Describe the technical sequence of events that led to the incident. Be specific and factual.)

### Contributing Factors

List all factors that contributed to the incident occurring or to its severity/duration. These are systemic issues, not individual mistakes.

1. **Factor:** ___________________________________
   **Why it matters:** ___________________________________

2. **Factor:** ___________________________________
   **Why it matters:** ___________________________________

3. **Factor:** ___________________________________
   **Why it matters:** ___________________________________

4. **Factor:** ___________________________________
   **Why it matters:** ___________________________________

### Trigger vs. Root Cause

| | Description |
|---|---|
| **Trigger** | (The specific event that initiated the incident) |
| **Root Cause** | (The underlying systemic issue that allowed the trigger to cause impact) |

---

## What Went Well

Identify things that worked as intended or better than expected. These are practices to reinforce.

- 
- 
- 
- 

---

## What Could Be Improved

Identify areas where the response or systems fell short. Focus on processes and systems, not people.

- 
- 
- 
- 

---

## Where We Got Lucky

Identify factors that limited the blast radius or duration that we did not intentionally design for. These represent hidden risks.

- 
- 

---

## Action Items

Every action item must have an owner and a due date. Use priority labels to indicate urgency.

| # | Priority | Action Item | Owner | Due Date | Tracking Issue | Status |
|---|----------|-------------|-------|----------|----------------|--------|
| 1 | P0 | | | | | |
| 2 | P0 | | | | | |
| 3 | P1 | | | | | |
| 4 | P1 | | | | | |
| 5 | P2 | | | | | |
| 6 | P2 | | | | | |

**Priority definitions:**
- **P0:** Must be completed before next on-call rotation. Prevents immediate recurrence.
- **P1:** Complete within 2 weeks. Addresses root cause or significant contributor.
- **P2:** Complete within 30 days. Improves detection, response, or resilience.

---

## Lessons Learned

What did this incident teach us that we did not know before? What assumption was proven wrong?

1. 

2. 

3. 

---

## Appendix

### Related Incidents

| Incident ID | Date | Relationship |
|-------------|------|--------------|
| | | |

### Supporting Data

(Links to dashboards, logs, graphs, or other evidence referenced in this postmortem)

- 
- 
- 

---

## Postmortem Review Checklist

Before closing this postmortem:

- [ ] All sections are filled in with factual, blameless language
- [ ] Timeline is accurate and verified by multiple participants
- [ ] All action items have owners and due dates
- [ ] Action items are tracked in the team's issue tracker
- [ ] The postmortem has been reviewed in a meeting with the incident team
- [ ] Lessons learned have been shared with the broader engineering org
- [ ] Follow-up review scheduled to verify action item completion

---

## Blameless Culture Reminder

This postmortem is a learning document, not a blame document. We operate under these principles:

- People did reasonable things given the information they had at the time
- We focus on systemic improvements, not individual punishment
- The goal is to make the system more resilient, not to find fault
- If someone feels blamed by this document, it needs revision
