# Incident Communication Templates

## Overview

Clear, timely communication during incidents reduces confusion, builds trust, and prevents escalation. Use these templates as starting points and customize for your organization.

**Principles:**
- State facts, not speculation
- Include what you know AND what you do not know
- Provide next update time (and honor it)
- Write for the audience (technical vs. non-technical)

---

## 1. Internal Stakeholder Update (Slack/Email)

### Initial Notification

```
INCIDENT: [Service Name] - [Brief Description]
Severity: SEV-[1/2/3/4]
Status: Investigating / Identified / Mitigating

IMPACT:
[What users are experiencing. Be specific: "Users cannot log in" 
not "auth service is down."]

AFFECTED:
- Services: [list]
- Regions: [list]  
- Estimated users: [number or percentage]

CURRENT ACTIONS:
- [What the team is doing right now]

INCIDENT TEAM:
- Commander: [name]
- Channel: #inc-[name]

NEXT UPDATE: [time] UTC (in [X] minutes)
```

### Follow-Up Update

```
UPDATE #[N]: [Service Name] Incident
Time: [HH:MM] UTC
Status: Investigating / Identified / Mitigating / Monitoring

WHAT CHANGED SINCE LAST UPDATE:
- [bullet points of new information or actions taken]

CURRENT STATUS:
[1-2 sentences on where things stand now]

ROOT CAUSE:
[If identified: brief description]
[If not: "Still investigating. Current hypothesis: ___"]

ETA TO RESOLUTION:
[Specific time estimate OR "Unknown, reassessing in [X] minutes"]

NEXT UPDATE: [time] UTC
```

### Resolution Notification

```
RESOLVED: [Service Name] Incident
Duration: [start time] - [end time] UTC ([X] hours [Y] minutes)

SUMMARY:
[2-3 sentences: what happened, what was impacted, how it was fixed]

ROOT CAUSE:
[Brief, non-speculative description]

IMPACT:
- Duration: [time]
- Users affected: [number/percentage]
- Requests failed: [number if applicable]
- Revenue impact: [if applicable]

IMMEDIATE FOLLOW-UP:
- [ ] Postmortem scheduled for [date]
- [ ] [Any immediate actions taken to prevent recurrence]

Postmortem doc: [link]
Questions? Reach out in #inc-[name] or to [IC name].
```

---

## 2. External Status Page Updates

### Initial Status Page Post

```
Title: [Service Name] - Degraded Performance / Partial Outage / Major Outage

We are investigating reports of [user-visible symptom in plain language].

Some users may experience [specific impact: slow loading, failed 
transactions, inability to access feature X].

Our engineering team is actively investigating and we will provide 
updates as we learn more.

Next update in [30/60] minutes or sooner if the situation changes.
```

### Progress Update

```
Title: [Service Name] - Update

We have identified the cause of [the issue described in our earlier 
update]. [One sentence: what the cause is in non-technical terms.]

Our team is [implementing a fix / rolling back the change / working 
with our infrastructure provider to resolve this].

[If partial recovery]: Some users may notice improvement. We are 
continuing to work toward full resolution.

We expect to provide our next update in [30/60] minutes.

We apologize for the inconvenience and appreciate your patience.
```

### Resolution Post

```
Title: [Service Name] - Resolved

This incident has been resolved. All services are operating normally.

Duration: [start time] to [end time] ([total duration])

What happened: [1-2 sentences in plain, non-technical language 
describing the user impact]

What we did: [1-2 sentences on the fix, accessible to non-technical 
readers]

We understand the impact this had on your work and we are taking 
steps to prevent a recurrence. We will publish a full incident 
report within [3/5] business days.

If you continue to experience issues, please contact [support 
channel].
```

---

## 3. Executive Summary Template

Use this for leadership briefings on SEV-1/SEV-2 incidents. Send within 2 hours of resolution or at end of business day for extended incidents.

```
Subject: Incident Summary - [Service] [Date]

EXECUTIVE SUMMARY
-----------------
[2-3 sentences: what broke, who was affected, how long, and 
current status]

BUSINESS IMPACT
--------------
- Duration: [X hours Y minutes]
- Customers affected: [number or segment]
- Revenue impact: [$X estimated / None / Under investigation]
- SLA implications: [Any contractual SLA breached? Credit owed?]
- Support tickets generated: [number]

TIMELINE (key events only)
---------
[HH:MM] - [First sign of problem]
[HH:MM] - [Incident declared]
[HH:MM] - [Root cause identified]
[HH:MM] - [Mitigation applied]
[HH:MM] - [Service restored]

ROOT CAUSE
----------
[2-3 sentences. Non-technical. What went wrong and why.]

IMMEDIATE ACTIONS TAKEN
-----------------------
1. [What was done to resolve]
2. [What was done to prevent immediate recurrence]

NEXT STEPS
----------
1. Postmortem review: [scheduled date]
2. [Key follow-up action with owner]
3. [Key follow-up action with owner]

QUESTIONS?
----------
Contact: [IC name and channel]
Full incident timeline: [link]
```

---

## 4. Customer-Facing Email (for Major Incidents)

Use when the incident warrants direct customer communication beyond the status page.

```
Subject: Service Disruption on [Date] - Summary and Next Steps

Dear [Customer / Team],

On [date], [service name] experienced [a service disruption / 
degraded performance] between [start time] and [end time] UTC, 
lasting approximately [duration].

WHAT HAPPENED
During this time, [describe user-visible impact in plain language: 
"you may have been unable to..." or "you may have experienced..."].

WHAT WE DID
Our engineering team [identified the issue within X minutes / 
implemented a fix / restored service]. [One sentence on what the 
fix was, non-technically.]

WHAT WE ARE DOING TO PREVENT RECURRENCE
We take reliability seriously. In response to this incident, we are:
- [Action 1: something concrete and meaningful]
- [Action 2: something concrete and meaningful]

[If SLA credit applies]:
IMPACT TO YOUR ACCOUNT
Based on our service level agreement, this incident qualifies for 
a service credit of [X%] on your [month] invoice. This will be 
applied automatically; no action is needed on your part.

We sincerely apologize for the disruption to your operations. If 
you have questions or continue to experience issues, please contact 
[support email / link].

Sincerely,
[Name]
[Title]
```

---

## Communication Timing Guide

| Severity | First Update | Subsequent Updates | Stakeholders |
|----------|-------------|-------------------|--------------|
| SEV-1 | Within 10 minutes | Every 15-30 minutes | All: internal, status page, exec, affected customers |
| SEV-2 | Within 15 minutes | Every 30-60 minutes | Internal, status page, exec (if >1hr) |
| SEV-3 | Within 30 minutes | Every 1-2 hours | Internal team, status page (if customer-facing) |
| SEV-4 | Within 1 hour | As needed | Internal team only |

---

## Common Pitfalls

| Pitfall | Instead |
|---------|---------|
| "We are aware of the issue" (no detail) | Describe what users are experiencing |
| Speculation about root cause before confirmed | "We are investigating" or "Current hypothesis is..." |
| Missing next update time | Always commit to a next-update time |
| Technical jargon in customer-facing comms | Describe impact in terms of user experience |
| Blame ("a third-party vendor caused...") | Focus on impact and resolution, not blame |
| Radio silence during extended incidents | Update even if status is unchanged: "Still investigating, no change" |
