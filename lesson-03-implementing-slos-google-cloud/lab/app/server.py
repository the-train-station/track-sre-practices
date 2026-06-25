"""Simple HTTP server that exposes Prometheus metrics for SLO monitoring lab."""

import random
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST,
)

# Metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.5],
)


class MetricsHandler(BaseHTTPRequestHandler):
    """HTTP handler with endpoints that simulate realistic behavior."""

    def do_GET(self):
        if self.path == "/metrics":
            self._serve_metrics()
        elif self.path == "/api/data":
            self._handle_api_data()
        elif self.path == "/":
            self._handle_root()
        else:
            self._respond(404, "Not Found")
            REQUEST_COUNT.labels("GET", self.path, "404").inc()

    def do_POST(self):
        if self.path == "/api/submit":
            self._handle_api_submit()
        else:
            self._respond(404, "Not Found")
            REQUEST_COUNT.labels("POST", self.path, "404").inc()

    def _handle_root(self):
        """Always succeeds quickly."""
        start = time.time()
        time.sleep(random.uniform(0.005, 0.02))
        self._respond(200, '{"status": "ok"}')
        duration = time.time() - start
        REQUEST_COUNT.labels("GET", "/", "200").inc()
        REQUEST_DURATION.labels("GET", "/").observe(duration)

    def _handle_api_data(self):
        """5% of requests are slow (over 300ms)."""
        start = time.time()
        if random.random() < 0.05:
            # Slow request: 400-800ms
            time.sleep(random.uniform(0.4, 0.8))
        else:
            # Normal request: 10-50ms
            time.sleep(random.uniform(0.01, 0.05))
        self._respond(200, '{"data": [1, 2, 3]}')
        duration = time.time() - start
        REQUEST_COUNT.labels("GET", "/api/data", "200").inc()
        REQUEST_DURATION.labels("GET", "/api/data").observe(duration)

    def _handle_api_submit(self):
        """2% of requests return 500."""
        start = time.time()
        time.sleep(random.uniform(0.02, 0.08))
        if random.random() < 0.02:
            self._respond(500, '{"error": "internal server error"}')
            duration = time.time() - start
            REQUEST_COUNT.labels("POST", "/api/submit", "500").inc()
        else:
            self._respond(200, '{"accepted": true}')
            duration = time.time() - start
            REQUEST_COUNT.labels("POST", "/api/submit", "200").inc()
        REQUEST_DURATION.labels("POST", "/api/submit").observe(duration)

    def _serve_metrics(self):
        """Expose Prometheus metrics."""
        output = generate_latest()
        self.send_response(200)
        self.send_header("Content-Type", CONTENT_TYPE_LATEST)
        self.send_header("Content-Length", str(len(output)))
        self.end_headers()
        self.wfile.write(output)

    def _respond(self, status, body):
        """Send a JSON response."""
        encoded = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format, *args):
        """Suppress default request logging to keep output clean."""
        pass


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), MetricsHandler)
    print("App server running on :8080")
    server.serve_forever()
