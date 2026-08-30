class AdaptiveChunker:

    def split(
        self,
        text: str
    ):
        size = 500 if len(text) < 5000 else 1500

        return [
            text[i:i+size]
            for i in range(
                0,
                len(text),
                size
            )
        ]