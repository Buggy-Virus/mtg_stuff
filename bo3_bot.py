import discord
import random
from dotenv import load_dotenv

# discord API
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# Deck weights, themes, colors
SUG_NUM = 3
WILD_WEIGHT = 0.05
BAN_NUM = 2
END_WEIGHT = 0.45
NUM_PLAYERS = 2

colors = ["red", "black", "blue", "white", "green"]
keywords = {
    "red": ["knights", "goblins", "dragons", "instants", "satyrs", "warriors"],
    "black": ["deathtouch", "flying", "sacrifice", "enchantments", "graveyard", "heal", "mill", "vampire", "discard", "rogues", "knights", "zombies", "demons", "nightmare"],
    "blue": ["flying", "instants", "counter", "wizards", "rogues", "mill", "enchantments", "water", "scry"],
    "white": ["cats", "clerics", "knights", "enchantments", "flying", "humans", "dogs", "heal", "angels"],
    "green": ["counters", "landRamp", "spiders", "elves"],
    "wildcard": ["artifact", "party", "landfall", "colorless", "mutate", "adventure"]
}

# Function to roll a deck, with suggestions and bans, for a single player

def rollDeck():
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
  player_suggestions = set()
  while len(player_suggestions) < SUG_NUM:
      player_suggestions.add(random.choice(keywords[random.choice(list(player_colors))]))
  if random.random() < WILD_WEIGHT:
      player_suggestions.add(random.choice(keywords["wildcard"]))

  # Choose Bans
  num_themes = 0
  for color in player_colors:
      num_themes += len(keywords[color])

  player_bans = set()
  while len(player_bans) < BAN_NUM:
      if num_themes == len(player_bans) + len(player_suggestions):
          break

      proposed_ban = random.choice(keywords[random.choice(list(player_colors))])
      if proposed_ban not in player_suggestions:
          player_bans.add(proposed_ban)

  # TODO set user name
  introLine = "Deck Prompt"
  colorLine = "Colors:" + ' '.join(player_colors)
  suggestionsLine = "Suggestions:" + ' '.join(player_suggestions)
  banLine = "Bans:" + ' '.join(player_bans)

  ret = introLine + colorLine + suggestionsLine + banLine
  return(ret)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!rolldeck':
        response = rollDeck()
        await message.channel.send(response)

client.run(TOKEN)
