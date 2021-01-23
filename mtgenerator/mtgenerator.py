import os
import discord
import random
from dotenv import load_dotenv
from gen_suggestion

# .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

# Function to roll a deck, with suggestions and bans, for a single player

def rollDeck(user, colorblind=False):

  # assemble return string
  introLine = ":crossed_swords: \n" "Deck prompt for "+ user + "\n"

  colorLine = "Colors: "
  for color in player_colors:
    if colorblind:
        colorLine += color + " "
    else:
        colorLine += color_emoticon[color] + "  "
  colorLine += "\n"

  suggestionsLine = "Themes:  " + ' '.join(player_themes) + "\n"
  banLine = "Bans:  " + ' '.join(player_bans) + "\n"

  ret = introLine + colorLine + suggestionsLine + banLine
  return(ret)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!rolldeck':
        user = str(message.author)
        response = rollDeck(user)
        print(response)
        await message.channel.send(response)

    if message.content == '!rolldeck-colorblind':
        user = str(message.author)
        response = rollDeck(user, True)
        print(response)
        await message.channel.send(response)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            print(
                f'{client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
            break

client.run(TOKEN)
