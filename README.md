Program Pengelolaan Data Barang Gudang
    • Data barang: nama, kategori, stok, harga.
    • Disimpan dalam list of dictionary.
    • Kategori unik dalam set.
    • Fitur:
        o Tambah barang -> tambah_data_barang.py
        o Cari barang (nested if → berdasarkan nama atau kategori) -> cari_data_barang.py
        o Hitung total nilai stok (stok × harga) per kategori -> lihat_stok_barang.py
        o Peringatan stok menipis (stok < 5) -> lihat_nilai_barang.py

    Fitur Tambahan: 
        o Hapus Data Barang -> hapus_data_barang.py
        o Tampilkan Data Barang -> tampilkan_data_barang.py
        o Save Data (.json) -> save_load_data_barang.py

Untuk Fitur "Save Data (.json) -> save_load_data_barang.py" saya tambahkan agar saat user menjalankan aplikasi lagi, data barang masih tersimpan

controller.py -> berisi semua import modul