# SLO Dashboard Lab - Local Monitoring Stack

A fully functional Docker Compose stack for learning SLO (Service Level Objective) monitoring without needing a cloud account. This lab gives you hands-on experience with Prometheus metrics, recording rules, error budgets, and burn rate alerting.

## What This Stack Does

- **App**: A Python HTTP server that exposes Prometheus metrics and has endpoints with realistic failure/latency characteristics
- **Prometheus**: Scrapes the app metrics, evaluates SLI recording rules, and calculates error budgets and burn rates
- **Grafana**: Visualizes SLIs, error budgets, and burn rates on a pre-built dashboard
- **Load Generator**: Continuously sends traffic to the app so you see real data immediately

## Architecture

```
load-generator --> app:8080 (/  /api/data  /api/submit)
                      |
                      | /metrics
                      v
                prometheus:9090
                      |
                      | datasource
                      v
                grafana:3000
```

## Prerequisites

- Docker and Docker Compose (v2)
- ~512MB free RAM
- Ports 3000, 8080, 9090 available

## Quick Start

```bash
docker compose up --build
```

Then open:

| Service    | URL                        |
|------------|----------------------------|
| Grafana    | http://localhost:3000       |
| Prometheus | http://localhost:9090       |
| App        | http://localhost:8080       |

Grafana credentials: `admin` / `admin` (skip the password change prompt).

Navigate to **Dashboards > SLO Dashboard** to see the panels.

## What to Observe

1. **Availability SLI** - Watch the ratio of successful (non-5xx) requests. The app returns 500 errors ~2% of the time on POST /api/submit.
2. **Latency SLI** - Ratio of requests completing under 300ms. About 5% of GET /api/data requests are artificially slow.
3. **Error Budget** - Starts at 100% and depletes as errors accumulate. With a 99.5% SLO target, you have a 0.5% error budget.
4. **Burn Rate** - How fast the error budget is being consumed. A burn rate of 1.0 means the budget will last exactly the SLO window.

## Exercises

1. Increase the error rate: edit `app/server.py` and change the failure probability, then rebuild with `docker compose up --build app`. Watch the error budget drain faster.
2. Change the SLO target in `rules/sli-recording-rules.yml` and reload Prometheus (`curl -X POST http://localhost:9090/-/reload`).
3. Add a new endpoint with different latency characteristics and create a recording rule for it.

## Stopping

```bash
docker compose down
```

To also remove stored data:

```bash
docker compose down -v
```
