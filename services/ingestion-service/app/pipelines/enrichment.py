class EnrichmentPipeline:

    def enrich(
        self,
        chunk: str
    ):

        return {
            "content": chunk,
            "length": len(chunk)
        }