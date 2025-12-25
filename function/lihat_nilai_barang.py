from database import data as data

def lihat_nilai_barang():
    if not data.data_barang:
        print("Data kosong")
        return

    garis = "-" * 90

    # Header tabel
    print(garis)
    print(
        f"{'No':<4} "
        f"{'Kategori':<20} "
        f"{'Nama Barang':<25} "
        f"{'Harga':<15} "
        f"{'Stok':<10} "
        f"{'Nilai Barang':<15}"
    )
    print(garis)

    # Isi tabel
    for i, b in enumerate(data.data_barang, start=1):
        nilai_barang = b['harga'] * b['stok']
        print(
            f"{i:<4} "
            f"{b['kategori']:<20} "
            f"{b['nama']:<25} "
            f"{b['harga']:<15} "
            f"{b['stok']:<10} "
            f"{nilai_barang:<15}"
        )

    print(garis)
