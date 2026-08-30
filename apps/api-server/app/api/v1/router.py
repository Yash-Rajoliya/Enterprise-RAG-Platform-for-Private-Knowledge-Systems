from fastapi import APIRouter

from .endpoints import (
    auth,
    query,
    chat,
    ingestion,
    admin,
    health
)

router = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth"
)

router.include_router(
    query.router,
    prefix="/query"
)

router.include_router(
    chat.router,
    prefix="/chat"
)

router.include_router(
    ingestion.router,
    prefix="/ingest"
)

router.include_router(
    admin.router,
    prefix="/admin"
)

router.include_router(
    health.router,
    prefix="/health"
)