# Brand brief

<!-- scan:allow-filler -->

The rules a brand runs on, in one portable file.

Hex codes and font names are the easy part of a brand, and any tool reads them accurately. Judgment is the part that gets lost: when the accent is allowed to appear, how much air a layout carries, what the brand refuses to do. This file carries the judgment.

Fill every bracket. Delete what does not apply. Vague answers produce a vague system.

Use it wherever something needs to be told how the brand behaves rather than what colors it owns: alongside logos and a finished page when a tool asks for brand assets, in a project's knowledge, at the top of a repo, or in a client handoff.

---

## The brand in one line

[Who it serves and what it does. One sentence. No adjectives you would not defend.]

**Voice.** [Two or three sentences. How headlines sound. How much the brand explains itself. Whether it is warm, flat, dry, loud.]

**Surfaces.** [Where this brand appears: website, decks, social, packaging, print, signage, apparel.]

---

## Anti-patterns

The most useful part of this document. List at least five things the brand does not do. Be concrete enough that a literal reader could catch a violation.

- [e.g. No rounded corners anywhere. Border radius is zero on every surface.]
- [e.g. No drop shadows. Depth comes from tonal surfaces, not from blur.]
- [e.g. No gradient as a background. Flat color only.]
- [e.g. No stock photography of people at laptops.]
- [e.g. No centered layouts. The grid is left-aligned.]
- [e.g. Never more than one accent color in a single frame.]

---

## Color behavior

Hex codes belong in `tokens.css`. This section is about when each color is allowed to appear.

- **Base.** [Which ground is the default, and when the dark ground is used instead.]
- **Accent.** [What earns the accent. A call to action only? A single focal element? Never as body text?]
- **Reserved.** [Any color held for one meaning. e.g. Signal red is only ever an actionable state, never decoration.]
- **Forbidden pairings.** [e.g. Accent on light ground never carries body text. It failed contrast, so it is display and UI only.]

Every text pairing has been computed against WCAG 2.2 AA, not eyeballed. Body copy clears 4.5:1, large text and UI clear 3:1. Do not introduce a pairing that has not been checked.

---

## Typography behavior

- **Display.** [Family, and what it is for. e.g. Condensed heavy, headlines only, never below 32px.]
- **Body.** [Family, and the floor. Body never sets below 16px.]
- **Utility.** [Family for labels, metadata, counters, file codes. e.g. Monospace carries every instrumentation role.]
- **Case.** [Where uppercase is allowed. Body copy is never uppercase.]
- **Scale.** [One base size, one ratio. Name them. e.g. base 16, ratio 1.333.]
- **Tracking.** [Set in em, never px. Display tightens, caps and small labels open.]

Fonts must load from a CDN such as Google Fonts or Adobe Fonts to render in the output. A proprietary face has to be handled after export.

---

## Layout behavior

- **Grid.** [Column count and alignment. e.g. 12 columns, left-aligned, heavy negative space.]
- **Spacing.** [Base unit. Everything is a multiple of it. e.g. 8pt base, 4pt for fine type work.]
- **Air.** [How much white space, and where. e.g. Generous margins, one baseline gap inside a group, double between groups.]
- **Density.** [Whether a page runs sparse or packed, and when that flips.]
- **Focal point.** [One dominant element per view. Three levels of dominance maximum.]

---

## Structure

Prompt in shapes rather than adjectives. Name the page shape and the parts, and the output lands inside the system instead of beside it.

Shapes in use: [e.g. Ledger for specs, Broadsheet for long reads, Placard for single-action pages, Index for catalogs.]

Parts in use: [e.g. nav:mark and foot:line as defaults. Never the wordmark-links-button bar or the four-column footer.]

The full catalog is in `references/shapes.md` and `references/parts.md`.

---

## Motion

- [What is allowed to move, and on what trigger.]
- [What never moves.]
- Every motion layer ships a `prefers-reduced-motion: reduce` path. No fallback means no motion.

---

## Copy rules

- [Words the brand does not use. e.g. leverage, robust, seamless, unlock, empower, streamline, comprehensive, elevate.]
- [Punctuation rules. e.g. No em dash anywhere.]
- [Whether numbers, claims, and testimonials may be generated. Default: never invent a figure. Use a real one, a labeled placeholder, or a layout that does not need one.]

---

## Attribution

[Credit line that appears on every artifact.]

---

Designed by IamAlvinV
