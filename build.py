#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SheVan website build script.

Usage:
    python build.py                # build to dist/
    python build.py --inline       # build + inline assets (self-contained pages)
    python build.py --out custom/  # build to custom directory

The output is a static site — no server, no database. Drop dist/ into
any web hosting (Netlify, Vercel, IONOS, GitHub Pages, etc).
"""
import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT))

from src.builder import build_all
from src.inliner import inline_assets


def main():
    parser = argparse.ArgumentParser(description="Build the SheVan static website.")
    parser.add_argument(
        "--out", type=Path, default=REPO_ROOT / "dist",
        help="Output directory (default: dist/)",
    )
    parser.add_argument(
        "--assets", type=Path, default=REPO_ROOT / "assets",
        help="Source assets directory (default: assets/)",
    )
    parser.add_argument(
        "--inline", action="store_true",
        help="Inline CSS and base64-encode logos into every HTML "
             "(makes each page self-contained for local preview).",
    )
    args = parser.parse_args()

    print(f"→ Building to {args.out}/")
    pages = build_all(out_dir=args.out, assets_dir=args.assets)
    html_count = sum(1 for p in pages if p.endswith(".html"))
    print(f"  ✓ {html_count} HTML pages + CSS + logos written")

    if args.inline:
        print(f"→ Inlining CSS + logos into every page…")
        patched = inline_assets(args.out)
        print(f"  ✓ {len(patched)} pages now self-contained")

    print(f"\n✓ Done. Open {args.out}/index.html in a browser to preview.")


if __name__ == "__main__":
    main()
