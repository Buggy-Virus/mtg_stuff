import csv
import os
import sys
import discord
import random
import mtgen_docs
from datetime import datetime
from dotenv import load_dotenv
from gen_suggestion import suggest_deck

# .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

COLOR_EMOTICONS = {
    "Red": ":red_circle:",
    "Black": ":new_moon:",
    "Blue": ":blue_circle:",
    "White": ":white_circle:",
    "Green": ":green_circle:"
}

MOST_RECENT_DECKS = {}

async def rollDeck(message, args):
    # Parse colorblind and deck suggestion args
    colorblind = ("colorblind" in args)

    # TODO HACK ALWAYS COLORBLIND:
    colorblind = True

    deck_args = [
        "themes", 
        "tribes", 
        "mechs", 
        "wildcards", 
        "bans", 
        "colors", 
        "color_weight",
    ]

    kwargs = {}
    for arg, value in args.items():
        if arg in deck_args:
            # assume the first value of any argument is correct
            kwargs[arg] = value[0]

    # Generate deck suggestion
    deck = suggest_deck(**kwargs)
    user = str(message.author)
    user = user[:user.find("#")]
    MOST_RECENT_DECKS[user] = deck

    # Assemble return string
    intro = f"\n:crossed_swords: **Deck Prompt For {user}** :crossed_swords:\n"

    colors = "Colors:   "
    for color in deck["colors"]:
        if colorblind:
            colors += f"{color} "
        else:
            colors += f"{COLOR_EMOTICONS[color]}  "
    colors += "\n"

    themes = f"Themes:   {', '.join(deck['themes'])}\n"
    reqs   = f"Require:  {', '.join(deck['reqs'])}\n"
    bans   = f"Bans:     {', '.join(deck['bans'])}\n"

    response = f"{intro}```{colors}{themes}{reqs}{bans}```"
    print(response)
    await message.channel.send(response)


async def sendImage(message, file, file_type="jpg"):
    await message.channel.send(file=discord.File(f"./CRITICAL_MEDIA/{file}.{file_type}"))

async def fierceImage(message, args):
    await sendImage(message, 'fierce_empath_small')

async def pounceImage(message, args):
    await sendImage(message, 'pouncing_shoreshark_small')

async def redcapImage(message, args):
    await sendImage(message, 'weaselback_redcap_small')

async def buggyImage(message, args):
    await sendImage(message, 'buggy')


async def recordMatch(message, args):
    if "winner" in args:
        winner = ' '.join(args["winner"])
    else:
        winner = str(message.author)
        winner = winner[:winner.find("#")]

    if "loser" in args:
        loser = ' '.join(args["loser"])
    else:
        loser = "unlisted"

    if winner in MOST_RECENT_DECKS:
        colors_1 = ','.join(MOST_RECENT_DECKS[winner]["colors"])
        themes_1 = ','.join(MOST_RECENT_DECKS[winner]["themes"])
        reqs_1 = ','.join(MOST_RECENT_DECKS[winner]["reqs"])
        bans_1 = ','.join(MOST_RECENT_DECKS[winner]["bans"])
    else:
        colors_1 = "not_recorded"
        themes_1 = "not_recorded"
        reqs_1 = "not_recorded"
        bans_1 = "not_recorded"

    if loser in MOST_RECENT_DECKS:
        colors_2 = ','.join(MOST_RECENT_DECKS[loser]["colors"])
        themes_2 = ','.join(MOST_RECENT_DECKS[loser]["themes"])
        reqs_2 = ','.join(MOST_RECENT_DECKS[loser]["reqs"])
        bans_2 = ','.join(MOST_RECENT_DECKS[loser]["bans"])
    else:
        colors_2 = "not_recorded"
        themes_2 = "not_recorded"
        reqs_2 = "not_recorded"
        bans_2 = "not_recorded"

    match_record = {
        "date": datetime.today().strftime('%Y%m%d'),
        "time": datetime.today().strftime('%H%M%S'),
        "player_1": winner,
        "player_2": loser,
        "colors_1": colors_1,
        "themes_1": themes_1,
        "reqs_1": reqs_1,
        "bans_1": bans_1,
        "colors_2": colors_2,
        "themes_2": themes_2,
        "reqs_2": reqs_2,
        "bans_2": bans_2,
        "winner": winner
    }

    with open(os.path.join(sys.path[0], "matches.csv"), 'a', newline='') as csvfile:
        fieldnames = match_record.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(match_record)

    if loser != "unlisted":
        response = f"Recording match between {winner} and {loser}. {winner} won!"
    else:
        response = f"Recording a win for {winner}!"

    additions = [
        f" Nice going {winner}!",
        f" Way to drop those lands {winner}!",
        f" Way to play those scorpions {winner}!",
        f" {winner} is the wizard supreme!",
        f" {winner} drew too many cards!",
        f" Great deck building {winner}!",
        f"You really walked those planes {winner}!"
    ]
    if loser != "unlisted":
        additions += [
            f" Maybe play more land ramp next time {loser}!",
            f" Time to go tweak your deck {loser}!",
            f" You'll get 'em next time {loser}!",
            f" Maybe play less scorpions {loser}!",
            f" All of {loser}'s creatured got removed!",
            f" Nice try {loser}!",
        ]
    response += random.choice(additions)
    await message.channel.send(F"`{response}`")

async def showWins(message, args):
    if "player" in args:
        player = ' '.join(args["player"])
    else:
        player = str(message.author)
        player = player[:player.find("#")]

    if "opponent" in args:
        opponent = ' '.join(args["opponent"])
    else:
        opponent = None

    wins = 0
    losses = 0

    with open(os.path.join(sys.path[0], "matches.csv"), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for match in reader:
            print(match)
            if player == match["winner"] and (opponent is None or opponent in [match["player_1"], match["player_2"]]):
                wins += 1

            if opponent is not None and opponent == match["winner"] and (player in [match["player_1"], match["player_2"]]):
                losses += 1

    if opponent is None:
        response = f"`{player} has won {wins} matches!`"
    else:
        response = f"`{player} has {wins} wins and {losses} losses against {opponent}!`"
    print(response)
    await message.channel.send(response)

async def mtgenerator(message, args):
    await message.channel.send(mtgen_docs.help_docs["!mtgenerator"])

async def parse_command(message):
    print(f"Incoming command: \"{message.content}\"")
    tokens = message.content.split()
    command = tokens.pop(0)
    args_dict = {}
    cur_arg = None
    for token in tokens:
        if token[:2] == "--":
            cur_arg = token[2:]
            args_dict[cur_arg] = []
        elif cur_arg is not None:
            args_dict[cur_arg].append(token)
        else:
            arg_error = {f"malformed command, \"{message.content}\", expected first argument beginning with \"--\", got {token}"}
            print(arg_error)
            await message.channel.send(arg_error)
    return command, args_dict


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content[0] != "!":
        return

    commands = {
        "!mtgenerator": mtgenerator,
        "!rolldeck": rollDeck,
        "!checkmate": recordMatch,
        "!wins": showWins,
        "!fierce": fierceImage,
        "!pounce": pounceImage,
        "!redcap": redcapImage,
        "!buggy": buggyImage
    }

    if message.content.split()[0] in commands:
        command, args = await parse_command(message)
        if "help" in args:
            await message.channel.send(mtgen_docs.help_docs[command])
        else:
            await commands[command](message, args)


@client.event
async def on_ready():
    print(f'mtgenerator bot spinning up')
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            print(
                f'{client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
            break

def main():
    print("running mtgenerator discord bot")
    client.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()