# Component scope

Most requests are one element, not a page. Running the full page apparatus on a button is wrong and expensive.

## Route here when

- The brief names one element: button, input, card, modal, dropdown, tooltip, select, checkbox, switch, tab strip, chip, badge, banner, toast, popover, slider, date picker, avatar.
- The brief is short and refers to one thing.
- The target is a single file.
- The user says just the X, only the Y, this one element, a single.

Two signals fire, route component. If the brief is genuinely ambiguous, ask one short question and default to component when the answer does not come. A single artifact is cheaper to redirect than a full page.

## What still applies

- Survey. Read the existing tokens, fonts, and spacing scale. A button in a project with an established system adopts that system. It does not invent one.
- Every contrast, target size, and focus gate in `gates.md`.
- Token discipline. The component references named tokens, never inline hex.
- The eight states, in full, from `parts.md`. Mandatory here, not advisory.
- The reduction pass.

## What is skipped

- Shape pick. Components have no shape. Say so: "Component scope, skipping shape."
- Nav and footer parts.
- Hero and enrichment decisions.
- The rotation log. Components do not rotate.

## What ships

Two files.

1. **The component**, matching the project's conventions. React, Vue, Svelte, or plain CSS and HTML. It consumes tokens by name.
2. **A state preview**, a standalone file rendering all eight states stacked and labeled. The user opens it once, confirms, deletes it. It is not production code.

The preview forces each state by class in addition to the real pseudo-class, so all eight render at once:

```css
.btn:hover,         .btn.is-hover  { background: var(--surface-2); }
.btn:focus-visible, .btn.is-focus  { outline: 2px solid var(--focus); outline-offset: 2px; }
.btn:active,        .btn.is-active { transform: translateY(1px); }
```

## Stamp

```
/* Straightedge · component: button · states: default hover focus active disabled loading error success
 * contrast: pass · targets: 48px
 */
```

The `component:` prefix tells the next run this artifact is component scoped and does not enter rotation.

---

Designed by IamAlvinV
