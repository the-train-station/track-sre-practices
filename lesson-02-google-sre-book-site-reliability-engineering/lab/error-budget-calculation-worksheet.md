# Error Budget Calculation Worksheet

## Concepts

An **error budget** is the maximum amount of unreliability your service is allowed, derived from the SLO target. It quantifies how much failure is acceptable and creates a shared currency for product/reliability tradeoffs.

**Key formula:**

```
Error Budget = 1 - SLO Target
```

If your SLO is 99.9%, your error budget is 0.1% of requests (or time) that are allowed to fail.

---

## Formula Reference

### Availability Error Budget

```
Allowed Downtime = (1 - SLO) x Time Window

Example (30-day window):
  SLO = 99.9%
  Allowed downtime = (1 - 0.999) x 30 days x 24 hrs x 60 min
                   = 0.001 x 43,200 min
                   = 43.2 minutes/month
```

### Request-Based Error Budget

```
Allowed Failed Requests = (1 - SLO) x Total Requests

Example:
  SLO = 99.95%
  Total requests in window = 10,000,000
  Allowed failures = (1 - 0.9995) x 10,000,000
                   = 0.0005 x 10,000,000
                   = 5,000 failed requests
```

### Error Budget Consumption

```
Budget Consumed (%) = (Actual Bad Events / Allowed Bad Events) x 100

Example:
  Allowed failures = 5,000
  Actual failures this period = 3,200
  Budget consumed = (3,200 / 5,000) x 100 = 64%
  Budget remaining = 36%
```

### Burn Rate

Burn rate measures how fast you are consuming your error budget relative to the expected steady-state rate.

```
Burn Rate = (Actual Error Rate) / (SLO Error Rate)

Where:
  SLO Error Rate = 1 - SLO Target

Example:
  SLO = 99.9% (SLO Error Rate = 0.1%)
  Current error rate = 0.5%
  Burn Rate = 0.5% / 0.1% = 5x

Interpretation: At 5x burn rate, you will exhaust your 30-day
error budget in 30/5 = 6 days.
```

### Time to Budget Exhaustion

```
Time to Exhaustion = (Budget Remaining %) / Burn Rate x Window Duration

Example:
  Budget remaining = 80%
  Burn rate = 3x
  Window = 30 days
  Time to exhaustion = 0.80 / 3 x 30 = 8 days
```

### Multi-Window Burn Rate Alerts

Multiple windows catch both fast-burning and slow-burning problems:

| Alert Severity | Long Window | Short Window | Burn Rate | Budget Consumed (if sustained for long window) |
|---------------|-------------|--------------|-----------|----------------------------------------------|
| Page (critical) | 1 hour | 5 minutes | 14.4x | 2% in 1 hour |
| Page (critical) | 6 hours | 30 minutes | 6x | 5% in 6 hours |
| Ticket (warning) | 3 days | 6 hours | 1x | 10% in 3 days |

**Logic for multi-window alert:**

```
Alert fires when:
  burn_rate(long_window) > threshold
  AND
  burn_rate(short_window) > threshold
```

The short window confirms the problem is still happening (not a brief spike that already resolved).

---

## Worked Example 1: Availability SLO (99.9%)

**Service:** Payment API
**SLO:** 99.9% availability over a 30-day rolling window
**SLI:** Proportion of HTTP requests that return a non-5xx response within 500ms

### Step 1: Calculate the Error Budget

```
Error Budget = 1 - 0.999 = 0.001 (0.1%)

In time:    0.001 x 30 days x 24 hours x 60 min = 43.2 minutes
In requests: 0.001 x 12,000,000 requests/month = 12,000 allowed failures
```

### Step 2: Track Consumption (Week 1)

| Day | Total Requests | Failed Requests | Daily Error Rate |
|-----|---------------|-----------------|------------------|
| 1 | 400,000 | 120 | 0.030% |
| 2 | 420,000 | 95 | 0.023% |
| 3 | 390,000 | 2,100 | 0.538% |
| 4 | 410,000 | 180 | 0.044% |
| 5 | 430,000 | 110 | 0.026% |
| 6 | 380,000 | 90 | 0.024% |
| 7 | 400,000 | 105 | 0.026% |

**Week 1 totals:** 2,830,000 requests, 2,800 failures

```
Budget consumed = 2,800 / 12,000 = 23.3%
Budget remaining = 76.7%
Days remaining in window = 23
```

### Step 3: Assess Burn Rate on Day 3

```
Day 3 error rate = 0.538%
SLO error rate = 0.1%
Burn rate on Day 3 = 0.538% / 0.1% = 5.38x

Time to exhaustion at that rate = (1.0 / 5.38) x 30 = 5.6 days
```

**Decision:** Day 3's burn rate would trigger a page alert (exceeds 6x over a short window). The team should investigate the cause of the 2,100 failures.

### Step 4: Alert Configuration

```yaml
# Prometheus alerting rules for this SLO
groups:
  - name: payment_api_slo
    rules:
      - alert: PaymentAPIHighBurnRate_Critical
        expr: |
          (
            sum(rate(http_requests_total{service="payment-api",code=~"5.."}[1h]))
            /
            sum(rate(http_requests_total{service="payment-api"}[1h]))
          ) > (14.4 * 0.001)
          and
          (
            sum(rate(http_requests_total{service="payment-api",code=~"5.."}[5m]))
            /
            sum(rate(http_requests_total{service="payment-api"}[5m]))
          ) > (14.4 * 0.001)
        labels:
          severity: critical

      - alert: PaymentAPIHighBurnRate_Warning
        expr: |
          (
            sum(rate(http_requests_total{service="payment-api",code=~"5.."}[6h]))
            /
            sum(rate(http_requests_total{service="payment-api"}[6h]))
          ) > (6 * 0.001)
          and
          (
            sum(rate(http_requests_total{service="payment-api",code=~"5.."}[30m]))
            /
            sum(rate(http_requests_total{service="payment-api"}[30m]))
          ) > (6 * 0.001)
        labels:
          severity: warning
```

---

## Worked Example 2: Latency SLO (99th Percentile)

**Service:** Search API
**SLO:** 99% of requests complete within 200ms over a 7-day rolling window
**SLI:** Proportion of requests with latency <= 200ms

### Step 1: Calculate the Error Budget

```
Error Budget = 1 - 0.99 = 0.01 (1%)

In requests: 0.01 x 5,000,000 requests/week = 50,000 allowed slow requests
```

### Step 2: Track Consumption

| Day | Total Requests | Slow Requests (>200ms) | Daily Slow Rate |
|-----|---------------|----------------------|-----------------|
| 1 | 700,000 | 4,200 | 0.60% |
| 2 | 720,000 | 4,500 | 0.63% |
| 3 | 680,000 | 12,000 | 1.76% |
| 4 | 710,000 | 5,100 | 0.72% |
| 5 | 750,000 | 4,800 | 0.64% |

**5-day totals:** 3,560,000 requests, 30,600 slow requests

```
Budget consumed = 30,600 / 50,000 = 61.2%
Budget remaining = 38.8%
Days remaining in window = 2
```

### Step 3: Forecast

```
Average daily slow requests (excluding Day 3 anomaly) = ~4,650
Projected remaining consumption = 4,650 x 2 = 9,300
Projected total = 30,600 + 9,300 = 39,900

39,900 / 50,000 = 79.8% budget consumed by end of window
```

**Decision:** Even with the Day 3 incident, the service will likely stay within budget. However, the Day 3 burn rate (1.76x) merits investigation to prevent recurrence.

---

## Worked Example 3: Combined SLO (Availability + Latency)

**Service:** User Profile API
**SLOs:**
- Availability: 99.95% of requests return non-error responses (30-day window)
- Latency: 99% of successful requests complete within 100ms (30-day window)

### Step 1: Calculate Both Error Budgets

```
Availability budget:
  (1 - 0.9995) x 20,000,000 requests/month = 10,000 allowed errors

Latency budget:
  (1 - 0.99) x 19,990,000 successful requests/month = 199,900 allowed slow requests
```

### Step 2: Independent Tracking

| Metric | Budget | Consumed | Remaining | Status |
|--------|--------|----------|-----------|--------|
| Availability | 10,000 errors | 3,400 (34%) | 6,600 (66%) | Healthy |
| Latency | 199,900 slow | 145,000 (72.5%) | 54,900 (27.5%) | At Risk |

### Step 3: Decision Framework

```
Combined health = min(availability_remaining, latency_remaining)
                = min(66%, 27.5%)
                = 27.5% (driven by latency)
```

**Decision:** The latency SLO is the binding constraint. The team should:
1. Investigate the cause of elevated latency (likely database or cache performance)
2. Consider freezing non-critical deployments until the latency budget recovers
3. If the problem persists, trigger an error-budget policy review

---

## Practice Problems

Complete these calculations on your own:

### Problem 1

Your API has a 99.99% availability SLO over a 30-day window. You serve 50 million requests per month. On Day 12, a bad deploy causes 3,000 errors over 45 minutes before rollback.

- What is your total error budget in requests?
- What percentage of budget did this incident consume?
- What was the burn rate during the 45-minute incident?

### Problem 2

Your SLO is 99.5% of requests under 500ms (28-day window). You serve 1 million requests per day. Your current 14-day rolling consumption is 62%.

- How many slow requests have you had in the first 14 days?
- At the current average daily rate, will you exhaust your budget before the window resets?
- What burn rate threshold should trigger a warning alert?

### Problem 3

Design multi-window burn rate alerts for a 99.9% availability SLO over a 30-day window. Define the thresholds for:

- Critical page (should fire when 2% of budget consumed in 1 hour)
- Warning page (should fire when 5% of budget consumed in 6 hours)
- Ticket (should fire when 10% of budget consumed in 3 days)

Show your burn rate calculations.
