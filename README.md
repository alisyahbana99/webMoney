Money-Stocking - Dashboard Finance & Inventory

Aplikasi web dashboard untuk manajemen keuangan dan pencatatan transaksi, dirancang untuk mempermudah tim Finance dalam memantau arus kas secara *real-time*.

## Fitur Utama
* **Authentication:** Sistem login aman untuk mengakses dashboard.
* **Interactive Chart:** Visualisasi data Pemasukan vs Pengeluaran menggunakan Chart.js.
* **Transaction Records:** Mencatat riwayat transaksi dengan kategori yang jelas.
* **Export Data:** Mengunduh laporan transaksi dalam format CSV (bisa dibuka di Excel).

## Teknologi yang Digunakan
* **Backend:** Python (Flask)
* **Database:** SQL (SQLite)
* **Frontend:** HTML5, CSS3, JavaScript (Chart.js)

## Cara Menjalankan Secara Lokal
1. Clone repository ini: `git clone https://github.com/alisyahbana99/Money-Stocking.git`
2. Masuk ke folder: `cd Money-Stocking`
3. Buat virtual environment: `python -m venv venv`
4. Aktifkan venv (Windows): `.\venv\Scripts\Activate.ps1`
5. Install Flask: `pip install Flask`
6. Buat database: `python database.py`
7. Jalankan aplikasi: `python app.py`
8. Buka `http://127.0.0.1:5000` di browser. (Login default: `admin` / `admin123`)
