from prometheus_client import (
    Counter,
    Histogram
)


REQUEST_COUNT = Counter(
    "rag_requests_total",
    "Total requests"
)

REQUEST_LATENCY = Histogram(
    "rag_request_latency_seconds",
    "Latency"
)


class Metrics:

    @staticmethod
    def record():
        REQUEST_COUNT.inc()

    @staticmethod
    def observe_latency(
        seconds: float
    ):
        REQUEST_LATENCY.observe(
            seconds
        )