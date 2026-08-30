from openai import AsyncOpenAI
import os


class OpenAIProvider:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    async def generate(
        self,
        prompt: str,
        model: str = "gpt-4o"
    ):
        response = await self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    async def stream(
        self,
        prompt: str,
        model: str = "gpt-4o"
    ):
        stream = await self.client.chat.completions.create(
            model=model,
            stream=True,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        async for chunk in stream:
            if chunk.choices:
                yield chunk.choices[0].delta.content or ""