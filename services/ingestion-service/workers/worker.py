import asyncio


class Worker:

    async def process(
        self,
        func,
        *args
    ):
        return await asyncio.to_thread(
            func,
            *args
        )