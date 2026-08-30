import time
import logging

from starlette.middleware.base import (
    BaseHTTPMiddleware
)

logger = logging.getLogger()


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):
        start = time.time()

        response = await call_next(
            request
        )

        logger.info(
            f"{request.url} "
            f"{time.time()-start}"
        )

        return response