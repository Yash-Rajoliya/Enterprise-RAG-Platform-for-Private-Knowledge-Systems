class QueryExecutor:

    async def execute(
        self,
        plan
    ):
        return {
            "retrieved_docs": [],
            "reasoning": "completed",
            "validated": True
        }