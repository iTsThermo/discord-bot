from openai import OpenAI
import os
from dotenv import load_dotenv

def response_from_gpt(user_input) -> str:
    load_dotenv()
    client = OpenAI(
        api_key=os.getenv('CHATGPT_TOKEN'),
    )

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user", "content": user_input,
        }
    ],
    model="gpt-3.5-turbo",
    )
    print(chat_completion)
    return chat_completion.choices[0].message.content