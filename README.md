# Straightedge

A design execution engine for Claude.ai, Claude Code, Cursor, and Codex.

It makes design work pass before it ships: real contrast math, a shape catalog that refuses to repeat itself, and a scan that blocks delivery on a defect. The format follows the open Agent Skills standard, a folder with a SKILL.md, so it runs in any tool that reads that standard.

Built by Alvin V, brand and visual systems designer, New Orleans. [IAMALVINV.COM](https://iamalvinv.com) · @IAMALVINV

## Six briefs, six shapes

Built with Straightedge in one sitting. No two consecutive pages share a shape, a nav, a footer, or more than one dressing axis. Every color pairing computed, every page reflow-tested at five widths. Full set and the gate report in [`examples/`](examples/).

| | | |
|:---:|:---:|:---:|
| [![Statement](examples/renders/01.png)](examples/01-statement.html) | [![Console](examples/renders/02.png)](examples/02-console.html) | [![Counter](examples/renders/03.png)](examples/03-counter.html) |
| **Statement** | **Console** | **Counter** |
| [![Timeline](examples/renders/04.png)](examples/04-timeline.html) | [![Register](examples/renders/05.png)](examples/05-register.html) | [![Gallery](examples/renders/06.png)](examples/index.html) |
| **Timeline** | **Register** | **Gallery** |

It does four things:

1. Holds every measurable standard in one place and refuses to ship work that fails one.
2. Picks a shape from a catalog before it picks any visual rule, and logs it so the next piece is a different shape.
3. Routes a task to the right references instead of loading all of them.
4. Computes the numbers with scripts rather than estimating them by eye.

Craft is decided here. Taste and direction are not.

Four verbs: build (default), `audit`, `restyle`, `extract`.

## Prior art

Straightedge shares a premise with [Hallmark](https://github.com/Nutlope/hallmark) (MIT): a design tool should pick a page shape before it picks a palette, and it should refuse the defaults every model was trained into. That premise is Hallmark's, and it is credited.

The comparison below describes Hallmark as of August 2026. It is an active project, so check the repo rather than trusting this table if the difference matters to you.

Where the two differ:

| | Hallmark | Straightedge |
|---|---|---|
| Gate verification | Gates are checked by the model as it works; the repo ships no scripts | Python computes contrast, rotation, reflow, and the ship scan; scripts exit non-zero |
| Rotation | A log file the model reads and judges against | A script parses the hex values, derives the axes, and refuses the repeat |
| Mediums | Web | Web, print, signage, packaging, apparel, identity, decks, social |
| Claim discipline | An anti-patterns reference | A sourced blocklist of debunked design statistics, enforced by string scan |
| Standards | Cited in the rule-set | Every gate traced to WCAG 2.2, Material 3, Apple HIG, or Core Web Vitals in `sources.md` |
| Themes | A catalog of named themes to dress the page in | None, on purpose. Shapes and gates ship; palette and type voice come from your brand, so two users never land the same look |

The shape catalog, part library, gates, blocklist, and all five scripts are written from scratch. No Hallmark file, table, or catalog is reproduced here.

## What you can make with it

Straightedge is not a website tool. It covers any medium a designer ships:

- **Web**: landing pages, full sites, dashboards, UI components, emails
- **Print**: posters, flyers, programs, menus, editorial spreads
- **Brand**: logo and identity systems, favicons and app icons, token sets, guidelines
- **Marketing**: social posts, carousels, campaign sets, ads, pitch decks
- **Physical**: packaging, signage, environmental graphics, apparel

Same gates everywhere. The medium changes which reference loads, not whether the work has to pass.

## What is in it

```
straightedge/
  SKILL.md              gate card, order of operations, verbs, routing, ship check
  LICENSE               MIT
  templates/
    brand-brief.md      the soft rules a brand runs on, in a portable format
    tokens.css          three-tier token starter, ready for a brand swap
    tokens.json         the same tokens in W3C DTCG format
  references/
    gates.md            every pass/fail line in the system
    blocklist.md        folklore and debunked claims, never enter the work
    shapes.md           22 named shapes, screen and print, plus the rotation rule
    parts.md            nav, hero, section head, feature, CTA, footer, states, motion
    component.md        single-element scope and the state preview
    color.md            OKLCH ramps, tokens, roles, emotional and competitive color
    type.md             scale, hierarchy, weight, pairing, tracking, voice
    layout.md           grid, space, Gestalt, eye path, balance, depth, rhythm
    concept.md          objective, one idea, incongruity, reduction, memorability
    print.md            poster, signage, packaging, apparel, production specs
    web.md              landing pages, UI, motion, trend tiers, performance
    identity.md         logo, variants, favicon and app icon system
    sequence.md         carousels, campaigns, decks, spreads
    extract.md          pulling the system out of a supplied reference
    sources.md          where each rule came from, and how to fold in new research
  scripts/
    contrast.py         WCAG contrast and colorblind simulation
    typescale.py        type scale from a base and a ratio, as CSS custom properties
    rotate.py           project memory, refuses a repeated shape or dressing
    scan.py             ship scan: em dash, folklore, filler, craft defects
    render.py           Playwright PNG render, squint frame, 320px reflow check
```

## Dependencies

None beyond the runtime. The skill is self-contained: markdown plus five Python scripts on the standard library, Pillow for the squint frame, and Playwright for rendering. Every rule is already written into `references/`. Nothing is read from outside the folder at build time. `references/sources.md` is a provenance record, not a manifest.

## Install

**Claude Code** gets the whole packet: references, scripts, templates. This is the full experience, since the scripts actually run.

```bash
# personal, available in every project
mkdir -p ~/.claude/skills && cp -r straightedge ~/.claude/skills/

# or project scope, committed and shared with the repo
mkdir -p .claude/skills && cp -r straightedge .claude/skills/
```

The path must be `skills/straightedge/SKILL.md`, not nested one level deeper.

**Claude.ai**: zip this folder and upload it under Customize, Skills. Claude reads the references and applies the gates; the scripts run when the chat has code execution turned on. On Team or Enterprise plans an admin enables Skills in organization settings first. A Claude project also works: drop the folder contents into project knowledge, everything is plain markdown.

**Cursor** reads skills from `.cursor/skills/straightedge/`, loaded on demand when a task matches the description. Copy the folder there. For always-on guidance instead, put the body of `SKILL.md` in a `.cursor/rules/*.mdc` file, which Cursor injects by glob or by mode. Cursor also reads a root `AGENTS.md`.

**Codex** reads skills from `$HOME/.agents/skills/straightedge/` for personal scope, or `.agents/skills/straightedge/` checked into a repo for a team. Copy the folder there unchanged. Codex uses the same progressive disclosure as Claude Code: description first, `SKILL.md` when chosen, references and scripts only when needed.

One packet, four surfaces. Nothing is rebuilt per platform; what changes is how much runs. Claude Code, Cursor, and Codex execute the scripts. Chat surfaces apply the rules and run scripts where code execution is available.

Paths change. If an install path here does not match what your tool documents, trust the tool.

## Use

The skill fires on any design or build task without being named. To call it directly:

```
Use straightedge. Poster for [X], read at 20 feet, one accent.
straightedge extract <screenshot or URL>
straightedge audit <file or page>
straightedge restyle <file or page>
```

## Templates

Three files in `templates/`, useful anywhere, tied to no platform.

- **`brand-brief.md`.** The soft rules. Anti-patterns, when the accent is allowed to appear, forbidden color pairings, case discipline, how much air the layout carries. Hex codes and font names are the easy part of a brand; this is the part that gets lost. Fill it in once and hand it to whatever tool needs to know how the brand behaves.
- **`tokens.css` and `tokens.json`.** A three-tier token starter, primitives through semantic to component, in CSS custom properties and in W3C DTCG format. Swap the primitive values and everything downstream follows.

## Scripts

```bash
python3 scripts/contrast.py --pair "#0F0E0C" "#C6E220"
python3 scripts/contrast.py --palette "#E9E7DE,#0F0E0C,#C6E220,#DE7256"
python3 scripts/contrast.py --cvd "#C6E220,#DE7256"

python3 scripts/typescale.py --base 16 --ratio 1.333 --steps 6

python3 scripts/rotate.py suggest
python3 scripts/rotate.py check --shape Bento --base "#0F0E0C" --accent "#C6E220" --display "condensed heavy"
python3 scripts/rotate.py log   --shape Bento --base "#0F0E0C" --accent "#C6E220" --display "condensed heavy" --nav nav:pill --foot foot:mark --brief "tool page"
python3 scripts/rotate.py history

python3 scripts/scan.py page.html
python3 scripts/scan.py ./build --recursive

python3 scripts/render.py page.html --width 1440 --out render.png --reflow
```

`scan.py` and `rotate.py check` both exit non-zero on a failure, so they drop straight into a build step.

## Extending it

New research, a house style, a client system, a medium not covered yet. `references/sources.md` has the procedure: measurable lines go to `gates.md`, false claims go to `blocklist.md`, judgment goes to a topic file or a new one, and a new string-matchable claim gets a pattern in `scan.py`. Nothing here caps what the system covers.

---

Designed by IamAlvinV
