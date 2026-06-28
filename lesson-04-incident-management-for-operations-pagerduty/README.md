---
title: "Incident Management for Operations (PagerDuty)"
type: whitepaper
difficulty: intermediate
tier: free
platform: "PagerDuty"
url: "https://www.pagerduty.com/resources/incident-management-response/learn/what-is-incident-management/"
tags: ["incident-management", "on-call", "sre", "pagerduty"]
---

# Incident Management for Operations (PagerDuty)

## Overview

PagerDuty's incident management guidance focuses on turning unplanned work into a disciplined, well-coordinated response. This lesson covers the incident lifecycle from detection to post-incident learning, with emphasis on clear roles, fast decision-making, effective stakeholder communication, and durable remediation. You will map the guidance to your team's on-call model, define a minimal playbook, and practice a short tabletop so the process is usable when it matters.

This is a useful resource for SRE learners because it treats incident response as an operating system for the team, not just a ticketing workflow. The real value is in how it structures coordination: who makes decisions, who communicates externally, when to escalate, when to stabilize before investigating deeply, and how to turn an outage into changes that reduce repeat incidents.

## Prerequisites

- Basic familiarity with production operations and on-call rotations
- Access to an alerting source or monitoring system that can trigger incidents
- A collaboration channel for response, such as Slack or Microsoft Teams, and a ticket tracker for follow-ups
- Optional: A PagerDuty account to configure services, escalation policies, and on-call schedules

## Key Takeaways

1. **A clear incident lifecycle reduces coordination overhead** - Teams recover faster when detection, declaration, mitigation, communication, and review follow a shared model.
2. **Defined roles improve response quality** - An Incident Commander leads, a communications lead handles updates, and responders focus on mitigation rather than competing for control.
3. **Good communication is part of the technical response** - Short, frequent, audience-appropriate updates reduce duplicate interruptions and help the team maintain decision quality.
4. **Post-incident review is part of the workflow** - Contributing factors, decisions, and follow-up actions should be documented without blame so the organization learns from real failures.
5. **Small playbooks outperform giant manuals** - Lightweight checklists and templates are easier to follow under pressure than long documents no one can navigate during an outage.

## How to Use

### Step 1: Define Your Incident Lifecycle

Adopt a simple flow such as Detect, Declare, Assess, Assign Roles, Mitigate, Communicate, Restore, and Review. Then define severities, for example:

- `SEV1` for customer-impacting outages
- `SEV2` for partial degradation
- `SEV3` for limited-scope issues

Make the expected engagement for each severity explicit so responders do not negotiate process during an outage.

### Step 2: Establish Core Roles and Hand-Offs

Define the minimum roles your team needs during a serious incident:

- **Incident Commander** - Owns the response outcome and tempo, delegates work, and keeps the team focused on the next decision
- **Communications Lead** - Drafts updates, posts on an agreed cadence, and manages the status page or stakeholder channel
- **Operations or Subject Matter Responders** - Investigate, mitigate, and confirm recovery signals
- **Scribe** - Optional for higher-severity incidents; maintains the timeline and action list

### Step 3: Prepare the Response System

If you use PagerDuty, create a service and connect the alert sources that should open or escalate incidents, such as monitoring alarms, logs, or SLO burn alerts. Configure an escalation policy with at least two levels, set on-call schedules, and test a non-disruptive alert to verify routing.

It is also worth defining incident tags or categories such as `database`, `deploy`, or `network`. These make triage and later reporting easier.

### Step 4: Write a Minimal Playbook

Create a one-page playbook that covers:

- How to declare the incident and page the Incident Commander
- Which channel, bridge, or document becomes the source of truth
- A first-15-minutes checklist covering impact confirmation, role assignment, mitigation choices, and update cadence
- Two or three communication templates for internal and external updates
- Recovery criteria that define what "restored" actually means

### Step 5: Run a 30-Minute Tabletop

Choose a realistic scenario, such as increased error rates after a deploy that prevents user login. Practice the full response: page the Incident Commander, create the incident channel, assign roles, evaluate mitigation options, post status updates, and declare recovery.

Finish by capturing three improvements in tooling, documentation, or process that you can apply in the next sprint.

### Step 6: Run the Post-Incident Review Quickly

Hold the review within three to five business days while details are still fresh. Build a fact-based timeline, identify contributing factors without blame, and separate corrective actions from preventive actions. Assign owners and due dates so the review produces actual change rather than archival notes.

It is also useful to track a small set of health metrics such as pages per on-call, false-positive rate, time to acknowledge, and time to mitigate. Use them for trend awareness, not as scorecards.

### Step 7: Iterate and Automate

Convert repeated manual response steps into runbooks or automation, such as rollback scripts, feature flag toggles, or canary abort commands. Periodically test escalation paths and notification hygiene as well. Incident management quality decays if the workflow is never exercised until a real outage occurs.

## Deliverable

Create an incident lifecycle playbook, run a 30-minute tabletop, and review the follow-up actions.

Playbook template:

| Section | Learner answer |
|---------|----------------|
| Incident severities |  |
| Declaration path |  |
| Source-of-truth channel/document |  |
| Incident Commander duties |  |
| Communications lead duties |  |
| First 15 minutes checklist |  |
| Recovery criteria |  |
| Post-incident review trigger |  |

30-minute tabletop:

1. Minute 0-5: declare a scenario such as login failures after a deploy and assign roles.
2. Minute 5-15: inspect the symptom, choose a mitigation, and post the first stakeholder update.
3. Minute 15-25: decide whether to roll back, disable a feature, scale capacity, or continue investigation.
4. Minute 25-30: declare recovery criteria and capture three follow-up actions.

Action-item review rubric:

| Score | Criteria |
|-------|----------|
| 3 | Action prevents, detects, or mitigates a repeat incident; has owner, due date, and validation evidence. |
| 2 | Action is useful but needs sharper scope, ownership, or proof of completion. |
| 1 | Action is vague, blame-oriented, cosmetic, or unlikely to change future outcomes. |

Reflection questions:

- Which decision in the tabletop created the most ambiguity?
- Which update would you send to customers versus internal stakeholders?
- Which follow-up action reduces future risk the most, and how will you verify it worked?

## Practice Notes

- Convert reading into decisions. Pull out three recommendations, rate whether your current or sample workload follows them, and write the gap as an actionable backlog item.
- Frame the lesson around a production service: user-visible symptom, SLI/SLO impact, alert or dashboard signal, incident action, and follow-up work that reduces future toil.
- Completion checkpoint: you can adapt the pattern to a second environment, identify its tradeoffs, and explain the operational risks it introduces.
- Portfolio artifact: create a short note titled "Incident Management for Operations (PagerDuty) - applied takeaway" with the scenario you used, the decision you made, and one follow-up task you would assign to yourself or a team.

## Related Resources

- [What is Incident Management?](https://www.pagerduty.com/resources/incident-management-response/learn/what-is-incident-management/) - PagerDuty's overview of the incident lifecycle and why structured response matters
- [PagerDuty Incident Management](https://www.pagerduty.com/platform/incident-management/) - Product-oriented view of how PagerDuty supports coordination, escalation, and stakeholder communication
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) - Foundational reading on incident response and postmortem practice
- [PagerDuty Resources](https://www.pagerduty.com/resources/) - Broader operational guides, reports, and runbook examples
- [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/) - Additional practical incident-management and operations guidance

## Estimated Time

- **Reading this lesson and drafting your playbook**: 30-45 minutes
- **Configuring a basic PagerDuty service, escalation policy, and test incident**: 30-60 minutes
- **Running a 30-minute tabletop drill**: 30 minutes
- **Completing a post-incident review template with follow-up actions**: 30-45 minutes
- **Total for this lesson**: ~2-3 hours for a first pass, plus another 1-2 hours to implement the identified improvements
