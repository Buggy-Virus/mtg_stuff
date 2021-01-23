import argparse
import random as r
import math as m

THEME_NUM = 1
TRIBE_NUM = 1
MECH_NUM = 1
WILD_NUM = 3
BAN_NUM = 5
END_WEIGHT = 0.25

COLORS = ["red", "black", "blue", "white", "green"]

TRIBES = {
    "red": ["knights", "goblins", "dragons", "satyrs", "warriors", "dwarves", "dogs", "firey"],
    "black": ["vampire", "rogues", "knights", "zombies", "demons", "nightmare", "snakes", "swampy"],
    "blue": ["wizards", "rogues", "artifacts", "birds", "merfolk", "sphinx", "watery"],
    "white": ["cats", "clerics", "knights", "humans", "dogs", "angels", "soldiers", "warriors", "kor"],
    "green": ["spiders", "elves", "dinosaurs", "elementals", "beasts", "animals", "insects", "plants", "serpents"],
}

MECHANICS = {
    "red": ["instants", "discard", "sacrifice", "equipment", "burn", "landfall", "conversion"],
    "black": ["deathtouch", "flying", "sacrifice", "enchantments", "graveyard", "heal", "mill", "discard", "removal"],
    "blue": ["flying", "instants", "counter", "mill", "enchantments", "scry"],
    "white": ["enchantments", "flying", "heal", "equipment", "landfall"],
    "green": ["counters", "ramp", "landfall", "food"],
    "wild": ["artifacts", "party", "mutate", "adventure", "sagas", "gods"]
}

def suggest_deck(themes=THEME_NUM, tribes=TRIBE_NUM, mechs=MECH_NUM, wildcards=WILD_NUM, bans=BAN_NUM, colors=None, color_weight=END_WEIGHT):
    # Choose Colors
    if colors is None:
        colors = 1
        while r.random() > (color_weight ** (1 / colors)) and colors < 5:
            colors += 1
    deck_colors = r.sample(COLORS, colors)

    # Build Tribe/Mech Lists
    rel_tribes = []
    rel_mechs = []
    rel_wild = MECHANICS["wild"]
    for color in deck_colors:
        rel_tribes += TRIBES[color]
        rel_mechs += MECHANICS[color]

    # Choose Themes
    deck_themes = r.sample(rel_tribes + rel_mechs, themes)
    for theme in deck_themes:
        if theme in rel_tribes:
            rel_tribes.remove(theme)
        else:
            rel_mechs.remove(theme)

    # Choose requirements
    deck_tribes = r.sample(rel_tribes, tribes)
    rel_tribes = [tribe for tribe in rel_tribes if tribe not in deck_tribes]
    deck_mechs = r.sample(rel_mechs, mechs)
    rel_mechs = [mech for mech in rel_mechs if mech not in deck_mechs]
    deck_wildcards = r.sample(rel_tribes + rel_mechs + rel_wild, wildcards)
    for wildcard in deck_wildcards:
        if wildcard in rel_tribes:
            rel_tribes.remove(wildcard)
        elif wildcard in rel_mechs:
            rel_mechs.remove(wildcard)
        
        if wildcard in rel_wild:
            rel_wild.remove(wildcard)

    deck_requirements = deck_tribes + deck_mechs + deck_wildcards
            
    # Choose Bans
    deck_bans = r.sample(rel_tribes + rel_mechs + rel_wild, bans)

    # Return deck Object
    return {
        "colors": deck_colors,
        "themes": deck_themes,
        "reqs": deck_requirements,
        "bans": deck_bans 
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-themes", type=int,
        help="Number of themes to be suggested")
    parser.add_argument("-tribes", type=int,
        help="Number of tribes to be suggested")
    parser.add_argument("-mechs", type=int,
        help="Number of mechanics to be suggested")
    parser.add_argument("-wildcards", type=int,
        help="Number of additional mechanics and themes to be suggested")
    parser.add_argument("-bans", type=int,
        help="Number of mechanics and themes to ban")
    parser.add_argument("-colors", type=int,
        help="Number of colors to be suggested")
    parser.add_argument("-color_weight", type=float,
        help="Probability weight used to randomly generate the number of colors for the deck")
    args = parser.parse_args()

    arg_dict = {
        "themes": args.themes,
        "tribes": args.tribes,
        "mechs": args.mechs,
        "wildcards": args.wildcards,
        "bans": args.bans,
        "colors": args.colors,
        "color_weight": args.color_weight
    }

    deck = suggest_deck(**{k: v for k, v in arg_dict.items() if v is not None})

    print("Deck Suggestion:")
    print(f"Colors: {', '.join(deck['colors'])}")
    print(f"Themes: {', '.join(deck['themes'])}")
    print(f"Requirements: {', '.join(deck['reqs'])}")
    print(f"Bans: {', '.join(deck['bans'])}")

if __name__ == "__main__":
    main()