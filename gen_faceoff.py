import random as r

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

for player in range(NUM_PLAYERS):

    # Choose Colors
    player_colors = set()
    picking_colors = True
    while picking_colors:
        cur_num = len(player_colors)
        if cur_num == 0:
            player_colors.add(r.choice(colors))
        elif cur_num == 1:
            player_colors.add(r.choice(colors))
        elif r.random() > END_WEIGHT:
            player_colors.add(r.choice(colors))

        if cur_num == len(player_colors):
            picking_colors = False

    # Choose Keywords
    player_suggestions = set()
    while len(player_suggestions) < SUG_NUM:
        player_suggestions.add(r.choice(keywords[r.choice(list(player_colors))]))
    if r.random() < WILD_WEIGHT:
        player_suggestions.add(r.choice(keywords["wildcard"]))

    # Choose Bans
    num_themes = 0
    for color in player_colors:
        num_themes += len(keywords[color])

    player_bans = set()
    while len(player_bans) < BAN_NUM:
        if num_themes == len(player_bans) + len(player_suggestions):
            break
            
        proposed_ban = r.choice(keywords[r.choice(list(player_colors))])
        if proposed_ban not in player_suggestions:
            player_bans.add(proposed_ban)

    print(f"Player {player + 1}")
    print(f"Colors: {' '.join(player_colors)}")
    print(f"Suggestions: {' '.join(player_suggestions)}")
    print(f"Bans: {' '.join(player_bans)}")
    print()