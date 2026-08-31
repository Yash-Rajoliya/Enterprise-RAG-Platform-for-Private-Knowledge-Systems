from authlib.integrations.starlette_client import (
    OAuth
)

oauth = OAuth()


def configure_oauth(
    app
):
    oauth.register(
        name="google",
        client_id="google-client-id",
        client_secret="google-secret",
        server_metadata_url=(
            "https://accounts.google.com/"
            ".well-known/openid-configuration"
        ),
        client_kwargs={
            "scope":
            "openid email profile"
        }
    )

    oauth.init_app(app)