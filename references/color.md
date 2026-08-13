# Color

Order: build the palette, pass the gate, design in gray, add color, decide conform or stand out, screen culture if the audience is global.

## Build

Build ramps in **OKLCH**, not HSL. HSL steps look uneven and go muddy at the ends.

Ramp 50 to 950 per hue. Base identity sits at 500.

| Step | Job |
|---|---|
| 50 to 100 | backgrounds, hover states, subtle dividers |
| 200 to 300 | borders, dividers, secondary surfaces |
| 500 | base brand color |
| 700 to 800 | body text on light surfaces |

Build one ramp each for primary, accent, and neutral gray. Add status hues if the UI needs them: success, warning, error, info. Material does not ship these. Error red still has to hit 4.5:1 on its background.

## Tokens

Three tiers, W3C DTCG structure.

1. **Primitives.** The raw 50 to 950 scale values.
2. **Semantic.** Roles pointing at primitives: `--color-primary`, `--button-bg`, `--text-muted`.
3. **Component.** References semantic, never primitives directly.

Change the primitive once, everything updates. Components referencing primitives directly is what breaks dark mode and theming.

Dark mode: invert lightness, hold hue and chroma.

## Color roles

- **Primary.** Key actions and identity. Used sparingly. Not everything is primary.
- **Secondary.** Support and depth. Does not compete with primary.
- **Accent.** Attention. CTA and focal points. Must contrast against its immediate surroundings, not just the page.
- **Neutral.** Structure, spacing, readability. Most of the UI. Let it carry the layout.

## Apply

- **Gray first.** Build hierarchy with contrast, size, and placement before any hue goes in. If the layout does not work in gray, color will not fix it.
- Color does less work than beginners think. Hierarchy and contrast carry the layout.
- Saturated primary is for key actions only.
- 60-30-10 is a balance check, not a law. Use it as a sanity scan.
- Harmony schemes are brainstorming aids, not guarantees. Value and saturation balance matter more than wheel relationship. Analogous palettes lack hierarchy and usually need an out-of-scheme accent.

## Hue contrast is not luminance contrast

Two different things both called contrast.

- **Hue contrast** is color-wheel opposition.
- **Luminance contrast** is difference in lightness.

Readability and visual pop are driven by luminance. Complementary pairs can share almost identical luminance, which reads as vibrating and often fails legibility. Black on white is the practical perceptual maximum at about 21:1. Use it as the mental anchor for how strong contrast gets, not as a target.

## Emotional color (guide)

- Associations are real and partly universal, but probabilistic.
- Lightness and chroma drive feeling more than hue. Lighter plus higher chroma reads happier. Darker plus desaturated reads heavier.
- Context shifts meaning. Typography, imagery, industry, and audience all move how a hue reads. The same red can read premium, loud, or playful.
- Blue reads trust, and also cold, corporate, and clinical.

## Competitive color (guide)

- Categories cluster. Blue in finance and tech (55%+ of finance, about 60% of tech leaders). Red in retail. Black and gold in luxury.
- Decide on purpose: conform for instant category legibility, or pick a distinctive-but-appropriate hue for memory. Both are valid.
- Color alone is a weak brand asset. It becomes ownable through consistent use over years, paired with a mark, type, and layout system.
- Uniqueness matters more than the specific hue. Changing the asset later resets the clock.

## Culture (screen only for global or specific-market work)

Well documented:
- **White.** Purity and weddings in the West. Mourning and death in much of East and South Asia. The big one for white-heavy palettes.
- **Red.** Luck and celebration in China, Korea, South Asia. Danger everywhere in safety contexts.

Verify per market: green (prosperity in China, sacred in Islam, nature broadly), purple (mourning in Thailand and Brazil, royalty in the West).

## Current direction (guide, dated)

Soft neutrals and off-whites as the base, with teal, jewel tones, or one restrained accent on top. Neon is a micro-accent now, not a base. Gradients trend smoky, ambient, and mesh rather than harsh neon transitions. The palette passes contrast first. Taste comes after the numbers pass.

## Checklist

```
[ ] Ramps built in OKLCH, 50 to 950, for primary, accent, neutral
[ ] Semantic tokens defined over primitives, components never touch primitives
[ ] Every text pairing computed, body uses the 700 to 800 step
[ ] UI components and icons pass 3:1
[ ] No meaning carried by color alone
[ ] Deuteranopia sim run
[ ] Layout worked in gray before color went in
[ ] Primary reserved for key actions
[ ] Conform-or-stand-out decided on purpose
[ ] Culture screened if the audience is global
[ ] No folklore stats anywhere in the rationale
```

---

Designed by IamAlvinV
