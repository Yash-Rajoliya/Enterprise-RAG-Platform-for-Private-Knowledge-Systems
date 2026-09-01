from locust import HttpUser, task


class RAGUser(HttpUser):

    @task
    def query(self):
        self.client.post(
            "/v1/query",
            json={"query": "enterprise rag"},
        )