class RecursiveChunker:

    def split(
        self,
        text: str,
        size: int = 1000
    ):

        return [
            text[i:i + size]
            for i in range(
                0,
                len(text),
                size
            )
        ]