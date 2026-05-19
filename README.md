# Promo.lelemuku.com — Multi-Business Linktree Platform

Platform Link in Bio untuk berbagai bisnis (hotel, restoran, mall, toko, usaha, instansi) di Papua & Maluku.

## 🌐 Live URLs

| URL | Bisnis |
|-----|--------|
| `https://promo.lelemuku.com/` | Halaman landing — daftar semua bisnis |
| `https://promo.lelemuku.com/swissbelexpress-jayapura/` | Swiss-Belexpress Jayapura |
| `https://promo.lelemuku.com/swissbelexpress-abe/` | Swiss-Belexpress Abe |
| `https://promo.lelemuku.com/swissbelexpress-timika/` | Swiss-Belexpress Timika |
| `https://promo.lelemuku.com/swissbelexpress-merauke/` | Swiss-Belexpress Merauke |
| `https://promo.lelemuku.com/swissbelexpress-sentani/` | Swiss-Belexpress Sentani |
| `https://promo.lelemuku.com/mercure-timika/` | Mercure Timika |
| `https://promo.lelemuku.com/mercure-jayapura/` | Mercure Jayapura |
| `https://promo.lelemuku.com/hotelmaxone-jayapura/` | Hotel MaxOne Jayapura |
| `https://promo.lelemuku.com/lelemuku-cafe/` | Lelemuku Café |
| `https://promo.lelemuku.com/jayapura-mall/` | Jayapura Mall |

---

## 📁 Struktur File

```
promo-lelemuku.com/
├── index.html              ← Landing page (daftar semua bisnis)
├── style.css               ← CSS shared (dinamis per brand)
├── main.js                 ← JavaScript shared
├── businesses.json         ← Data semua bisnis
├── CNAME                   ← Custom domain
├── README.md               ← File ini
│
├── swissbelexpress-jayapura/
│   └── index.html          ← Halaman Swiss-Belexpress Jayapura
├── swissbelexpress-abe/
│   └── index.html
├── swissbelexpress-timika/
│   └── index.html
├── swissbelexpress-merauke/
│   └── index.html
├── swissbelexpress-sentani/
│   └── index.html
├── mercure-timika/
│   └── index.html
├── mercure-jayapura/
│   └── index.html
├── hotelmaxone-jayapura/
│   └── index.html
├── lelemuku-cafe/
│   └── index.html
└── jayapura-mall/
    └── index.html
```

---

## 🚀 Cara Deploy ke GitHub Pages

### 1. Buat Repository Baru

1. Login ke [github.com](https://github.com)
2. Klik **New repository**
3. Nama repo: `promo-lelemuku` (bebas)
4. Set ke **Public**
5. Klik **Create repository**

### 2. Upload Semua File

Upload seluruh isi folder ini ke repository:
- `index.html`, `style.css`, `main.js`, `businesses.json`, `CNAME`
- Semua folder bisnis (`swissbelexpress-jayapura/`, `mercure-timika/`, dst.)

Cara termudah: klik **Add file → Upload files** di GitHub, atau gunakan Git CLI.

### 3. Aktifkan GitHub Pages

1. Buka **Settings** di repository
2. Klik **Pages** di sidebar kiri
3. Di **Source**, pilih branch **main** dan folder **/ (root)**
4. Klik **Save**

### 4. Setting Custom Domain

1. Di halaman **Settings → Pages**, masukkan `promo.lelemuku.com` di kolom **Custom domain**
2. Klik **Save**
3. Centang **Enforce HTTPS** (setelah DNS aktif)

### 5. Setting DNS (di Domain Manager)

Tambahkan **CNAME record**:

| Type  | Name  | Value                | TTL  |
|-------|-------|----------------------|------|
| CNAME | promo | `username.github.io` | 3600 |

> Ganti `username` dengan username GitHub Anda.

Atau pakai **A records**:

| Type | Name  | Value           |
|------|-------|-----------------|
| A    | promo | 185.199.108.153 |
| A    | promo | 185.199.109.153 |
| A    | promo | 185.199.110.153 |
| A    | promo | 185.199.111.153 |

---

## 🎨 Cara Menambah Bisnis Baru

### Metode 1: Edit `businesses.json` + Regenerate (Direkomendasikan)

1. Buka `businesses.json`
2. Tambahkan entry baru dengan format:

```json
"nama-slug": {
  "name": "Nama Bisnis",
  "tagline": "Tagline Bisnis",
  "category": "hotel|restaurant|mall|shop|business|institution",
  "brand_color": "#hexwarna",
  "brand_color_light": "#hexwarna_light",
  "brand_color_dim": "#hexwarna_dim",
  "avatar": "https://url-foto.jpg",
  "socials": {
    "instagram": "https://instagram.com/...",
    "facebook": "https://facebook.com/...",
    "email": "mailto:email@bisnis.com"
  },
  "links": [
    {"type": "primary", "icon": "🏅", "title": "Judul Link", "subtitle": "Deskripsi", "url": "https://..."},
    {"type": "whatsapp", "icon": "wa", "title": "WhatsApp", "subtitle": "+62...", "url": "https://wa.me/..."},
    {"type": "normal", "icon": "📋", "title": "Judul", "subtitle": "Deskripsi", "url": "https://..."},
    {"type": "offer", "icon": "🎉", "title": "Promo", "subtitle": "Detail promo", "url": "https://..."}
  ]
}
```

3. Jalankan script generator (lihat `scripts/generate.py`)
4. Upload hasil ke GitHub

### Metode 2: Manual Copy-Paste

1. Copy folder bisnis yang sudah ada (misal `swissbelexpress-jayapura/`)
2. Rename folder sesuai slug baru
3. Edit `index.html` di dalam folder tersebut:
   - Ganti `--brand-color` di `<style>`
   - Ganti nama, tagline, avatar
   - Ganti link social media
   - Ganti semua link cards
4. Update `index.html` (landing page) — tambahkan card baru

---

## 🎯 Fitur

- ✅ **Brand color dinamis** — tiap bisnis punya warna brand sendiri
- ✅ **Landing page** dengan pencarian & filter kategori
- ✅ **Responsive** — mobile-first design
- ✅ **SEO optimized** — Open Graph tags per halaman
- ✅ **Ripple effect** — interaktif saat tap/click
- ✅ **Analytics ready** — tracking clicks (console log, bisa dihubungkan ke GA)
- ✅ **Mudah scale** — tambah bisnis baru tanpa repot

---

## 🛠️ Tech Stack

- **Static HTML** — no backend needed
- **CSS Variables** — theming dinamis
- **Vanilla JS** — lightweight, no dependencies
- **GitHub Pages** — free hosting + custom domain

---

## 📞 Kontak

Email: hello@lelemuku.com
