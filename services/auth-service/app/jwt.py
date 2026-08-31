import os
import jwt
from datetime import (
    datetime,
    timedelta
)

SECRET = os.getenv(
    "JWT_SECRET",
    "super-secret-key"
)

ALGORITHM = "HS256"


class JWTManager:

    @staticmethod
    def create_token(
        subject: str,
        role: str
    ):
        payload = {
            "sub": subject,
            "role": role,
            "exp": datetime.utcnow()
            + timedelta(hours=12)
        }

        return jwt.encode(
            payload,
            SECRET,
            algorithm=ALGORITHM
        )

    @staticmethod
    def decode(
        token: str
    ):
        return jwt.decode(
            token,
            SECRET,
            algorithms=[
                ALGORITHM
            ]
        )