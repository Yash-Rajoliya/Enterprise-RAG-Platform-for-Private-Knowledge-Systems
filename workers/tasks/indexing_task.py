from workers.celery_app import celery
import logging
import time


logger = logging.getLogger(
    __name__
)


@celery.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True
)
def build_vector_index(
    self,
    tenant_id: str,
    embeddings: list
):

    logger.info(
        f"building vector index for {tenant_id}"
    )

    time.sleep(2)

    index_id = (
        f"faiss-index-{tenant_id}"
    )

    logger.info(
        f"index ready {index_id}"
    )

    return {
        "status": "indexed",
        "tenant_id": tenant_id,
        "index_id": index_id
    }