from openai import OpenAI
import os
from dotenv import load_dotenv

def response_from_gpt(messages: list) -> str:
    #calls .env file to load
    load_dotenv()
    #creats new instance for OpenAI
    client = OpenAI(
        #Takes Token and gives it to the OpenAI instance
        api_key=os.getenv('CHATGPT_TOKEN'),
    )

    #Using previous chat logs, the AI bases its response to the newest input
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )

    #Returns the text content of the response
    return chat_completion.choices[0].message.content