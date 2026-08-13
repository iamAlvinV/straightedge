# Layout

## Grid

- Set the grid before content. Step one, not cleanup.
- Parts: columns, gutters, margins, baseline grid.
- Columns: 12 desktop, 8 tablet, 4 mobile. 12 is the default because it splits into halves, thirds, fourths, and sixths.
- Web default gutter: 24px. Material margins: 16px compact, 24px medium. Desktop artboard: about 60px container margin on 1440px width.
- Column count and margin width flex with the layout. Having a grid is the rule. The exact numbers are the guide.

Breakpoints are not standardized. Frameworks disagree. Pick the value where the layout actually breaks. Common anchors: 600 / 840 / 1200 / 1600 (Material) or 640 / 768 / 1024 / 1280 (utility frameworks).

## Space as grouping

Whitespace is a grouping tool, not leftover room. More space between unrelated blocks, less within a group.

- One baseline value inside a group, for example 16.
- At least double between groups, for example 32.
- Equal gaps between large blocks across the layout, for example a consistent 104 between nav, text block, and image.
- More space around an element reads as more importance.
- Micro whitespace: between lines, paragraphs, letters. Macro whitespace: between major blocks and at page margins.

## Hierarchy

- Name the communication goal first. The most important element is decided by the goal, not by reflex. The hero is not always the biggest thing. On an event poster the date or location can outrank the image.
- One dominant focal point. At most one secondary. Three levels of dominance total.
- Size is not the only source of emphasis. When size is wrong for the job, use isolation, contrast, or placement.
- Isolating an element with space makes it the focal point. Works through proximity and figure-ground.

Focal point tactics, pick exactly one:

1. **Unique hue.** Mute everything else, give the focal element its own color.
2. **Unexpected scale.** Oversize it, let it bleed to the edge.
3. **Subtle motion.** Blur, trail, or movement, on that one element only.

Too many different elements cancel out. One isolation move per composition. If using motion or color as the differentiator, account for motion-sensitive and colorblind viewers.

## Gestalt

- **Proximity.** Items placed close together read as related. Use gap, not lines.
- **Common region.** A shared container groups items even across distance.
- **Similarity.** Shared color, shape, or size signals one set.
- **Continuity.** The eye follows aligned edges. Align to a shared axis.
- **Figure and ground.** Decide which is which on purpose.
- Alignment is grouping. A clean left edge does more work than a border. Alignment is most visible when absent. Check edges.

Review pass, CRAP: contrast, repetition, alignment, proximity.

## Reading direction and eye path

- Start point depends on the reader's language, not on a universal law. Left-to-right readers start top-left and weight attention left. Right-to-left readers (Arabic, Hebrew) mirror it. Flip every top-left assumption for RTL.
- Top and left carry natural prominence in LTR. Place the primary message high. Above the fold gets most viewing time, but users scroll. Do not cram everything up top.
- A centered focal point is usually the easiest thing to see. Center bias is real. Center for stability, break it for movement.
- **Break the F-pattern.** It is a fallback caused by weak formatting, not a target. Use headings, bold key terms, bullets, front-loaded words, and visual grouping.
- Target the **layer-cake pattern**: descriptive visually distinct subheads, chunked content, front-loaded keywords. The most efficient scan pattern.
- Z-pattern and the Gutenberg diagram apply only to sparse low-hierarchy layouts, simple posters and minimal landing pages. The moment real hierarchy exists, they stop applying.

## Directional cues (reinforcement only)

- **Gaze.** A face or figure looking toward an element pulls attention there. Harder to override than an arrow. Point gaze at the thing you want seen, never out of frame.
- **Leading lines, angles, diagonals, curves.** Guide along an implied path (continuation). Move from the dominant element to the next in order.
- **Arrows.** The bluntest version. Spread attention across the whole cued region. Use when clarity beats subtlety.
- **Light and shadow.** Weakest cue. A nudge, not a lever.
- Give a subject room to move into the frame. A right-facing subject sits left of center.
- Every cue serves the hierarchy. The effect is small. It biases a first glance. It does not fix weak hierarchy.

## Balance

- Symmetry reads stable and formal. Asymmetry reads active and modern.
- Balance by visual weight: size, color density, and contrast pull the eye. Offset a heavy element with space or a cluster of lighter ones.
- No fixed number governs balance. This is craft. Do not present it to a client as measured fact.

## Depth

- Prefer tonal elevation, surface lightens or tints as it rises, over heavy shadows. Reserve shadows and scrims for the one element that needs focus.
- Think in layers. One element forward, one sitting back.
- One strong 3D element plus clean 2D layering beats a wall of 3D assets.
- Depth hurts scannability when overused. Too many competing layers is a fail, not a flex.
- Elevation levels and how to source their values: `references/gates.md`.

## Rhythm and disruption

- Rhythm controls where the eye moves and rests: fast hit, slower scan, open pause. A bold hero, then dense detail, then whitespace around a single element.
- Implied motion is real. Repetition, progressive scaling, motion blur, and directional patterns make a static design feel like it moves.
- Flow disruption works by breaking a pattern. An element that interrupts the expected path becomes a focal point. Use it deliberately to slow the viewer at a key message. Do not scatter disruptions.
- Break symmetry on purpose. Imperfection must be intentional. Sloppiness is not the skill.

## Squint test

Blur the design, or squint at it. The headline and primary focal point must still dominate. If it flattens into one blob, fix size, weight, spacing, or contrast before anything else. `scripts/render.py` produces the blurred frame.

---

Designed by IamAlvinV
