import discord
import configparser
import ollama

config = configparser.ConfigParser()

config.read('config.ini')

token=config["Discord"]["token"]

def generate(message):
    if not "llama3:8b" in ollama.list().get("models"): ollama.pull("llama3:8b")
    messages=[{"role":"user","content":message}]
    try:
        response=ollama.chat(model="llama3:8b",messages=messages)
    except:
        response={"message":{"content":"Error"}}
    return response.get("message",{}).get("content","Error")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Check if the message is from the specified channel
        target_channel_id = 1273808145143173207  # Replace with your channel ID
        if message.channel.id != target_channel_id:
            return  # Ignore messages not from the specified channel

        # Check if the message starts with the specific command
        if message.content.startswith("!bot-reply"):  # Replace with your command
            args = message.content.split()[1:]  # Split by spaces and skip the command itself
            if args:
                response = generate(" ".join(args))
            else:
                response = "No message."
            await message.channel.send(response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)