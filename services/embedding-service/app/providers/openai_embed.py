import os
from openai import AsyncOpenAI


class OpenAIEmbedder:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    async def embed(
        self,
        texts: list[str]
    ):
        response = await self.client.embeddings.create(
            model="text-embedding-3-large",
            input=texts
        )

        return [
            item.embedding
            for item in response.data
        ]