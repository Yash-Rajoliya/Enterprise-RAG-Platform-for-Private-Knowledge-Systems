from fastapi import FastAPI
from orchestrator.pipeline import Pipeline

app = FastAPI()
pipeline = Pipeline()


@app.post("/query")
async def query(
    payload: dict
):
    return await pipeline.run(
        payload["query"]
    )