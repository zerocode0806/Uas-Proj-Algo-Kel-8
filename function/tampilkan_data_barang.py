from database import data as data

def tampilkan_data_barang():
    if not data.data_barang:
        print("Data kosong")
        return

    garis = "-" * 90

    # Header tabel
    print(garis)
    print(f"{'No':<4} {'Nama Barang':<25} {'Kategori':<20} {'Stok':<10} {'Harga':<15}")
    print(garis)

    # Isi tabel
    for i, b in enumerate(data.data_barang, start=1):
        print(
            f"{i:<4} "
            f"{b['nama']:<25} "
            f"{b['kategori']:<20} "
            f"{b['stok']:<10} "
            f"{b['harga']:<15}"
        )

    print(garis)
