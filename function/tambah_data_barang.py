import database.data as data
from function.save_load_data_barang import save_data

def tambah_data_barang():
    jumlah_barang = int(input("Masukkan jumlah barang yang akan ditambahkan: "))
    for i in range(jumlah_barang):
        print(f"---------- Menginput barang ke-{i + 1} ----------")
        nama = input("Masukkan nama barang: ")
        kategori_input = input("Masukkan kategori barang: ").strip()
        
        # simpan kategori unik
        if kategori_input not in data.kategori_barang:
            data.kategori_barang = data.kategori_barang + (kategori_input,)

        stok = int(input("Masukkan stok: "))
        harga = int(input("Masukkan harga: "))

        data.data_barang.append({
            "nama": nama,
            "kategori": kategori_input,
            "stok": stok,
            "harga": harga
        })

    save_data()
    print("Data berhasil disimpan")
