import os
import discord
from dotenv import load_dotenv
from gen_suggestion import suggest_deck

# .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

COLOR_EMOTICONS = {
    "red": ":red_circle:",
    "black": ":new_moon:",
    "blue": ":blue_circle:",
    "white": ":white_circle:",
    "green": ":green_circle:"
}

async def rollDeck(message, args):
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
    user = str(message.author)
    user = user[:user.find("#")]
    intro = f"\n:crossed_swords: Deck Prompt For {user} :crossed_swords:\n"

    colors = "Colors:  "
    for color in deck["colors"]:
        if colorblind:
            colors += f"{color} "
        else:
            colors += f"{COLOR_EMOTICONS[color]}  "
    colors += "\n"

    themes = f"Themes:  {', '.join(deck['themes'])}\n"
    reqs = f"Requirements:  {', '.join(deck['reqs'])}\n"
    bans = f"Bans:  {', '.join(deck['bans'])}\n"

    response = intro + colors + themes + reqs + bans
    print(response)
    await message.channel.send(response)


async def sendImage(message, file, file_type="jpg"):
    await message.channel.send(file=discord.File(f"./CRITICAL_MEDIA/{file}.{file_type}"))


async def parse_command(message):
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

    command, args = await parse_command(message)

    if command == '!rolldeck':
        await rollDeck(message, args)
    elif command == '!fierce':
        await sendImage(message, 'fierce_empath_small')
    elif command == '!pounce':
        await sendImage(message, 'pouncing_shoreshark_small')
    elif command == '!redcap':
        await sendImage(message, 'weaselback_redcap_small')
    elif command == '!buggy':
        await sendImage(message, 'buggy')


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