import logging

from workers.tasks.indexing_task import (
    build_vector_index
)

logger = logging.getLogger(
    __name__
)


class IndexingPipeline:

    def run(
        self,
        tenant_id: str,
        embeddings: list
    ):

        logger.info(
            "starting indexing pipeline"
        )

        task = build_vector_index.delay(
            tenant_id,
            embeddings
        )

        logger.info(
            "index build queued"
        )

        return {
            "tenant_id":
            tenant_id,

            "task_id":
            task.id,

            "status":
            "indexing"
        }