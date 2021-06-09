"""
Filename: huntinghorn.py
Author:   simshadows <contact@simshadows.com>

Hardcoded parts for Hunting Horn data
"""

# Specification to build the data
# {category: [(tree name, [(name, id, rarity), ...]), ...]}
HARDCODED_HH_SPEC = [
    ("Kamura Tree", [
        ("Kamura Chorus I"  , "1a"),
        ("Kamura Chorus II" , "1b"),
        ("Kamura Chorus III", "1c"),
        ("Kamura Chorus IV" , "1d"),
        ("Kamura Chorus V"  , "1e"),
        ("Kamura Ninja Horn", "1f"),
    ]),
    ("Mizutsune Tree", [
        ("Poetic Bell I", "2a"),
        ("Poetic Bell II", "2b"),
        ("Summoning Bell", "2c"),
    ]),
    ("Rakna-Kadaki Tree", [
        ("Sublime Bell I", "3a"),
        ("Sublime Bell II", "3b"),
        ("Araknahorn", "3c"),
    ]),
    ("Basarios Tree", [
        ("Basarios Rock I", "4a"),
        ("Basarios Rock Mk.II", "4b"),
        ("Gigant Rock", "4c"),
    ]),
    ("Zinogre Tree", [
        ("Usurper's Growl I", "5a"),
        ("Usurper's Growl II", "5b"),
        ("Despot's Thunderclap", "5c"),
    ]),
    ("Arzuros Tree", [
        ("Zurogong Primo I", "6a"),
        ("Zurogong Primo II", "6b"),
        ("Zurogong Secundo", "6c"),
    ]),
    ("Tigrex Tree", [
        ("Striped Dragonga I", "7a"),
        ("Striped Dragonga II", "7b"),
        ("Tigrex Horn", "7c"),
    ]),
    ("Barioth Tree", [
        ("Bariguiro I", "8a"),
        ("Bariguiro II", "8b"),
        ("Algiguiro", "8c"),
    ]),
    ("Somnacanth Tree", [
        ("Frilled Flute I", "9a"),
        ("Frilled Flute II", "9b"),
        ("Illusory Flute", "9c"),
    ]),
    ("Ore Tree", [
        ("Iron Horn I", "10a"),
        ("Wind Horn", "10b"),
        ("Metal Bagpipe I", "10c"),
        ("Great Bagpipe", "10d"),
        ("Heavy Bagpipe I", "10e"),
        ("Fortissimo", "10f"),
    ]),
    ("Nargacuga Tree", [
        ("Hidden Harmonic I", "11a"),
        ("Hidden Harmonic II", "11b"),
        ("Cry in the Night", "11c"),
    ]),
    ("Pukei-Pukei Tree", [
        ("Pukei Bagpipe I", "12a"),
        ("Pukei Bagpipe II", "12b"),
        ("Datura Lurr", "12c"),
    ]),
    ("Anjanath Tree", [
        ("Flammenkornett I", "13a"),
        ("Flammenkornett II", "13b"),
        ("Forte Flammenkornett", "13c"),
    ]),
    ("Rathian Tree", [
        ("Valkyrie Chordmaker I", "14a"),
        ("Valkyrie Chordmaker II", "14b"),
        ("Queen Chordmaker", "14c"),
    ]),
    ("Barroth Tree", [
        ("Sandpipe I", "15a"),
        ("Sandpipe II", "15b"),
        ("Sandcrier", "15c"),
    ]),
    ("Tetranadon Tree", [
        ("Frog Flute I", "16a"),
        ("Frog Flute II", "16b"),
        ("Amphibia Allargando", "16c"),
    ]),
    ("Izuchi Tree", [
        ("Wind Thief Horn I", "17a"),
        ("Wind Thief Horn II", "17b"),
        ("Gale Horn", "17c"),
    ]),
    ("Royal Ludroth Tree", [
        ("Droth Drone I", "18a"),
        ("Droth Drone II", "18b"),
        ("Droth Roar", "18c"),
    ]),
    ("Bone Tree", [
        ("Bone Horn I", "19a"),
        ("Bone Horn II", "19b"),
        ("Hardened Bone Horn", "19c"),
        ("Hunter's Horn I", "19d"),
        ("Native's Horn", "19e"),
    ]),
    ("Diablos Tree", [
        ("Duo Horn I", "20a"),
        ("Duo Horn II", "20b"),
        ("Duo Risoluto", "20c"),
    ]),
    ("Bullfango Tree", [
        ("Bull Grunt I", "21a"),
        ("Bull Grunt II", "21b"),
        ("Wild Grunt", "21c"),
    ]),
    ("Rathalos Tree", [
        ("Flame Feroce I", "22a"),
        ("Flame Feroce II", "22b"),
        ("Rathalos Feroce", "22c"),
    ]),
    ("Kulu-Ya-Ku Tree", [
        ("Kulu Mosso I", "23a"),
        ("Kulu Mosso II", "23b"),
        ("Kulu Grosso", "23c"),
    ]),
    ("Khezu Tree", [
        ("Khezu Horn I", "24a"),
        ("Khezu Horn II", "24b"),
        ("Khezu Flute", "24c"),
    ]),
    ("Bnahabra Tree", [
        ("Vicello Nulo I", "25a"),
        ("Vicello Nulo II", "25b"),
        ("Vicello Unu", "25c"),
        ("Vicello Nulo Black I", "25d"),
        ("Vicello Nulo Black II", "25e"),
        ("Vicello Uno Black", "25f"),
    ]),
    ("Bnahabra (Paralysis)", [
        ("Vicello Nulo Green I", "26a"),
        ("Vicello Nulo Green II", "26b"),
        ("Vicello Unu Green", "26c"),
    ]),
    ("Bnahabra (Ice)", [
        ("Vicello Nulo White I", "27a"),
        ("Vicello Nulo White II", "27b"),
        ("Vicello Unu White", "27c"),
    ]),
    ("Magnamalo Tree", [
        ("Sinister Strum I", "28a"),
        ("Sinister Strum II", "28b"),
        ("Sinister Shadestrum", "28c"),
    ]),
    ("Rajang Tree", [
        ("Denden Daiko I", "29a"),
        ("Denden Daiko II", "29b"),
        ("Denden Doomsounder", "29c"),
    ]),
    ("Ibushi Tree", [
        ("Azure Elder Horn I", "30a"),
        ("Azure Elder Horn II", "30b"),
        ("Abyssal Gale Horn", "30c"),
    ]),
    ("Narwa Tree", [
        ("Thunderbolt Horn I", "31a"),
        ("Abyssal Storm Horn", "31b"),
    ]),
    ("Bazelgeuse Tree", [
        ("Rookslayer Drum I", "32a"),
        ("Rookslayer Drum II", "32b"),
        ("Bazelreid Rookslayer", "32c"),
    ]),
    ("Kushala Daora Tree", [
        ("Daora's Taus I", "33a"),
        ("Daora's Baphophone", "33b"),
    ]),
    ("Teostra Tree", [
        ("Teostra's Tiple I", "34a"),
        ("Teostra's Orph\u00e9e", "34b"), # Will need to be fixed to include the accent
    ]),
    ("Chameleos Tree", [
        ("Blessed Ocarina I", "35a"),
        ("Cursed Ocarina", "35b"),
    ]),
    ("Valstrax Tree", [
        ("Redwing Flute I", "36a"),
        ("Reddnaught Ritmico", "36b"),
    ]),
    ("Chaos Tree", [
        ("Poison Fungasax I", "37a"),
        ("Poison Fungasax II", "37b"),
        ("Toxic Fungasax", "37c"),
    ]),
    ("Magia Tree", [
        ("Magia Charm I", "38a"),
        ("Magia Charm II", "38b"),
        ("Magia Charm III", "38c"),
        ("Magia Charmbell", "38d"),
    ]),
    ("Spio Tree", [
        ("Cornupion I", "39a"),
        ("Cornupion II", "39b"),
        ("Webbed Cornupion", "39c"),
    ]),
    ("Bombadgy Tree", [
        ("Grass Flute I", "40a"),
        ("Grass Flute II", "40b"),
        ("Bombadgy's Cry", "40c"),
    ]),
    ("Rampage Tree", [
        ("Rampage Agitato I"  , "41a"),
        ("Rampage Agitato II" , "41b"),
        ("Rampage Agitato III", "41c"),
        ("Rampage Agitato IV" , "41d"),
        ("Rampage Agitato V"  , "41e"),
        ("Rampage Agitato S"  , "41f"),
    ]),
]
