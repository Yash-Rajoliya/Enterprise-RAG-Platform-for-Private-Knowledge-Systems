from transformers import pipeline


class LocalLLM:

    def __init__(self):
        self.pipe = pipeline(
            "text-generation",
            model="mistralai/Mistral-7B-Instruct-v0.2"
        )

    async def generate(
        self,
        prompt
    ):
        result = self.pipe(
            prompt,
            max_new_tokens=512
        )

        return result[0]["generated_text"]