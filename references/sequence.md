# Social, carousels, campaigns, decks, spreads

Any piece that is read as a set rather than a single frame.

## Sequence rules

- Hold one visual language across the set. Consistency is the constant. Tension is the variable.
- Vary rhythm across frames: open with tension, expand, shift emphasis, add a breather, resolve on the payoff.
- Do not clone one layout across every frame. Repeating a template is not sequencing.
- Ask four questions of any sequence: where does the eye begin, where does it escalate, where does it pause, where does it resolve.
- Pacing is real craft. "This exact tension curve boosts engagement" is not proven. Do not attach a metric.

## Per-frame discipline

Every frame is still a poster. It gets the full hierarchy treatment:

- One first-notice element per frame.
- Three type sizes, three contrast levels.
- The point lands without the caption. Assume the caption is never read.
- Frame one carries the whole idea. Treat it as the only frame that will be seen.

## Thumbnails

A contact sheet is read at thumbnail size, so the frame is chosen for that size. Capture the first screen, not the full page. A long page reduced to a grid cell becomes a vertical strip with no legible content, which reports the page as worse than it is. `scripts/render.py --thumb` does this: 1440 by 900, downscaled to 1200 wide.

## Platform reality

- Confirm current dimensions and safe areas before building. Platform specs change and are an outside authority.
- Build to the largest supported size, then check legibility at the feed thumbnail size. Most work fails at thumbnail, not at full size.
- Platforms recompress. Flat color and vector survive. Fine gradients and film grain band badly.
- Text is a legibility problem at thumbnail scale, not a design problem at full scale. Test both.
- Do not put critical content in the outer margins. Crops and UI overlays eat them.

## Decks

- One idea per slide. If a slide needs a paragraph, it is a document, not a slide.
- Slide titles are statements, not labels. "Revenue grew 40% in Q3" beats "Q3 Revenue."
- Body text on a slide is read at projection distance. Apply the distance formula, not screen sizes.
- Build a master grid and hold it. A deck that drifts off grid reads as amateur faster than any other format.
- Data slides: one chart, one takeaway, labeled directly. No legend the eye has to travel to.

## Editorial spreads

- The spread is the unit, not the page. Design across the gutter.
- Set a baseline grid and hold every column to it.
- Entry point per spread: one image or one display element that starts the read.
- Pull quotes are a pacing device. One per spread maximum.

## Checklist

```
[ ] One visual language across the set
[ ] Rhythm varied, not a cloned template
[ ] Eye path across the set: begin, escalate, pause, resolve
[ ] Frame one carries the whole idea alone
[ ] Every frame passes hierarchy caps on its own
[ ] The point lands without the caption
[ ] Current platform dimensions and safe areas confirmed
[ ] Legibility checked at thumbnail, not just full size
[ ] Compression-safe: flat color and vector where possible
[ ] Contrast computed on every frame
[ ] Credit line present
```

---

Designed by IamAlvinV
