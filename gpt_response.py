from openai import OpenAI
import os
from dotenv import load_dotenv

def response_from_gpt(messages: list) -> str:
    load_dotenv()
    client = OpenAI(
        api_key=os.getenv('CHATGPT_TOKEN'),
    )

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content