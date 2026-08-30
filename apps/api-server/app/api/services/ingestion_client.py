class IngestionClient:

    async def ingest(
        self,
        file
    ):
        return {
            "filename":
            file.filename
        }