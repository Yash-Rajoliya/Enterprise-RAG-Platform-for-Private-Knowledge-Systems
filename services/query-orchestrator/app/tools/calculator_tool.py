class CalculatorTool:

    async def calculate(
        self,
        expr
    ):
        return eval(expr)