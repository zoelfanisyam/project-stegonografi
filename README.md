# 🔐 Alpha Channel Image Steganography

Web-based **Steganografi Gambar PNG** menggunakan **Alpha Channel** (transparansi) untuk menyisipkan pesan rahasia secara aman tanpa mengubah tampilan visual gambar.

> Dibangun dengan Python + Flask, dan dirancang dengan tampilan modern berkat Tailwind CSS.

---

## ✨ Fitur Utama

- 🖼️ Menyisipkan pesan rahasia ke dalam gambar PNG
- 🔒 Proteksi pesan dengan **PIN** (berbasis hash SHA256)
- 🕵️ Mengekstrak pesan dari gambar hasil steganografi
- 🎨 Antarmuka gelap (Dark Mode) dengan **Tailwind CSS**
- 🔁 Perbandingan langsung antara **gambar asli dan stego**

---

## 📸 Tampilan Antarmuka

| Fitur                                                                                   | Screenshot                                                                                                      |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Form Sisipkan** <br> Untuk menyisipkan pesan rahasia ke dalam gambar PNG.             | ![Form Sisipkan](https://github.com/zoelfanisyam/project-stegonografi/blob/main/assets/Halaman_sisipkan.png)    |
| **Form Ekstrak** <br> Untuk mengambil pesan dari gambar stego dengan verifikasi PIN.    | ![Form Ekstrak](https://github.com/zoelfanisyam/project-stegonografi/blob/main/assets/Halaman_extrak.png)       |
| **Hasil Ekstrak** <br> Menampilkan pesan rahasia dan perbandingan gambar asli vs stego. | ![Hasil Ekstrak](https://github.com/zoelfanisyam/project-stegonografi/blob/main/assets/Halaman_hasilExtrak.png) |

---

## 🚀 Cara Menjalankan Aplikasi

### 1. 🔽 Clone Repository

```bash
git clone https://github.com/zoelfanisyam/project-stegonografi.git
cd project-stegonografi
```

### 2. 📦 Install Dependensi

```bash
pip install -r requirements.txt
```

### 3. ▶️ Jalankan Aplikasi

```bash
python app.py
```

### 4. 🌐 Akses di Browser

Buka browser dan akses:

```bash
http://localhost:5000
```

### 5. 📁 Struktur Folder

```bash
project-stegonografi/
├── stegano_alpha.py
├── templates/
│   ├── index.html        # Halaman utama (form sisipkan / ekstrak)
│   └── result.html        # Halaman hasil ekstraksi
├── outputs/              # Folder gambar stego
├── uploads/              # Folder gambar asli
├── app.py                # Main Flask App
└── requirements.txt      # Dependensi Python
```

### 6. 💡 Teknologi yang Digunakan

⚙️ Python + Flask (server-side)
🎨 Tailwind CSS (UI responsif & dark mode)
🧠 LSB (Least Significant Bit) pada channel alpha
🔐 SHA256 untuk validasi PIN

### 7. 🛡️ Catatan Keamanan

Jangan gunakan gambar JPEG/JPG karena tidak mendukung alpha channel.
PIN yang digunakan tidak disimpan, tetapi divalidasi menggunakan hash.

### 🤝 Kontribusi

Pull request, feedback, dan issue sangat terbuka! Jangan lupa ⭐ repo ini kalau kamu merasa terbantu.
