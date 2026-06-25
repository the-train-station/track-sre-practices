# SRE Self-Assessment Checklist

Rate yourself on each skill using the following scale:

- **Novice (N):** Limited exposure. Can describe the concept but have not applied it in production.
- **Practitioner (P):** Have applied this in production environments. Can execute independently with occasional guidance.
- **Expert (E):** Deep experience. Can design solutions, mentor others, and handle edge cases.

Be honest. This is a growth tool, not a performance evaluation.

---

## 1. Monitoring and Observability

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 1.1 | Implement the four golden signals (latency, traffic, errors, saturation) | | | | |
| 1.2 | Design and build dashboards that answer specific operational questions | | | | |
| 1.3 | Implement distributed tracing across multiple services | | | | |
| 1.4 | Write and tune alerting rules with appropriate thresholds | | | | |
| 1.5 | Differentiate between symptoms and causes in monitoring data | | | | |
| 1.6 | Set up structured logging with correlation IDs | | | | |
| 1.7 | Use observability data to drive architectural decisions | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## 2. Incident Response

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 2.1 | Declare and classify incidents by severity | | | | |
| 2.2 | Serve as Incident Commander during a live incident | | | | |
| 2.3 | Communicate status updates to stakeholders during an incident | | | | |
| 2.4 | Coordinate across multiple teams to resolve a complex incident | | | | |
| 2.5 | Perform systematic troubleshooting under pressure | | | | |
| 2.6 | Make rollback/mitigation decisions with incomplete information | | | | |
| 2.7 | De-escalate and close out an incident with proper handoff | | | | |
| 2.8 | Design and run tabletop exercises for incident preparedness | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## 3. SLOs, SLIs, and Error Budgets

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 3.1 | Identify appropriate SLIs for different service types (serving, pipeline, storage) | | | | |
| 3.2 | Set realistic SLO targets based on user expectations and business needs | | | | |
| 3.3 | Calculate and track error budget consumption | | | | |
| 3.4 | Implement burn-rate alerting (multi-window, multi-burn-rate) | | | | |
| 3.5 | Use error budget data to make development vs. reliability tradeoff decisions | | | | |
| 3.6 | Facilitate SLO review meetings with engineering and product stakeholders | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## 4. Capacity Planning

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 4.1 | Measure and project resource utilization trends | | | | |
| 4.2 | Model the impact of traffic growth on infrastructure needs | | | | |
| 4.3 | Perform load testing and interpret results | | | | |
| 4.4 | Identify bottlenecks and saturation points in a system | | | | |
| 4.5 | Plan capacity for peak events (launches, seasonal traffic) | | | | |
| 4.6 | Balance cost optimization against reliability headroom | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## 5. Automation and Toil Reduction

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 5.1 | Identify and measure toil (manual, repetitive, automatable, no lasting value) | | | | |
| 5.2 | Prioritize automation projects based on ROI | | | | |
| 5.3 | Build self-service tooling that reduces operational burden | | | | |
| 5.4 | Implement infrastructure as code for repeatable deployments | | | | |
| 5.5 | Design automation with appropriate safety guardrails | | | | |
| 5.6 | Measure toil reduction impact over time | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## 6. Change Management

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 6.1 | Implement progressive rollout strategies (canary, blue-green, feature flags) | | | | |
| 6.2 | Design and enforce deployment pipelines with safety checks | | | | |
| 6.3 | Perform and validate rollbacks quickly | | | | |
| 6.4 | Assess blast radius of a proposed change | | | | |
| 6.5 | Implement and monitor canary analysis (automated comparison) | | | | |
| 6.6 | Manage database schema migrations safely in production | | | | |
| 6.7 | Coordinate multi-service deployments with dependency ordering | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## 7. Postmortems and Continuous Improvement

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 7.1 | Write a clear, blameless postmortem document | | | | |
| 7.2 | Facilitate a postmortem review meeting | | | | |
| 7.3 | Identify systemic contributing factors beyond the immediate trigger | | | | |
| 7.4 | Write actionable follow-up items with owners and deadlines | | | | |
| 7.5 | Track postmortem action items to completion | | | | |
| 7.6 | Identify patterns across multiple postmortems | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## 8. On-Call and Operational Readiness

| # | Skill | N | P | E | Notes / Evidence |
|---|-------|---|---|---|------------------|
| 8.1 | Respond to pages and triage effectively within SLA | | | | |
| 8.2 | Write and maintain operational runbooks | | | | |
| 8.3 | Perform on-call handoffs with proper context transfer | | | | |
| 8.4 | Balance on-call load and manage alert fatigue | | | | |
| 8.5 | Design on-call rotations that are sustainable for the team | | | | |
| 8.6 | Escalate appropriately when an issue exceeds your expertise | | | | |
| 8.7 | Conduct operational readiness reviews for new services | | | | |

**Strongest area:** ___________________________________

**Biggest gap:** ___________________________________

---

## Summary and Action Plan

### Score Summary

Count your ratings across all sections:

| Rating | Count |
|--------|-------|
| Novice (N) | |
| Practitioner (P) | |
| Expert (E) | |

### Top 3 Strengths (Expert-rated skills you can mentor others on)

1. ___________________________________
2. ___________________________________
3. ___________________________________

### Top 3 Growth Areas (Novice-rated skills most critical to your role)

1. ___________________________________
2. ___________________________________
3. ___________________________________

### 90-Day Development Plan

For each growth area, identify one concrete action:

| Growth Area | Action | Target Date | Success Measure |
|-------------|--------|-------------|-----------------|
| | | | |
| | | | |
| | | | |

---

## Reassessment Schedule

Retake this assessment quarterly. Track your progression:

| Date | Total N | Total P | Total E | Focus Areas |
|------|---------|---------|---------|-------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
