import os
import dotenv
from openai import OpenAI


dotenv.load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found in the .env file."
    )


llm = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)


def bot(messages):

    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
    )

    return response.choices[0].message.content