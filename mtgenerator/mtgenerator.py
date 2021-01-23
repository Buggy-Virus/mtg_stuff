import os
import discord
import random
from dotenv import load_dotenv
from gen_suggestion import suggest_deck

# .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()


def rollDeck(user, args):
    # Parse colorblind and deck suggestion args
    colorblind = ("colorblind" in args)

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

    # Assemble return string
    intro = ":crossed_swords: \n" "Deck prompt for "+ user + " :crossed_swords:\n"

    colors = "Colors: "
    for color in deck["colors"]:
        if colorblind:
            colors += f"{color} "
        else:
            colors += f"{color_emoticon[color]}  "
    colors += "\n"

    themes = f"Themes:  {' '.join(deck['themes'])}\n"
    reqs = f"Requirements:  {' '.join(deck['reqs'])}\n"
    bans = f"Bans:  {' '.join(deck['bans'])}\n"

    return intro + colors + themes + reqs + bans


def parse_command(message):
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

    command, args = parse_command(message)

    if command == '!rolldeck':
        user = str(message.author)
        response = rollDeck(user, args)
        print(response)
        await message.channel.send(response)


@client.event
async def on_ready():
    print(f'mtgenerator bot spinning up')
    for guild in client.guilds:
        if guild.name == GUILD:
            print(
                f'{client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
            break

def main():
    print("running mtgenerator discord bot")
    client.run(TOKEN)

if __name__ == "__main__":
    main()