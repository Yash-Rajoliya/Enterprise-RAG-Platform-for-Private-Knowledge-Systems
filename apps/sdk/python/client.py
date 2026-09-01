import requests
from typing import Dict

from .config import SDKConfig


class EnterpriseRAGClient:

    def __init__(
        self,
        config: SDKConfig
    ):
        self.config = config

        self.headers = {
            "Authorization":
            f"Bearer {config.api_key}"
        }

    def query(
        self,
        question: str,
        tenant_id: str
    ) -> Dict:

        response = requests.post(
            f"{self.config.api_url}/api/v1/query",
            json={
                "query": question,
                "tenant_id": tenant_id
            },
            headers=self.headers,
            timeout=self.config.timeout
        )

        response.raise_for_status()

        return response.json()

    def upload_document(
        self,
        file_path: str,
        tenant_id: str
    ):

        with open(
            file_path,
            "rb"
        ) as f:

            response = requests.post(
                (
                    f"{self.config.api_url}"
                    "/api/v1/ingestion/upload"
                ),
                files={
                    "file": f
                },
                data={
                    "tenant_id":
                    tenant_id
                },
                headers=self.headers
            )

        response.raise_for_status()

        return response.json()

    def health(self):

        response = requests.get(
            (
                f"{self.config.api_url}"
                "/api/v1/health"
            )
        )

        return response.json()