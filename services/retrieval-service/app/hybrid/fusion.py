class ReciprocalRankFusion:

    @staticmethod
    def fuse(*ranked_lists):
        scores = {}

        for result_set in ranked_lists:
            for rank, item in enumerate(result_set):
                doc = item[0]
                scores[doc] = scores.get(doc, 0) + 1 / (rank + 60)

        return sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )