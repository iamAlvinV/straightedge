# Gates

Every measurable pass/fail line in the system, in one place. If a line is here, it is not a preference. Compute it, do not estimate it.

Contents: Contrast, Type and measure, Space and grid, Targets, Reflow and text-spacing, Motion, Web performance, SEO and HTML, Legal, Print and signage, Logo and icon, Legibility distance, Concept gates.

---

## Contrast (WCAG 2.2 AA)

| Element | Minimum |
|---|---|
| Body text (SC 1.4.3) | 4.5:1 |
| Large text (24px, or 18.66px bold) | 3:1 |
| UI components, meaningful icons, form borders, focus rings (SC 1.4.11) | 3:1 |
| AAA body, SC 1.4.6 (government, healthcare, finance, accessibility-exposed) | 7:1 |
| AAA large | 4.5:1 |

- Thresholds are hard. 4.49:1 fails. Do not round up.
- 4.5:1 is passing, not good. Body text should sit above it.
- Do not use pure black on pure white. 21:1 causes strain. Sit inside a band.
- Body text on a light surface uses the 700 to 800 ramp step, not 500.
- Check text over gradients and images at the worst-case point.
- Recheck contrast after adding any texture, gradient, or overlay behind text.
- Never drop contrast below the gate to de-emphasize. Reduce size or weight instead.
- Never encode meaning in color alone (WCAG 1.4.1). Pair with text, icon, shape, or position.
- Thin or hairline type at low contrast is a readability failure even when the number passes. Hold a higher bar for light weights.
- Exempt: logos, brand names, purely decorative text, disabled or inactive components, default browser focus styles.
- The logo exemption ends the moment the logo functions as a link or a button.

Color vision deficiency: about 4.5% of men globally, up to 8% of men of Northern European descent, about 0.5% of women. Roughly 99% is red-green, deuteranomaly most common. Run one deuteranopia sim. Avoid red-green, green-brown, and blue-purple as the only difference between two states.

Note: APCA is perceptual and handles white-on-orange better than WCAG 2, but it is not law. WCAG 3.0 is a draft, years out. Use APCA to inform, conform to 2.2 AA.

---

## Type and measure

- Body floor: 16px on screen.
- Anything under 24px, or under 18.66px bold, is normal text and must clear 4.5:1.
- Measure: 50 to 75 characters. 66 is the target for a single column. 80 is the hard ceiling (WCAG SC 1.4.8, Level AAA). UI microcopy 25 to 40 characters is fine.
- Set measure in `ch` or `em`. A pixel width only holds at one font size.
- Body line-height: at least 1.5, unitless.
- Keep line-heights on multiples of 4 so baselines land on the grid.
- Set tracking in `em`, never px.
- No body copy in all caps. Uppercase reads faster only for one or two glanceable words.
- Maximum three type sizes visible in one view.

---

## Space and grid

- Base unit 8px. Every margin, padding, and dimension a multiple of 8.
- 4px sub-step for fine type and icon adjustment only.
- Working scale: 4, 8, 16, 24, 32, 40, 48, 64, 104.
- Type baselines align to a 4pt grid.
- Grouping: one baseline gap inside a group, at least double between groups. Keep gaps between large blocks equal across the layout.

---

## Targets

- Minimum interactive target: 24 by 24 CSS px (WCAG 2.2 SC 2.5.8, Level AA).
- Primary and touch-first controls: 44 by 44pt (Apple) or 48 by 48dp (Material). Treat 44 to 48 as the working target.
- Undersized targets can still pass by spacing: center a 24px circle on each one and confirm no circle intersects another target or another undersized circle, which means centers at least 24px apart (the SC 2.5.8 Spacing exception).
- The AAA version, SC 2.5.5, asks for 44 by 44 CSS px.

---

## Reflow and text-spacing survival

- Layout works at 320 CSS px width with no two-dimensional scrolling (WCAG 2.2 SC 1.4.10, Reflow). Equals a 1280px desktop at 400% zoom. Exceptions: data tables, maps, complex toolbars.
- Nothing breaks or clips when the user forces all four at once: line-height 1.5, paragraph spacing 2x font size, letter-spacing 0.12em, word-spacing 0.16em (WCAG 1.4.12).
- No fixed-height text containers.

---

## Motion

- Ship a `prefers-reduced-motion: reduce` fallback for any non-essential motion. No fallback, no motion.
- Interaction-triggered motion must be disable-able unless essential to the content (WCAG 2.3.3).
- Named vestibular risks: parallax, zoom, spin, autoplay carousels, large-movement effects.
- Audio silent by default. Sound is opt-in.
- Custom cursors are not an affordance.

---

## Web performance (Core Web Vitals, 75th percentile of real users)

| Metric | Pass |
|---|---|
| LCP, Largest Contentful Paint | 2.5s or less |
| INP, Interaction to Next Paint | 200ms or less |
| CLS, Cumulative Layout Shift | 0.1 or less |

- Compress and preload hero media.
- Set explicit width and height on images.
- Defer heavy scripts. JavaScript is the main INP driver.
- `font-display: swap`.
- Budget motion. Heavy hero media and animation are the usual LCP and INP failures.
- 3D and WebGL: single hero moment only, lazy-loaded, static fallback, reduced-motion path, tested on a real mid-tier Android.

---

## SEO and HTML

- One clear descriptive H1 per page, written for humans.
- Title tag written separately from the H1. It is the SERP title.
- Do not paste a raw search phrase into the hero H1. UX cost, little ranking gain.
- H1 count is not a ranking factor. Do not chase it.
- Google indexes the mobile version. Content, structured data, and metadata on mobile must match desktop.
- Design mobile in parallel with desktop, not after.

---

## Legal

- Privacy policy required when the site collects any personal data. Contact forms, analytics, and cookies all count.
- Cookie notice and terms where data use and jurisdiction require them.
- Jurisdiction-dependent. Confirm current law for the audience. This is not legal advice.

---

## Legibility by viewing distance (print, signage, environmental)

Formula: letter height = maximum viewing distance / Legibility Index.

Two indices. They answer different questions. Do not swap them.

- **Research legibility**, can it be read at all: LI about 30. Roughly 1 inch of cap height per 30 feet.
- **Best-impact**, does it read effortlessly at a glance: roughly 1 inch of cap height per 10 feet. Conservative commercial rule. Use when the goal is glance-and-go.

Specific LI values, external sans-serif, standard conditions:

| Setting | LI |
|---|---|
| Black Helvetica on white, upper and lower case | about 29 |
| Black Helvetica on white, all caps | about 25 |
| High-contrast reversed, all caps (white on black, yellow on green) | about 22 |

Worked check: 600 feet maximum distance at LI 30 gives 600 / 30 = 20 inches minimum letter height.

---

## Logo and icon

- Master built in vector. SVG, AI, or EPS. Paths, not pixels. Raster is fixed-size delivery only.
- Designed in solid black on white before any color.
- Black-and-white legibility test at 24px height. Fail means simplify the form, not the color.
- Minimum sizes stated in both px and mm. Digital full lockup 80 to 120px wide floor. Digital icon-only 24px height floor. Favicon 16px. Print full wordmark 15 to 25mm. Business card about 20mm.
- Clear space as a proportional unit, a multiple of a repeating logo element. Common: 0.5x logo height, or the wordmark cap-height. Never a fixed pixel value.
- Alt text on every logo placement (WCAG 1.1.1).

Icon and app specs:

| Asset | Spec |
|---|---|
| favicon.ico | contains 16, 32, often 48 |
| Browser tab PNG | 32 by 32 |
| apple-touch-icon | 180 by 180 PNG, opaque, corners not pre-rounded, not over-padded. iOS applies its own mask and about 10% padding |
| PWA / web manifest | 192 and 512 PNG |
| iOS app master | 1024 by 1024, no alpha, sRGB or P3 |
| Android adaptive | two 108 by 108dp layers, both fully drawn |
| Android mask | system masks to 72 by 72dp maximum, outer 18dp per side clipped |
| Android safe zone | all critical content inside a centered 66dp circle |
| Play Store | 512 by 512 PNG |
| Android notification | separate monochrome silhouette, white on transparent |

Material construction grids:

- System icons: 24 by 24dp grid, 2dp stroke, 2dp corner radius on silhouettes, square interior corners.
- Product icons: 48dp grid with 1dp live edges, scaled 400% to 192 by 192dp holding the 48-unit ratio.
- Keyline shapes: circle, square, portrait and landscape rectangles.

---

## Elevation (Material Design 3)

- Six levels, named for relative distance above the surface: 0, +1, +2, +3, +4, +5.
- Resting states use 0 to +3. Levels +4 and +5 are reserved for user-interacted states such as hover and dragged.
- Elevation can be expressed with shadow **or** with tonal difference between surfaces, a surface fill that lightens as it rises. Prefer tonal.
- Take the dp value and shadow token for each level from the current Material 3 elevation spec rather than from memory. The values have changed between Material 2 and Material 3, and reproducing a stale token is worse than reading the spec.

## Concept gates

Not measurable in pixels, still pass/fail.

- **One first-notice element.** Exactly one. If a viewer cannot tell what to look at first, the hierarchy failed.
- **Three levels of dominance, maximum.** More reads as noise.
- **Three contrast variations, maximum.** If everything contrasts, nothing stands out.
- **Moderate incongruity only.** A resolvable surprise. Extreme incongruity performs worse than both a moderate surprise and a clean expected design. The relationship is an inverted U, not a slope.
- **One disruption per piece.** Not several competing ones.
- **The surprise attaches to the brand or message.** Test: name the one thing a viewer remembers ten seconds later. If it is the gag and not the brand, the piece failed.
- **Reduction pass on every piece before export.** Any element that cannot justify why it stays, goes.
- **Objective written before opening software.** Audience, emotion, business goal.
- **Never ship raw AI output as final.** Human QA pass on every generated asset: hallucinated details, changed proportions, style drift.
- **Do not rely on base-model consistency for a multi-asset brand system.** Single-subject consistency is solved. Full system coherence across packaging, social, web, motion, and type is not.

---

## Pre-attentive timing (design consequence, treated as a rule)

- Aesthetic first impression of a visual: about 50ms. Fastest measured 17 to 50ms.
- Trust judgment from a face: about 100ms.
- Pre-attentive detection of color, size, orientation: about 200 to 250ms.

Consequence: the hero and the intended feeling land through image, size, color, and layout, not through text. If the piece needs the viewer to read words to get the point, it failed the first glance.

Impression latency is not dwell time. Do not pace a design as if the viewer has seconds to decide.

---

Designed by IamAlvinV
