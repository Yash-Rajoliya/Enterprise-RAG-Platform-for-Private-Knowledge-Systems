class CostTracker:

    PRICE_PER_1K = 0.03

    def calculate(
        self,
        tokens: int
    ):
        return (
            tokens / 1000
        ) * self.PRICE_PER_1K