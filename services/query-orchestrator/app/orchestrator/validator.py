class Validator:

    async def validate(
        self,
        output
    ):
        return output.get(
            "validated",
            False
        )