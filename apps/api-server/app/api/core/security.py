from jose import jwt

SECRET = "secret"


def sign(payload):
    return jwt.encode(
        payload,
        SECRET
    )


def verify(token):
    return jwt.decode(
        token,
        SECRET
    )