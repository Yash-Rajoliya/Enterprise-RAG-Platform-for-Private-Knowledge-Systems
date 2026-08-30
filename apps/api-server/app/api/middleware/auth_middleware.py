from starlette.middleware.base import (
    BaseHTTPMiddleware
)


class AuthMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):
        request.state.user = "user"
        return await call_next(
            request
        )