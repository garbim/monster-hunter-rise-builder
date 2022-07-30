#!/usr/bin/env python3

"""
Filename: run_code_generator.py
Author:   simshadows <contact@simshadows.com>

Runs the code generator.
"""

import os
import json

from general import generate_source_file
from utils import ramp_id_to_object_name

from skills import generate_skills_source_file
from decorations import generate_decos_source_file
from armour import generate_armour_source_file
from weapons import generate_weapon_source_files
from hardcoded_data.rampage_skills_procedural import get_procedural_rampage_skills

GENERATED_CODE_NOTICE = """\
/*
 *      SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTT     OOOOOOOOO     PPPPPPPPPPPPPPPPP   
 *    SS:::::::::::::::ST:::::::::::::::::::::T   OO:::::::::OO   P::::::::::::::::P  
 *   S:::::SSSSSS::::::ST:::::::::::::::::::::T OO:::::::::::::OO P::::::PPPPPP:::::P 
 *   S:::::S     SSSSSSST:::::TT:::::::TT:::::TO:::::::OOO:::::::OPP:::::P     P:::::P
 *   S:::::S            TTTTTT  T:::::T  TTTTTTO::::::O   O::::::O  P::::P     P:::::P
 *   S:::::S                    T:::::T        O:::::O     O:::::O  P::::P     P:::::P
 *    S::::SSSS                 T:::::T        O:::::O     O:::::O  P::::PPPPPP:::::P 
 *     SS::::::SSSSS            T:::::T        O:::::O     O:::::O  P:::::::::::::PP  
 *       SSS::::::::SS          T:::::T        O:::::O     O:::::O  P::::PPPPPPPPP    
 *          SSSSSS::::S         T:::::T        O:::::O     O:::::O  P::::P            
 *               S:::::S        T:::::T        O:::::O     O:::::O  P::::P            
 *               S:::::S        T:::::T        O::::::O   O::::::O  P::::P            
 *   SSSSSSS     S:::::S      TT:::::::TT      O:::::::OOO:::::::OPP::::::PP          
 *   S::::::SSSSSS:::::S      T:::::::::T       OO:::::::::::::OO P::::::::P          
 *   S:::::::::::::::SS       T:::::::::T         OO:::::::::OO   P::::::::P          
 *    SSSSSSSSSSSSSSS         TTTTTTTTTTT           OOOOOOOOO     PPPPPPPPPP
 *
 *
 * This is a generated source code file.
 *
 * Do NOT edit this file directly!
 *
 * Instead, you must edit the corresponding code generator files located in /dev_scripts at
 * the root of this repository, then run the code generators with the following command:
 *      $ yarn run-code-generators
 *
 * (ASCII art generated using <https://patorjk.com/software/taag/#p=display&h=0&f=Doh&t=STOP>)
 *
 */


/*
 * Code Generator Author: simshadows <contact@simshadows.com>
 * License: GNU Affero General Public License v3 (AGPL-3.0)
 */

"""

DATA_PATH_FMT = "./dev_scripts/mhrb/code_generators/hardcoded_data/{s}"
SCRAPED_DECOS_PATH = "./dev_scripts/mhrb/kiranico_scrape/downloaded_data/downloaded_data_decorations.json"

OUTPUT_PATH_FMT = "./src/mhrb/_app/database/generated_code/{s}"

def read_data(s):
    with open(DATA_PATH_FMT.format(s=s), encoding="utf-8", mode="r") as f:
        return json.loads(f.read())
def read_deco_data():
    with open(SCRAPED_DECOS_PATH, encoding="utf-8", mode="r") as f:
        return json.loads(f.read())

def write_source_file(s, data):
    assert isinstance(data, str)
    with open(OUTPUT_PATH_FMT.format(s=s), "w") as f:
        f.write(GENERATED_CODE_NOTICE + data)

def run():
    print(f"Current working directory: {os.getcwd()}")

    skills_data = read_data("skills.json")
    write_source_file("_generated_skills.ts", generate_skills_source_file(skills_data))
    print(f"Discovered {len(skills_data)} skills.")

    ramps_data = get_procedural_rampage_skills() + read_data("rampage_skills_individual.json")
    write_source_file(
        "_generated_rampage_skills.ts",
        generate_source_file(
            {
                "keys": ["id", "shortID", "name"],
                "array": "rampsArray",
                "type": "RampageSkill",
                "obj_name_map": ramp_id_to_object_name,
            },
            ramps_data,
        ),
    )
    print(f"Discovered {len(ramps_data)} rampage skills.")

    decos_data = read_data("decorations.json")
    decos_data_scraped = read_deco_data()
    write_source_file("_generated_decorations.ts", generate_decos_source_file(decos_data, decos_data_scraped))
    print(f"Discovered {len(decos_data)} decorations.")

    armour_data = read_data("armour.json")
    armour_naming_schemes_data = read_data("armour_naming_schemes.json")
    write_source_file("_generated_armour.ts", generate_armour_source_file(armour_data, armour_naming_schemes_data))
    print(f"Discovered {len(armour_data)} armour sets.")

    weapon_data = {
        "greatsword":     read_data("../../kiranico_scrape/output/weapons_greatsword.json"    ),
        "longsword":      read_data("../../kiranico_scrape/output/weapons_longsword.json"     ),
        "swordandshield": read_data("../../kiranico_scrape/output/weapons_swordandshield.json"),
        "dualblades":     read_data("../../kiranico_scrape/output/weapons_dualblades.json"    ),
        "lance":          read_data("../../kiranico_scrape/output/weapons_lance.json"         ),
        "gunlance":       read_data("../../kiranico_scrape/output/weapons_gunlance.json"      ),
        "hammer":         read_data("../../kiranico_scrape/output/weapons_hammer.json"        ),
        "huntinghorn":    read_data("../../kiranico_scrape/output/weapons_huntinghorn.json"   ),
        "switchaxe":      read_data("../../kiranico_scrape/output/weapons_switchaxe.json"     ),
        "chargeblade":    read_data("../../kiranico_scrape/output/weapons_chargeblade.json"   ),
        "insectglaive":   read_data("../../kiranico_scrape/output/weapons_insectglaive.json"  ),
        "lightbowgun":    read_data("../../kiranico_scrape/output/weapons_lightbowgun.json"   ),
        "heavybowgun":    read_data("../../kiranico_scrape/output/weapons_heavybowgun.json"   ),
        "bow":            read_data("../../kiranico_scrape/output/weapons_bow.json"           ),
    }
    weapon_source_files_content = generate_weapon_source_files(weapon_data)
    write_source_file("_generated_weapon_greatsword.ts"    , weapon_source_files_content["greatsword"    ])
    write_source_file("_generated_weapon_longsword.ts"     , weapon_source_files_content["longsword"     ])
    write_source_file("_generated_weapon_swordandshield.ts", weapon_source_files_content["swordandshield"])
    write_source_file("_generated_weapon_dualblades.ts"    , weapon_source_files_content["dualblades"    ])
    write_source_file("_generated_weapon_lance.ts"         , weapon_source_files_content["lance"         ])
    write_source_file("_generated_weapon_gunlance.ts"      , weapon_source_files_content["gunlance"      ])
    write_source_file("_generated_weapon_hammer.ts"        , weapon_source_files_content["hammer"        ])
    write_source_file("_generated_weapon_huntinghorn.ts"   , weapon_source_files_content["huntinghorn"   ])
    write_source_file("_generated_weapon_switchaxe.ts"     , weapon_source_files_content["switchaxe"     ])
    write_source_file("_generated_weapon_chargeblade.ts"   , weapon_source_files_content["chargeblade"   ])
    write_source_file("_generated_weapon_insectglaive.ts"  , weapon_source_files_content["insectglaive"  ])
    write_source_file("_generated_weapon_lightbowgun.ts"   , weapon_source_files_content["lightbowgun"   ])
    write_source_file("_generated_weapon_heavybowgun.ts"   , weapon_source_files_content["heavybowgun"   ])
    write_source_file("_generated_weapon_bow.ts"           , weapon_source_files_content["bow"           ])
    for (k, v) in weapon_data.items():
        print(f"Discovered {len(v)} weapon trees of category '{k}'.")

if __name__ == "__main__":
    run()

