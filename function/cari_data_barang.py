import database.data as data

def cari_data_barang():
    keyword = input("Masukkan nama atau kategori barang: ").lower()
    ditemukan = False

    garis = "-" * 90

    print(garis)
    print(f"{'No':<4} {'Kategori':<20} {'Nama Barang':<25} {'Stok':<10} {'Harga':<15}")
    print(garis)

    for i, b in enumerate(data.data_barang, start=1):
        if keyword in b["nama"].lower() or keyword in b["kategori"].lower():
            print(
                f"{i:<4} "
                f"{b['kategori']:<20} "
                f"{b['nama']:<25} "
                f"{b['stok']:<10} "
                f"{b['harga']:<15}"
            )
            ditemukan = True

    if not ditemukan:
        print("Barang tidak ditemukan")

    print(garis)
