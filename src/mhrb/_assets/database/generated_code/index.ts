/*
 * Author:  simshadows <contact@simshadows.com>
 * License: GNU Affero General Public License v3 (AGPL-3.0)
 *
 * This file is NOT generated code.
 * The generated code files are the '_generated_*.ts' files.
 *
 * This file processes the generated code for consumption by the rest of the application.
 */

import {
    isPositiveInt,
} from "../../generic/check";
import {
    FrozenMap,
} from "../../generic/frozen-containers";

import {
    type SkillRO,
    type DecorationRO,
    type ArmourSlot,
    type ArmourPieceRO,
    type ArmourSetRO,
} from "../../common/types";
import {
    toNameFilterString,
} from "../../common/mappings";
import {
    populate,
} from "../_internals";

import {skillsArray} from "./_generated_skills";
import {decosArray} from "./_generated_decorations";
import {armourSetsArray} from "./_generated_armour";

/*** Skills ***/

const skillMap = new Map<string, SkillRO>();
const skillMapShortIds = new Map<number, SkillRO>();

for (const obj of skillsArray) {
    // Validate
    console.assert(/^[_a-z0-9]+$/.test(obj.id));
    console.assert(isPositiveInt(obj.shortId));
    console.assert(obj.name !== "");
    console.assert(isPositiveInt(obj.maxLevels) && (obj.maxLevels < 8)); // Change if needed

    console.assert(obj.filterHelpers.nameLower !== "");
    console.assert(obj.filterHelpers.nameLower === toNameFilterString(obj.name));
    
    // Check for duplicates
    console.assert(!skillMap.has(obj.id));
    console.assert(!skillMapShortIds.has(obj.shortId));

    skillMap.set(obj.id, obj);
    skillMapShortIds.set(obj.shortId, obj);
}

const finalSkillMap = new FrozenMap<string, SkillRO>(skillMap);
const finalSkillMapShortIds = new FrozenMap<number, SkillRO>(skillMapShortIds);

/*** Decorations ***/

const decosMap: FrozenMap<number, DecorationRO> = populate(
    decosArray,
    (obj) => {
        // Validate
        console.assert(isPositiveInt(obj.id));
        console.assert(obj.name !== "");
        console.assert(obj.skills.length > 0); // Should be at least one skill in there
        for (const [_, v] of obj.skills) console.assert(isPositiveInt(v));

        console.assert(obj.filterHelpers.nameLower !== "");
        console.assert(obj.filterHelpers.nameLower === toNameFilterString(obj.name));

        return obj;
    },
);

/*** Armour ***/

const tmpSlotIDList: ArmourSlot[] = ["head", "chest", "arms", "waist", "legs"];

const armourMap: FrozenMap<number, ArmourSetRO> = populate(
    armourSetsArray,
    (obj) => {
        // Validate
        console.assert(isPositiveInt(obj.id));
        console.assert(obj.name !== "");
        for (const slotID of tmpSlotIDList) {
            const piece = obj[slotID]
            if (!piece) continue;
            console.assert(piece.setID === obj.id);
            console.assert(piece.setName === obj.name);
            console.assert(piece.name !== "");
            for (const [_, v] of piece.skills) console.assert(isPositiveInt(v));

            console.assert((piece.defenseAtLevel1 % 1 === 0) && (piece.defenseAtLevel1 >= 0));
            console.assert(piece.fireRes    % 1 === 0);
            console.assert(piece.waterRes   % 1 === 0);
            console.assert(piece.thunderRes % 1 === 0);
            console.assert(piece.iceRes     % 1 === 0);
            console.assert(piece.dragonRes  % 1 === 0);

            console.assert(piece.filterHelpers.nameLower !== "");
            console.assert(piece.filterHelpers.nameLower === toNameFilterString(piece.name));

            console.assert(piece.filterHelpers.setNameLower !== "");
            console.assert(piece.filterHelpers.setNameLower === toNameFilterString(piece.setName));

            // piece.filterHelpers.hintStrLower doesn't need validation
        }
        return obj;
    },
);

const armourArrays: Readonly<{[key in ArmourSlot]: Readonly<ArmourPieceRO[]>}> = (()=>{
    const ret: {[key in ArmourSlot]: ArmourPieceRO[]} = {
        head:  [],
        chest: [],
        arms:  [],
        waist: [],
        legs:  [],
    };
    for (const [_, armourSet] of armourMap.entries()) {
        for (const slotID of tmpSlotIDList) {
            const armourPiece = armourSet[slotID];
            if (armourPiece) ret[slotID].push(armourPiece);
        }
    }
    return ret;
})();

export {
    finalSkillMap as skillMap,
    finalSkillMapShortIds as skillMapShortIds,
    decosMap,
    armourMap,
    armourArrays,
};
