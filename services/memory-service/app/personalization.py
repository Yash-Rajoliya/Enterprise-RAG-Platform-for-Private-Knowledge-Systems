class PersonalizationEngine:

    def profile(
        self,
        interactions
    ):
        return {
            "total_interactions":
            len(interactions),

            "preferences":
            [
                "technical-depth",
                "low-latency"
            ]
        }