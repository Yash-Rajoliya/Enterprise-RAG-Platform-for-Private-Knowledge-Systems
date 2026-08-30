class EmbeddingRouter:

    def route(
        self,
        size: int
    ):
        if size < 10:
            return "local"

        return "openai"