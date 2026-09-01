import time


class OnlineEvaluator:

    def track(
        self,
        latency: float,
        user_feedback: int
    ):

        return {
            "timestamp":
            time.time(),

            "latency":
            latency,

            "feedback":
            user_feedback,

            "healthy":
            latency < 3 and user_feedback > 0
        }