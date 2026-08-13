#!/usr/bin/env python3
"""Rotation and project memory. Stops the same shape and the same dressing shipping twice.

  python3 rotate.py check --shape Bento --base "#0F0E0C" --accent "#C6E220" --display "condensed heavy"
  python3 rotate.py log   --shape Bento --base "#0F0E0C" --accent "#C6E220" --display "condensed heavy" \
                          --nav nav:pill --foot foot:mark --brief "client tool page"
  python3 rotate.py history
  python3 rotate.py suggest

Log lives at .straightedge/log.json in the current project. Last 20 entries.
"""
import argparse
import colorsys
import json
import os
import sys
from datetime import date

LOG_DIR = ".straightedge"
LOG_PATH = os.path.join(LOG_DIR, "log.json")
KEEP = 20

SCREEN = ["Stack", "Ledger", "Statement", "Bento", "Broadsheet", "Console", "Index",
          "Split", "Counter", "Letter", "Timeline", "Gallery", "Readout", "Placard"]
PRINT = ["Type slab", "Frame", "Bleed", "Register", "Stack cut", "Diagonal", "Center", "Margin note"]
SHAPES = SCREEN + PRINT

DISPLAY_VOICES = ["condensed heavy", "geometric sans", "grotesque", "serif", "mono",
                  "script", "display slab"]


def parse_hex(value):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    return tuple(int(v[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def band(hex_value):
    r, g, b = parse_hex(hex_value)
    lightness = colorsys.rgb_to_hls(r, g, b)[1] * 100
    if lightness < 30:
        return "dark"
    if lightness <= 85:
        return "mid"
    return "light"


def temperature(hex_value):
    r, g, b = parse_hex(hex_value)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if s < 0.10:
        return "none"
    deg = h * 360
    if 10 <= deg <= 60:
        return "warm"
    if 200 <= deg <= 300:
        return "cool"
    return "chromatic other"


def axes(base, accent, display):
    return {"band": band(base), "voice": display.strip().lower(), "temp": temperature(accent)}


def load():
    if not os.path.exists(LOG_PATH):
        return []
    try:
        return json.load(open(LOG_PATH))
    except (ValueError, OSError):
        return []


def save(entries):
    os.makedirs(LOG_DIR, exist_ok=True)
    json.dump(entries[:KEEP], open(LOG_PATH, "w"), indent=2)


def cmd_check(a):
    entries = load()
    if not entries:
        print("First run in this project. No constraint. Log it after delivery.")
        return 0

    new = axes(a.base, a.accent, a.display)
    last3 = entries[:3]
    prev = entries[0]
    fails = []

    if a.shape in [e.get("shape") for e in last3]:
        fails.append("shape %s used in the last three runs" % a.shape)

    old = prev.get("axes", {})
    matched = [k for k in ("band", "voice", "temp") if old.get(k) == new[k]]
    if len(matched) >= 2:
        fails.append("matches the previous piece on %s. Two of three is a repeat." % " and ".join(matched))

    if a.nav and a.nav == prev.get("nav"):
        fails.append("nav %s repeats the previous run" % a.nav)
    if a.foot and a.foot == prev.get("foot"):
        fails.append("footer %s repeats the previous run" % a.foot)

    print("\ncandidate: %s | band %s | voice %s | accent %s"
          % (a.shape, new["band"], new["voice"], new["temp"]))
    print("previous:  %s | band %s | voice %s | accent %s"
          % (prev.get("shape"), old.get("band"), old.get("voice"), old.get("temp")))

    if fails:
        print("\nREFUSED")
        for f in fails:
            print("  " + f)
        used = [e.get("shape") for e in last3]
        pool = [s for s in (PRINT if a.shape in PRINT else SCREEN) if s not in used]
        print("\nopen shapes: %s" % ", ".join(pool[:8]))
        return 1

    print("\nCLEAR. Differs on: %s"
          % ", ".join(k for k in ("band", "voice", "temp") if old.get(k) != new[k]))
    return 0


def cmd_log(a):
    entries = load()
    entries.insert(0, {
        "date": str(date.today()),
        "shape": a.shape,
        "base": a.base,
        "accent": a.accent,
        "display": a.display,
        "axes": axes(a.base, a.accent, a.display),
        "nav": a.nav,
        "foot": a.foot,
        "brief": a.brief,
    })
    save(entries)
    print("logged. %d entries in %s" % (min(len(entries), KEEP), LOG_PATH))
    print("\nstamp for the artifact:")
    print("/* Straightedge · shape: %s · base: %s · accent: %s · display: %s */"
          % (a.shape, a.base, a.accent, a.display))
    return 0


def cmd_history(a):
    entries = load()
    if not entries:
        print("no history in this project")
        return 0
    print("\n%-12s %-12s %-6s %-18s %-8s %-10s %s"
          % ("DATE", "SHAPE", "BAND", "VOICE", "ACCENT", "NAV", "BRIEF"))
    print("-" * 96)
    for e in entries:
        ax = e.get("axes", {})
        print("%-12s %-12s %-6s %-18s %-8s %-10s %s" % (
            e.get("date", ""), e.get("shape", "")[:12], ax.get("band", ""),
            ax.get("voice", "")[:18], ax.get("temp", "")[:8], e.get("nav") or "", e.get("brief", "")[:28]))
    counts = {}
    for e in entries[:5]:
        counts[e.get("shape")] = counts.get(e.get("shape"), 0) + 1
    over = [s for s, n in counts.items() if n >= 2]
    if over:
        print("\noverused in the last five: %s" % ", ".join(over))
    return 0


def cmd_suggest(a):
    entries = load()
    used = [e.get("shape") for e in entries[:3]]
    pool = [s for s in SHAPES if s not in used]
    print("\nused recently: %s" % (", ".join(used) if used else "nothing"))
    print("\nscreen: %s" % ", ".join(s for s in pool if s in SCREEN))
    print("print:  %s" % ", ".join(s for s in pool if s in PRINT))
    if entries:
        old = entries[0].get("axes", {})
        print("\nprevious dressing was band %s, voice %s, accent %s."
              % (old.get("band"), old.get("voice"), old.get("temp")))
        print("Move at least two of those.")
    return 0


def main():
    p = argparse.ArgumentParser(description="Rotation and project memory")
    sub = p.add_subparsers(dest="cmd")

    def common(sp, required):
        sp.add_argument("--shape", required=required)
        sp.add_argument("--base", required=required, help="base surface hex")
        sp.add_argument("--accent", required=required, help="accent hex")
        sp.add_argument("--display", required=required, help="display voice, see shapes.md")
        sp.add_argument("--nav", default=None, help="nav slug, see parts.md")
        sp.add_argument("--foot", default=None, help="footer slug, see parts.md")

    c = sub.add_parser("check")
    common(c, True)
    lg = sub.add_parser("log")
    common(lg, True)
    lg.add_argument("--brief", default="")
    sub.add_parser("history")
    sub.add_parser("suggest")

    a = p.parse_args()
    if a.cmd == "check":
        return cmd_check(a)
    if a.cmd == "log":
        return cmd_log(a)
    if a.cmd == "history":
        return cmd_history(a)
    if a.cmd == "suggest":
        return cmd_suggest(a)
    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
