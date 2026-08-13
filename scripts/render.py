#!/usr/bin/env python3
"""Render an HTML file to PNG and produce the blurred squint-test frame.

  python3 render.py page.html --width 1440 --out render.png
  python3 render.py page.html --width 390 --out mobile.png
  python3 render.py page.html --reflow           # also renders the 320px gate check
"""
import argparse
import os
import sys


def render(path, width, height, out, full_page):
    from playwright.sync_api import sync_playwright
    url = "file://" + os.path.abspath(path) if not path.startswith("http") else path
    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=["--no-sandbox", "--font-render-hinting=none"])
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=2)
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(700)
        overflow = page.evaluate(
            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
        page.screenshot(path=out, full_page=full_page)
        browser.close()
    return overflow


def squint(src, dst, radius=14):
    from PIL import Image, ImageFilter
    img = Image.open(src).convert("RGB")
    img.filter(ImageFilter.GaussianBlur(radius)).save(dst)


def main():
    p = argparse.ArgumentParser(description="Render and squint-test")
    p.add_argument("path")
    p.add_argument("--width", type=int, default=1440)
    p.add_argument("--height", type=int, default=900)
    p.add_argument("--out", default="render.png")
    p.add_argument("--no-full-page", action="store_true")
    p.add_argument("--no-squint", action="store_true")
    p.add_argument("--reflow", action="store_true", help="also render the 320px reflow gate")
    args = p.parse_args()

    overflow = render(args.path, args.width, args.height, args.out, not args.no_full_page)
    print("rendered %s at %dpx" % (args.out, args.width))
    if overflow:
        print("GATE FAIL: horizontal scroll at %dpx." % args.width)

    if not args.no_squint:
        base, ext = os.path.splitext(args.out)
        blur = base + "-squint" + ext
        squint(args.out, blur)
        print("squint frame %s" % blur)
        print("Open it. The intended focal point must still dominate. If it flattens, fix")
        print("size, weight, spacing, or contrast before touching anything else.")

    if args.reflow:
        base, ext = os.path.splitext(args.out)
        rf = base + "-320" + ext
        of = render(args.path, 320, 800, rf, True)
        print("\nreflow frame %s" % rf)
        print("320px reflow gate: %s" % ("FAIL, horizontal scroll present" if of else "PASS"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
