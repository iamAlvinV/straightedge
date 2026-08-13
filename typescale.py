#!/usr/bin/env python3
"""Type scale generator. One base, one ratio, locked steps.

  python3 typescale.py --base 16 --ratio 1.333 --steps 7
  python3 typescale.py --base 16 --ratio display --steps 6 --unit rem
"""
import argparse
import sys

RATIOS = {
    "minor-second": 1.067, "major-second": 1.125, "minor-third": 1.2,
    "major-third": 1.25, "perfect-fourth": 1.333, "augmented-fourth": 1.414,
    "perfect-fifth": 1.5, "golden": 1.618,
    "ui": 1.25, "web": 1.333, "display": 1.5,
}

ROLES = ["body", "subhead", "title", "headline", "display", "display-lg", "display-xl", "display-2xl"]


def main():
    p = argparse.ArgumentParser(description="Type scale generator")
    p.add_argument("--base", type=float, default=16.0)
    p.add_argument("--ratio", default="1.333")
    p.add_argument("--steps", type=int, default=6)
    p.add_argument("--down", type=int, default=2, help="steps below base for labels and captions")
    p.add_argument("--unit", choices=["px", "rem"], default="px")
    args = p.parse_args()

    key = args.ratio.strip().lower()
    ratio = RATIOS.get(key)
    if ratio is None:
        try:
            ratio = float(args.ratio)
        except ValueError:
            print("Unknown ratio. Named options: %s" % ", ".join(sorted(RATIOS)))
            return 1

    if args.base < 16:
        print("GATE: body floor is 16px on screen. %.0fpx fails." % args.base)
    if ratio >= 1.5:
        print("Note: %.3f is display-led. Do not run body copy on it. 1.2 to 1.333 for body-inclusive work." % ratio)

    sizes = []
    for i in range(-args.down, args.steps):
        px = args.base * (ratio ** i)
        sizes.append((i, round(px, 1)))

    print("\nbase %.0fpx, ratio %.3f\n" % (args.base, ratio))
    print("%-14s %-9s %-9s %-11s %s" % ("ROLE", "PX", "REM", "LINE-HEIGHT", "TRACKING"))
    print("-" * 62)
    for idx, (i, px) in enumerate(sizes):
        role = "label-%d" % abs(i) if i < 0 else (ROLES[i] if i < len(ROLES) else "display-%d" % i)
        if px >= 60:
            lh, tr = 1.05, "-0.03em"
        elif px >= 32:
            lh, tr = 1.1, "-0.02em"
        elif px >= 20:
            lh, tr = 1.2, "0"
        elif px >= 16:
            lh, tr = 1.55, "0"
        else:
            lh, tr = 1.5, "+0.02em"
        lh_px = int(round(px * lh / 4.0)) * 4  # snap leading to the 4pt grid
        if px < 24 and lh_px / px < 1.45:      # hold the body leading gate
            lh_px += 4
        print("%-14s %-9s %-9s %-11s %s" % (
            role, "%.1fpx" % px, "%.3frem" % (px / 16.0), "%dpx (%.2f)" % (lh_px, lh_px / px), tr))

    print("\n:root {")
    for i, px in sizes:
        role = "label-%d" % abs(i) if i < 0 else (ROLES[i] if i < len(ROLES) else "display-%d" % i)
        val = "%.3frem" % (px / 16.0) if args.unit == "rem" else "%.1fpx" % px
        print("  --text-%s: %s;" % (role, val))
    print("}")
    print("\nShow 2 to 3 of these in one view. Not all of them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
