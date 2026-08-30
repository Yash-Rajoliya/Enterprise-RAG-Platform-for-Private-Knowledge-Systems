import os
import json
import redis.asyncio as redis


class RedisMemory:

    def __init__(self):
        self.client = redis.from_url(
            os.getenv(
                "REDIS_URL",
                "redis://localhost:6379"
            )
        )

    async def save(
        self,
        session_id: str,
        data: dict
    ):
        await self.client.set(
            session_id,
            json.dumps(data)
        )

    async def get(
        self,
        session_id: str
    ):
        value = await self.client.get(
            session_id
        )

        if not value:
            return None

        return json.loads(value)

    async def delete(
        self,
        session_id: str
    ):
        await self.client.delete(
            session_id
        )