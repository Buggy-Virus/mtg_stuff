mtgenerator = ":question:\n"
              "```Bot for generating random mtg deck suggestions and recording wins\n"
              "\n"
              "Commands:\n"
              "!mtgenerator  Generates a deck with specific colors, themes, requirements, and bans\n"
              "!checkmate    Mark a victory in your record\n"
              "!wins         Check victories in your record\n"
              "!<redacted>   Secret commands for MTG art afficionados\n"
              "\n"
              "Use !<command> --help to see additional information and arguments for each command```"

rolldeck = "`!rolldeck` :question:\n"
           "```Generates a deck with random colors, themes, requirements, and bans\n"
           "\n"
           "Optional Arguments:\n"
           "--themes        (int) Number of theme requirements\n"
           "--tribes        (int) Number of tribe requirements\n"
           "--mechs         (int) Number of mechanic requirements\n"
           "--wildcards     (int) Number of wildcard requirements\n"
           "--bans          (int) Number of mechanics and themes to ban\n"
           "--colors        (int) Number of deck colors, overrides color_weight\n"
           "--color_weight  (dbl) Probability weight when drawing multiple colors\n"
           "--colorblind    (flag) Print deck colors as text```"

checkmate = "`!checkmate` :question:\n"
            "```Record a victory in your record\n"
            "\n"
            "Optional Arguments:\n"
            "--winner  (str) Discord tag of winner, defaults to author\n"
            "--loser   (str) Discord tag of loser```"

wins = "`!wins` :question:\n"
       "```Report the number of wins for a specific player\n"
       "\n"
       "Optional Arguments:\n"
       "--player    (str) Discord tag of the focal player, defaults to author\n"
       "--opponent  (str) Discord tag of requested opponent```"

help_docs = {
    "!mtgenerator": mtgenerator,
    "!rolldeck": rolldeck,
    "!checkmate": checkmate,
    "!wins": wins
}
