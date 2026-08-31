import logging
from datetime import datetime


logger = logging.getLogger(
    __name__
)


class ReindexingPipeline:

    def run(
        self,
        tenant_id: str
    ):

        logger.info(
            f"reindexing tenant {tenant_id}"
        )

        return {
            "tenant_id":
            tenant_id,

            "started_at":
            datetime.utcnow().isoformat(),

            "status":
            "reindexing"
        }