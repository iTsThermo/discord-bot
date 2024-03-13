from discord import Intents, Client, Message
from typing import Final
import os
from dotenv import load_dotenv
from gpt_response import response_from_gpt

#Load in our discord API token from .env file
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#Setup intents for the discord bot
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

logs_of_messages = [{"role": "system", "content": "You are an informative assistant. You will be helping programmers develope programs so be sure you give code and descriptive descriptions of that code."},]

#Takes in the users response and calls the response_from_gpt function from gpt_response.py
async def take_in_response_from_users(message: Message, user_message: str) -> None:
    #Checks if the message is empty
    if not user_message:
        print("Message was empty")

    #The command to talk to the bot is "."
    is_command = user_message[0] == '.'

    #removes the "." from the message to not confuse the gpt
    if is_command:
        user_message = user_message[1:]

    #try catch block to get a response and send the response back to the users channel
    try:
        if is_command:
            logs_of_messages.append({"role": "user", "content": user_message},)
            str_response_from_ai: list = response_from_gpt(logs_of_messages)
            await message.channel.send(str_response_from_ai)
            return str_response_from_ai
    except Exception as e:
            await message.channel.send(e)

    

#Notifies the user that the bot is up and running
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    try:
        str_response_from_ai = await take_in_response_from_users(message, user_message)
        logs_of_messages.append({"role": "system", "content": str_response_from_ai},)
    except Exception as e:
        print(f"An error occurred while processing the message: {e}")

#Runs the bot using the .run() function
def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()