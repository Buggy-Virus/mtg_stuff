mtgenerator = (":question:\n"
               "```Bot for generating random MTG deck suggestions and recording wins\n"
               "\n"
               "Commands:\n"
               "!rolldeck         Generates a deck with random colors, themes, requirements, and bans\n"
               "!checkmate        Mark a victory in your record\n"
               "!wins             Check victories in your record\n"
               "!<redacted>       Secret commands for MTG art afficionados\n"
               "\n"
               "Use !<command> --help to see additional information and arguments for each command```"
)

rolldeck = ("`!rolldeck` :question:\n"
            "```Generates a deck with random colors, themes, requirements, and bans\n"
            "\n"
            "Optional Arguments:\n"
            "--themes          (int) Number of theme requirements\n"
            "--tribes          (int) Number of tribe requirements\n"
            "--mechs           (int) Number of mechanic requirements\n"
            "--wildcards       (int) Number of wildcard requirements\n"
            "--bans            (int) Number of mechanics and themes to ban\n"
            "--colors          (int) Number of deck colors, overrides color_weight\n"
            "--color_weight    (dbl) Probability weight when drawing multiple colors\n"
            "--colorblind      (flag) Print deck colors as text```"
)

checkmate = ("`!checkmate` :question:\n"
             "```Record a victory in your record\n"
             "\n"
             "Optional Arguments:\n"
             "--winner          (str) Discord tag of winner, defaults to author\n"
             "--loser           (str) Discord tag of loser```"
)

wins = ("`!wins` :question:\n"
        "```Report the number of wins for a specific player\n"
        "\n"
        "Optional Arguments:\n"
        "--player          (str) Discord tag of the focal player, defaults to author\n"
        "--opponent        (str) Discord tag of requested opponent```"
)

pounce = "Uncommon Shark Beast"

fierce = "ELF"

redcap = "I :muscle::muscle::muscle: would rather :weary: cast :man_mage::man_mage: myself into the abyss :volcano::volcano::volcano: than let my blood :drop_of_blood::broken_heart: stain the cap :billed_cap: of those monsters <:tatas:800107201640267777>"

buggy = """ In the coming weeks, Valve's digital trading card game, Artifact{:target="_blank"}, is slated for release. The game promises some of the most strategic and deep gameplay in the card game genre, and after Valve uncharacteristically marketing the game, featuring various other card games' professional players and streamers testing the beta and a reveal tournament, it seems to poised to fulfill that promise. Despite this, all news and discussion about the game has been overshadowed by one thing: the economy. The process by which you can gain cards, and the fact that it is purely through buying them, which is a point of consternation for many people in the age of free to play card games. There are two main contentions. First, one of the main methods of play, draft mode, requires tickets you need to purchase in order to play. In draft, instead of using a deck you own, you draft a unique deck from a selection of presented cards, then go against players sporting similarly drafted decks until you lose twice. Depending on your number of wins you receive rewards. One complaint is this gates one of the main play modes behind a pay-wall. Further many complained the expected rewards for what you paid were necessarily going to be poor, as your opponent is determined through a sort of ELO matchmaking, thus you should expect a 50% win-rate. Since the beginning of the controversy, Valve has announced there will be a way to play draft for free with no rewards, but the cost of the draft with rewards still remain a source of discomfort for many considering the game. The second contention is the fact packs can only be purchased with real money. Most other games provide some method to grind in order to build up virtual currency that can be spent on packs, in addition to being able to purchase them directly. But to alleviate these concerns, cards can be sold directly on the Steam user marketplace. Traditionally items sold on Valve market places have had extr """

help_docs = {
    "!mtgenerator": mtgenerator,
    "!rolldeck": rolldeck,
    "!checkmate": checkmate,
    "!wins": wins,
    "!pounce": pounce,
    "!fierce": fierce,
    "!redcap": redcap,
    "!buggy": buggy
}
