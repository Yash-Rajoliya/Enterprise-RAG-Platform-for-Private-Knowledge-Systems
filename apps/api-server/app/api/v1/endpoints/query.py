from fastapi import APIRouter
from app.schemas.request import QueryRequest
from app.services.orchestrator_client import (
    OrchestratorClient
)

router = APIRouter()
client = OrchestratorClient()


@router.post("/")
async def query(
    payload: QueryRequest
):
    return await client.query(
        payload.query,
        payload.tenant_id
    )