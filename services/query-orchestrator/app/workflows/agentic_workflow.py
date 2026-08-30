class AgenticWorkflow:

    async def run(
        self,
        query
    ):
        return {
            "agentic":
            True,
            "query":
            query
        }