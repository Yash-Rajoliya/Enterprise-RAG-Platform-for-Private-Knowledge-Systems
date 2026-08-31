from workers.celery_app import celery
import logging
import time


logger = logging.getLogger(
    __name__
)


@celery.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3}
)
def generate_embeddings(
    self,
    documents: list[str]
):

    logger.info(
        "starting embedding generation"
    )

    embeddings = []

    for doc in documents:

        time.sleep(0.1)

        embeddings.append({
            "document": doc,
            "embedding":
            [0.01] * 1536
        })

    logger.info(
        "embedding generation completed"
    )

    return {
        "status": "success",
        "count": len(embeddings),
        "embeddings": embeddings
    }