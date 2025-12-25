from database import data as data

def lihat_stok_barang():
    if not data.data_barang:
        print("Data kosong")
        return

    garis = "-" * 90

    # Header tabel
    print(garis)
    print(f"{'No':<4} {'Kategori':<20} {'Nama Barang':<25} {'Stok':<10} {'Status':<15}")
    print(garis)

    # Isi tabel
    for i, b in enumerate(data.data_barang, start=1):
        status = "Stok hampir habis" if b['stok'] < 5 else "Stok masih banyak"
        print(
            f"{i:<4} "
            f"{b['kategori']:<20} "
            f"{b['nama']:<25} "
            f"{b['stok']:<10} "
            f"{status:<15}"
        )

    print(garis)