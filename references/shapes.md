# Structure

Pick the shape before any visual rule. Type, color, and surface are dressing. If the shape is the same every time, changing the dressing produces the same piece in a different costume.

This is the fix for the sameness problem. Two briefs should produce two different shapes, not two color swaps of one template.

## How to use it

1. Read the index. Pick one name.
2. Check the rotation. `scripts/rotate.py check` refuses a shape used in the last three runs.
3. State the pick in plain text before writing anything: shape, why it fits the brief, what it differs from.
4. Load only that shape's row. Do not read the whole catalog into the build.

The shape decides section rhythm, entry point, divider language, and image treatment. It does not decide the palette.

## Screen shapes

| Shape | The rhythm | Fits |
|---|---|---|
| **Stack** | Hero, then evenly weighted sections down a single column. The honest default. Earns its place only when content genuinely is a sequence. | Docs, changelog, simple service page |
| **Ledger** | Two columns, left holds labels and metadata, right holds content. Reads like a spec sheet. | Technical products, pricing, comparison |
| **Statement** | One oversized display line occupies the first screen alone. Everything else is small and below it. | Manifesto, launch, brand position |
| **Bento** | Irregular tile grid, tiles of unequal span, one tile carries the hero. | Feature sets, dashboards, product tours |
| **Broadsheet** | Long-form reading column, generous margins, sidenotes, a running head. No cards anywhere. | Essays, research, editorial, case studies |
| **Console** | Interface first. The product is the hero, copy sits around it. | Tools, editors, dashboards |
| **Index** | The page is a list. Rows, not cards. Rules between, not borders around. | Catalogs, archives, portfolios, directories |
| **Split** | Fixed panel on one side, scrolling content on the other. Two speeds at once. | Case studies, product detail, galleries |
| **Counter** | Numbers lead. Large figures set the hierarchy, prose supports them. Requires real numbers. | Reports, results, proof pages |
| **Letter** | Addressed prose, signed. One voice speaking directly. Minimal structure. | Founder notes, apologies, announcements |
| **Timeline** | Ordered progression down or across. The order is the content. | History, process, roadmap, changelog |
| **Gallery** | Image-led, text is caption. Grid or sequence, never both. | Photography, product, portfolio |
| **Readout** | Monospace, ruled, dense. Information allowed to look like information. | Developer tools, status pages, data |
| **Placard** | One idea, one image, one line. Almost no scroll. The page is a single frame. | Events, campaigns, single-action pages |

## Print and static shapes

| Shape | The composition | Fits |
|---|---|---|
| **Type slab** | Display type is the image. No photograph. Fills the field. | Gigs, statements, typographic posters |
| **Frame** | Image occupies a bounded rectangle, type sits in the margin around it. | Exhibitions, film, product |
| **Bleed** | Image runs edge to edge, type sits on top in one cluster. | Fashion, travel, atmosphere |
| **Register** | Strict grid, content in cells, rules visible. Swiss discipline. | Schedules, programs, data posters |
| **Stack cut** | Horizontal bands of different heights, one band per idea. | Line-ups, menus, multi-item announcements |
| **Diagonal** | The primary axis is not horizontal. Everything aligns to a single tilt. | Sport, motion, energy |
| **Center** | Symmetrical, axial, formal. Deliberate, not lazy. | Formal invitations, luxury, ceremony |
| **Margin note** | Content sits low or off-center, most of the field is empty. | Luxury, minimal, high-restraint work |

## Rotation

Two consecutive pieces must differ on the shape. That alone is not enough. They must also differ on at least one of three visual axes:

- **Base band.** Dark (under 30% lightness), mid (30 to 85%), light (over 85%).
- **Display voice.** Condensed heavy, geometric sans, grotesque, serif, mono, script, display slab.
- **Accent temperature.** Warm (10 to 60 degrees hue), cool (200 to 300), chromatic other, or none.

If a candidate matches the previous piece on two of the three, pick something further away.

`scripts/rotate.py` computes this. It reads the log, computes the axes from the actual hex values, and refuses a repeat.

```bash
python3 scripts/rotate.py check --shape Bento --base "#0F0E0C" --accent "#C6E220" --display "condensed heavy"
python3 scripts/rotate.py log --shape Bento --base "#0F0E0C" --accent "#C6E220" --display "condensed heavy" --nav nav:pill --foot foot:mark --brief "client tool page"
python3 scripts/rotate.py history
```

The log lives at `.straightedge/log.json` in the project. It holds the last twenty entries.

## The stamp

Every delivered piece carries a stamp. In CSS it is the first line. In a document it is a metadata line. In a static image it is the filename.

```
/* Straightedge · shape: Bento · base: #0F0E0C · accent: #C6E220 · display: condensed heavy
 * gates: contrast pass · reflow pass · scan clean
 */
```

The next run reads the stamp and picks something else. Without it, rotation is a claim rather than a fact.

## When the brief is vague

Do not default. Offer three shapes from categorically different groups: one grid-led, one document-led, one poster-led. Three concrete options beat seven abstract adjectives.

---

Designed by IamAlvinV
