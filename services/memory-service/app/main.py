from fastapi import FastAPI
from pydantic import BaseModel

from app.short_term.redis_memory import (
    RedisMemory
)

from app.summarizer import (
    SessionSummarizer
)

app = FastAPI()

memory = RedisMemory()
summarizer = SessionSummarizer()


class MemoryRequest(
    BaseModel
):
    session_id: str
    payload: dict


@app.post("/save")
async def save(
    req: MemoryRequest
):
    await memory.save(
        req.session_id,
        req.payload
    )

    return {
        "saved": True
    }


@app.get("/get/{session_id}")
async def get(
    session_id: str
):
    return await memory.get(
        session_id
    )


@app.post("/summarize")
async def summarize(
    messages: list[str]
):
    return {
        "summary":
        await summarizer.summarize(
            messages
        )
    }