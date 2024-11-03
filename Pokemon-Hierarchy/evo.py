evolution_tree = {
    "Abra": ["Kadabra", "Alakazam"],
    "Aerodactyl": [],
    "Alolan Sandslash": [],
    "Arbok": [],
    "Arcanine": [],
    "Articuno": [],
    "Beedrill": [],
    "Bellsprout": ["Weepinbell", "Victreebel"],
    "Blastoise": [],
    "Bulbasaur": ["Ivysaur", "Venusaur"],
    "Butterfree": [],
    "Caterpie": ["Metapod", "Butterfree"],
    "Chansey": [],
    "Charizard": [],
    "Charmander": ["Charmeleon", "Charizard"],
    "Clefable": [],
    "Clefairy": ["Clefable"],
    "Cloyster": [],
    "Cubone": ["Marowak"],
    "Dewgong": [],
    "Diglett": ["Dugtrio"],
    "Ditto": [],
    "Dodrio": [],
    "Doduo": ["Dodrio"],
    "Dragonair": ["Dragonite"],
    "Dratini": ["Dragonair", "Dragonite"],
    "Drowzee": ["Hypno"],
    "Dugtrio": [],
    "Eevee": ["Vaporeon", "Jolteon", "Flareon"],
    "Ekans": ["Arbok"],
    "Electabuzz": [],
    "Electrode": [],
    "Exeggcute": ["Exeggutor"],
    "Exeggutor": [],
    "Farfetchd": [],
    "Fearow": [],
    "Flareon": [],
    "Gastly": ["Haunter", "Gengar"],
    "Geodude": ["Graveler", "Golem"],
    "Gloom": ["Vileplume"],
    "Golbat": [],
    "Goldeen": ["Seaking"],
    "Golduck": [],
    "Golem": [],
    "Graveler": ["Golem"],
    "Grimer": ["Muk"],
    "Growlithe": ["Arcanine"],
    "Gyarados": [],
    "Haunter": ["Gengar"],
    "Hitmonchan": [],
    "Hitmonlee": [],
    "Horsea": ["Seadra"],
    "Hypno": [],
    "Ivysaur": ["Venusaur"],
    "Jigglypuff": ["Wigglytuff"],
    "Jolteon": [],
    "Jynx": [],
    "Kabuto": ["Kabutops"],
    "Kabutops": [],
    "Kadabra": ["Alakazam"],
    "Kakuna": ["Beedrill"],
    "Kangaskhan": [],
    "Kingler": [],
    "Koffing": ["Weezing"],
    "Krabby": ["Kingler"],
    "Lapras": [],
    "Lickitung": [],
    "Machamp": [],
    "Machoke": ["Machamp"],
    "Machop": ["Machoke", "Machamp"],
    "Magikarp": ["Gyarados"],
    "Magmar": [],
    "Magnemite": ["Magneton"],
    "Magneton": [],
    "Mankey": ["Primeape"],
    "Marowak": [],
    "Meowth": ["Persian"],
    "Metapod": ["Butterfree"],
    "Mew": [],
    "Mewtwo": [],
    "MrMime": [],
    "Muk": [],
    "Nidoking": [],
    "Nidoqueen": [],
    "Nidorina": ["Nidoqueen"],
    "Nidorino": ["Nidoking"],
    "Ninetales": [],
    "Oddish": ["Gloom", "Vileplume"],
    "Omanyte": ["Omastar"],
    "Omastar": [],
    "Onix": [],
    "Paras": ["Parasect"],
    "Parasect": [],
    "Persian": [],
    "Pidgeot": [],
    "Pidgeotto": ["Pidgeot"],
    "Pidgey": ["Pidgeotto", "Pidgeot"],
    "Pikachu": ["Raichu"],
    "Pinsir": [],
    "Poliwag": ["Poliwhirl", "Poliwrath"],
    "Poliwhirl": ["Poliwrath"],
    "Ponyta": ["Rapidash"],
    "Porygon": [],
    "Primeape": [],
    "Psyduck": ["Golduck"],
    "Raichu": [],
    "Rapidash": [],
    "Raticate": [],
    "Rattata": ["Raticate"],
    "Rhydon": [],
    "Rhyhorn": ["Rhydon"],
    "Sandshrew": ["Sandslash"],
    "Sandslash": [],
    "Scyther": [],
    "Seadra": [],
    "Seaking": [],
    "Seel": ["Dewgong"],
    "Shellder": ["Cloyster"],
    "Slowbro": [],
    "Slowpoke": ["Slowbro"],
    "Snorlax": [],
    "Spearow": ["Fearow"],
    "Squirtle": ["Wartortle", "Blastoise"],
    "Starmie": [],
    "Staryu": ["Starmie"],
    "Tangela": [],
    "Tauros": [],
    "Tentacool": ["Tentacruel"],
    "Tentacruel": [],
    "Vaporeon": [],
    "Venomoth": [],
    "Venonat": ["Venomoth"],
    "Venusaur": [],
    "Victreebel": [],
    "Vileplume": [],
    "Voltorb": ["Electrode"],
    "Vulpix": ["Ninetales"],
    "Wartortle": ["Blastoise"],
    "Weedle": ["Kakuna", "Beedrill"],
    "Weepinbell": ["Victreebel"],
    "Weezing": [],
    "Wigglytuff": [],
    "Zapdos": [],
    "Zubat": ["Golbat"]
}

classid2name = {}
with open('class_names.txt', 'r') as file:
    for line in file:
        name = ' '.join(line.strip().split()[1:])
        id = int(line.strip().split()[0])
        classid2name[id] = name

classname2id = {v: k for k, v in classid2name.items()}

child2parent = {}
for cid, name in classid2name.items():
    if cid == 0:
        continue
    child2parent[cid] = 0

for parent, children in evolution_tree.items():
    if len(children) > 0:
        child_id = classname2id[children[0]]
        parent_id = classname2id[parent]
        child2parent[child_id] = parent_id


output_file = open('./Pokemon.parent-child.txt', 'w')

for child, parent in child2parent.items():
    output_file.write(f"{parent} {child}\n")