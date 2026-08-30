import logging
from .planner import QueryPlanner
from .executor import QueryExecutor
from .validator import Validator
from .reasoning import ReasoningAgent

logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(self):
        self.planner = QueryPlanner()
        self.executor = QueryExecutor()
        self.validator = Validator()
        self.reasoner = ReasoningAgent()

    async def run(self, query: str):
        try:
            plan = await self.planner.create_plan(query)
            raw_result = await self.executor.execute(plan)

            # Refine execution result through the reasoning flow
            reasoned_result = await self.reasoner.reason(
                query=query, plan=plan, execution_result=raw_result
            )

            # Validate final output
            is_valid = await self.validator.validate(reasoned_result)

            if not is_valid:
                logger.warning(
                    "Validation failed for reasoning output. Falling back to default handling."
                )

            return {
                "plan": plan,
                "result": reasoned_result,
                "valid": is_valid,
                "status": "success" if is_valid else "validation_failed",
            }
        except Exception as e:
            logger.error(f"Pipeline execution error: {str(e)}", exc_info=True)
            return {
                "plan": None,
                "result": None,
                "valid": False,
                "status": f"error: {str(e)}",
            }