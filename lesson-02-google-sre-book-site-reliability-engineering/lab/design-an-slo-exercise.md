# Design an SLO Exercise

## Objective

Design a complete, production-ready SLO for a service you own or are familiar with. By the end of this exercise, you will have a documented SLO that can be implemented in your monitoring system and used to drive reliability decisions.

---

## Step 1: Choose Your Service

Select a real service to design an SLO for. Answer these questions:

**Service Name:** ___________________________________

**Service Type:** (circle one)
- Serving system (synchronous request/response)
- Data processing pipeline (batch or streaming)
- Storage system (reads, writes, durability)

**Primary Users:** ___________________________________

**What does this service do in one sentence?**

___________________________________

**What happens when this service is degraded or unavailable?**

___________________________________

---

## Step 2: Identify User Journeys

List the critical user journeys (CUJs) that depend on this service. A CUJ is an end-to-end interaction that matters to users.

| # | User Journey | Frequency | Business Criticality (H/M/L) |
|---|-------------|-----------|-------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

**Select 1-2 journeys to build SLOs for.** Start with the most critical.

Selected journey: ___________________________________

---

## Step 3: Choose SLI Type

For your selected journey, choose the appropriate SLI specification:

### For Serving Systems

| SLI Type | Definition | When to Use |
|----------|-----------|-------------|
| Availability | Proportion of valid requests served successfully | Almost always; baseline SLI |
| Latency | Proportion of valid requests served faster than threshold | When speed affects UX |
| Quality | Proportion of valid requests served without degradation | When partial responses are possible |

### For Data Processing Pipelines

| SLI Type | Definition | When to Use |
|----------|-----------|-------------|
| Freshness | Proportion of time data is updated within threshold | Streaming/near-real-time |
| Correctness | Proportion of records processed correctly | Data integrity matters |
| Coverage | Proportion of expected data that was processed | No records should be dropped |

### For Storage Systems

| SLI Type | Definition | When to Use |
|----------|-----------|-------------|
| Durability | Proportion of written data that can be read back | Data must not be lost |
| Availability | Proportion of read/write attempts that succeed | System must be accessible |
| Latency | Proportion of operations completing within threshold | Performance-sensitive |

**Selected SLI type:** ___________________________________

**Rationale:** ___________________________________

---

## Step 4: Define Good and Total Events

The SLI is calculated as:

```
SLI = (Good Events / Total Events) x 100%
```

Define precisely what constitutes a "good" event and what counts as a "total" event.

**Total Events (denominator):**

What counts as one event?

```
Example: "One HTTP request to the /api/v2/* endpoints, excluding health checks"
```

Your definition: ___________________________________

What is excluded from the count?

```
Example: "Synthetic monitoring probes, health check endpoints, requests
from internal tooling"
```

Your exclusions: ___________________________________

**Good Events (numerator):**

What makes an event "good"?

```
Example: "Request returns HTTP 2xx or 4xx (client errors are not our
fault) AND response time is <= 300ms"
```

Your definition: ___________________________________

---

## Step 5: Set the Target

### Choosing a Target

Consider these factors:

| Factor | Your Answer |
|--------|-------------|
| What is the current measured performance? | |
| What do users actually need? (not want, need) | |
| What do competing/comparable services offer? | |
| What can your team realistically maintain? | |
| What is the cost difference between 99.9% and 99.95%? | |

### Target Selection

**SLO Target:** ________ %

**Window:** ________ days (rolling)

**Justification (2-3 sentences):**

___________________________________

### Error Budget Calculation

```
Error Budget = 1 - [your SLO target]
             = 1 - ________
             = ________

In concrete terms (per window):
  Total events per window (estimate): ________
  Allowed bad events: ________
```

---

## Step 6: Define Alerting Thresholds

Configure multi-window burn rate alerts for your SLO:

### Critical Alert (Page)

```
Condition: Budget will be exhausted in ____ hours at current rate
Burn Rate Threshold: ____x
Long Window: ____ (e.g., 1 hour)
Short Window: ____ (e.g., 5 minutes)
Action: Page on-call engineer
```

### Warning Alert (Ticket)

```
Condition: Budget will be exhausted in ____ days at current rate
Burn Rate Threshold: ____x
Long Window: ____ (e.g., 6 hours)
Short Window: ____ (e.g., 30 minutes)
Action: Create ticket for investigation
```

### Slow Burn Alert (Notification)

```
Condition: Budget consumption trending above ____ % at midpoint
Burn Rate Threshold: ____x
Long Window: ____ (e.g., 3 days)
Short Window: ____ (e.g., 6 hours)
Action: Notify team channel
```

---

## Step 7: Document the SLO

Fill in this standard SLO document. This is what you would present to stakeholders and store in your SLO registry.

---

### SLO Document

**Service:** ___________________________________

**Owner Team:** ___________________________________

**Approver:** ___________________________________

**Created:** ___________________________________

**Last Reviewed:** ___________________________________

#### SLO Specification

| Field | Value |
|-------|-------|
| SLI Description | |
| Good Events | |
| Total Events | |
| SLO Target | |
| Window | |
| Data Source | |

#### Error Budget Policy

When the error budget is:

| Budget Remaining | Action |
|-----------------|--------|
| > 50% | Normal development velocity. Feature work proceeds. |
| 25% - 50% | Increased caution. High-risk deploys require additional review. |
| 5% - 25% | Reliability focus. Feature freeze for this service. Prioritize reliability work. |
| < 5% or exhausted | Full stop. No changes except reliability fixes. Postmortem required for any further budget consumption. |

#### Stakeholder Agreement

| Role | Name | Agreement |
|------|------|-----------|
| Service Owner | | [ ] Approved |
| Product Manager | | [ ] Approved |
| SRE Lead | | [ ] Approved |

#### Review Schedule

- **Quarterly review:** Assess if target is appropriate (too tight? too loose?)
- **Trigger review:** If budget exhausted 2+ times in a quarter
- **Annual review:** Full SLO redesign consideration

---

## Step 8: Implementation Checklist

Before this SLO is "live," confirm:

- [ ] SLI measurement is implemented in monitoring system
- [ ] Dashboard shows current SLI value and budget remaining
- [ ] Burn rate alerts are configured and tested
- [ ] Error budget policy is documented and agreed upon
- [ ] On-call team knows what to do when alerts fire
- [ ] Stakeholders have reviewed and approved the SLO target
- [ ] Review cadence is scheduled (calendar invite sent)

---

## Reflection Questions

1. Was it harder to define "good events" or to choose the target? Why?

2. What information did you wish you had when setting the target?

3. How would you explain this SLO to a non-technical product manager in 30 seconds?

4. What is the first thing that would break if you tightened the SLO by 10x (e.g., 99.9% to 99.99%)?

5. How will you know in 3 months if this SLO was set at the right level?
