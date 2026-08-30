import httpx


class OrchestratorClient:

    async def query(
        self,
        query,
        tenant
    ):
        async with httpx.AsyncClient() as c:
            r = await c.post(
                "http://query-orchestrator/query",
                json={
                    "query": query,
                    "tenant": tenant
                }
            )
            return r.json()

    async def chat(
        self,
        session,
        msg
    ):
        return {
            "session": session,
            "response": msg
        }