from typing import List
import statistics


class OfflineEvaluator:

    def evaluate(
        self,
        scores: List[float]
    ):

        if not scores:
            return {
                "average_score": 0
            }

        return {
            "average_score":
            round(
                statistics.mean(scores),
                3
            ),

            "max_score":
            max(scores),

            "min_score":
            min(scores)
        }