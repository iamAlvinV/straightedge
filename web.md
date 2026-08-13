# Web, UI, and landing pages

All of `gates.md` applies. This file is the build order and the calls that are web-specific.

## Order

1. Content and copy structure first. Cut walls of text into blocks, one idea each. Convert scannable content to lists.
2. Set the measure.
3. Lay the grid and space on the 8pt system, grouped by proximity.
4. Set leading. Body first, then headings.
5. Set tracking. Body default, display and caps only.
6. Pair the type. One superfamily or a tested pairing.
7. Add color into a layout that already works in gray.
8. Decoration last. Gradients, textures, shadows, subtle and behind content.
9. Squint test and contrast check. Fix what does not survive.
10. Performance pass. Then reflow, text-spacing, motion, and targets.

## Copy structure

- No block over three or four sentences.
- Bullets for parallel scannable items. Keep them short and grammatically parallel. A bullet that runs three lines is a paragraph wearing a dot.
- Numbered lists only when order or count matters. Readers read numbers as steps.
- Users scan. About 79% scan, roughly 20 to 28% of words get read.

## Hero and first impression

- The hero carries the objective. What it is, who it is for, what to do next.
- One primary action. A second competing CTA of equal weight halves both.
- The H1 is written for a human. The title tag is written separately for the SERP.
- Do not put the hero's meaning in an image the user has to interpret. Image supports, text confirms.
- Hero media is the usual LCP failure. Compress, size explicitly, preload.

## Decoration discipline

- Content is the focus. Decoration supports, never competes.
- When a background texture fights copy, drop a soft radial gradient or a solid plate behind the text. Do not lower the text contrast to fix it.
- Give a form field or CTA its own background fill so it reads as the action.
- Recheck contrast after every texture, gradient, or overlay.
- Adding elements past the point of clarity subtracts from the message.

## Motion

- Continuous, state-driven motion reads alive. Entrance-only animation reads static.
- CSS scroll-driven animation runs off the main thread. It is the performance-safe way to get movement.
- Fades and opacity changes are generally safe. Parallax, zoom, spin, and autoplay carousels are the named vestibular risks.
- Every layer respects `prefers-reduced-motion`. This is where motion work fails.
- Do not animate everything. Motion works with restraint and one clear focal point.

## Trend adoption tiers (guide, dated)

**Safe.** Minimalism with expressive typography. Blueprint and technical aesthetic with annotation lines and monospace labels, used sparingly before it turns into parody. Tech gradient as a small accent, pushed past the default sphere fade. Maximalism inside a grid: bigger header type, one pop color, controlled density. CSS scroll-driven animation.

**With guardrails.** WebGL and 3D via Spline, Unicorn Studio, or Rive: one hero moment, lazy-loaded, static fallback, reduced-motion path, four to eight hours budgeted, tested on a real mid-tier Android. 3D breaks scroll, click, and text selection, so isolate it. Y2K and internet nostalgia: yes to colors, type, pixel art, retro framing. No to custom cursors as an affordance. Interaction sound: click-triggered only, muted by default, global toggle, one soft tone.

**Reject.** Anti-UX as breaking navigation and affordance conventions. Unpolished visuals are fine. Breaking how the site is used is a usability regression. Autoplay background audio, blocked by browsers and a WCAG risk.

## Responsive

- Mobile in parallel with desktop, not after. Google indexes mobile.
- Breakpoints chosen where the layout breaks, not by device name.
- Reflow at 320px with no horizontal scroll.
- Touch targets at 44 to 48, not 24, on anything primary.

## Delivery

- Ship the working file. An HTML file, a component, a rendered page. Not a description of one.
- Single file where practical. CSS and JS inline for HTML deliverables.
- No browser storage APIs in Claude artifacts. React state or in-memory JS only.
- Render and inspect the result with `scripts/render.py` before calling it done. Looking at the code is not looking at the page.

## Checklist

```
[ ] Copy chunked, lists parallel and short
[ ] Measure in ch or em, 50 to 75, under 80
[ ] 8pt grid, proximity grouping, equal gaps between large blocks
[ ] Body line-height at least 1.5 unitless, headings 1.1 to 1.2
[ ] Tracking in em, body at default
[ ] One superfamily or a tested pairing
[ ] Contrast computed: 4.5:1 body, 3:1 large and UI, rechecked after decoration
[ ] No fixed-height text containers, text-spacing override survived
[ ] Targets 44 to 48px primary, 24px floor
[ ] Reflow at 320px
[ ] prefers-reduced-motion path on every motion layer
[ ] LCP, INP, CLS budgeted, images sized, scripts deferred, font-display swap
[ ] One H1 for humans, title tag written separately
[ ] Privacy policy if any personal data is collected
[ ] Squint test passed, headline and primary CTA dominate under blur
[ ] scan.py clean
[ ] Credit line present
```

---

Designed by IamAlvinV
