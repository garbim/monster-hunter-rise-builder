# Monster Hunter Rise Builder

A web-based build calculator for Monster Hunter Rise.

This project was inspired by Honey's [MHW build calculator](https://honeyhunterworld.com/mhwbi/).

The application is currently almost minimally feature-complete for EFR/EFE/EFS calculations, with only some important features missing or unverified (see *Missing/Unverified Features* below). Defense calculations will be implemented later. UI improvements will continue to be made throughout development.

## Where can I access this website?

I'm currently hosting it at:

- <https://monsterhunter.simshadows.com/mhrb/> (stable version)
- <https://monsterhunter-dev.simshadows.com/mhrb/> (unstable/development version)

Please use and link to the stable version where possible.

Only use the unstable/development version if you're interested in using features unavailable in the stable version (e.g. for new armour pieces, or to try out new features).

## How do I compile the website?

First, you need to install node and npm. On Debian, this can be done with:
```
sudo apt-get install nodejs npm
```

Afterwards, you'll need to clone and enter the repo:
```
git clone https://github.com/simshadows/react-tsx-ghpages-toolchain-test.git
cd react-tsx-ghpages-toolchain-test
```

Optionally, set up npm with a globals directory (and reopen your terminal session):
```
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
```

Now, install yarn globally (and optionally, check its version):
```
npm install -g yarn
yarn --version
```

Now you're good to go! Build and serve the app using:
```
yarn build
yarn serve
```

Or, you can use webpack's development server:
```
yarn start
```

## Key Features Missing/Unverified

- Element/Status calculations in general will need to be verified.
- Many bowgun rampage skills will need to be verified.
    - To save time/resources, I took guesses, which are marked with `TODO` comments in `calculate/step1_get_base_values.js`.
- Bowgun ammo attributes aren't implemented (including LBG rapid fire).
    - This data is not available on Kiranico, and I don't want to manually collect this data at this stage.
- HBG special ammo.
    - This data is also not available on Kiranico.
- Bowgun Power Barrel/Long Barrel calculation needs to be verified
    - Particularly, at the line `const baseRaw = Math.trunc((b.baseRaw * b.baseRawMul) + b.baseRawAdd + 0.1);` in `calculate/index.js`.
- Important damage-related features not yet implemented:
    - Magnamalo Soul (Rampage Skill)
    - Dulling Strike (Rampage Skill)
    - Brutal Strike (Rampage Skill)
    - Silkbind Boost (Rampage Skill)
    - Element Exploit (Rampage Skill)
    - Fogoblight Exploit (Rampage Skill)
    - Waterblight Exploit (Rampage Skill)
    - Thunderblight Exploit (Rampage Skill)
    - Geloblight Exploit (Rampage Skill)
    - Small Monster Exploit (Rampage Skill)
    - Anti-Aerial Species (Rampage Skill) elemental/status damage contribution (if it has any)
    - Anti-Aquatic Species (Rampage Skill) elemental/status damage contribution (if it has any)
    - Wyvern Exploit (Rampage Skill) elemental/status damage contribution (if it has any)
    - Rapid Fire Up (Armour Skill)
    - Normal/Rapid Fire Up (Armour Skill)
    - Pierce Up (Armour Skill)
    - Spread Up (Armour Skill)
    - Stormsoul (Armour Skill)

## Roadmap

### Future Release: v1.x.x

Particularly in-demand features missing from v1.0.0 may be implemented in patches. Otherwise, no more new features are planned before the codebase port (which will probably be v3.0).

I will also not implement defense calculations until after the codebase port.

### Future Release: v2.0

Updated builder for the Sunbreak expansion.

### Future Release: v3.0

**The second release of the app will be a codebase port. No new features are planned for v3.0 at this time, but will come with performance improvements and will ultimately pave the way for future features and sustainable development.**

The app before v3.0 is a totally toolchainless codebase. This was done because I only want to introduce complexity as it is needed. Without a toolchain, the entire codebase is only dependent on the browser, and three front-end libraries (React, html2canvas, and FileSaver).

v2.0 will allow me to reassess the project's needs, benchmark the app's performance, and experiment with different toolchain configurations, all with a fully-functional web app with all core features implemented.

I expect the codebase to be ported to a fully Typescript codebase (either plain Typescript or TSX), with major things rewritten for modularity, type/logic safety, and for unit testing, as well as address some glaring technical debt incurred during rapid development of v1.0.

In addition to porting the codebase, I expect to optimize the graphics to reduce download sizes and implement efficient image preloading.

*(NOTE: If time permits, I might do this codebase port as v2.0 instead, and update for Sunbreak as v3.0.)*

### Future Release: v3.x

Along with bug fixes, math adjustments, and minor improvements, I expect to implement:

- key UI improvements (e.g. talisman configuration screen),
- defense calculations, and
- responsive UI.

I don't want to do defense calculations and math improvements too early since it will make the Sunbreak update and codebase port releases take longer to develop.

### Future Release: v4.0 and Beyond

**It is not guaranteed that I will be continuing adding features beyond v3.x. Anything written here is an indication of intent, if time allows.**

Beyond v3.x, the focus of the development will be on game math. Tentative roadmap:

- v4.0: Build Search

    - Users will be able to let the app automatically come up with builds.

    - v4.0 will first attempt to reimplement <https://mhrise.wiki-db.com/sim/?hl=en>. v4.1 and beyond will build on v4.0, adding addtional search constraints and features.

- v5.0: Combat Modelling

    - Users will be able to build a benchmark consisting of one or many weapon moves (or "Motion Values"), and one or many monster parts (or "Hitzone Values").

    - Weapon moves and monster parts are selected from motion value tables and hitzone value tables (such as `Deathcream#1576`'s Weapon Attack Tables [[link](http://bit.ly/MHRWeaponAttackTables)] [[alternative link](https://docs.google.com/spreadsheets/d/e/2PACX-1vSMMtrWj7JH1-_Qr_xKb2lxZaZJ_Sq-ta43u6fLmpzVwqMfiTR-KqAFRDk6Zuw9WzM1sCgU9Th5lMoj/pubhtml)]). This data will be available in-app.

    - Based on the user's selected benchmark, the app will display how much real damage (raw, elemental, and status) is done.

    - Alternatively, the user can let the program analyze the best monster parts to attack.

    - **Factoring in damage from poison will be difficult due to its time-dependence. (On the other hand, blast is time-independent, making it possible to model by counting stat buildup and blast procs.)**

Server-side functionality is unlikely to be implemented. The entire app will remain 100% client-side.

### Long-Term Goals

I aim to design this codebase in such a way that it can be easily reused to build other Monster Hunter builder apps, or maybe even similar apps for games outside of Monster Hunter. This way, when the next game is released, we should hopefully have a fully-working builder within weeks, or even days!

### Cut Features

Features intentionally cut:

- **Switch Skill Selection**: Switch Skills are not important in core calculations. I'll add them later after getting feedback on the first iteration of the web app.

- **Kinsect Selection**: Also not important in core calculations, but I'll listen to feedback in case people want it.

- **Localization**: Due to time and resource constraints, the only language this app will be available in is English. I'll reconsider depending on the app's popularity, user feedback, funding, and if I can get consistent volunteers. It's a lot of commitment for such a small and niche app with relatively high UI complexity.

- **Accessibility**: This is also due to time and resource constraints. May be considered for a future app release.

## Error Handling

Good error handling is currently severely lacking. Only render errors are caught, and that wipes the screen to display an error.

Errors in event handlers will silently fail. This is especially bad.

Errors in script imports will also silently fail, and the only way a user will know is if they're stuck on the loading screen for too long, or if they look at the browser developer tools.

## Contributing

I am not accepting code contributions and pull requests at this time, but I am happily accepting feedback. Feel free to [open an issue](https://github.com/simshadows/monster-hunter-rise-builder/issues)!

Or, feel free to fork and improve, or use this as a template for a builder program for other games! My only request is to maintain the AGPL licensing and include appropriate attribution.

## License

All original source code is licensed under the [*GNU Affero General Public License v3.0 (AGPLv3)*](https://www.gnu.org/licenses/agpl-3.0.en.html).

All non-original source code is contained in `/js/dependencies` and have their own attached licenses. *(Exception: The loading spinner is in-line in `./index.html` and is licensed under CC0.)*

All original images are licensed under the [*Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)*](https://creativecommons.org/licenses/by-sa/4.0/).

All non-original and derived images are contained in `/images/derived` and `/images/placeholders`. I am currently working on replacing them with original or properly-licensed sourced creations.

