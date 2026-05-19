#!/usr/bin/env python3
"""
Generator otomatis untuk halaman bisnis promo.lelemuku.com

Usage:
  1. Edit businesses.json
  2. Jalankan: python scripts/generate.py
  3. Upload hasil ke GitHub Pages
"""

import json
import os
import sys

# SVG Icons
INSTAGRAM_SVG = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>'''

FACEBOOK_SVG = '''<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>'''

EMAIL_SVG = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="2,4 12,13 22,4"/></svg>'''

WA_SVG = '''<svg viewBox="0 0 24 24" fill="currentColor" class="wa-icon"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>'''


def generate_page(slug, data):
    """Generate HTML page for a business"""

    # Build social buttons
    socials_html = []
    if data['socials'].get('instagram'):
        socials_html.append(f'<a href="{data["socials"]["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram" class="social-btn">{INSTAGRAM_SVG}</a>')
    if data['socials'].get('facebook'):
        socials_html.append(f'<a href="{data["socials"]["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook" class="social-btn">{FACEBOOK_SVG}</a>')
    if data['socials'].get('email'):
        socials_html.append(f'<a href="{data["socials"]["email"]}" aria-label="Email" class="social-btn">{EMAIL_SVG}</a>')

    # Build links
    links_html = []
    current_section = None

    for link in data['links']:
        link_type = link['type']

        if link_type != current_section:
            if link_type == 'whatsapp':
                links_html.append('<p class="section-label">Contact Us</p>')
            elif link_type == 'normal' and current_section in [None, 'primary', 'whatsapp']:
                links_html.append('<p class="section-label">About Us</p>')
            elif link_type == 'offer':
                links_html.append('<p class="section-label">Special Offers & Partners</p>')
            current_section = link_type

        icon = WA_SVG if link['icon'] == 'wa' else f'<span class="link-icon">{link["icon"]}</span>'

        links_html.append(f'''        <a href="{link["url"]}" target="_blank" rel="noopener" class="link-card link-{link_type}">
          {icon}
          <span class="link-text">
            <span class="link-title">{link["title"]}</span>
            <span class="link-sub">{link["subtitle"]}</span>
          </span>
          <span class="link-arrow">›</span>
        </a>''')

    html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>{data["name"]} | {data["tagline"]}</title>
  <meta name="description" content="{data["tagline"]} – {data["name"]} official links." />
  <meta property="og:title" content="{data["name"]}" />
  <meta property="og:description" content="{data["tagline"]}" />
  <meta property="og:image" content="{data["avatar"]}" />
  <meta property="og:url" content="https://promo.lelemuku.com/{slug}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Jost:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../style.css" />
  <style>
    :root {{
      --brand-color: {data["brand_color"]};
      --brand-color-light: {data["brand_color_light"]};
      --brand-color-dim: {data["brand_color_dim"]};
    }}
  </style>
</head>
<body>

  <div class="bg-layer bg-gold"></div>
  <div class="bg-layer bg-noise"></div>

  <main class="container">

    <section class="profile">
      <div class="avatar-wrap">
        <img
          src="{data["avatar"]}"
          alt="{data["name"]}"
          class="avatar"
          onerror="this.src='https://placehold.co/120x120/{data["brand_color"].replace("#", "")}/fff?text={"+".join(data["name"].split()[:2])}'"
        />
      </div>
      <span class="category-badge">{data["category"]}</span>
      <h1 class="hotel-name">{data["name"]}</h1>
      <p class="tagline">{data["tagline"]}</p>

      <div class="socials">
        {chr(10).join(socials_html)}
      </div>
    </section>

    <section class="links">
      <div class="link-group">
        {chr(10).join(links_html)}
      </div>
    </section>

    <footer class="footer">
      <p>© 2025 {data["name"]} · All rights reserved</p>
      <p class="footer-domain">promo.lelemuku.com/{slug}</p>
    </footer>

  </main>

  <script src="../main.js"></script>
</body>
</html>'''

    return html


def generate_landing(businesses):
    """Generate landing page HTML"""

    # Group by category
    categories = {}
    for slug, data in businesses.items():
        cat = data['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((slug, data))

    # Category display names
    cat_names = {
        'hotel': 'Hotel',
        'restaurant': 'Restoran',
        'mall': 'Mall',
        'shop': 'Toko',
        'business': 'Bisnis',
        'institution': 'Instansi'
    }

    sections = []
    for cat, items in categories.items():
        cat_name = cat_names.get(cat, cat.capitalize())
        cards = []
        for slug, data in items:
            cards.append(f'''      <a href="{slug}/" class="business-card" data-name="{slug.replace('-', ' ')}">
        <img src="{data["avatar"]}" class="business-avatar" alt="{data["name"]}" onerror="this.src='https://placehold.co/48x48/{data["brand_color"].replace("#", "")}/fff?text={data["name"][:2]}'" />
        <div class="business-info">
          <div class="business-name">{data["name"]}</div>
          <div class="business-tagline">{data["tagline"]}</div>
        </div>
        <span class="business-arrow">›</span>
      </a>''')

        sections.append(f'''    <div class="category-title">{cat_name} <span class="business-category-tag">{len(items)} bisnis</span></div>
    <div class="business-grid" data-category="{cat}">
      {chr(10).join(cards)}
    </div>''')

    # Full landing HTML (simplified, full version in actual file)
    return sections


def main():
    # Load data
    with open('businesses.json', 'r', encoding='utf-8') as f:
        businesses = json.load(f)

    print(f"Generating {len(businesses)} business pages...")

    # Generate each business page
    for slug, data in businesses.items():
        folder = slug
        os.makedirs(folder, exist_ok=True)

        html = generate_page(slug, data)

        with open(f'{folder}/index.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"  ✅ {slug}/ → {data['name']}")

    print("\nDone! Upload all files to GitHub Pages.")


if __name__ == '__main__':
    main()
