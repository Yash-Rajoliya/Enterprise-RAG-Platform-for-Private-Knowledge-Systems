from fastapi import APIRouter
from app.services.analytics_client import (
    AnalyticsClient
)

router = APIRouter()
analytics = AnalyticsClient()


@router.get("/metrics")
async def metrics():
    return await analytics.metrics()