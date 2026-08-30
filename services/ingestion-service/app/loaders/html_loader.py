from bs4 import BeautifulSoup


class HTMLLoader:

    def load(
        self,
        content: str
    ) -> str:

        soup = BeautifulSoup(
            content,
            "html.parser"
        )

        return soup.get_text()