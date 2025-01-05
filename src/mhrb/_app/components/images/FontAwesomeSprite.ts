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

*/
// Caminhos dos arquivos de sprite
const spritesPath = {
    solid: "./solid.svg",  // Caminho para o arquivo solid.svg
    brands: "./brands.svg",  // Caminho para o arquivo brands.svg
};

type Props = {
    readonly style?: "solid" | "brands";  // Estilo do ícone (solid ou brands)
    readonly fragment: string;            // Nome do ícone, ex: "discord", "home", etc.
};

export function FontAwesomeSprite(props: Props): JSX.Element { // Tipagem JSX.Element
    const {
        style = "solid",  // Valor padrão: "solid"
        fragment,          // Nome do ícone
        ...otherProps
    } = props;

    console.assert(style.length > 0);
    console.assert(fragment.length > 0);

    // Verifica se o caminho do sprite está correto
    const spritePath = spritesPath[style];

    // Retorna um erro se o caminho do ícone não for encontrado
    if (!spritePath) {
        return <span>Ícone não encontrado</span>; // Retorna o componente <span>
    }

    // Renderiza o ícone do FontAwesome
    return ele("svg", otherProps, 
        ele("use", { href: `${spritePath}#${fragment}` })  // Usando o sprite
    );
}
