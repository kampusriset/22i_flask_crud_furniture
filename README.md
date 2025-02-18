# 🏠 Toko InStyle Furniture
Sistem e-commerce sederhana untuk mengelola produk furnitur, termasuk fitur CRUD, autentikasi login, dan dashboard stok.

## 🌟 Fitur Utama
✅ **Autentikasi Login** (Hashing password dengan bcrypt)  
✅ **CRUD Produk** (Tambah, Edit, Hapus, Tampilkan barang)  
✅ **Manajemen Stok** (Update jumlah barang)  
✅ **Dashboard dengan Grafik Stok** (Menggunakan Chart.js)  
✅ **Pencarian Produk** (Live search di halaman kelola barang)  

## 📌 Teknologi yang Digunakan
- **Backend:** Flask (Python)
- **Database:** MySQL (phpMyAdmin) dengan PyMySQL
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Library:** Flask-Login, Flask-WTF, Chart.js

## 🚀 Cara Instalasi & Menjalankan Proyek
### 1️⃣ Clone Repository
```sh
git clone https://github.com/username/InStyleFurniture.git
cd InStyleFurniture
```
### 2️⃣ Buat Virtual Environment & Install Dependensi
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```
### 3️⃣ Konfigurasi Database
- Pastikan MySQL sudah terinstal & berjalan.  
- Buat database `instyle_furniture` di phpMyAdmin.  
- Import file `instyle_furniture.sql` yang sudah disediakan.  
- Sesuaikan konfigurasi database di `database.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password_anda', # Umumnya jika belum disetting kosong atau ''
    'database': 'instyle_furniture'
}
```

### 4️⃣ Jalankan Aplikasi
```sh
python app.py
```
Aplikasi akan berjalan di `http://127.0.0.1:5000/`.

Untuk login bisa langsung menggunakan username dan password admin karena sudah tersimpan didatabase instyle_furniture
bisa juga register/membuat akun baru

---

## 📊 Struktur Proyek
```
InStyleFurniture/
│── app.py               # File utama Flask
│── database.py          # Koneksi ke MySQL dengan PyMySQL
│── instyle_furniture.sql # Struktur database MySQL
│── requirements.txt     # Dependensi proyek
│── README.md            # Dokumentasi
│── static/              # Folder asset (CSS, JS, gambar)
│── templates/           # HTML
│── venv/                # Virtual environment
```

## ✨ Kontributor
- **Irsyad Badruddin**
- **Tegar Risky Nugrahanto**
- **Syamsul Dahlan**
- **Moh. Dzakirin Amrulloh**

---

## 💎 Requirements.txt
Berikut adalah daftar dependensi proyek yang digunakan:
```txt
Flask==3.0.0
Werkzeug==3.0.1
PyMySQL==1.1.0
```

Untuk menginstal semua dependensi, jalankan perintah berikut:
```sh
pip install -r requirements.txt
```

## 💎 Database
Pastikan Anda mengimpor `instyle_furniture.sql` ke phpMyAdmin sebelum menjalankan aplikasi.

## 📧 Kontak
Jika ada pertanyaan, silakan hubungi:  
📩 Email: example@email.com  
🌐 Website: [example.com](https://example.com)

---
🔥 **Happy Coding!** 🚀