from fastapi import Header


async def get_tenant(
    x_tenant: str = Header()
):
    return x_tenant