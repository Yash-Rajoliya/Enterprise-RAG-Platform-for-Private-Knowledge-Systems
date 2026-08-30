from pathlib import Path


class PromptRegistry:

    BASE = Path(
        "app/prompts/templates"
    )

    @classmethod
    def load(
        cls,
        name
    ):
        with open(
            cls.BASE / name
        ) as f:
            return f.read()