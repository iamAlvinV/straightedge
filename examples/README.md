# Examples

Six pages built with Straightedge. Five demonstrate a different structural shape, the sixth is a Gallery index that links them.

The point of the set is rotation. Every page differs from the one before it on the shape, on the navigation part, on the footer part, and on at least two of the three dressing axes. Nothing here is one template in six colorways.

Each file is a single self-contained HTML document. Inline CSS, no build step, no bundler, no framework. Open any of them directly in a browser. Display and body faces load from the Google Fonts CDN, so a machine without those faces installed still gets the intended typographic voice.

```
examples/
  index.html          Gallery, the set
  01-statement.html   Statement
  02-console.html     Console
  03-counter.html     Counter
  04-timeline.html    Timeline
  05-register.html    Register, a print shape
  renders/            01 to 06 at 1440px, plus the squint and 320px frames
  README.md
```

## The set

| # | Shape | Nav | Foot | Band | Voice | Accent |
|---|---|---|---|---|---|---|
| 01 | Statement | `nav:mark` | `foot:statement` | Light, `#F4F1EA` | Condensed heavy, Anton | `#B3261E`, chromatic other |
| 02 | Console | `nav:tier` | `foot:line` | Dark, `#0E1116` | Mono, JetBrains Mono | `#79C0FF`, cool |
| 03 | Counter | `nav:links` | `foot:pair` | Mid, `#BFB8AA` | Grotesque, Space Grotesk | `#6E2F0E`, warm |
| 04 | Timeline | `nav:index` | `foot:invert` | Light, `#FBFAF7` | Serif, Fraunces | `#2F5D50`, chromatic other |
| 05 | Register | `nav:band` | `foot:mark` | Dark, `#131211` | Geometric sans, Jost | `#EA5A2B`, warm |
| 06 | Gallery | `nav:pill` | `foot:index` | Mid, `#C8C3B8` | Display slab, Alfa Slab One | `#1B4D8F`, cool |

Body faces, all from the Google Fonts CDN: Public Sans, IBM Plex Sans, Source Sans 3, Karla, Work Sans, Rubik.

No two consecutive rows share a shape, a nav slug, a foot slug, or more than one dressing axis. In fact every consecutive pair differs on all three axes, which `rotate.py check` reported as `CLEAR. Differs on: band, voice, temp` at each of the six checks.

`nav:bar` and `foot:columns`, the two shapes named in the skill as the most recognizable machine tells, appear nowhere in the set.

## Subjects

Every page documents something real from this repository or from a published standard. No invented metrics, no fabricated testimonials, no placeholder logos, no stock imagery.

- **01 Statement.** The gate and guide distinction, and the conflict order, from `SKILL.md`. One idea: a gate is not an opinion.
- **02 Console.** The unedited terminal output of the `contrast.py` and `scan.py` runs that set and corrected the palette of example 03. The output shown is verbatim, including the two failing rows.
- **03 Counter.** The numeric floors, each attributed to its clause. WCAG 2.2 SC 1.4.3, 1.4.6, 1.4.8, 1.4.10, 1.4.11, 1.4.12, 2.5.5, 2.5.8, and the three Core Web Vitals thresholds. The one figure that is not a published criterion, the 16px body floor, is labeled on the page as a house rule.
- **04 Timeline.** The sixteen steps of the order of operations, from `SKILL.md`.
- **05 Register.** All twenty-two shapes from `references/shapes.md`, with the six used in this set marked in the cells.
- **06 Gallery.** Real screenshots of the five pages, taken by `render.py`, presented in `figure` elements with captions. No re-drawn browser chrome anywhere in the set.

Credit line on all six.

## Computed gate results

Every pairing below was computed with `scripts/contrast.py`. None were estimated.

### Contrast, per page

| Page | Pairing | Ratio | Body 4.5:1 | Large and UI 3:1 |
|---|---|---|---|---|
| 01 | `#17150F` ink on `#F4F1EA` paper | 16.18:1 | pass | pass |
| 01 | `#4A463C` secondary on paper | 8.34:1 | pass | pass |
| 01 | `#B3261E` accent on paper | 5.79:1 | pass | pass |
| 01 | `#8B8474` rule on paper | 3.29:1 | n/a | pass |
| 02 | `#D9E0E8` text on `#0E1116` ground | 14.21:1 | pass | pass |
| 02 | `#A2ADBA` secondary on ground | 8.31:1 | pass | pass |
| 02 | `#79C0FF` accent on ground | 9.72:1 | pass | pass |
| 02 | `#D9E0E8` text on `#171C24` panel | 12.85:1 | pass | pass |
| 02 | `#79C0FF` accent on panel | 8.79:1 | pass | pass |
| 02 | `#626C7A` rule on ground | 3.55:1 | n/a | pass |
| 03 | `#1B1712` ink on `#BFB8AA` field | 9.04:1 | pass | pass |
| 03 | `#423A2E` secondary on field | 5.68:1 | pass | pass |
| 03 | `#6E2F0E` accent on field | 5.13:1 | pass | pass |
| 03 | `#5F5A50` rule on field | 3.48:1 | n/a | pass |
| 04 | `#1A1A18` ink on `#FBFAF7` page | 16.70:1 | pass | pass |
| 04 | `#4E4E48` secondary on page | 8.02:1 | pass | pass |
| 04 | `#2F5D50` accent on page | 7.18:1 | pass | pass |
| 04 | `#8E8B83` rule on page | 3.26:1 | n/a | pass |
| 04 | `#FBFAF7` page on `#1A1A18` inverted footer | 16.70:1 | pass | pass |
| 04 | `#8E8B83` secondary on inverted footer | 5.12:1 | pass | pass |
| 04 | `#7FB8A6` accent lift on inverted footer | 7.73:1 | pass | pass |
| 05 | `#EDE9E1` ink on `#131211` field | 15.45:1 | pass | pass |
| 05 | `#A9A296` secondary on field | 7.39:1 | pass | pass |
| 05 | `#EA5A2B` accent on field | 5.34:1 | pass | pass |
| 05 | `#131211` field on `#EA5A2B` nav band | 5.34:1 | pass | pass |
| 05 | `#6B655C` rule on field | 3.24:1 | n/a | pass |
| 06 | `#14120F` ink on `#C8C3B8` field | 10.64:1 | pass | pass |
| 06 | `#45403A` secondary on field | 5.84:1 | pass | pass |
| 06 | `#1B4D8F` accent on field | 4.77:1 | pass | pass |
| 06 | `#C8C3B8` field on `#14120F` nav pill | 10.64:1 | pass | pass |
| 06 | `#63605A` rule on field | 3.57:1 | n/a | pass |

Rows marked `n/a` for body are rules and borders. They are held to the 3:1 non-text floor of SC 1.4.11 rather than the 4.5:1 body floor, and no type is set on them.

Lowest body pairing in the set is `#C8C3B8` on `#1B4D8F` at 4.77:1. Lowest non-text pairing is `#6B655C` on `#131211` at 3.24:1. Both clear their gate.

### Color vision deficiency

`contrast.py --cvd` run on the field, ink, and accent of each page. No collisions under deuteranopia, protanopia, or tritanopia on any of the six. Nothing in the set carries meaning by color alone: severity in example 02 is spelled `FAIL` and `WARN` in text and carries a distinct block glyph, the pivot steps in example 04 are labeled `Pivot step`, and the set markers in example 05 read `Set 01` through `Set 06`.

### Reflow and text spacing

Checked at 320, 375, 414, 768, and 1440px. At each width, twice: once as shipped, once with the WCAG SC 1.4.12 override forced on every element (line height 1.5, letter spacing 0.12em, word spacing 0.16em, paragraph spacing 2em).

| Page | 320 | 375 | 414 | 768 | 1440 |
|---|---|---|---|---|---|
| 01 | pass | pass | pass | pass | pass |
| 02 | pass | pass | pass | pass | pass |
| 03 | pass | pass | pass | pass | pass |
| 04 | pass | pass | pass | pass | pass |
| 05 | pass | pass | pass | pass | pass |
| 06 | pass | pass | pass | pass | pass |

No horizontal scroll at any width, in either state. No element with clipped overflow had content exceeding its box, so nothing is cut off when a reader forces their own spacing. The `render.py --reflow` gate reported `320px reflow gate: PASS` on all six independently.

### Other gates

- Type scale from one base and one ratio, 16px at 1.333, from `typescale.py`. Body 16px on every page, line height 1.6.
- Measure set in `ch` throughout. Prose columns sit between 34ch and 66ch, under the 80ch ceiling of SC 1.4.8.
- Tracking in `em` everywhere. `scan.py` reports no px tracking.
- Targets: links carry a 24px minimum height. The primary actions on the Gallery index and its footer rows are 44px.
- Motion: link color transitions only, 140ms, with a `prefers-reduced-motion: reduce` path on every page. No parallax, no autoplay, no spin.
- Performance: fonts load with `display=swap` via the CDN URL, with `preconnect` to both Google Fonts hosts. Every image in the Gallery carries explicit `width` and `height` plus a CSS `aspect-ratio`, so the plates reserve their space before the PNG arrives. No JavaScript on any page.
- Tokens locked. Every color and face is a named custom property. No inline hex, no bare `font-family` mid-render.
- Squint frames generated for all six. The intended focal point survives the blur on each: the statement line, the console panel, the 4.5:1 figure, the step-ten headline, the catalog title, the index headline.

### Ship scan

`python scripts/scan.py` across all six files: **0 FAIL, 42 WARN**.

Zero em dashes. No folklore claims. No filler vocabulary. Credit line found on all six.

## What failed a gate

Nothing was worked around quietly. This is the full list.

**1. Four color pairings failed on the first computation.** Caught by `contrast.py` before any markup was written, and fixed by moving the token, not by moving the text off the color.

| Page | Original | Ratio | Gate missed | Replaced with | New ratio |
|---|---|---|---|---|---|
| 03 | accent `#8A3B12` on field | 3.92:1 | body 4.5:1 | `#6E2F0E` | 5.13:1 |
| 05 | accent `#D4451B` on field | 4.16:1 | body 4.5:1 | `#EA5A2B` | 5.34:1 |
| 05 | rule `#55504A` on field | 2.35:1 | non-text 3:1 | `#6B655C` | 3.24:1 |
| 02 | rule `#2A323C` on ground | 1.46:1 | non-text 3:1 | `#626C7A` | 3.55:1 |

Two further rules, `#C9C3B4` on the example 01 paper at 1.56:1 and `#4A5460` on the example 02 ground at 2.46:1, were rejected as candidates during the same pass and never shipped.

**2. A contrast failure that only the render caught.** On example 04 the `Pivot step` tag was declared `color: var(--page)` on an accent background, but the earlier `.track p` rule had higher specificity and won, leaving `#4E4E48` on `#2F5D50` at **1.12:1**. Invisible. The 1440px render showed it as an empty green rectangle. Fixed by raising the selector to `.track p.pivot-tag`. The identical trap was then found and fixed pre-emptively on example 05, where `.cell p` would have overridden the set marker to `#A9A296` on `#EA5A2B` at 1.78:1.

This one is worth naming: the palette matrix passed, the tokens were correct, and the page still shipped an unreadable element. Computing the palette is not the same as computing the page.

**3. A broken grid on example 01.** The conflict-order list put three children into a two-column grid, so every description wrapped into a 3ch column, one word per line. Visible only in the render. Fixed by wrapping the text in a single grid child.

**4. A dead cell on example 05.** Fourteen screen shapes do not divide into a four-column grid, and the rule color was being drawn by the grid gap, so the two empty tracks rendered as a large grey block. Rewritten to draw the rules as cell borders, which leaves the ragged tail open rather than filled.

**5. Sixteen scan FAILs on the first ship scan.** All one cause: BEM modifier class names, the kind that separate block from modifier with two hyphens, match the scanner's paired-hyphen rule. That rule exists to catch two hyphens standing in for a dash in copy, so these were false positives in intent, but they were real failures against the gate. The classes were renamed to single hyphens rather than the check being suppressed. The scan is now clean.

The same caution applies to this file: it documents the failure without reproducing the pattern, because a scan that a delivery file is allowed to fail is not a gate.

## Warnings accepted, and why

The 42 remaining `scan.py` WARNs fall into two groups. Both were reviewed rather than dismissed.

**Uppercase, 29 instances.** All `text-transform: uppercase` on micro-labels, wordmarks, section labels, and display headings. No body copy is set in caps anywhere in the set.

**Line height under 1.4, 13 instances.** All on display and heading type, never body. Body copy is 1.6 unitless on all six pages.

Two deviations that the scanner does not catch, stated rather than hidden:

- **Display line height below the 1.1 card figure.** The skill card asks for 1.1 to 1.2 on headings. Several display lines in this set are tighter: 1.02 on the example 01 statement, 0.98 on the example 05 poster title, 0.9 on its footer mark, 0.86 on the example 03 lead figure. At 90px and above, 1.1 opens visible gaps between lines of a single thought. This is a convention default, ranked fifth in the conflict order, not an accessibility gate. The accessibility-relevant figure, body line height of at least 1.5, is met at 1.6 everywhere.
- **Micro-labels at 14px.** The `--size-label` token is `0.875rem`. That is below the 16px body floor, and `scan.py` does not flag it because the declarations reference a token rather than a literal. These are caps labels, clause citations, and metadata rows, not body copy, and each still clears 4.5:1. Flagging it here so it is a decision on the record rather than an oversight.

## Rotation log

Written by `rotate.py log` after each build, read by `rotate.py check` before the next.

```
DATE         SHAPE        BAND   VOICE              ACCENT   NAV        BRIEF
------------------------------------------------------------------------------
2026-08-13   Gallery      mid    display slab       cool     nav:pill   example 06
2026-08-13   Register     dark   geometric sans     warm     nav:band   example 05
2026-08-13   Timeline     light  serif              chromatic nav:index example 04
2026-08-13   Counter      mid    grotesque          warm     nav:links  example 03
2026-08-13   Console      dark   mono               cool     nav:tier   example 02
2026-08-13   Statement    light  condensed heavy    chromatic nav:mark  example 01
```

The log lives at `.straightedge/log.json` at the repository root.

## Reproducing the checks

Run from the repository root.

```bash
python scripts/contrast.py --palette "#BFB8AA,#1B1712,#423A2E,#6E2F0E,#5F5A50"
python scripts/contrast.py --cvd "#BFB8AA,#1B1712,#6E2F0E"
python scripts/scan.py examples/01-statement.html examples/02-console.html \
                       examples/03-counter.html examples/04-timeline.html \
                       examples/05-register.html examples/index.html
python scripts/render.py examples/01-statement.html --width 1440 \
                         --out examples/renders/01.png --reflow
python scripts/rotate.py history
```

`render.py` needs `playwright` with the Chromium browser installed, and `pillow` for the squint frame. It loads the pages over `file://` and waits for the network, so the Google Fonts CDN must be reachable for the renders to carry the intended faces.

---

Designed by IamAlvinV
