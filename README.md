# Sistem Manajemen Gudang

### UAS Proyek Algoritma dan Pemrograman - Kelompok 8

Aplikasi berbasis CLI (Command Line Interface) untuk pengelolaan stok barang dan pencatatan transaksi penjualan menggunakan penyimpanan data JSON.

    Program Pengelolaan Data Barang Gudang Requirement:
        o Data barang: nama, kategori, stok, harga.
        o Disimpan dalam list of dictionary.
        o Kategori unik dalam set.

    Fitur utama:
        o Tambah barang -> tambah_data_barang.py
        o Cari barang (nested if → berdasarkan nama atau kategori) -> cari_data_barang.py
        o Hitung total nilai stok (stok × harga) per kategori -> lihat_stok_barang.py
        o Peringatan stok menipis (stok < 5) -> lihat_nilai_barang.py

    Fitur Tambahan:
        o Hapus Data Barang -> hapus_data_barang.py
        o Tampilkan Data Barang -> tampilkan_data_barang.py
        o Save Data (.json) -> save_load_data_barang.py

---

## Anggota Kelompok 8

| No  | Nama Anggota          | NIM |
| :-: | :-------------------- | :-: |
|  1  | M Ubaidilla Dahlan    | 146 |
|  2  | Aira Diandra Z M      | 121 |
|  3  | Abdul Rozak Choirudin | 122 |
|  4  | Muhammad Adam H       | 128 |

---

## truktur Folder Proyek

Berikut adalah susunan direktori agar kode tetap modular dan mudah dikelola:

```text
UAS-PROJ-ALGO-KEL-8/
├── database/                    # Penyimpanan Data (Persistence)
│   ├── __init__.py              # Inisialisasi package database
│   ├── data.py                  # Penampung list data di memori (runtime)
│   └── data_barang.json         # File fisik database barang
│
├── function/                    # Modul Logika Fitur Aplikasi
│   ├── __init__.py              # Inisialisasi package function
│   ├── cari_data_barang.py      # Logika pencarian barang
│   ├── hapus_data_barang.py     # Logika penghapusan barang
│   ├── lihat_nilai_barang.py    # Logika kalkulasi total aset barang
│   ├── lihat_stok_barang.py     # Logika pengecekan stok menipis
│   ├── save_load_data_barang.py # Fungsi simpan/muat data barang ke JSON
│   ├── tambah_data_barang.py    # Logika penambahan barang baru
│   └── tampilkan_data_barang.py # Logika menampilkan tabel barang
│
├── controller.py                # Penghubung (Bridge) antara main dan function
├── main.py                      # Entry point / Menu utama aplikasi
├── flowchart-system.fprg        # Rancangan alur sistem (Flowgorithm)
└── README.md                    # Dokumentasi proyek


```
