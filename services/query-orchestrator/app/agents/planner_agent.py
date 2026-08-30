class PlannerAgent:

    async def run(
        self,
        query
    ):
        return {
            "task_graph": [
                "semantic_search",
                "rerank",
                "llm"
            ]
        }