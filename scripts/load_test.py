import asyncio
import httpx


async def run():
    async with httpx.AsyncClient() as client:
        for _ in range(100):
            await client.post(
                "http://localhost:8000/v1/query",
                json={"query": "test"},
            )


asyncio.run(run())