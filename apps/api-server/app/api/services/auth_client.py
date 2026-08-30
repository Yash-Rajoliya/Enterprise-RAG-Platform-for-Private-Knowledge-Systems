from fastapi import APIRouter, Depends, HTTPException, Header, status
from app.schemas.auth import LoginRequest
from app.services.auth_client import AuthClient

router = APIRouter()

# Dependency function to provide AuthClient instance
def get_auth_client() -> AuthClient:
    return AuthClient()


@router.post("/login")
async def login(
    payload: LoginRequest,
    auth: AuthClient = Depends(get_auth_client)
):
    token = await auth.login(
        payload.email,
        payload.password
    )

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"access_token": token, "token_type": "bearer"}


@router.post("/refresh")
async def refresh(
    authorization: str = Header(..., alias="Authorization"),
    auth: AuthClient = Depends(get_auth_client)
):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token scheme"
        )
    
    token = authorization.split(" ")[1]
    new_token = await auth.refresh(token)
    
    if not new_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token refresh failed"
        )
        
    return {"access_token": new_token, "token_type": "bearer"}