from dataclasses import dataclass


@dataclass
class SDKConfig:

    api_url: str = (
        "http://localhost:8000"
    )

    api_key: str = ""

    timeout: int = 30

    retries: int = 3