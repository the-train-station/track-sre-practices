# Tabletop Exercise: Authentication Service Degradation

## Exercise Overview

| Field | Value |
|-------|-------|
| **Duration** | 90 minutes |
| **Participants** | 4-8 engineers (on-call team, incident commanders, service owners) |
| **Facilitator** | 1 person (does not participate as responder) |
| **Materials Needed** | This script, timer, whiteboard or shared doc for notes |
| **Objective** | Practice incident declaration, role assignment, investigation, communication, and decision-making under escalating pressure |

---

## Facilitator Guide

### Before the Exercise

1. Print or share this scenario with the facilitator only (not participants)
2. Prepare a shared document for participants to use as their incident timeline
3. Assign initial roles or let the team self-organize (part of the exercise)
4. Set expectations: this is practice, not a test. There are no "wrong" answers, only learning opportunities.

### During the Exercise

- Read each inject aloud at the designated time
- Give the team 5-8 minutes between injects to discuss and decide
- Do not help or hint unless the team is completely stuck for >3 minutes
- Note: who speaks first? Who takes charge? Who asks clarifying questions?
- Track decisions made and their rationale

### Timing

| Clock | Activity |
|-------|----------|
| 0:00 | Exercise briefing and role assignment |
| 0:05 | Inject 1: Initial alert |
| 0:15 | Inject 2: Escalation |
| 0:25 | Inject 3: Conflicting data |
| 0:35 | Inject 4: External pressure |
| 0:45 | Inject 5: Decision point |
| 0:55 | Inject 6: Resolution path |
| 1:05 | Exercise ends, debrief begins |
| 1:05 - 1:30 | Debrief discussion |

---

## Scenario Background

Read this aloud to participants at the start:

> "Your company operates an e-commerce platform. It is Tuesday at 14:30 UTC. Traffic is at normal levels. Your authentication service handles all user logins, session validation, and OAuth token management. It processes approximately 2,000 requests per second during business hours. The service was last deployed yesterday (Monday) at 16:00 UTC with what was described as a 'minor performance improvement to session caching.' All automated tests passed. The deploy was flagged as low-risk and received standard review."

---

## Inject 1: Initial Alert (T+0:00)

Read aloud:

> **PagerDuty Alert:** `[WARNING] Auth Service - P99 latency exceeded threshold`
>
> The auth service P99 latency has risen from its normal 45ms to 180ms over the last 10 minutes. The alert fired at the WARNING level. Error rate is currently unchanged at 0.02%. No customer complaints received yet. Your monitoring dashboard shows a gradual climb starting approximately 8 minutes ago.

**Decision points for the team:**
- Do you acknowledge this as an incident or continue monitoring?
- Who owns the initial investigation?
- What is your first diagnostic action?

**Facilitator notes:** Watch for whether the team assigns ownership or lets it drift. Note if anyone checks the recent deploy as a potential cause.

---

## Inject 2: Escalation (T+10:00)

Read aloud:

> **10 minutes later.** P99 latency is now at 450ms and climbing. The error rate has increased to 0.8%. Your metrics show that 95% of errors are HTTP 503 (Service Unavailable) from the auth service. Customer support has received 3 tickets in the last 5 minutes from users reporting "slow login." The session cache hit ratio has dropped from 92% to 34%. CPU utilization on auth service pods is at 78% and climbing.

**Decision points for the team:**
- What severity do you declare?
- Who is the Incident Commander?
- What roles do you assign?
- What do you communicate, to whom, and through what channel?
- What is your investigation priority: the cache hit ratio drop or the CPU increase?

**Facilitator notes:** This is where structure matters. Teams that skip role assignment often struggle in later injects. The cache hit ratio drop is the key signal pointing toward yesterday's deploy.

---

## Inject 3: Conflicting Data (T+20:00)

Read aloud:

> **10 minutes later.** The team that deployed yesterday's caching change reports: "We tested thoroughly. The change only modified TTL values for session tokens from 1 hour to 15 minutes. It shouldn't cause this." However, your investigation shows:
>
> - Auth database connections are at 85% of pool limit (normally 30%)
> - Memory usage on auth pods has grown 40% since yesterday's deploy
> - A separate team deployed a marketing analytics tracker at 13:00 UTC today that adds a session validation call on every page view
> - The Redis cluster hosting the session cache shows no errors but replication lag is at 3 seconds (normally <100ms)
>
> Error rate is now at 2.1%. P99 latency is at 1,200ms. Some login attempts are timing out entirely.

**Decision points for the team:**
- You have multiple potential causes. How do you prioritize investigation?
- Do you roll back yesterday's deploy, today's analytics tracker, or both?
- What is the risk of each rollback?
- Do you update severity?
- What do you communicate to affected users?

**Facilitator notes:** This tests the team's ability to handle ambiguity. The correct answer is that BOTH changes contributed: shorter TTL means more cache misses, and the analytics tracker multiplied the request volume to the auth service. Watch for confirmation bias (latching onto one theory and ignoring contradicting evidence).

---

## Inject 4: External Pressure (T+30:00)

Read aloud:

> **The VP of Sales sends a message to the incident channel:** "I'm on a call with [Large Enterprise Customer]. They say their entire team of 500 users can't log in. They are threatening to escalate to their CEO. What do I tell them? When will this be fixed?"
>
> **Simultaneously**, your status page shows 15 customer-reported issues in the last 10 minutes. Error rate is at 4.3%. About 1 in 20 login attempts is failing outright. The rest are succeeding but taking 2-5 seconds.
>
> **Your Redis cluster has triggered a high-memory alert.** Memory utilization is at 91%. The operations team notes that if it hits 95%, Redis will start evicting session keys, which could cause a sudden spike in auth failures.

**Decision points for the team:**
- How do you respond to the VP of Sales?
- Do you update the status page? What do you say?
- The Redis memory situation is a ticking clock. What is your plan?
- Do you need to escalate further?
- What is your mitigation strategy right now (not root cause fix, but stop the bleeding)?

**Facilitator notes:** This tests communication under pressure and prioritization. The VP needs a response, but it should come from the Communications Lead, not distract the people investigating. The Redis memory is the most urgent technical risk and should drive immediate action.

---

## Inject 5: Decision Point (T+40:00)

Read aloud:

> **The team has identified the combined root cause.** Yesterday's TTL reduction (1hr to 15min) means sessions expire 4x faster. Today's analytics tracker validates sessions on every page view, multiplying auth requests by ~3x. Combined effect: 12x more requests hitting the auth database instead of cache.
>
> **You have three options:**
>
> **Option A:** Roll back yesterday's TTL change. Risk: it was deployed 22 hours ago; there may be sessions created with the new TTL that behave unexpectedly if the old code reads them. Estimated time: 10 minutes to deploy.
>
> **Option B:** Disable the analytics tracker's session validation. Risk: the marketing team says they are mid-campaign and losing this data costs them visibility. Estimated time: 5 minutes via feature flag.
>
> **Option C:** Scale the auth service horizontally (add pods) and increase the database connection pool. Risk: may not be fast enough if Redis hits 95% first. Estimated time: 15-20 minutes to fully stabilize.
>
> **Redis memory is now at 93%.**

**Decision points for the team:**
- Which option(s) do you choose?
- In what order?
- Who authorizes the decision?
- How do you communicate the plan?

**Facilitator notes:** The optimal response is B (fastest relief) immediately, then C (additional headroom), then A (proper fix after stabilization). But any reasonable plan with clear rationale is acceptable. Watch for analysis paralysis vs. decisive action. Note whether the IC makes the call or the team debates endlessly.

---

## Inject 6: Resolution Path (T+50:00)

Read aloud:

> **The team has executed their plan.** [Narrate based on their actual decision.]
>
> If they disabled the analytics tracker: Error rate is dropping. Redis memory has stabilized at 93% and is slowly declining. P99 latency is falling: 800ms... 500ms... 200ms. Login success rate is recovering.
>
> If they rolled back TTL: The deploy is rolling out. You see session cache hit ratio climbing: 40%... 55%... 70%. Some users may need to re-authenticate as their short-TTL sessions were invalidated during the rollback. Error rate is declining.
>
> If they scaled horizontally: Pods are starting but not yet healthy. Redis is at 94.2%. You have approximately 3-4 minutes before potential eviction cascade.
>
> **Regardless of path:** 5 minutes after initial mitigation takes effect, metrics are trending toward normal. The VP of Sales messages: "Customer confirms they can log in now. Thank you."

**Final decision points:**
- When do you declare the incident resolved vs. monitoring?
- What is your immediate follow-up plan?
- When do you schedule the postmortem?
- What are the first action items you can identify right now?

---

## Exercise End

Read aloud:

> "The exercise is now complete. Let's take a 2-minute break and then debrief."

---

## Debrief Guide (25 minutes)

### Round 1: Individual Reflection (5 minutes)

Each participant answers (1 minute each):
- "What is one thing that went well in our response?"
- "What is one thing you would do differently next time?"

### Round 2: Process Discussion (10 minutes)

Facilitator-led questions:

1. **Role clarity:** Was it clear who was in charge at every point? Where did confusion arise?

2. **Decision-making:** How did we make the critical decisions (severity classification, mitigation choice)? Was the process efficient?

3. **Communication:** Did the right people get the right information at the right time? Where did communication break down?

4. **Investigation:** Did we follow a systematic approach or did we jump to conclusions? Did we consider multiple hypotheses simultaneously?

5. **Time pressure:** How did the Redis memory situation and the VP's message affect our decision quality? Did we let urgency override thoroughness?

### Round 3: Action Items (10 minutes)

As a team, identify:

1. **Process improvements:** What would we change about our incident response process based on this exercise?

2. **Tooling gaps:** What tool or automation would have helped during this exercise?

3. **Knowledge gaps:** What information did we wish we had? How would we get it faster in a real incident?

4. **Communication templates:** Were our communication templates adequate? What would we add?

5. **Training needs:** Does anyone on the team need additional training based on what we observed?

---

## Facilitator Scoring Rubric (Optional)

Use this to provide structured feedback. Not for grading; for identifying team growth areas.

| Competency | Strong | Adequate | Needs Work |
|------------|--------|----------|------------|
| **Incident declaration** | Declared promptly with correct severity | Declared but severity debated too long | Did not formally declare or assign severity |
| **Role assignment** | Clear IC and roles assigned within 2 minutes | Roles eventually assigned but late | Roles unclear throughout |
| **Investigation method** | Systematic, multiple hypotheses considered | Eventually found root cause but inefficiently | Tunnel vision on single theory |
| **Decision-making** | IC made clear decision with rationale | Decision made but slowly or by committee | Analysis paralysis or no clear decision |
| **Communication** | Stakeholders updated timely and clearly | Updates happened but were late or unclear | Stakeholders left in the dark |
| **Prioritization** | Addressed highest-risk item first (Redis) | Addressed risks but not in optimal order | Did not identify the time-sensitive risk |
| **Escalation** | Appropriate escalation at correct time | Over- or under-escalated slightly | Failed to escalate when needed |

---

## Variations for Repeat Use

To run this exercise again with the same team, swap in one of these alternative scenarios:

- **Database failover gone wrong:** Primary DB fails, replica promotes, but replication lag means 30 seconds of writes are lost
- **DDoS during deployment:** Traffic spike that looks like an attack but is actually a viral marketing event, happening while a critical migration is in progress
- **Cascading failure:** A single microservice timeout causes retry storms across 5 dependent services
- **Third-party outage:** Your CDN provider is degraded but their status page says "all systems operational"
