from fastapi import FastAPI
import time

from app.logging.logger import (
    get_logger
)

from app.metrics.metrics import (
    Metrics
)

from app.cost.estimator import (
    CostEstimator
)

app = FastAPI()

logger = get_logger(
    "analytics"
)

estimator = CostEstimator()


@app.get("/health")
async def health():
    start = time.time()

    Metrics.record()

    latency = time.time() - start

    Metrics.observe_latency(
        latency
    )

    logger.info(
        "health check"
    )

    return {
        "status": "ok",
        "latency": latency
    }


@app.post("/estimate")
async def estimate(
    payload: dict
):
    return estimator.estimate(
        payload["prompt_tokens"],
        payload["completion_tokens"]
    )