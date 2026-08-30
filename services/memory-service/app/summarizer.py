class SessionSummarizer:

    async def summarize(
        self,
        messages: list[str]
    ):
        joined = "\n".join(
            messages
        )

        return joined[:1000]