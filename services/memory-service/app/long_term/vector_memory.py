import faiss
import numpy as np


class VectorMemory:

    def __init__(
        self,
        dim: int = 1536
    ):
        self.index = faiss.IndexFlatL2(
            dim
        )

        self.records = []

    def add(
        self,
        embedding,
        payload
    ):
        vec = np.array(
            [embedding]
        ).astype("float32")

        self.index.add(vec)

        self.records.append(
            payload
        )

    def search(
        self,
        embedding,
        k=5
    ):
        vec = np.array(
            [embedding]
        ).astype("float32")

        _, ids = self.index.search(
            vec,
            k
        )

        return [
            self.records[i]
            for i in ids[0]
            if i != -1
        ]