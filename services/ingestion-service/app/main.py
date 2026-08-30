from fastapi import FastAPI, UploadFile
from .pipelines.ingestion_pipeline import (
    IngestionPipeline
)

app = FastAPI()
pipeline = IngestionPipeline()


@app.post("/ingest")
async def ingest(
    file: UploadFile
):
    content = await file.read()

    chunks = pipeline.run(
        content.decode()
    )

    return {
        "chunks": len(chunks)
    }