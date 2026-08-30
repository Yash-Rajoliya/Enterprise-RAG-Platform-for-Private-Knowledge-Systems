from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, corpus):
        tokenized = [d.split() for d in corpus]
        self.bm25 = BM25Okapi(tokenized)
        self.corpus = corpus

    def search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())
        ranked = sorted(
            zip(self.corpus, scores),
            key=lambda x: x[1],
            reverse=True
        )
        return ranked[:k]