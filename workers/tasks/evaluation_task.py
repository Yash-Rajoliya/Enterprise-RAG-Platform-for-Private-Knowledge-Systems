from workers.celery_app import celery
import random


@celery.task
def evaluate_rag_response(
    question: str,
    answer: str,
    contexts: list[str]
):

    hallucination_score = round(
        random.uniform(0, 1),
        2
    )

    retrieval_score = round(
        random.uniform(0.5, 1),
        2
    )

    return {
        "question": question,

        "hallucination_score":
        hallucination_score,

        "retrieval_score":
        retrieval_score,

        "contexts_used":
        len(contexts)
    }