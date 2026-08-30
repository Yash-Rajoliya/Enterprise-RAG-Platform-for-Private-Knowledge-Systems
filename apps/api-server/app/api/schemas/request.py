from pydantic import BaseModel


class QueryRequest(
    BaseModel
):
    query: str
    tenant_id: str


class ChatRequest(
    BaseModel
):
    session_id: str
    message: str