from fastapi import APIRouter, UploadFile
from app.services.ingestion_client import (
    IngestionClient
)

router = APIRouter()
client = IngestionClient()


@router.post("/")
async def ingest(
    file: UploadFile
):
    return await client.ingest(file)