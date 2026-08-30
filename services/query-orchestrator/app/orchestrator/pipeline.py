from .planner import QueryPlanner
from .executor import QueryExecutor
from .validator import Validator


class Pipeline:

    def __init__(self):
        self.planner = QueryPlanner()
        self.executor = QueryExecutor()
        self.validator = Validator()

    async def run(
        self,
        query
    ):
        plan = await self.planner.create_plan(query)

        result = await self.executor.execute(
            plan
        )

        valid = await self.validator.validate(
            result
        )

        return {
            "plan": plan,
            "result": result,
            "valid": valid
        }