from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import LoginRequest
from app.services.auth_client import AuthClient

router = APIRouter()
auth = AuthClient()


@router.post("/login")
async def login(payload: LoginRequest):
    token = await auth.login(
        payload.email,
        payload.password
    )

    if not token:
        raise HTTPException(401)

    return {"token": token}


@router.post("/refresh")
async def refresh(token: str):
    return await auth.refresh(token)