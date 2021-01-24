docs_main = (":question:\n"
             "MTGenerator Bot Functions (call functions with `!<FUNCTION> --help` for more)\n"
             "`!mtgenerator : Generates a deck with specific colors, themes, requirements, and bans`\n"
             "`!checkmate   : Mark a victory in your record`\n"
             "`!wins        : Check victories in your record`\n"
             "And other secrets only 2020-Standard MTG Card Art prodigies will know!"
            )

docs_mtgenerator = ("`!mtgenerator` :question:\n"
                    "Generates a deck with specific colors, themes, requirements, and bans\n"
                    "Optional Arguments:\n"
                    "`--colors       : (int) Number of deck colors`\n"
                    "`--themes       : (int) Number of theme requirements`\n"
                    "`--tribes       : (int) Number of tribe requirements`\n"
                    "`--mechs        : (int) Number of mechanic requirements`\n"
                    "`--wildcards    : (int) Number of wildcard requirements`\n"
                    "`--bans         : (int) Number of mechanics and themes to ban`\n"
                    "`--color_weight : (dbl) Probability weight when drawing multiple colors`\n"
                    "`--colorblind   : (flag) Print deck colors as text`"
                   )

docs_checkmate = ("`!checkmate` :question:\n"
                  "Mark a victory in your record\n"
                  "Optional Arguments:\n"
                  "`--winner : (str) Name of the winner`\n"
                  "`--loser  : (str) Name of the loooooooOOOooser`\n"
                  )

docs_wins = ("`!wins` :question:\n"
             "Check victories in your record\n"
             "Optional Arguments:\n"
             "`--player   : (str) Discord tag of the focal player`\n"
             "`--opponent : (str) Discord tag of that player's opponent`\n"
            )
