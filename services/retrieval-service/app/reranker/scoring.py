def normalize(scores):
    max_s = max(scores)

    return [
        s / max_s
        for s in scores
    ]