import httpx


class APILoader:

    async def load(
        self,
        url: str
    ):

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        return response.text