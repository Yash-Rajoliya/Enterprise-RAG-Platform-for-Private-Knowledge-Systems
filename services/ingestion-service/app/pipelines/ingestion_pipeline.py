from .preprocessing import Preprocessor
from .enrichment import EnrichmentPipeline
from ..chunking.adaptive import AdaptiveChunker


class IngestionPipeline:

    def __init__(self):
        self.pre = Preprocessor()
        self.chunker = AdaptiveChunker()
        self.enrich = EnrichmentPipeline()

    def run(
        self,
        text: str
    ):
        cleaned = self.pre.clean(text)

        chunks = self.chunker.split(cleaned)

        return [
            self.enrich.enrich(c)
            for c in chunks
        ]