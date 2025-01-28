# Fact-Checker
A discord bot that arbitrarily but deterministically applies the True or False Morgan Freeman reaction. 

# Usage
- Add a `.env` file to the root, and add your own bot token (formatted as `BOT_TOKEN = ""`) using discords application bot account.
   - The bot will need permissions to read messages and add reactions.
   - The bot will also need emojis called "true" and "false", and you may need to update the emoji-ids in `bot.py`.
   - Learn more [here](https://discordpy.readthedocs.io/en/stable/discord.html).


# Scripts
- From the root run `./.venv/Scripts/Activate` to activate the virtual environment.
- From the root run `python src/bot.py` to launch the bot. There is a debug variable to print some extra info.
- From the root run `python scripts/clean.py` to format and lint scripts and src.
