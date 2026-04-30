import glob, re
from PIL import Image

# ── FAVICON MAKEN VAN LOGO.PNG ───────────────────────────────────────────
img = Image.open('logo.png').convert('RGBA')

# Maak vierkant met transparante padding
w, h = img.size
size = max(w, h)
square = Image.new('RGBA', (size, size), (0, 0, 0, 0))
square.paste(img, ((size - w) // 2, (size - h) // 2))

# favicon.ico (16, 32, 48)
ico_sizes = [(16,16),(32,32),(48,48)]
icons = [square.resize(s, Image.LANCZOS) for s in ico_sizes]
icons[0].save('favicon.ico', format='ICO', sizes=ico_sizes, append_images=icons[1:])

# PNG varianten
square.resize((32,32), Image.LANCZOS).save('favicon-32x32.png')
square.resize((16,16), Image.LANCZOS).save('favicon-16x16.png')
square.resize((180,180), Image.LANCZOS).save('apple-touch-icon.png')
square.resize((192,192), Image.LANCZOS).save('icon-192.png')

print('Favicon bestanden aangemaakt.')

# ── SEO TAGS PER PAGINA ───────────────────────────────────────────────────
FAVICON_TAGS = '''  <link rel="icon" href="favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png" />'''

SCHEMA_HOMEPAGE = '''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "RoofingContractor",
    "name": "Dakbedrijf \\'T Noorden",
    "description": "Specialist in dakrenovatie, dakreparatie en dakonderhoud in Noord-Nederland.",
    "telephone": "+31612370853",
    "email": "info@dakbedrijftnoorden.nl",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Leonard Springerlaan 35",
      "addressLocality": "Groningen",
      "postalCode": "9727 KB",
      "addressCountry": "NL"
    },
    "areaServed": ["Groningen", "Friesland", "Drenthe", "Zwolle", "Utrecht"],
    "openingHours": ["Mo-Fr 07:30-17:30", "Sa 08:00-13:00"],
    "priceRange": "\\u20ac\\u20ac"
  }
  </script>'''

# Info per pagina: (title, description, keywords)
PAGE_INFO = {
    'index.html': (
        "Dakbedrijf 'T Noorden | Dakspecialist Noord-Nederland",
        "Dakbedrijf 'T Noorden: specialist in dakrenovatie, dakreparatie, bitumen daken en dakonderhoud in Groningen, Friesland, Drenthe, Zwolle en Utrecht.",
        "dakbedrijf, dakrenovatie, dakreparatie, bitumen dak, daklekkage, dakinspectie, noord-nederland, groningen, friesland, drenthe"
    ),
    'dakrenovatie.html': (
        "Dakrenovatie Noord-Nederland | Dakbedrijf 'T Noorden",
        "Professionele dakrenovatie in Noord-Nederland. Van inspectie tot volledige vernieuwing. Gratis offerte aanvragen.",
        "dakrenovatie, nieuw dak, dakvernieuwing, dakpannen, noord-nederland"
    ),
    'bitumen-daken.html': (
        "Bitumen Daken Noord-Nederland | Dakbedrijf 'T Noorden",
        "Specialist in bitumen dakbedekking voor platte daken in Noord-Nederland. Installatie, renovatie en onderhoud. Gratis offerte.",
        "bitumen dak, plat dak, bitumen dakbedekking, SBS bitumen, noord-nederland"
    ),
    'nokvorsten.html': (
        "Nokvorsten Reparatie & Vervanging | Dakbedrijf 'T Noorden",
        "Losse of gebroken nokvorsten in Noord-Nederland? Wij repareren en vervangen vakkundig. Gratis inspectie aanvragen.",
        "nokvorsten, nok reparatie, nokvorst vervangen, pannendak, noord-nederland"
    ),
    'schoorsteen-onderhoud.html': (
        "Schoorsteen Onderhoud Noord-Nederland | Dakbedrijf 'T Noorden",
        "Professioneel schoorsteenonderhoud in Noord-Nederland. Voegwerk, loodwerk en inspectie. Gratis offerte aanvragen.",
        "schoorsteen onderhoud, schoorsteen reparatie, schoorsteenvoegen, loodwerk, noord-nederland"
    ),
    'loodreparaties.html': (
        "Loodreparaties Noord-Nederland | Dakbedrijf 'T Noorden",
        "Vakkundige loodreparaties in Noord-Nederland. Loslatend of beschadigd lood hersteld. Gratis inspectie aanvragen.",
        "loodreparaties, loodwerk dak, loodaansluiting, schoorsteen lood, noord-nederland"
    ),
    'dakgootreiniging.html': (
        "Dakgootreiniging Noord-Nederland | Dakbedrijf 'T Noorden",
        "Grondige dakgootreiniging in Noord-Nederland. Verstoppingen voorkomen en waterafvoer garanderen. Afspraak aanvragen.",
        "dakgootreiniging, dakgoot reinigen, goot schoonmaken, dakgoot verstopt, noord-nederland"
    ),
    'spoed.html': (
        "Spoed Dakservice 24/7 Noord-Nederland | Dakbedrijf 'T Noorden",
        "Acute dakschade? Onze 24/7 spoedservice staat dag en nacht klaar in Noord-Nederland. Bel 06 12 37 08 53.",
        "spoed dakservice, noodreparatie dak, stormschade dak, daklekkage spoed, noord-nederland"
    ),
    'dakinspectie.html': (
        "Gratis Dakinspectie Noord-Nederland | Dakbedrijf 'T Noorden",
        "Professionele dakinspectie in Noord-Nederland. Volledig dakonderzoek met rapport. Gratis en vrijblijvend aanvragen.",
        "dakinspectie, dakkeuring, dak laten inspecteren, dakrapport, noord-nederland"
    ),
    'daklekkage.html': (
        "Daklekkage Oplossen Noord-Nederland | Dakbedrijf 'T Noorden",
        "Lekkend dak in Noord-Nederland? Wij lokaliseren de oorzaak snel en repareren direct en duurzaam. Gratis inspectie.",
        "daklekkage, lekkend dak, daklek repareren, lekkage dak oplossen, noord-nederland"
    ),
    'dak-isolatie.html': (
        "Dakisolatie Noord-Nederland | Dakbedrijf 'T Noorden",
        "Professionele dakisolatie in Noord-Nederland. Lagere energiekosten, meer comfort. Gratis advies aanvragen.",
        "dakisolatie, dak isoleren, plat dak isolatie, schuindak isolatie, energie besparen, noord-nederland"
    ),
    'vogelwering.html': (
        "Vogelwering Noord-Nederland | Dakbedrijf 'T Noorden",
        "Effectieve vogelwering voor uw dak in Noord-Nederland. Duiven, meeuwen en spreeuwen weren. Gratis inspectie.",
        "vogelwering, duiven weren, vogels dak, anti-vogel systeem, noord-nederland"
    ),
    'dak-reparatie.html': (
        "Dakreparatie Noord-Nederland | Dakbedrijf 'T Noorden",
        "Snelle en vakkundige dakreparatie in Noord-Nederland. Stormschade, lekkage of kapotte pannen? Wij lossen het op.",
        "dakreparatie, dak repareren, stormschade dak, kapotte dakpannen, noord-nederland"
    ),
}

files = glob.glob('*.html')
count = 0
for f in files:
    if f in ('algemene-voorwaarden.html', 'privacybeleid.html'):
        # Just add favicon to these
        content = open(f, encoding='utf-8').read()
        if 'favicon.ico' not in content:
            content = content.replace('</head>', FAVICON_TAGS + '\n</head>', 1)
            open(f, 'w', encoding='utf-8').write(content)
            count += 1
        continue

    content = open(f, encoding='utf-8').read()
    orig = content

    info = PAGE_INFO.get(f)
    if not info:
        continue
    title, desc, keywords = info

    # Update <title>
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)

    # Build SEO block
    seo = f'''  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{keywords}" />
  <meta name="robots" content="index, follow" />
  <meta name="author" content="Dakbedrijf \\'T Noorden" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="logo.png" />
  <meta property="og:locale" content="nl_NL" />
  <meta property="og:site_name" content="Dakbedrijf \\'T Noorden" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
{FAVICON_TAGS}'''

    # Remove any existing SEO tags then insert fresh block after viewport meta
    content = re.sub(r'\s*<meta name="description"[^>]*/>', '', content)
    content = re.sub(r'\s*<meta name="keywords"[^>]*/>', '', content)
    content = re.sub(r'\s*<meta name="robots"[^>]*/>', '', content)
    content = re.sub(r'\s*<meta name="author"[^>]*/>', '', content)
    content = re.sub(r'\s*<meta property="og:[^>]*/>', '', content)
    content = re.sub(r'\s*<meta name="twitter:[^>]*/>', '', content)
    content = re.sub(r'\s*<link rel="icon"[^>]*/>', '', content)
    content = re.sub(r'\s*<link rel="apple-touch-icon"[^>]*/>', '', content)

    # Insert after viewport meta tag
    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0" />',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n' + seo
    )

    # Add JSON-LD schema for homepage
    if f == 'index.html' and 'application/ld+json' not in content:
        content = content.replace('</head>', SCHEMA_HOMEPAGE + '\n</head>', 1)

    if content != orig:
        open(f, 'w', encoding='utf-8').write(content)
        count += 1
        print('Updated:', f)

print(f'Done - {count} files updated')
