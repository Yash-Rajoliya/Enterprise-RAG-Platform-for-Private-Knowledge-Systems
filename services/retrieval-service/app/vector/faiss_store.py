import faiss
import numpy as np


class FAISSStore:
    def __init__(self, dim: int = 1536):
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add(self, embeddings, docs):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.documents.extend(docs)

    def search(self, embedding, k=5):
        vec = np.array([embedding]).astype("float32")
        distances, ids = self.index.search(vec, k)

        return [
            {
                "doc": self.documents[i],
                "score": float(distances[0][idx])
            }
            for idx, i in enumerate(ids[0])
            if i != -1
        ]