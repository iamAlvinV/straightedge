# Print, poster, signage, packaging, apparel

Everything in `gates.md` still applies except the web-only sections. The changes below are what the medium adds.

## Start with distance, not the canvas

Fix the maximum viewing distance before sizing anything. Then apply the formula.

`letter height = maximum viewing distance / Legibility Index`

- Bare readability: LI about 30. Roughly 1 inch cap height per 30 feet.
- Glance-and-go impact: roughly 1 inch cap height per 10 feet. The conservative commercial rule.

LI values, external sans-serif: black on white upper and lower case about 29, all caps about 25, high-contrast reversed all caps about 22.

Set a recognition target at each distance. A gig poster read at 6 feet in a hallway and a trade poster read at 30 feet across a hall are different pieces.

## Hierarchy caps hold harder here

- Exactly one first-notice element.
- Three type sizes maximum.
- Three contrast variations maximum.
- Two large attention elements per view maximum.

A poster has no scroll and no hover. Everything competes at once. This is where cap violations show fastest.

## Contrast in print

- WCAG is a screen standard, but the luminance logic transfers. Compute the pair anyway. A palette that fails on screen usually fails on paper too.
- Ink on uncoated stock gains. Fine reversed type fills in. Do not set hairline reversed text under about 8pt on uncoated.
- Coated stock holds detail and pushes saturation. Uncoated mutes and desaturates. Expect a shift.
- Build in CMYK for offset, or supply RGB with a stated profile if the printer is digital and asks for it. Confirm which before building, not after.
- Rich black for large solid areas, not 100K alone. Single-channel black for small type.

## Production specs to confirm before building

Ask, do not assume. Every number below is the common default, not a standard. The printer's spec wins.

- Final trim size and orientation.
- Bleed, usually 3mm or 0.125in. Extend every background element into it.
- Safe margin for critical content, usually 3 to 5mm inside trim.
- Fold, score, die-cut, or perforation lines, on their own layer.
- Stock, coating, and finish.
- Spot colors, foil, emboss, or varnish as separate plates.
- Resolution: 300ppi at final size for photography, 150ppi acceptable for large-format viewed at distance, vector for everything else.

## Apparel

Craft guides, not gates. Confirm with the decorator.

- The mark has to survive one-color reproduction. This is the black-and-white test again, in cloth.
- Screen print: limit colors. Every color is a screen and a cost.
- Avoid hairline strokes and fine gaps. They clog or break.
- Halftones behave differently on fabric than paper. Coarse the screen.
- Embroidery kills detail. Simplify to shape and mass, no gradients, no thin lines under about 1mm.
- Placement and size in inches on a garment spec, not px.

## Packaging

Craft guides. Regulatory and supplier specs are the gates.

- The panel is read in sequence, not at once. Decide front-panel hierarchy, then side, then back.
- The front panel is a signage problem. Apply the distance formula at shelf distance, roughly 3 to 6 feet.
- Mandatory copy (ingredients, weight, barcode, regulatory) is a fixed constraint. Lay it in before the design, not after.
- Barcode quiet zone and minimum size are supplier specs. Get them.
- Test on the actual dieline, flat and mocked in 3D.

## Signage and environmental

- Distance formula is the whole job.
- Viewing angle changes effective distance. Off-axis needs more height.
- Reversed type reads smaller than positive type at the same size. The index drops from about 25 to about 22 for all caps, so size up roughly 15% when reversing. See the LI table in `gates.md`.
- Ambient light, glare, and motion of the viewer all cut legibility. Round up, never down.
- Local sign ordinances are an outside authority. They outrank taste and they outrank the brand system.

## Checklist

```
[ ] Maximum viewing distance fixed, recognition target per distance
[ ] Hero and headline sized by the formula, correct LI for the case and contrast
[ ] Exactly one first-notice element
[ ] Three type sizes maximum, three contrast levels maximum
[ ] Feeling carried by image, size, color, layout, not by text
[ ] Trim, bleed, safe margin confirmed with the printer
[ ] Color space and stock confirmed, black built correctly
[ ] Resolution correct at final size, vector where possible
[ ] Fold and die lines on their own layer
[ ] Mark survives one-color reproduction
[ ] Reduction pass done, secondary info grouped tight
[ ] Squint test passed
[ ] Credit line present
```

---

Designed by IamAlvinV
