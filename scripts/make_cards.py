#!/usr/bin/env python3
"""Build an 800x420 profile card from a repo's own figure.

Usage:
  python3 scripts/make_cards.py --name gene-structure-annotation \
      --subtitle "Gene models and GFF3 from a genome" \
      --figure path/to/structure_overview.png --accent "#2e8b57" --out-prefix assets/card-x
Writes <out-prefix>-light.png and <out-prefix>-dark.png. Refuses to overwrite.
Needs Pillow and the Inter variable font (path set by --font).
"""
import argparse
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 800, 420
THEMES = {
    "light": {"bg": (255, 255, 255), "title": None, "text": (31, 35, 40), "border": (208, 215, 222)},
    "dark": {"bg": (13, 17, 23), "title": (240, 246, 252), "text": (230, 237, 243), "border": (48, 54, 61)},
}


def font(path, size, weight):
    f = ImageFont.truetype(path, size)
    try:
        f.set_variation_by_axes([14 if size < 30 else 32, weight])
    except Exception:
        pass
    return f


def card(theme, name, subtitle, fig_path, accent, font_path):
    t = THEMES[theme]
    im = Image.new("RGB", (W, H), t["bg"])
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=14, outline=t["border"], width=2, fill=t["bg"])
    d.rectangle([0, 0, 9, H], fill=accent)
    d.text((40, 28), name, font=font(font_path, 36, 700), fill=t["title"] or accent)
    d.text((40, 84), subtitle, font=font(font_path, 22, 400), fill=t["text"])
    # inset panel with the repo's own figure, scaled to fit
    px0, py0, px1, py1 = 40, 134, W - 40, H - 28
    d.rounded_rectangle([px0, py0, px1, py1], radius=10, fill=(255, 255, 255), outline=t["border"], width=1)
    fig = Image.open(fig_path).convert("RGB")
    bw, bh = px1 - px0 - 20, py1 - py0 - 16
    s = min(bw / fig.width, bh / fig.height)
    fig = fig.resize((max(1, int(fig.width * s)), max(1, int(fig.height * s))), Image.LANCZOS)
    im.paste(fig, (px0 + (px1 - px0 - fig.width) // 2, py0 + (py1 - py0 - fig.height) // 2))
    return im


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    p.add_argument("--subtitle", required=True)
    p.add_argument("--figure", required=True)
    p.add_argument("--accent", required=True)
    p.add_argument("--out-prefix", required=True)
    p.add_argument("--font", default="/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf")
    a = p.parse_args()
    accent = tuple(int(a.accent.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    for theme in ("light", "dark"):
        out = f"{a.out_prefix}-{theme}.png"
        if os.path.exists(out):
            raise SystemExit(f"{out} exists; not overwriting")
        im = card(theme, a.name, a.subtitle, a.figure, accent, a.font)
        with open(out, "xb") as f:
            im.save(f, format="PNG", optimize=True)
        print(out)


if __name__ == "__main__":
    main()
