from fastapi import Header, HTTPException, status


async def get_tenant(
    x_tenant: str | None = Header(None, alias="X-Tenant-ID")
) -> str:
    if not x_tenant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="X-Tenant-ID header missing"
        )
    return x_tenant