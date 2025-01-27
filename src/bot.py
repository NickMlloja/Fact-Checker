import discord
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

TRUE_EMOJI = "true:1333475095401730273"
FALSE_EMOJI = "false:1333475249911627828"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

debug = False


async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):

    if client.user in message.mentions:

        print(message.content)

        if debug:
            print("Bot mentioned.")

        reaction = False
        truth_value = 0
        for char in message.content:

            if debug:
                print(f"Char {char} has unicode value {ord(char)}")

            truth_value += ord(char)

        if truth_value % 2 == 0:
            reaction = True

        if debug:
            print(f"Truth-Value: {truth_value}\tReaction: {reaction}")

        if reaction:
            await message.add_reaction(f"<:{TRUE_EMOJI}>")
        else:
            await message.add_reaction(f"<:{FALSE_EMOJI}>")


client.run(BOT_TOKEN)
