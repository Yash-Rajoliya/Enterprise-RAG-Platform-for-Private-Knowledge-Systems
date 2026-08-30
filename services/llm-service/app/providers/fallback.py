import logging

logger = logging.getLogger(__name__)


class FallbackProvider:

    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    async def generate(self, prompt: str):
        try:
            return await self.primary.generate(prompt)
        except Exception as primary_err:
            logger.warning(
                f"Primary provider failed: {primary_err}. Falling back to secondary provider."
            )
            try:
                return await self.secondary.generate(prompt)
            except Exception as secondary_err:
                logger.error(
                    f"Secondary provider also failed: {secondary_err}."
                )
                raise RuntimeError(
                    "Both primary and secondary providers failed to generate a response."
                ) from secondary_err