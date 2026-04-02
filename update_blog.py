import re, glob

# ── 1. REPLACE ALL DATES IN ALL BLOG FILES ───────────────────────────────────
old_dates = [
    '15 maart 2025', '2 april 2025', '18 april 2025', '5 mei 2025',
    '20 mei 2025', '10 juni 2025', '28 juni 2025', '15 juli 2025',
    '1 augustus 2025', '18 augustus 2025',
]
new_date = '2 april 2026'

blog_files = ['blog.html'] + glob.glob('blog-*.html')
for f in blog_files:
    content = open(f, encoding='utf-8').read()
    orig = content
    for d in old_dates:
        content = content.replace(d, new_date)
    if content != orig:
        open(f, 'w', encoding='utf-8').write(content)
        print(f'Dates updated: {f}')

# ── 2. UPDATE CARD IMAGES IN blog.html ───────────────────────────────────────
# Photo assignments per card (cards that previously had SVG placeholders)
# card_id → (photo_path, alt_text)
CARD_PHOTOS = {
    'blog-dakschade-storm.html':      ('tnoordenfoto/2025-10-07 (3).webp',  'Dakschade na storm'),
    'blog-levensduur-dak.html':       ('tnoordenfoto/2025-05-20 (1).webp',  'Dakpannen van dichtbij'),
    'blog-plat-dak-problemen.html':   ('tnoordenfoto/2026-02-09.webp',      'Plat dak inspectie'),
    'blog-daklekkage-oorzaken.html':  ('tnoordenfoto/dakgoot.webp',         'Dakgoot en afvoer'),
    'blog-bitumen-epdm-verschil.html':('tnoordenfoto/unnamed.webp',         'Bitumen dakbedekking'),
    'blog-stormschade-verzekering.html':('tnoordenfoto/2025-10-07 (5).webp','Stormschade aan dak'),
}

content = open('blog.html', encoding='utf-8').read()
orig = content

for href, (photo, alt) in CARD_PHOTOS.items():
    # Find the blog-card-img block for this card and replace the SVG placeholder with an img
    # The SVG placeholder looks like:
    # <svg width="64" height="64" ... style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)">...</svg>
    # We need to insert an <img> before the <span class="blog-card-cat">
    # Pattern: find the card-img div for this specific href card
    # Each card starts with: <a class="blog-card reveal" href="blog-xxx.html">
    # Then <div class="blog-card-img" style="background: ...">
    # Then the SVG
    # Then <span class="blog-card-cat">

    # Replace the SVG placeholder img for this specific card
    # Match the card-img div that contains an SVG placeholder (no <img> tag)
    # inside the card with this href

    # Strategy: find the block containing href="blog-xxx.html" and within it
    # replace the SVG placeholder with an actual img tag

    # Build pattern to find SVG inside the card-img of the right card
    card_start = f'href="{href}"'
    idx = content.find(card_start)
    if idx == -1:
        print(f'  Card not found: {href}')
        continue

    # Find the blog-card-img div after card_start
    img_div_start = content.find('<div class="blog-card-img"', idx)
    if img_div_start == -1:
        print(f'  blog-card-img not found for: {href}')
        continue

    # Find the end of this blog-card-img div (find the next </div>)
    img_div_end = content.find('</div>', img_div_start) + len('</div>')

    img_block = content[img_div_start:img_div_end]

    # If already has an <img> tag, skip
    if '<img ' in img_block:
        print(f'  Already has img: {href}')
        continue

    # Find the SVG element within this block and replace it with an img
    # The SVG starts with <svg and ends with </svg>
    svg_start = img_block.find('<svg ')
    svg_end = img_block.find('</svg>') + len('</svg>')
    if svg_start == -1:
        print(f'  No SVG found: {href}')
        continue

    img_tag = f'<img src="{photo}" alt="{alt}" loading="lazy" />'
    new_img_block = img_block[:svg_start] + img_tag + img_block[svg_end:]

    content = content[:img_div_start] + new_img_block + content[img_div_end:]
    print(f'  Photo added to card: {href}')

if content != orig:
    open('blog.html', 'w', encoding='utf-8').write(content)
    print('blog.html card images updated.')

print('\nDone.')
