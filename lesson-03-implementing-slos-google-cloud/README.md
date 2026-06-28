---
title: "Implementing SLOs (Google Cloud)"
type: lab
difficulty: intermediate
tier: free
platform: "Google"
url: "https://docs.cloud.google.com/monitoring/slo-monitoring"
tags: ["slo", "google-cloud", "monitoring", "reliability"]
---

# Implementing SLOs (Google Cloud)

## Overview

Service Level Objectives (SLOs) turn reliability from a vague aspiration into an explicit contract with users. On Google Cloud, you can design and operate SLOs using Cloud Monitoring's Service Level Objectives features and, for service-mesh-based applications, the SLO design guidance in Google's observability documentation. This lesson walks through choosing a user-centric service level indicator, setting a target and window, selecting the right metrics, creating the SLO in Cloud Monitoring, and wiring error-budget burn alerts that help teams react before customers are broadly impacted.

The resource is especially useful because it does not stop at theory. It shows how Google Cloud expects SLOs to be represented operationally: as monitored services, request-based SLIs, rolling windows, error-budget views, and alerts that tie directly to customer experience. By the end, you should have one measurable SLO, a budget you can track, and an alerting policy that balances fast detection with noise control.

## Prerequisites

- A Google Cloud project where you can view/create Monitoring Services, SLOs, and alerting policies
- IAM permissions such as `roles/monitoring.editor` or higher for setup work, with `roles/monitoring.viewer` sufficient for review-only access
- A target service deployed on Google Cloud, such as Cloud Run, GKE, Anthos Service Mesh, GCE behind a load balancer, or an API exposed through API Gateway or Cloud Endpoints
- Basic familiarity with SRE concepts such as SLI, SLO, error budget, burn rate, and multi-window alerting
- Metrics available in Cloud Monitoring for your service requests and outcomes, or a plan to emit them

## Key Takeaways

1. **Start with user journeys, not internal components** - Choose latency or availability signals tied to what users notice, then work backward to the supporting metrics.
2. **Use the SLO types Google Cloud supports well** - Request-based SLIs such as good/bad ratio and latency distribution cuts are the fastest path to a practical first SLO.
3. **Set targets and windows that match business risk** - Common objectives range from 99% to 99.9% over 28- or 30-day windows, but the right number depends on what failure actually costs your users and team.
4. **Burn-rate alerts work better than raw threshold pages** - Multi-window error-budget alerts catch fast regressions without training on-call engineers to ignore noisy conditions.
5. **SLOs need operational review, not one-time setup** - As traffic, architecture, and expectations shift, your SLI definitions and thresholds should change with them.

## How to Use

### Step 1: Define the User Journey and SLI

List the one or two operations that matter most to your users, such as `POST /checkout` or `GET /api/v1/search`. For each one, choose the SLI type that best captures the experience:

- Availability or error rate: fraction of successful requests, modeled as a good/bad ratio
- Latency: fraction of requests served under a defined threshold, modeled as a distribution cut

Write the SLI in plain language before you build it. For example: "99.9% of search requests succeed in a 30-day window" or "99% of checkout requests complete under 500 ms in a 30-day window."

### Step 2: Ensure Metrics Exist in Cloud Monitoring

Prefer managed ingress or platform metrics when possible, such as HTTPS Load Balancer metrics, Cloud Run request metrics, or Anthos Service Mesh Envoy metrics. These already integrate with Cloud Monitoring and reduce instrumentation work.

If you run on GKE without a mesh, expose application metrics through OpenTelemetry or Prometheus and export them into Cloud Monitoring. For availability SLIs, you need counters for total requests and good requests. For latency SLIs, you need a distribution metric with meaningful buckets.

### Step 3: Create a Monitoring Service

In the Cloud Console, go to Monitoring, then Services, then create a service scoped to the workload you want to measure. Name it after the user journey, API, or service that the SLO will represent. Keep the identity stable so the SLO math remains continuous over time.

### Step 4: Define the SLO in Cloud Monitoring

For availability SLOs, define a good filter for successful requests and a total filter for all requests. For latency SLOs, choose the request latency distribution and set the threshold that counts as good, such as `<= 300 ms`. Then set the target, such as `99.9%`, and pick a rolling window such as 28 or 30 days.

Before moving on, verify that the preview graph shows believable historic values. If the graph looks implausible, fix the filters now instead of building alerts on top of bad math.

### Step 5: Add Error-Budget Burn Alerts

Create at least two alerting policies to balance sensitivity and noise:

- A fast-burn alert for sharp regressions that could exhaust the budget quickly
- A slow-burn alert for sustained degradation that deserves investigation but may not require an immediate page

In Cloud Monitoring, choose the error-budget burn-rate condition type for the SLO and route notifications to the correct on-call path with names that make urgency obvious.

### Step 6: Build an SLO Dashboard

Add the SLO status widget, error-budget remaining, and the underlying SLI charts such as success ratio or latency. Include the upstream and downstream dependency charts that engineers actually use during incidents, such as database saturation, queue depth, or load balancer errors. A useful SLO dashboard should help the responder move from symptom to likely cause quickly.

### Step 7: Validate and Iterate

Trigger a safe test, such as a small amount of injected latency or a controlled error condition in staging, and confirm the alerts behave as expected. After the first month, review actual burn patterns. If you see frequent false alarms, refine the SLI filter, adjust the threshold, or route the alert differently. Document what the team is expected to do when each alert fires.

### Step 8: Apply Mesh-Aware Design When Relevant

If you use Anthos Service Mesh, prefer Envoy and mesh-level metrics for consistent request accounting across services. Start with route-level SLIs for the user-critical paths, then expand to service-level SLOs once the request accounting is stable. Be careful not to count retries as success unless that truly matches what users experience.

## Deliverable

Produce an SLO definition worksheet and a small burn-rate exercise for one user journey.

SLO worksheet:

| Field | Learner answer |
|-------|----------------|
| User journey |  |
| User-visible success condition |  |
| SLI type and metric source |  |
| Good events filter |  |
| Total events filter |  |
| Target and window |  |
| Error budget |  |
| Fast-burn alert |  |
| Slow-burn alert |  |
| Dashboard panels |  |
| First response action |  |

Burn-rate exercise:

1. Assume a 99.9% availability SLO over 30 days.
2. Calculate the monthly error budget as `0.1%` of total requests.
3. Pick a traffic volume, then calculate how many bad requests would consume 10%, 50%, and 100% of the budget.
4. Describe what the fast-burn and slow-burn alerts should ask the responder to do.

Review criteria:

- The SLI measures user experience, not only an internal host or container metric.
- Good and total event definitions are precise enough that another engineer could implement them.
- Alert thresholds include an expected response, route, and urgency.
- The dashboard links SLO state to supporting signals that help explain likely causes.

Reflection questions:

- What user harm is hidden if you choose the wrong SLI?
- What product or release decision should change when half the budget is gone?
- Which part of the worksheet would you validate first in a staging environment?

## Practice Notes

- Run hands-on work in a sandbox and keep a short lab log with commands, screenshots or outputs, resources created, cleanup steps, and the one pattern you would reuse in production.
- Frame the lesson around a production service: user-visible symptom, SLI/SLO impact, alert or dashboard signal, incident action, and follow-up work that reduces future toil.
- Completion checkpoint: you can adapt the pattern to a second environment, identify its tradeoffs, and explain the operational risks it introduces.
- Portfolio artifact: create a short note titled "Implementing SLOs (Google Cloud) - applied takeaway" with the scenario you used, the decision you made, and one follow-up task you would assign to yourself or a team.

## Related Resources

- [Cloud Monitoring SLO Monitoring](https://docs.cloud.google.com/monitoring/slo-monitoring) - Primary Google Cloud guide for SLO features, SLI types, and error-budget burn alerts
- [Design SLOs for Service Mesh](https://cloud.google.com/service-mesh/docs/observability/design-slo) - Google Cloud guidance for modeling SLOs around service-mesh traffic and request paths
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) - Broader reliability context for SLOs, alerting, and error-budget policy
- [Alerting in Cloud Monitoring](https://cloud.google.com/monitoring/alerts) - Supporting reference for notification policies, conditions, and alert routing
- [Anthos Service Mesh Observability](https://cloud.google.com/service-mesh/docs/observability) - Additional mesh metrics context for teams operating service-mesh-based workloads

## Estimated Time

- **Identify user journeys and SLIs**: 30-45 minutes
- **Verify or enable metrics and create the Monitoring Service**: 20-40 minutes
- **Define one SLO and validate the SLI graphs**: 15-30 minutes
- **Create fast- and slow-burn alerts and wire notifications**: 20-30 minutes
- **Build an SLO dashboard with supporting dependency views**: 20-40 minutes
- **First review and iteration after the initial run**: 20-30 minutes
- **Total for this lesson**: ~2-3 hours for a first complete SLO with alerting and dashboards, plus ongoing refinement
