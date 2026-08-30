class FallbackProvider:

    def __init__(
        self,
        primary,
        secondary
    ):
        self.primary = primary
        self.secondary = secondary

    async def generate(
        self,
        prompt
    ):
        try:
            return await self.primary.generate(
                prompt
            )

        except Exception:
            return await self.secondary.generate(
                prompt
            )