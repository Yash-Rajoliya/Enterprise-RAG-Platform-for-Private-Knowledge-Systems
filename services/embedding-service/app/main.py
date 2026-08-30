from fastapi import FastAPI
from pydantic import BaseModel

from app.providers.openai_embed import (
    OpenAIEmbedder
)

from app.providers.local_embed import (
    LocalEmbedder
)

from app.router.embedding_router import (
    EmbeddingRouter
)

app = FastAPI()

router = EmbeddingRouter()

openai_provider = OpenAIEmbedder()
local_provider = LocalEmbedder()


class EmbedRequest(
    BaseModel
):
    texts: list[str]


@app.post("/embed")
async def embed(
    req: EmbedRequest
):
    provider = router.route(
        len(req.texts)
    )

    if provider == "local":
        vectors = await local_provider.embed(
            req.texts
        )
    else:
        vectors = await openai_provider.embed(
            req.texts
        )

    return {
        "provider": provider,
        "vectors": vectors
    }