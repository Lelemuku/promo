# Swiss-Belexpress Jayapura – Link in Bio

Website mirip Linktree untuk Swiss-Belexpress Jayapura, di-host di GitHub Pages dengan custom domain.

---

## 🚀 Cara Deploy ke GitHub Pages

### 1. Buat Repository GitHub

1. Login ke [github.com](https://github.com)
2. Klik **New repository**
3. Nama repo: `swissbelexpress-jayapura` (atau nama lain)
4. Set ke **Public**
5. Klik **Create repository**

### 2. Upload Files

Upload semua file ini ke repo:
```
index.html
style.css
main.js
CNAME
```

Cara termudah: klik **Add file → Upload files** di GitHub.

### 3. Aktifkan GitHub Pages

1. Buka **Settings** di repository
2. Klik **Pages** di sidebar kiri
3. Di **Source**, pilih branch **main** dan folder **/ (root)**
4. Klik **Save**

GitHub akan memberikan URL default: `https://username.github.io/nama-repo/`

### 4. Setting Custom Domain (`promo.lelemuku.com`)

#### A. Di GitHub:
- Pada halaman **Settings → Pages**, masukkan `promo.lelemuku.com` di kolom **Custom domain**
- Klik **Save**
- Centang **Enforce HTTPS** (setelah DNS aktif)

#### B. Di DNS Manager domain `lelemuku.com`:

Tambahkan **CNAME record**:

| Type  | Name  | Value                         | TTL  |
|-------|-------|-------------------------------|------|
| CNAME | promo | `username.github.io`          | 3600 |

> Ganti `username` dengan username GitHub Anda.

Atau kalau ingin pakai subdomain dari root domain, tambahkan **A records** ini:

| Type | Name  | Value          |
|------|-------|----------------|
| A    | promo | 185.199.108.153 |
| A    | promo | 185.199.109.153 |
| A    | promo | 185.199.110.153 |
| A    | promo | 185.199.111.153 |

DNS biasanya aktif dalam **5–30 menit** (kadang sampai 24 jam).

---

## 📁 Struktur File

```
swissbelexpress-jayapura/
├── index.html    ← Halaman utama
├── style.css     ← Styling & animasi
├── main.js       ← Interaksi (ripple effect)
├── CNAME         ← Custom domain GitHub Pages
└── README.md     ← Panduan ini
```

---

## ✏️ Cara Edit Konten

Buka `index.html` dan cari bagian yang ingin diubah:

- **Nama & tagline** → cari `<h1 class="hotel-name">` dan `<p class="tagline">`
- **Foto profil** → ganti URL di tag `<img class="avatar" src="...">`
- **Tambah link baru** → copy-paste salah satu blok `<a class="link-card">` dan ubah href + teks
- **Hapus link** → hapus blok `<a class="link-card">` yang tidak diperlukan

---

## 🎨 Kustomisasi Warna

Buka `style.css`, edit variabel di bagian `:root`:

```css
--gold:       #c9a84c;   /* Warna emas utama */
--dark:       #0e0c08;   /* Warna background */
--cream:      #f5f0e8;   /* Warna teks */
```
