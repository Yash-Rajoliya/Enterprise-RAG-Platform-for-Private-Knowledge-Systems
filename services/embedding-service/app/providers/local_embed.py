from sentence_transformers import (
    SentenceTransformer
)


class LocalEmbedder:

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-large-en"
        )

    async def embed(
        self,
        texts
    ):
        return self.model.encode(
            texts
        ).tolist()