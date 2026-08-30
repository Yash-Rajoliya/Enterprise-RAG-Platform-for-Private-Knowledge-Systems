class QueryPlanner:

    async def create_plan(
        self,
        query: str
    ):
        return {
            "steps": [
                "retrieve",
                "reason",
                "validate",
                "respond"
            ],
            "query": query
        }