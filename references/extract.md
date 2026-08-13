# Extract

Protocol for pulling a usable system out of a reference the user supplies: a screenshot, a URL, a photograph, a print scan, a moodboard.

The output is a **specification of structure**, not a copy of the reference. What transfers is the system. What does not transfer is the content, the industry theming, the illustration style, and anything protected.

## What to extract

Work down the list. Record a value for each, or write `not visible` and say so.

**Grid and structure**
- Container width and side margins.
- Column count, gutter width.
- Whether content is left-aligned, centered, or asymmetric.
- Vertical rhythm: the repeating gap between major blocks.
- Base spacing unit, inferred from the smallest repeating gap.

**Type**
- Number of distinct families. Name them if identifiable, otherwise classify: geometric sans, grotesque, humanist sans, transitional serif, slab, mono, display.
- Size steps visible, and the ratio between them.
- Weight steps in use.
- Body measure in characters, counted, not guessed.
- Line-height on body and on display.
- Tracking direction on display and on caps.
- Case discipline: where caps appear, where they do not.

**Color**
- Sample the actual hex values. Do not describe them from memory.
- Assign roles: base, surface, text, accent, and how many accents.
- Count how many colors appear more than once. That is the real palette.
- Compute contrast on every text pairing found.

**Hierarchy**
- What is the first-notice element and what makes it win: size, isolation, color, position.
- How many levels of dominance.
- How many contrast levels.

**Surface**
- Corner radius, one value or several.
- Shadow presence and depth. Tonal elevation or drop shadow.
- Border weight and color.
- Texture, grain, noise, and at roughly what opacity.
- Whether images are full-bleed, contained, or masked.

**Motion**, if it is a live URL
- What animates, on what trigger.
- Duration and easing if inspectable.
- Whether a reduced-motion path exists.

## How to record it

Emit design tokens, not prose. An extraction is finished when it produces something buildable:

```json
{
  "grid": { "container": 1200, "columns": 12, "gutter": 24, "margin": 60, "base": 8 },
  "type": {
    "families": ["grotesque sans", "mono"],
    "base": 16, "ratio": 1.333,
    "steps": [16, 21, 28, 38, 51],
    "weights": [400, 700],
    "measure_ch": 64,
    "leading": { "body": 1.55, "display": 1.05 },
    "tracking": { "display": "-0.02em", "caps": "+0.08em" }
  },
  "color": {
    "base": "#E9E7DE", "text": "#0F0E0C",
    "accent": ["#C6E220"], "surface": "#FFFFFF"
  },
  "surface": { "radius": 0, "shadow": "none", "border": "1px solid #0F0E0C" },
  "hierarchy": { "focal": "display headline, scale + isolation", "levels": 3, "contrast_levels": 2 }
}
```

## Gates still apply

The reference is not an authority. It is an input.

- If the reference fails contrast, the study records the failure and the build corrects it. Do not inherit a defect because it looked good.
- If the reference uses fixed-height text containers, px tracking, or a measure over 80 characters, note it and fix it in the build.
- If the reference is a slop default from the SKILL.md list, name it and propose the replacement rather than reproducing it.

## What not to copy

- Copy, headlines, taglines, and body text.
- Photography, illustration, and iconography that belongs to the reference.
- A logo or mark.
- The reference's industry framing. A layout studied from a fintech site is a structural skeleton. It is not a fintech design.
- Anything close enough that a viewer would recognize the source.

The line: structure, ratios, spacing logic, and hierarchy tactics transfer. Identity does not.

## Multiple references

When several are supplied, do not average them. Averaging produces the generic result the whole system exists to avoid.

- Extract each separately.
- Name what each one is actually contributing: one for grid, one for type voice, one for color, one for surface treatment.
- Pick one to lead. The others contribute a single named element each.
- If two references pull the same element in different directions, choose on the objective, not on preference.

---

Designed by IamAlvinV
