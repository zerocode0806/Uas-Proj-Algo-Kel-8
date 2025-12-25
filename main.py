from controller import (
    load_data,
    tambah_data_barang,
    tampilkan_data_barang,
    cari_data_barang,
    hapus_data_barang,
    lihat_stok_barang,
    lihat_nilai_barang,
)

load_data()

garis = "-" * 90
pembatas = "=" * 90

while True:
    print(pembatas)
    print("Aplikasi Manajemen Data Barang")
    print(pembatas)
    # fitur tambah barang
    print("1. Tambah Data Barang")
    # fitur tampilkan semua barang(fitur tambahan)
    print("2. Tampilkan Data Barang")
    # fitur cari barang
    print("3. Cari Data Barang")
    # fitur lihat stok barang dan notifikasi stok menipis
    print("4. Lihat Stok Barang")
    # fitur lihat nilai barang(harga * stok)
    print("5. Lihat Nilai Barang")
    # fitur hapus barang
    print("6. Hapus Data Barang")
    print("7. Keluar")
    print(garis)
    p = input("Pilih: ")

    if p == "1":
        tambah_data_barang()
    elif p == "2":
        tampilkan_data_barang()
    elif p == "3":
        cari_data_barang()
    elif p == "4":
        lihat_stok_barang()
    elif p == "5":  
        lihat_nilai_barang()
    elif p == "6":
        hapus_data_barang()
    elif p == "7":
        break
