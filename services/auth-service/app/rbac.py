class RBAC:

    permissions = {
        "admin": [
            "read",
            "write",
            "delete"
        ],
        "user": [
            "read",
            "write"
        ],
        "viewer": [
            "read"
        ]
    }

    @classmethod
    def allowed(
        cls,
        role: str,
        action: str
    ):
        return (
            action
            in cls.permissions.get(
                role,
                []
            )
        )