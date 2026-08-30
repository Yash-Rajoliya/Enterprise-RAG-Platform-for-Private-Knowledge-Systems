from pathlib import Path


class LocalStorage:

    def save(
        self,
        content,
        path
    ):
        Path(path).write_text(content)