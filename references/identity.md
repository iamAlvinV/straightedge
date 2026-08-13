# Logo and identity systems

## Order

1. Pick the logo type for the brand's current recognition level.
2. Build the master in vector, solid black on white, before any color.
3. Black-and-white legibility test at 24px height.
4. Build the variant system. Set minimum sizes in px and mm.
5. Set clear space as a proportional unit.
6. Render at favicon, app icon, and billboard scale. Check the Android 66dp safe circle and the iOS mask.
7. Grayscale test and colorblind simulation.
8. Apply color and type discipline.
9. Confirm alt text on every placement, and WCAG contrast if the logo is a control.
10. Export the file set.

Specs live in `references/gates.md` under Logo and icon. This file is the judgment.

## Logo type selection

| Type | When |
|---|---|
| Wordmark or logotype | Default for a new or unfamiliar name |
| Combination mark | Safe default while the name is still being learned |
| Lettermark or monogram | Needs prior recognition to work standalone |
| Brandmark, abstract mark, emblem | Strong once the brand is known |

New brand with uncertain recognition: lead with a wordmark or combination mark. Earn the icon-only mark later.

## Simplicity

- Aim for clarity and easy processing, not minimalism for its own sake.
- Moderately elaborate marks are often liked and recognized best. Too simple can fail.
- Descriptive marks help unfamiliar brands: faster processing, higher perceived authenticity.
- Deliberate craftsmanship and complexity can signal luxury.
- Working complex marks (Starbucks, Versace, crests) are not exceptions to a law. The absolute simplicity law does not exist.

## Negative space and dual meaning

A high-skill nice-to-have, not a best practice. Only a minority notice hidden elements and they are not processed subconsciously. Never require a hidden meaning. Never trade legibility for one.

## Symmetry

Asymmetry reads more excited and active. Symmetry reads more stable and higher quality. Pick by the brand attribute wanted, not by default.

## Color discipline

- Default to 2 to 3 core colors. Reproduction cost, consistency across substrates, scalability. Exceed only with a stated reason.
- Choose by fit to the brand and category, not by a hue-to-emotion chart.
- The mark must read by shape and luminance. Test grayscale and a CVD simulator.

## Timelessness

Avoiding trends is a strategy, not a testable rule. It coexists with legitimate flexible and dynamic identity systems.

## The system, not the lockup

Build the fixed responsive system before any dynamic behavior. A responsive logo (fixed variants per size and context) is not a living identity (controlled variation inside a system). Know which the brief needs. Most brands need the fixed system and documented guidelines first.

A modular system contains:

- Full lockup
- Simplified lockup
- Horizontal and stacked variants
- Icon or monogram
- Favicon
- One-color version
- Clear space rules
- Minimum sizes, px and mm
- Color tokens for light and dark
- Type scale
- Motion principles

Simplify detail as display size drops. Only the icon-only mark survives at 16px.

## Deliverable set

```
brand/
  logo/
    master.svg              vector, optimized with SVGO
    lockup-horizontal.svg
    lockup-stacked.svg
    icon.svg
    monogram.svg
    onecolor-black.svg
    onecolor-white.svg
  favicon/
    favicon.ico             16, 32, 48
    icon-32.png
    apple-touch-icon.png    180, opaque, corners not pre-rounded
    icon-192.png
    icon-512.png
  tokens/
    color.json              primitives, semantic, component
    type.json
  guidelines.md             clear space, min sizes, misuse, contrast notes
```

---

Designed by IamAlvinV
