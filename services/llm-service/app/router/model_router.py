class ModelRouter:

    def route(
        self,
        complexity: int
    ):
        if complexity < 4:
            return "local"

        return "openai"