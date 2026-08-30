from docx import Document


class DocxLoader:

    def load(
        self,
        file_path: str
    ) -> str:

        doc = Document(file_path)

        return "\n".join(
            p.text
            for p in doc.paragraphs
        )