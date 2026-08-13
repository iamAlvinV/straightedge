#!/usr/bin/env python3
"""Contrast gate. Computes WCAG 2.2 relative-luminance contrast. Never eyeball it.

  python3 contrast.py --pair "#0F0E0C" "#C6E220"
  python3 contrast.py --palette "#E9E7DE,#0F0E0C,#C6E220,#DE7256"
  python3 contrast.py --cvd "#C6E220,#DE7256"
"""
import argparse
import itertools
import sys


def parse_hex(value):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if len(v) != 6:
        raise ValueError("bad hex: %s" % value)
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def to_hex(rgb):
    return "#%02X%02X%02X" % tuple(max(0, min(255, int(round(c)))) for c in rgb)


def linearize(channel):
    c = channel / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (linearize(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


GATES = [
    ("body text", 4.5),
    ("large text (24px / 18.66px bold)", 3.0),
    ("UI components, icons, focus", 3.0),
    ("AAA body", 7.0),
    ("AAA large", 4.5),
]


def verdict(r):
    return "PASS" if r else "FAIL"


def report_pair(fg_hex, bg_hex):
    fg, bg = parse_hex(fg_hex), parse_hex(bg_hex)
    r = ratio(fg, bg)
    print("\n%s on %s" % (to_hex(fg), to_hex(bg)))
    print("ratio %.2f:1" % r)
    for label, threshold in GATES:
        print("  %-38s %-4s  needs %.1f:1" % (label, verdict(r >= threshold), threshold))
    if 4.5 <= r < 5.0:
        print("  note: passing but thin. 4.5 is the floor, not the target.")
    if r > 20:
        print("  note: near pure black on pure white. Sit inside a band, this strains the eye.")
    return r


def report_palette(colors):
    parsed = [(c, parse_hex(c)) for c in colors]
    print("\n%-10s %-10s %8s  %-5s %-6s %-5s" % ("FG", "BG", "RATIO", "BODY", "LARGE", "UI"))
    print("-" * 52)
    worst = []
    for (ah, a), (bh, b) in itertools.combinations(parsed, 2):
        r = ratio(a, b)
        print("%-10s %-10s %7.2f:1  %-5s %-6s %-5s" % (
            to_hex(a), to_hex(b), r,
            verdict(r >= 4.5), verdict(r >= 3.0), verdict(r >= 3.0)))
        if r < 3.0:
            worst.append((to_hex(a), to_hex(b), r))
    print()
    if worst:
        print("Unusable as a text or UI pairing (%d):" % len(worst))
        for a, b, r in worst:
            print("  %s on %s at %.2f:1" % (a, b, r))
        print("These are decoration-only pairs. Do not put type or a control across them.")
    else:
        print("Every pairing clears 3:1. Check which ones also clear 4.5:1 before setting body copy.")


# Brettel/Vienot style simulation, LMS approximation. Directional check, not a clinical tool.
def simulate_cvd(rgb, kind):
    r, g, b = (linearize(c) for c in rgb)
    l = 17.8824 * r + 43.5161 * g + 4.11935 * b
    m = 3.45565 * r + 27.1554 * g + 3.86714 * b
    s = 0.0299566 * r + 0.184309 * g + 1.46709 * b
    if kind == "protanopia":
        l2, m2, s2 = 0.0 * l + 2.02344 * m + -2.52581 * s, m, s
    elif kind == "deuteranopia":
        l2, m2, s2 = l, 0.494207 * l + 0.0 * m + 1.24827 * s, s
    else:  # tritanopia
        l2, m2, s2 = l, m, -0.395913 * l + 0.801109 * m + 0.0 * s
    r2 = 0.0809444479 * l2 + -0.130504409 * m2 + 0.116721066 * s2
    g2 = -0.0102485335 * l2 + 0.0540193266 * m2 + -0.113614708 * s2
    b2 = -0.000365296938 * l2 + -0.00412161469 * m2 + 0.693511405 * s2

    def delin(c):
        c = max(0.0, min(1.0, c))
        return 255.0 * (12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055)

    return (delin(r2), delin(g2), delin(b2))


def distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def report_cvd(colors):
    parsed = [parse_hex(c) for c in colors]
    kinds = ["deuteranopia", "protanopia", "tritanopia"]
    print("\n%-10s %-14s %-14s %-14s" % ("ORIGINAL", "DEUTERANOPIA", "PROTANOPIA", "TRITANOPIA"))
    print("-" * 56)
    sims = {}
    for c in parsed:
        row = [to_hex(simulate_cvd(c, k)) for k in kinds]
        sims[to_hex(c)] = row
        print("%-10s %-14s %-14s %-14s" % (to_hex(c), row[0], row[1], row[2]))
    print()
    collisions = 0
    for (ah, a), (bh, b) in itertools.combinations(list(sims.items()), 2):
        for i, k in enumerate(kinds):
            d = distance(parse_hex(a[i]), parse_hex(b[i]))
            if d < 40:
                print("COLLISION under %s: %s and %s converge (distance %.0f)" % (k, ah, bh, d))
                collisions += 1
    if collisions:
        print("\nThese pairs stop being distinguishable. If either one carries meaning,")
        print("add a second signal: text, shape, icon, or position. Color alone fails here.")
    else:
        print("No collisions under simulation. Color is still not allowed to be the only signal.")


def main():
    p = argparse.ArgumentParser(description="WCAG contrast and CVD gate")
    p.add_argument("--pair", nargs=2, metavar=("FG", "BG"))
    p.add_argument("--palette", help="comma separated hex values")
    p.add_argument("--cvd", help="comma separated hex values")
    args = p.parse_args()

    if not any([args.pair, args.palette, args.cvd]):
        p.print_help()
        return 1

    if args.pair:
        report_pair(*args.pair)
    if args.palette:
        report_palette([c for c in args.palette.split(",") if c.strip()])
    if args.cvd:
        report_cvd([c for c in args.cvd.split(",") if c.strip()])
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
