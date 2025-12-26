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

UAS-PROJ-ALGO-KEL-8/
│
├── database/ # Penyimpanan data (Persistence)
│ ├── **init**.py # Inisialisasi package database
│ ├── data.py # File penampung list data di memori
│ └── data_barang.json # File fisik database barang (JSON)
│
├── function/ # Modul fungsi fitur aplikasi
│ ├── **init**.py # Inisialisasi package function
│ ├── cari_data_barang.py # Logika pencarian barang
│ ├── hapus_data_barang.py # Logika penghapusan barang
│ ├── lihat_nilai_barang.py # Logika kalkulasi total aset barang
│ ├── lihat_stok_barang.py # Logika pengecekan stok menipis
│ ├── save_load_data_barang.py# Fungsi simpan/muat data barang ke JSON
│ ├── tambah_data_barang.py # Logika penambahan barang baru
│ └── tampilkan_data_barang.py# Logika menampilkan tabel barang
│
├── controller.py # Penghubung (Bridge) antara main dan function
├── main.py # Entry point/Menu utama aplikasi
├── flowchart-system.fprg # Rancangan alur sistem (Flowgorithm)
└── README.md # Dokumentasi proyek

Note Fitur:
o Untuk Fitur "Save Data (.json) -> save_load_data_barang.py" saya tambahkan agar saat user menjalankan aplikasi lagi, data barang masih tersimpan
o controller.py -> berisi semua import modul

Anggota Kelompok 8:
o M Ubaidilla Dahlan (146)
o Aira Diandra Z M (121)
o Abdul Rozak Choirudin (122)
o Muhammad Adam H (128)
