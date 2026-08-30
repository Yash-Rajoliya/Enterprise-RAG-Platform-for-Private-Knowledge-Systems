from starlette.middleware.base import (
    BaseHTTPMiddleware
)


class TenantMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):
        request.state.tenant = (
            request.headers.get(
                "x-tenant"
            )
        )

        return await call_next(
            request
        )