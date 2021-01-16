import os
import discord
import random
from dotenv import load_dotenv

# .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

# Deck weights, themes, colors
SUG_NUM = 3
WILD_WEIGHT = 0.05
BAN_NUM = 2
END_WEIGHT = 0.45
NUM_PLAYERS = 2

colors = ["red", "black", "blue", "white", "green"]
color_emoticon = {
    "red": ":red_circle:",
    "black": ":new_moon:",
    "blue": ":blue_circle:",
    "white": ":white_circle:",
    "green": ":green_circle:"
}
keywords = {
    "red": ["knights", "goblins", "dragons", "instants", "satyrs", "warriors"],
    "black": ["deathtouch", "flying", "sacrifice", "enchantments", "graveyard", "heal", "mill", "vampire", "discard", "rogues", "knights", "zombies", "demons", "nightmare"],
    "blue": ["flying", "instants", "counter", "wizards", "rogues", "mill", "enchantments", "water", "scry"],
    "white": ["cats", "clerics", "knights", "enchantments", "flying", "humans", "dogs", "heal", "angels"],
    "green": ["counters", "landRamp", "spiders", "elves"],
    "wildcard": ["artifact", "party", "landfall", "colorless", "mutate", "adventure"]
}

# Function to roll a deck, with suggestions and bans, for a single player

def rollDeck(user, colorblind=False):
  # Choose Colors
  player_colors = set()
  picking_colors = True
  while picking_colors:
      cur_num = len(player_colors)
      if cur_num == 0:
          player_colors.add(random.choice(colors))
      elif cur_num == 1:
          player_colors.add(random.choice(colors))
      elif random.random() > END_WEIGHT:
          player_colors.add(random.choice(colors))

      if cur_num == len(player_colors):
          picking_colors = False

  # Choose Keywords
  player_themes = set()
  while len(player_themes) < SUG_NUM:
      player_themes.add(random.choice(keywords[random.choice(list(player_colors))]))
  if random.random() < WILD_WEIGHT:
      player_themes.add(random.choice(keywords["wildcard"]))

  # Choose Bans
  num_themes = 0
  for color in player_colors:
      num_themes += len(keywords[color])

  player_bans = set()
  while len(player_bans) < BAN_NUM:
      if num_themes == len(player_bans) + len(player_themes):
          break

      proposed_ban = random.choice(keywords[random.choice(list(player_colors))])
      if proposed_ban not in player_themes:
          player_bans.add(proposed_ban)

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
        await message.channel.send(response)

    if message.content == '!rolldeck-colorblind':
        user = str(message.author)
        response = rollDeck(user, True)
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
