from fastapi import (
    FastAPI,
    HTTPException
)

from pydantic import (
    BaseModel
)

from app.jwt import (
    JWTManager
)

from app.rbac import (
    RBAC
)

app = FastAPI()


class LoginRequest(
    BaseModel
):
    username: str
    role: str


@app.post("/login")
async def login(
    req: LoginRequest
):
    token = JWTManager.create_token(
        req.username,
        req.role
    )

    return {
        "access_token":
        token
    }


@app.get("/validate")
async def validate(
    token: str
):
    try:
        return JWTManager.decode(
            token
        )

    except Exception:
        raise HTTPException(
            401,
            "Invalid token"
        )


@app.get("/authorize")
async def authorize(
    token: str,
    action: str
):
    payload = JWTManager.decode(
        token
    )

    allowed = RBAC.allowed(
        payload["role"],
        action
    )

    return {
        "authorized":
        allowed
    }