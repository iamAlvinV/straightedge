#!/usr/bin/env python3
"""Render an HTML file to PNG and produce the blurred squint-test frame.

  python3 render.py page.html --width 1440 --out render.png
  python3 render.py page.html --thumb --out thumb.png    # viewport crop for a gallery
  python3 render.py page.html --reflow                   # also the 320px gate check

Full-page capture is the default and it is the right frame for reviewing a whole
page. It is the wrong frame for a gallery: a long page becomes a tall strip that
renders as an unreadable sliver in a grid. Use --thumb for anything a viewer
scans at small size. It captures the first screen at 1440 by 900, the 16:10 crop
a reader actually meets first, and downscales to 1200 wide.
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
        page.wait_for_timeout(1200)   # webfonts from a CDN need the extra beat
        overflow = page.evaluate(
            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
        page.screenshot(path=out, full_page=full_page)
        browser.close()
    return overflow


def downscale(path, target_width=1200):
    from PIL import Image
    img = Image.open(path).convert("RGB")
    if img.width <= target_width:
        return
    h = round(img.height * target_width / img.width)
    img.resize((target_width, h), Image.LANCZOS).save(path, optimize=True)


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
    p.add_argument("--thumb", action="store_true",
                   help="first-screen crop at 1440x900, downscaled to 1200 wide, for a gallery")
    p.add_argument("--no-squint", action="store_true")
    p.add_argument("--reflow", action="store_true", help="also render the 320px reflow gate")
    args = p.parse_args()

    if args.thumb:
        args.width, args.height = 1440, 900
    full = (not args.no_full_page) and (not args.thumb)
    overflow = render(args.path, args.width, args.height, args.out, full)
    if args.thumb:
        downscale(args.out)
        print("thumb %s, first screen, 1200px wide" % args.out)
    else:
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
