/*
 * Author:  simshadows <contact@simshadows.com>
 * License: GNU Affero General Public License v3 (AGPL-3.0)
 */

import React from "react";
const ele = React.createElement;

/*import {
    imgFASolidSprites2,
    imgFABrandsSprites2
} from "../../images";*/

const imgFASolidSprites2  = "./public/images/solid.svg";
const imgFABrandsSprites2 = "./public/images/brands.svg";
 
// TODO: Is prop forwarding here a good idea?

type Props = {
    readonly style?:   "solid" | "brands";
    readonly fragment: string;
};// & React.ComponentProps<"svg">;

export function FontAwesomeSprite(props: Props) {
    const {
        style = "solid",
        fragment,
        ...otherProps
    } = props;

    console.assert(style.length > 0);
    console.assert(fragment.length > 0);

    const spritesPath = (style === "solid") ? imgFASolidSprites2 : imgFABrandsSprites2;

    return ele("svg",
        otherProps,
        ele("use", {href: `${spritesPath}#${fragment}`}),
    );
}

/*
import React from "react";
const ele = React.createElement;

// Caminhos dos arquivos de sprite
const spritesPathSolid =  "./solid.svg";  // Caminho para o arquivo solid.svg
const spritesPathBrands = "./brands.svg";  // Caminho para o arquivo brands.svg

type Props = {
    readonly style?: "solid" | "brands";  // Estilo do ícone (solid ou brands)
    readonly fragment: string;            // Nome do ícone, ex: "discord", "home", etc.
};

export function FontAwesomeSprite(props: Props) {
    const {
        style = "solid",
        fragment,
        ...otherProps
    } = props;

    console.assert(style.length > 0);
    console.assert(fragment.length > 0);

    const spritesPath = (style === "solid") ? spritesPathSolid : spritesPathBrands;

    return ele("svg",
        otherProps,
        ele("use", {href: `${spritesPath}#${fragment}`}),
    );
}*/