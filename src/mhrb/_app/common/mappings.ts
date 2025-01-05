/*
 * Author:  simshadows <contact@simshadows.com>
 * License: GNU Affero General Public License v3 (AGPL-3.0)
 */

import {
    type GLShellingType,
    type HHSong,
    type SAPhialType,
    type CBPhialType,
    type BowgunAmmoType,
    type BowgunAmmoInfo,
    type BowArcShotType,
    type BowChargeShotType,
} from "./types";
import {bowgunAmmoInfoMap} from "./_internals/bowgun_ammo_data";

export function toNameFilterString(s: string): string {
    // IMPORTANT: Please maintain parity between this Javascript implementation and the Python implementation.
    // TODO: Also strip out punctuation?
    return s.toLowerCase().replace(/\s/g, "");
}

export function glShellingTypeName(s: GLShellingType): string {
    switch (s) {
        default: console.error(`Unexpected value: ${s}`); // Fallthrough for graceful failure
        case "normal": return "Normal";
        case "long":   return "Long";
        case "wide":   return "Wide";
    }
}

export function hhSongName(s: HHSong): string {
    switch (s) {
        default: console.error(`Unexpected value: ${s}`); // Fallthrough for graceful failure
        case "attack_up":              return "Attack Up";
        case "affinity_up":            return "Affinity Up";
        case "defense_up":             return "Defense Up";
        case "attack_and_defense_up":  return "Attack and Defense Up";
        case "attack_and_affinity_up": return "Attack and Affinity Up";

        case "blight_negated":                  return "Blight Negated";
        case "divine_protection":               return "Divine Protection";
        case "earplugs_l":                      return "Earplugs (L)";
        case "earplugs_s":                      return "Earplugs (S)";
        case "elemental_attack_boost":          return "Elemental Reforço de Ataque";
        case "environment_damage_negated":      return "Environment Damage Negated";
        case "health_recovery_s":               return "Health Recovery (S)";
        case "health_recovery_s_plus_antidote": return "Health Recovery (S) + Antidote";
        case "health_recovery_l":               return "Health Recovery (L)";
        case "health_regeneration":             return "Health Regeneration";
        case "knockbacks_negated":              return "Knockbacks Negated";
        case "sharpness_loss_reduced":          return "Sharpness Loss Reduced";
        case "sonic_barrier":                   return "Sonic Barrier";
        case "sonic_wave":                      return "Sonic Wave";
        case "stamina_use_reduced":             return "Stamina Use Reduced";
        case "stamina_recovery_up":             return "Stamina Recovery Up";
        case "stun_negated":                    return "Stun Negated";
        case "tremors_negated":                 return "Tremors Negated";
        case "wind_pressure_negated":           return "Wind Pressure Negated";
    }
}

export function saPhialTypeName(s: SAPhialType): string {
    switch (s) {
        default: console.error(`Unexpected value: ${s}`); // Fallthrough for graceful failure
        case "power_phial":     return "Power Phial";
        case "element_phial":   return "Element Phial";
        case "poison_phial":    return "Poison Phial";
        case "paralysis_phial": return "Paralysis Phial";
        case "dragon_phial":    return "Dragon Phial";
        case "exhaust_phial":   return "Exhaust Phial";
    }
}

export function cbPhialTypeName(s: CBPhialType): string {
    switch (s) {
        default: console.error(`Unexpected value: ${s}`); // Fallthrough for graceful failure
        case "impact_phial":  return "Impact Phial";
        case "element_phial": return "Element Phial";
    }
}

export function getBowgunInfo(s: BowgunAmmoType): BowgunAmmoInfo {
    const ammoInfo = bowgunAmmoInfoMap.get(s);
    // TODO: Make this safer? (i.e. use a TypeScript mapping type, not ES6 Map?
    if (!ammoInfo) return {id: "unknown", name: "unknown", shortName: "unknown"};
    return ammoInfo;
}

export function bowArcShotTypeName(s: BowArcShotType): string {
    switch (s) {
        default: console.error(`Unexpected value: ${s}`); // Fallthrough for graceful failure
        case "recovery": return "Recovery";
        case "affinity": return "Affinity";
        case "brace":    return "Brace";
    }
}

export function bowChargeShotTypeName(s: BowChargeShotType): string {
    switch (s) {
        default: console.error(`Unexpected value: ${s}`); // Fallthrough for graceful failure
        case "pierce": return "Pierce";
        case "rapid":  return "Rapid";
        case "spread": return "Spread";
    }
}

