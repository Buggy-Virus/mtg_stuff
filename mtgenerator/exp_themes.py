STRIXHAVEN_TRIBES = {
    "Red": ["Humans", "Shamans", "Dwarves", "Spirits"],
    "Black": ["Warlocks", "Humans", "Eldritch", "Inklings", "Pests"],
    "Blue": ["Wizards", "Humans", "Birds", "Books"],
    "White": ["Humans", "Wizards", "Clerics", "Birds", "Kor", "Spirit", "Academia"],
    "Green": ["Mammals", "Druids", "Elves", "Swampy", "Pests"],
    "Wild": []
}

STRIXHAVEN_MECHANICS = {
    "Red": ["Haste", "Burn", "Instants"],
    "Black": ["Counters", "Heal", "Flying", "Discard", "Sacrifice", "Graveyard"],
    "Blue": ["Flying", "Bounce", "Tap", "Instants", "Counter", "Draw"],
    "White": ["Exile", "Counters", "Buff", "Aura", "Enchantments"],
    "Green": ["Trample", "Ramp", "Heal", "Counters", "Sacrifice"],
    "Wild": ["Learn", "Magecraft", "Artifacts"]
}

KALDHEIM_TRIBES = {
    "Red": ["Giants", "Berserkers", "Dwarves", "Dragons"],
    "Black": ["Berserkers", "Elves", "Angels", "Zombies", "Demons"],
    "Blue": ["Shapeshifters", "Giants", "Wizards", "Birds"],
    "White": ["Spirit", "Angel", "Warriors", "Humans", "Clerics"],
    "Green": ["Elf", "Shapeshifters", "Snow", "Mammals", "Trolls", "Warriors"],
    "Wild": ["Vehicles", "Snow"]
}

KALDHEIM_MECHANICS = {
    "Red": ["Boast", "Exile", "Haste", "Burn", "Instants", "Equipment"],
    "Black": ["Sacrifice", "discard", "mill"],
    "Blue": ["Counter", "Flash", "Flying", "Copy", "Foretell", "Scry"],
    "White": ["Second Spell", "Heal", "Exile", "Boast", "Runes", "Flying"],
    "Green": ["Deathtouch", "Counters"],
    "Wild": ["God", "Artifacts", "Runes"]
}

EVERGREEN_TRIBES = {
    "Red": ["Knights", "Goblins", "Dragons", "Satyrs", "Warriors", "Dwarves", "Dogs", "Firey"],
    "Black": ["Vampire", "Rogues", "Knights", "Zombies", "Demons", "Nightmare", "Snakes", "Swampy"],
    "Blue": ["Wizards", "Rogues", "Artifacts", "Birds", "Merfolk", "Sphinx", "Watery"],
    "White": ["Cats", "Clerics", "Knights", "Humans", "Dogs", "Angels", "Soldiers", "Warriors", "Kor"],
    "Green": ["Spiders", "Elves", "Dinosaurs", "Elementals", "Beasts", "Insects", "Plants", "Serpents", "Mammals"],
    "Wild": []
}

EVERGREEN_MECHANICS = {
    "Red": ["Instants", "Discard", "Sacrifice", "Equipment", "Burn", "Landfall", "Conversion"],
    "Black": ["Deathtouch", "Flying", "Sacrifice", "Enchantments", "Graveyard", "Heal", "Mill", "Discard", "Destroy"],
    "Blue": ["Flying", "Instants", "Counter", "Mill", "Enchantments", "Scry", "Tap", "Bounce", "Draw"],
    "White": ["Enchantments", "Flying", "Heal", "Equipment", "Landfall", "Exile"],
    "Green": ["Counters", "Ramp", "Landfall", "Food"],
    "Wild": ["Artifacts", "Party", "Mutate", "Adventure", "Sagas", "Gods"]
}

themes = {
    "Strixhaven": {"tribes": STRIXHAVEN_TRIBES, "mechs": STRIXHAVEN_MECHANICS},
    "Kaldheim": {"tribes": KALDHEIM_TRIBES, "mechs": KALDHEIM_MECHANICS},
    "Evergreen": {"tribes": EVERGREEN_TRIBES, "mechs": EVERGREEN_MECHANICS},
}