from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.post("/retrieve")
async def retrieve(
    request: QueryRequest
):
    return {
        "results": [],
        "query": request.query
    }