# SRE Learning Path Template

Use this template to build a structured, time-boxed learning path through Site Reliability Engineering. Customize the topics and resources to match your current role and organizational needs.

## How to Use This Template

1. Take the self-assessment checklist (companion exercise) to identify your current level
2. Start at the phase matching your assessment results
3. Set calendar reminders for milestone check-ins
4. Track completion in the progress log at the bottom

---

## Phase 1: Foundation (Weeks 1-8)

**Goal:** Understand core SRE philosophy, vocabulary, and principles.

| Week | Topic | Activities | Time Estimate |
|------|-------|-----------|---------------|
| 1-2 | SRE Philosophy & History | Read Google SRE Book chapters 1-3; watch "Keys to SRE" talk | 4-6 hrs |
| 3-4 | Monitoring & Observability Basics | Learn the four golden signals; set up a basic dashboard | 5-7 hrs |
| 5-6 | SLOs, SLIs, and Error Budgets | Read Art of SLOs whitepaper; define SLOs for a toy service | 5-7 hrs |
| 7-8 | Incident Response Fundamentals | Study PagerDuty incident response guide; shadow an on-call | 4-6 hrs |

### Milestone Criteria

- [ ] Can explain the difference between SRE and traditional operations
- [ ] Can define SLI, SLO, SLA and explain their relationships
- [ ] Can describe the four golden signals and when each applies
- [ ] Can explain what an error budget is and how it drives decisions
- [ ] Completed a basic monitoring setup for at least one service

---

## Phase 2: Intermediate (Weeks 9-20)

**Goal:** Apply SRE principles to real systems. Begin contributing to reliability work.

| Week | Topic | Activities | Time Estimate |
|------|-------|-----------|---------------|
| 9-10 | Toil Identification & Reduction | Audit toil in your team; propose one automation | 6-8 hrs |
| 11-12 | Alerting Strategy | Review existing alerts; implement multi-window burn rate alerts | 6-8 hrs |
| 13-14 | Change Management & Release Engineering | Study canary deployments; implement progressive rollout | 6-8 hrs |
| 15-16 | Capacity Planning | Model capacity for a service; create scaling runbook | 6-8 hrs |
| 17-18 | Postmortem Practice | Write a postmortem for a past incident; facilitate a review | 5-7 hrs |
| 19-20 | On-Call Best Practices | Design or improve an on-call rotation; build runbooks | 5-7 hrs |

### Milestone Criteria

- [ ] Successfully automated away at least one toil task
- [ ] Implemented burn-rate alerting for a production SLO
- [ ] Led or co-led at least one postmortem review meeting
- [ ] Created or improved a production runbook
- [ ] Participated in on-call rotation with confidence
- [ ] Can explain capacity planning methodology for your services

---

## Phase 3: Advanced (Weeks 21-36)

**Goal:** Design reliability strategies. Influence team and organizational practices.

| Week | Topic | Activities | Time Estimate |
|------|-------|-----------|---------------|
| 21-23 | Distributed Systems Reliability | Study consensus algorithms; analyze failure modes in your architecture | 8-10 hrs |
| 24-26 | Chaos Engineering | Design and run a Game Day; implement steady-state hypothesis testing | 8-10 hrs |
| 27-29 | SLO-Driven Development | Establish SLO review cadence; integrate error budgets into sprint planning | 6-8 hrs |
| 30-32 | Performance Engineering | Conduct load testing; identify and resolve bottlenecks | 8-10 hrs |
| 33-34 | Organizational Reliability | Design team topology for reliability; propose SRE engagement model | 5-7 hrs |
| 35-36 | Reliability Roadmapping | Build a quarterly reliability roadmap for your org | 5-7 hrs |

### Milestone Criteria

- [ ] Designed and executed a chaos engineering experiment
- [ ] Led an SLO review that resulted in an architectural decision
- [ ] Mentored a junior engineer through an incident
- [ ] Contributed to organizational reliability strategy
- [ ] Can analyze distributed system failure modes and propose mitigations
- [ ] Built a reliability roadmap adopted by engineering leadership

---

## Phase 4: Expert (Weeks 37-52)

**Goal:** Set reliability vision. Drive cultural transformation. Contribute to the community.

| Week | Topic | Activities | Time Estimate |
|------|-------|-----------|---------------|
| 37-40 | Reliability Program Design | Design an SRE program for an organization; define engagement models | 8-10 hrs |
| 41-44 | Advanced Capacity & Cost Optimization | Build predictive capacity models; optimize cloud spend vs reliability tradeoffs | 8-10 hrs |
| 45-48 | Cross-Org Incident Management | Design incident management across multiple teams/services; run large-scale exercises | 8-10 hrs |
| 49-52 | Teaching & Community Contribution | Write a blog post or give a talk; develop internal training material | 6-8 hrs |

### Milestone Criteria

- [ ] Designed an SRE engagement model for an organization
- [ ] Published or presented SRE content externally
- [ ] Mentored multiple engineers in SRE practices
- [ ] Led a reliability initiative that measurably improved system availability
- [ ] Can advise leadership on reliability investment decisions
- [ ] Contributed to open-source SRE tooling or community resources

---

## Progress Log

Track your progress here. Update weekly.

| Date | Phase | Topic Completed | Key Takeaway | Next Action |
|------|-------|----------------|--------------|-------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Recommended Resources by Phase

| Phase | Books | Online | Practice |
|-------|-------|--------|----------|
| Foundation | Google SRE Book (Ch 1-8) | Coursera SRE course | Home lab monitoring |
| Intermediate | SRE Workbook | SREcon talks | Production on-call |
| Advanced | Designing Data-Intensive Apps | Chaos engineering papers | Game Days |
| Expert | Accelerate (Forsgren et al.) | SREcon presentations | Org-wide programs |

## Notes

- Adjust time estimates based on your schedule (these assume 4-6 hrs/week of dedicated study)
- Phases can overlap; move to the next when milestone criteria are met, not by calendar
- Pair with a study buddy or mentor for accountability
- Revisit earlier phases as your understanding deepens
