# Parts

The component library. Nav, hero, section head, feature block, call to action, footer, plus interaction states and motion.

Pick per piece. Rotate across pieces. The nav and the footer are part of the piece's identity, not chrome bolted on at the end.

Load only what gets picked. Do not read this file end to end into a build.

## The two tells

These are the most recognizable machine-generated shapes on the web. Reach for either one only when the content genuinely demands it, and say why out loud.

- `nav:bar` wordmark left, four or five inline links center, one filled button right, full width, thin bottom border.
- `foot:columns` four columns of links, a social icon row, a small centered copyright.

## Navigation

| Slug | Shape |
|---|---|
| `nav:bar` | Wordmark, inline links, button right. The tell. Avoid. |
| `nav:mark` | Wordmark only. No links. The page is the navigation. |
| `nav:rail` | Left rail, vertical, fixed. Labels stacked. |
| `nav:tier` | Two rows. Utility strip above, primary below. |
| `nav:pill` | Floating, detached from the edge, solid or blurred behind. |
| `nav:band` | Full-bleed bar in the accent color, type reversed out. |
| `nav:links` | Links only, right aligned. The wordmark lives in the hero instead. |
| `nav:panel` | Trigger only at every width, overlay opens the full index. |
| `nav:inline` | No separate bar. Links sit under the headline inside the hero. |
| `nav:index` | Numbered list across the top, ruled. |

## Hero

| Slug | Shape |
|---|---|
| `hero:center` | Centered headline, subhead, two buttons. The tell. Avoid. |
| `hero:left` | Left-aligned headline at display scale, one action, no image. |
| `hero:pair` | Headline and image side by side, unequal split. |
| `hero:bleed` | Full-bleed media, headline overlaid in one corner cluster. |
| `hero:product` | The interface is the hero. Copy sits above it in one line. |
| `hero:statement` | Statement only, no action. The action comes later. |
| `hero:wrap` | Headline wraps around a shape or an image. |
| `hero:slab` | Type fills the frame edge to edge. The headline is the image. |
| `hero:figure` | One large number leads. The headline is its caption. |

## Section head

| Slug | Shape |
|---|---|
| `head:center` | Centered heading with a centered lede. Overused. |
| `head:split` | Heading left, lede right, one row. |
| `head:bare` | Heading alone. The lede folds into the first item. |
| `head:ruled` | Heading with a rule running the full measure beneath it. |
| `head:stack` | Small label above the heading, same column, left aligned. |

Labels and eyebrows default off. No `01 / FEATURES` unless the content is genuinely ordinal or the shape is Timeline, Broadsheet, or Index. Two per piece maximum.

When a label is used, stack it directly above the heading in the same column. The arrangement with the label hanging in a left margin and the heading in a right column is the most reliable templated tell in editorial layout. Do not use it.

## Feature block

| Slug | Shape |
|---|---|
| `feat:cards` | Three equal cards with icons. The tell. Avoid. |
| `feat:alt` | Alternating rows, image and text swapping sides. |
| `feat:list` | Rules between items, no containers. |
| `feat:grid` | Irregular grid, one item spanning two tracks. |
| `feat:table` | A table. When the content is comparable, compare it. |
| `feat:steps` | Numbered sequence. The order carries meaning. |

## Call to action

| Slug | Shape |
|---|---|
| `cta:box` | Centered box on a tinted band. The tell. Avoid. |
| `cta:band` | Full-bleed accent band, one line, one action. |
| `cta:inline` | Inside the flow, no dedicated section. |
| `cta:foot` | The footer is the call to action. No separate block. |
| `cta:dock` | Persistent, docked to an edge, dismissible. |

## Footer

| Slug | Shape |
|---|---|
| `foot:columns` | Four link columns plus a social row. The tell. Avoid. |
| `foot:line` | One line. Credit, one link, nothing else. |
| `foot:mark` | Large wordmark or statement, small links beneath. |
| `foot:pair` | Two columns. Contact left, index right. |
| `foot:statement` | A full sentence at display scale. |
| `foot:index` | Links as ruled rows, not columns. |
| `foot:invert` | Flips the base and text colors from the rest of the page. |
| `foot:map` | Exhaustive sitemap. Only for a genuine hub. |

## Rotation

Two consecutive pieces in a project do not share a nav slug or a footer slug. `scripts/rotate.py` records both and refuses a repeat.

## Interaction states

Every interactive element ships styling for all eight. Not seven.

`default` · `hover` · `focus-visible` · `active` · `disabled` · `loading` · `error` · `success`

What tends to get missed:

- `:focus-visible` appears instantly. Never animate the ring in. Ring contrast at least 3:1 against both the element and its background.
- Disabled is exempt from the contrast gate but must still read as disabled without relying on color alone.
- Loading needs a real signal, determinate or clearly indeterminate. A dimmed label is not a loading state.
- Error is announced to assistive technology, not only shown.
- Prefer silent success over a celebratory toast. Prefer an optimistic update with undo over a confirmation dialog.

## Motion

- Animate `transform` and `opacity` only. Never layout properties.
- Three named easings, used consistently. Never the browser default `ease`. No bounce or overshoot on UI state.
- Hover tooltips delay 800ms. Focus tooltips delay 0ms.
- Under three motion primitives per piece.
- The reduced-motion path collapses spatial motion to an opacity crossfade of 150ms or less.
- Cut motion before adding it. If removing an animation loses no information, remove it.

---

Designed by IamAlvinV
