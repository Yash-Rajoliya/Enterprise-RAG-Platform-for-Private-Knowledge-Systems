class CostEstimator:

    def estimate(
        self,
        prompt_tokens,
        completion_tokens
    ):
        total = (
            prompt_tokens
            + completion_tokens
        )

        return {
            "tokens": total,
            "estimated_cost":
            total * 0.00003
        }