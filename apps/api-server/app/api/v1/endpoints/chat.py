from fastapi import APIRouter
from app.schemas.request import ChatRequest
from app.services.orchestrator_client import (
    OrchestratorClient
)

router = APIRouter()
client = OrchestratorClient()


@router.post("/")
async def chat(
    payload: ChatRequest
):
    return await client.chat(
        payload.session_id,
        payload.message
    )