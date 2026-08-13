# Type

## Scale

Pick a base size, pick one ratio, multiply the steps. The method is the rule. The ratio is the choice.

| Ratio | Name | Use |
|---|---|---|
| 1.2 | Minor third | dense UI, tight hierarchy |
| 1.25 | Major third | safe default for UI |
| 1.333 | Perfect fourth | most common for web and editorial |
| 1.414 | Augmented fourth | editorial with room |
| 1.5 | Perfect fifth | dramatic display hierarchy |
| 1.618 | Golden | widest, most expressive, display only |

- Body-text-inclusive screen work: 1.2 to 1.333.
- Display-led short-text layouts, posters and hero sections: 1.5 to 1.618.
- Do not default to 1.618 for anything carrying real body copy. Too few usable sizes, oversized headings, breaks on mobile.

Classic print scale, a safe default: 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 21, 24, 36, 48, 60, 72.

Reference sizes for calibration (Material 3): Display 57/45/36, Headline 32/28/24, Title 22/16/14, Body 16/14/12, Label 14/12/11.

Web ranges that work: body 16px, subhead 18 to 22px, header 32px and up. Heading near 3x body gives clean separation. Rule of thumb, not a gate.

Run `scripts/typescale.py` to generate the steps as CSS custom properties.

## Hierarchy

- Three tiers is the floor: heading, subhead, body. Add a display level for big titles. Real systems run 4 to 6.
- Show only 2 to 3 sizes in a single view.
- Convey hierarchy through size and weight together, never size alone.
- Order of power: size, then weight, then color and contrast, then position, then spacing.
- Combine 2 to 3 cues per level. One cue alone is weak.
- Cap contrast variations at 3.
- Front-load the information-carrying words in headings and the first line of a block.

## Weight

- One variable superfamily across weights covers most hierarchies. Two typefaces are not required.
- Skip a weight. 400 with 700 reads. 400 with 300 does not. A working set: 400 body, 600 subhead, 800 headline.
- The requirement is clear distinction between roles, not a specific numeric gap.
- CSS numeric weights only render distinctly if the font ships them or has a continuous weight axis. Confirm the file supports what you specify.

## Pairing

- Prefer a superfamily. One system with sans, serif, and mono siblings built to sit together. Pairing across families is where cohesion is lost.
- Free superfamilies that work out of the box: Source (Sans, Serif, Code), Roboto (Sans, Serif, Slab, Mono, Condensed), DM (Sans, Serif Display, Serif Text, Mono).
- If pairing across families, pair by contrast in classification, not similar-but-different. A display or script face against a neutral serif or sans works because the contrast is clear. Two faces that are close but not identical read as a mistake.
- Match x-height and stroke contrast, and test at real sizes before committing.

## Tracking and leading

| Context | Tracking | Line-height |
|---|---|---|
| Body | 0, font default | 1.4 to 1.6, at least 1.5 |
| Display above 60px | -0.02 to -0.03em | 1.0 to 1.1 |
| Headings, multi-line | slightly tight | 1.1 to 1.2 |
| All caps, CTA labels | +0.05 to +0.1em | as set |
| Very small text | slightly open | looser |

Rule: smaller relative size wants more tracking, larger wants less. Set tracking in `em`. Never letterspace lowercase body text.

## Typographic voice

Take one typeface and force it to carry distinct moods using only weight, scale, tracking, italic, and alignment. No new fonts, no color. These cause-effect links are reliable:

- **Tracking changes tone.** Open reads calmer and more elegant. Tight reads denser and more urgent.
- **Weight changes confidence.** Heavier reads assertive. Lighter reads quiet.
- **Alignment changes intention.** Flush left, centered, and justified each signal a different formality. Choose on purpose.
- **Scale changes emphasis.** Size sets the reading order.

Exhaust the expressive range of the fonts already in hand before downloading another. Knowing fonts is picking a typeface. Knowing typography is controlling why a treatment creates trust, tension, or noise.

## Type personality (guide)

Serif reads traditional, formal, or premium. Sans reads modern or neutral. A soft tendency, culture and context dependent, not a rule. Going against the convention can create intrigue. That is a creative bet, not a law.

## In logos

- 1 to 2 typefaces maximum.
- Kern the wordmark by hand. Kerning is where amateur and professional split.
- Verify legibility at the stated minimum size.
- Avoid hairline strokes and extreme stroke contrast. They vanish small.
- Script is not banned. It fails small-size legibility and some categories, and works for luxury, personal, and food. Judge by legibility.

---

Designed by IamAlvinV
