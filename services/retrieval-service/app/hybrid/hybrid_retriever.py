from .fusion import ReciprocalRankFusion


class HybridRetriever:

    def __init__(self, vector_store, bm25):
        self.vector_store = vector_store
        self.bm25 = bm25

    def retrieve(self, embedding, query):
        dense = self.vector_store.search(embedding)
        sparse = self.bm25.search(query)

        return ReciprocalRankFusion.fuse(
            [(d["doc"], d["score"]) for d in dense],
            sparse
        )