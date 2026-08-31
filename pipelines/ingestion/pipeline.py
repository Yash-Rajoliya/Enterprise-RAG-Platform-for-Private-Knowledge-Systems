import logging
from typing import List

from workers.tasks.embedding_task import (
    generate_embeddings
)

logger = logging.getLogger(
    __name__
)


class IngestionPipeline:

    def __init__(
        self,
        tenant_id: str
    ):
        self.tenant_id = tenant_id

    def run(
        self,
        documents: List[str]
    ):

        logger.info(
            "starting ingestion pipeline"
        )

        task = generate_embeddings.delay(
            documents
        )

        logger.info(
            "embedding task queued"
        )

        return {
            "tenant_id":
            self.tenant_id,

            "task_id":
            task.id,

            "status":
            "processing"
        }