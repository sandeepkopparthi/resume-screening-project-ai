from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class LLMService:
    """
    Generic service responsible only for communicating with the Groq API.
    """

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY environment variable not found."
            )

        self.client = Groq(api_key=api_key)

        self.model = os.getenv(
            "MODEL_NAME",
            "llama-3.3-70b-versatile"
        )

    def generate(self, messages: list[dict],temperature:float=0) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature
        )

        return response.choices[0].message.content