# Sources

<!-- scan:allow-folklore -->

Where the rules came from, and how to add more.

Nothing in this file is loaded at build time. Straightedge is self-contained: every gate, guide, and blocklist entry is already written into the other files in this folder. This is a provenance record, so a rule can be traced back and defended, and so new research can be folded in without duplicating what is already covered.

## Standards the gates come from

These are the outside authorities. When one of them updates, the gates update.

| Standard | What it governs here |
|---|---|
| WCAG 2.2 Level AA | Contrast ratios, target size, reflow at 320px, text-spacing survival, motion, focus, alt text |
| WCAG 2.2 Level AAA | The 80-character measure ceiling, the 7:1 and 4.5:1 enhanced contrast targets |
| Material Design 3 | The 8pt grid convention, the six-level elevation model, icon construction grids, 48dp targets |
| Apple Human Interface Guidelines | 44pt tap target, app icon and touch icon specs, iOS mask behavior |
| Android adaptive icons | 108dp layers, 72dp mask, 66dp safe circle, notification silhouette |
| Core Web Vitals | LCP 2.5s, INP 200ms, CLS 0.1, measured at the 75th percentile |
| W3C DTCG | The three-tier token structure: primitives, semantic, component |
| W3C SVG | Vector master format for identity work |
| Google Search documentation | H1 and title tag guidance, mobile-first indexing |

Anything in `gates.md` traces to one of these. A line that cannot be traced does not belong in `gates.md`.

Two working rules that follow from this:

- **Cite the criterion, not the vibe.** Every accessibility gate carries its success criterion number so a reader can check it in one click.
- **Point at a living spec instead of copying a token.** Platform values change between versions. Reproducing an exact shadow token or dp value from memory is how a rule quietly goes stale, so where a value is versioned, the gate says where to read it rather than stating it.

## Research the guides come from

| Body of work | What it informs |
|---|---|
| Nielsen Norman Group eye-tracking | Scanning behavior, the F-pattern as a symptom, the layer-cake target, horizontal attention bias, the scan-not-read figures |
| Gestalt perception research | Proximity, similarity, continuity, common region, figure and ground |
| Fitts's Law, Hick's Law, Von Restorff | Target sizing, choice load, the isolation effect and its limits |
| Legibility Index research on signage | The distance formula and the LI values by case and contrast |
| Typographic convention, print and screen | Measure, leading, tracking, scale ratios, superfamily pairing |
| Color science and CVD prevalence data | OKLCH ramp construction, luminance versus hue contrast, deuteranopia rates |
| Pre-attentive processing research | The 50ms first-impression window and what it means for hero design |
| Incongruity and memory research | The inverted U on surprise, why extreme disruption underperforms |

Each of these informs a guide, not a gate. Guides carry judgment. They do not carry a pass or fail line.

## The blocklist

`blocklist.md` catalogs claims that circulate as fact and are not. Each entry was traced to its origin and failed: the source is a marketing leaflet, the study says something different, the statistic has no primary source, or the claim inverts what the research actually found.

That file is why this system does not repeat the 80 percent color statistic, the goldfish attention span, or the 20 percent whitespace figure. Rules are only as good as the claims underneath them.

## Adding to the system

New research, a house style, a client system, a medium not covered here. To fold something in:

1. **Measurable lines go to `gates.md`.** Anything with a number, a standard name, or a threshold that must pass. Note which authority it comes from.
2. **False or untraceable claims go to `blocklist.md`.** Anything the new material debunks, and anything in the new material that cannot be traced.
3. **Judgment goes to the matching topic file.** `color.md`, `type.md`, `layout.md`, `concept.md`, `print.md`, `web.md`, `identity.md`, `sequence.md`, `shapes.md`, `parts.md`. If nothing fits, add a file and add a row to the routing table in `SKILL.md`.
4. **A new string-matchable false claim gets a pattern in `scripts/scan.py`.** If a machine can catch it, a human should not have to.
5. **A new shape gets a row in `shapes.md`** and its name added to the catalog in `scripts/rotate.py`, so rotation knows it exists.

Nothing here caps what the system covers. It is built to take more.

---

Designed by IamAlvinV
