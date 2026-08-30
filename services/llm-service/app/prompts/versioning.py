from pathlib import Path


class PromptVersioning:

    BASE = Path(
        "app/prompts/templates"
    )

    @classmethod
    def load(
        cls,
        name: str
    ):
        return (
            cls.BASE / name
        ).read_text()