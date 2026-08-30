class RouterAgent:

    async def route(
        self,
        query
    ):
        if "calculate" in query:
            return "tool"

        return "rag"