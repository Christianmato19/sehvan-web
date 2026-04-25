# -*- coding: utf-8 -*-
"""
Post-build asset inliner.

Embeds the shared CSS file and PNG logos as inline `<style>` blocks and
base64 data URIs into every generated HTML file. This makes each page
self-contained — useful for local previews, email-attached demos, and
file:// browsing where sibling assets fail to load.

In production hosting this step is OPTIONAL; standard `<link>` and
`<img src>` references are more cache-friendly.
"""
import base64
import re
from pathlib import Path
from typing import List


def inline_assets(out_dir: Path) -> List[Path]:
    """
    Patch every .html file in out_dir to inline CSS + logos.

    Args:
        out_dir: directory containing styles.css, logo-*.png and HTML files.

    Returns:
        List of patched HTML file paths.
    """
    css_path = out_dir / "styles.css"
    yellow_path = out_dir / "logo-yellow.png"
    black_path = out_dir / "logo-black.png"

    if not css_path.exists():
        raise FileNotFoundError(f"Missing {css_path} — run builder first.")

    css_content = css_path.read_text(encoding="utf-8")
    yellow_uri = "data:image/png;base64," + base64.b64encode(yellow_path.read_bytes()).decode("ascii")
    black_uri = "data:image/png;base64," + base64.b64encode(black_path.read_bytes()).decode("ascii")

    html_files = sorted(out_dir.rglob("*.html"))
    patched = []

    for fp in html_files:
        html = fp.read_text(encoding="utf-8")

        # <link rel=stylesheet href=...styles.css> → inline <style>
        html = re.sub(
            r'<link rel="stylesheet" href="[^"]*styles\.css">',
            f'<style>\n{css_content}\n</style>',
            html,
        )

        # favicon → data URI
        html = re.sub(
            r'<link rel="icon" type="image/png" href="[^"]*logo-yellow\.png">',
            f'<link rel="icon" type="image/png" href="{yellow_uri}">',
            html,
        )

        # logo <img> elements → data URIs
        html = re.sub(r'src="(?:\.\./)*logo-yellow\.png"', f'src="{yellow_uri}"', html)
        html = re.sub(r'src="(?:\.\./)*logo-black\.png"', f'src="{black_uri}"', html)

        fp.write_text(html, encoding="utf-8")
        patched.append(fp)

    return patched
