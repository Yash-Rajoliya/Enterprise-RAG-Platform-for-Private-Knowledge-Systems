async def stream(
    text
):
    for token in text.split():
        yield token