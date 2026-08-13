#!/usr/bin/env python3
"""Ship scan. Runs before delivery on any file that carries copy or markup.

  python3 scan.py page.html
  python3 scan.py deck.md copy.txt styles.css
  python3 scan.py ./build --recursive
"""
import argparse
import os
import re
import sys

EXTS = {".html", ".htm", ".md", ".txt", ".css", ".jsx", ".tsx", ".js", ".ts", ".json", ".svg"}

# (label, regex, severity) severity: FAIL blocks delivery, WARN needs a look
CHECKS = [
    ("em dash U+2014", r"\u2014", "FAIL"),
    ("en dash used as a dash", r"\s\u2013\s", "WARN"),
    # alnum on both sides, or spaced. Skips |---| table rules, --custom-props, --cli-flags
    ("paired hyphens used as a dash", r"[A-Za-z0-9]--[A-Za-z0-9]|\s--\s", "FAIL"),
    ("decorative checkmark or arrow", r"[\u2713\u2714\u2705\u2192\u27a1\u21d2\u2794]", "WARN"),
]

FILLER = [
    "leverage", "leveraging", "robust", "seamless", "seamlessly", "unlock", "unlocking",
    "empower", "empowering", "streamline", "streamlined", "comprehensive", "transformative",
    "elevate", "elevating", "foster", "fostering", "cutting-edge", "game-changer",
    "revolutionize", "best-in-class", "synergy", "holistic", "bespoke solution",
    "in today's fast-paced", "delve into", "it's worth noting", "at the end of the day",
]

FOLKLORE = [
    (r"80\s*%.{0,40}brand recognition", "the 80% brand-recognition claim"),
    (r"(62|90)\s*(to|-|\u2013)\s*90\s*%", "the 62 to 90% color judgment claim"),
    (r"85\s*%.{0,30}purchase", "the 85% purchase-decision claim"),
    (r"8[- ]second attention", "the 8-second attention span"),
    (r"goldfish", "the goldfish attention comparison"),
    (r"golden ratio", "golden ratio as a design law, check the framing"),
    (r"fibonacci", "Fibonacci construction, check the framing"),
    (r"rule of thirds", "rule of thirds in UI, no evidence"),
    (r"(design|built|optimi[sz]ed) (for|around) the f[- ]pattern", "designing toward the F-pattern"),
    (r"z[- ]pattern.{0,40}(research|study|proven|validated)", "Z-pattern presented as validated"),
    (r"50\s*millisecond.{0,40}(stay|leave|bounce)", "the 50ms stay-or-leave misstatement"),
    (r"two seconds to make", "the two-second impression claim"),
    (r"white ?space.{0,30}20\s*%", "the 20% whitespace comprehension claim"),
    (r"308\s*%", "the 308% list-attention claim"),
    (r"dopamine.{0,30}(bullet|list)", "bullets and dopamine"),
    (r"40\s*%\s*more conversion", "the bare 40% conversion claim"),
    (r"(202|400)\s*%.{0,30}(convert|conversion)", "recirculated CRO percentages"),
    (r"\$500 (and|vs\.?|versus) (a )?\$5,?000", "the $500 vs $5,000 website line"),
    (r"blue\s*=\s*trust|red\s*=\s*energy", "fixed color-emotion equations"),
    (r"600\s*(to|-|\u2013)\s*700\s*pixels", "the 600 to 700px line-length claim"),
    (r"mullish", "typeface misspelling, it is Mulish"),
    (r"perfectly consistent|shot to shot identical", "vendor consistency language"),
    (r"9[05]\s*%\s*consistent", "untraceable AI consistency percentage"),
    (r"99\s*%\s*of designers", "the invented 99% stat pattern"),
]

CRAFT = [
    (r"letter-spacing\s*:\s*-?\d*\.?\d+px", "tracking set in px, use em so it scales", "FAIL"),
    (r"max-width\s*:\s*\d{3,4}px[^;]*;\s*/\*\s*measure", "measure set in px, use ch or em", "WARN"),
    (r"line-height\s*:\s*1(\.[0-3])?\s*;", "body line-height under 1.4, check it is not body copy", "WARN"),
    (r"height\s*:\s*\d+px[^;]*;[^}]*overflow\s*:\s*hidden", "fixed-height container with clipped overflow", "WARN"),
    (r"<img(?![^>]*\balt\s*=)[^>]*>", "img without alt", "FAIL"),
    (r"text-transform\s*:\s*uppercase", "uppercase, confirm it is not body copy", "WARN"),
    (r"font-size\s*:\s*(0?\.[0-8]\d*rem|[0-9]|1[0-5])px", "font-size under 16px, confirm it is not body", "WARN"),
    (r"outline\s*:\s*(none|0)", "focus outline removed with no replacement visible", "WARN"),
    (r"localStorage|sessionStorage", "browser storage, unsupported in Claude artifacts", "FAIL"),
]

MOTION = re.compile(r"@keyframes|animation\s*:|transition\s*:|framer-motion|gsap", re.I)
REDUCED = re.compile(r"prefers-reduced-motion", re.I)
CREDIT = re.compile(r"Designed by IamAlvinV", re.I)


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def scan_file(path):
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except (IsADirectoryError, PermissionError):
        return [], []
    fails, warns = [], []

    def add(sev, line, label, snippet=""):
        entry = (path, line, label, snippet.strip()[:70])
        (fails if sev == "FAIL" else warns).append(entry)

    for label, pattern, sev in CHECKS:
        for m in re.finditer(pattern, text):
            add(sev, line_of(text, m.start()), label, text[max(0, m.start() - 25):m.start() + 25])

    lowered = text.lower()
    allow_filler = "scan:allow-filler" in lowered
    for word in ([] if allow_filler else FILLER):
        for m in re.finditer(r"\b" + re.escape(word) + r"\b", lowered):
            add("WARN", line_of(text, m.start()), "filler vocabulary: %s" % word)

    # a file that catalogs the folklore is allowed to contain it
    allow_folklore = "scan:allow-folklore" in lowered or os.path.basename(path) == "blocklist.md"
    for pattern, label in ([] if allow_folklore else FOLKLORE):
        for m in re.finditer(pattern, lowered):
            add("FAIL", line_of(text, m.start()), "folklore claim: %s" % label,
                text[max(0, m.start() - 20):m.start() + 40])

    if path.endswith((".html", ".htm", ".css", ".jsx", ".tsx", ".js", ".ts", ".svg")):
        for pattern, label, sev in CRAFT:
            for m in re.finditer(pattern, text, re.I):
                add(sev, line_of(text, m.start()), label, m.group(0))
        if MOTION.search(text) and not REDUCED.search(text):
            add("FAIL", 0, "motion present with no prefers-reduced-motion fallback")

    if path.endswith((".html", ".htm", ".md", ".jsx", ".tsx")) and not CREDIT.search(text):
        add("WARN", 0, "no credit line: Designed by IamAlvinV")

    return fails, warns


def collect(paths, recursive):
    out = []
    for p in paths:
        if os.path.isdir(p):
            if not recursive:
                print("skipping directory %s, pass --recursive" % p)
                continue
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in {"node_modules", ".git", "dist", "__pycache__"}]
                for f in files:
                    if os.path.splitext(f)[1].lower() in EXTS:
                        out.append(os.path.join(root, f))
        else:
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser(description="Ship scan")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--recursive", action="store_true")
    args = ap.parse_args()

    all_fails, all_warns, count = [], [], 0
    for path in collect(args.paths, args.recursive):
        f, w = scan_file(path)
        all_fails += f
        all_warns += w
        count += 1

    def show(title, rows):
        print("\n%s (%d)" % (title, len(rows)))
        print("-" * 70)
        for path, line, label, snippet in rows:
            loc = "%s:%d" % (os.path.basename(path), line) if line else os.path.basename(path)
            print("  %-26s %s" % (loc, label))
            if snippet:
                print("  %-26s   %s" % ("", snippet.replace("\n", " ")))

    print("scanned %d file(s)" % count)
    if all_fails:
        show("FAIL, blocks delivery", all_fails)
    if all_warns:
        show("WARN, look at these", all_warns)
    if not all_fails and not all_warns:
        print("\nclean")

    print()
    return 1 if all_fails else 0


if __name__ == "__main__":
    sys.exit(main())
