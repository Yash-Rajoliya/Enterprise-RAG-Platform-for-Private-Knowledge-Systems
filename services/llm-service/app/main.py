from fastapi import FastAPI
from pydantic import BaseModel

from app.providers.openai_provider import (
    OpenAIProvider
)

from app.providers.local_llm import (
    LocalLLM
)

from app.providers.fallback import (
    FallbackProvider
)

from app.router.model_router import (
    ModelRouter
)

app = FastAPI()

router = ModelRouter()

provider = FallbackProvider(
    OpenAIProvider(),
    LocalLLM()
)


class GenerateRequest(
    BaseModel
):
    prompt: str
    complexity: int = 5


@app.post("/generate")
async def generate(
    req: GenerateRequest
):
    selected = router.route(
        req.complexity
    )

    result = await provider.generate(
        req.prompt
    )

    return {
        "provider": selected,
        "response": result
    }