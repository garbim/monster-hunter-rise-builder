/*
 * Author:  simshadows <contact@simshadows.com>
 * License: GNU Affero General Public License v3 (AGPL-3.0)
 */

import React from "react";
const ele = React.createElement;

/*import {
    imgFASolidSprites,
    imgFABrandsSprites,
} from "../../images";

// TODO: Is prop forwarding here a good idea?

type Props = {
    readonly style?:   "solid" | "brands";
    readonly fragment: string;
};// & React.ComponentProps<"svg">;
*/
// Caminhos dos arquivos de sprite
const spritesPath = {
    solid: "/images/fontawesome/solid.svg",  // Caminho para o arquivo solid.svg
    brands: "/images/fontawesome/brands.svg",  // Caminho para o arquivo brands.svg
};

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

    const spritesPath = (style === "solid") ? imgFASolidSprites : imgFABrandsSprites;

    return ele("svg",
        otherProps,
        ele("use", {href: `${spritesPath}#${fragment}`}),
    );
}

