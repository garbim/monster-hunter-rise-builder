/*
 * Author:  simshadows <contact@simshadows.com>
 * License: GNU Affero General Public License v3 (AGPL-3.0)
 *
 * Requires React and ReactDOM to be imported in HTML.
 */

import * as check from "../../check.js";

const element = React.createElement;
const assert = console.assert;

class PetalaceSelectView extends React.Component {
    render() {
        return element("div",
            {
            className: "select-view-wrap-box",
            id: "mhr-builder-app-petalace-select-view",
            },
            "This is the petalace select view! It's not implemented yet.",
        );
    }
}

export {PetalaceSelectView};

