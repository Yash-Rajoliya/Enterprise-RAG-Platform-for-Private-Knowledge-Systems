class SemanticChunker:

    def split(
        self,
        text: str
    ):
        return text.split("\n\n")