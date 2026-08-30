class AuthClient:

    async def login(
        self,
        email,
        password
    ):
        return "jwt-token"

    async def refresh(
        self,
        token
    ):
        return {
            "token": token
        }