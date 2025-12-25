import database.data as data
from function.save_load_data_barang import save_data
from function.tampilkan_data_barang import tampilkan_data_barang

def hapus_data_barang():
    tampilkan_data_barang()
    index = int(input("Pilih nomor barang yang dihapus: ")) - 1

    if 0 <= index < len(data.data_barang):
        data.data_barang.pop(index)
        save_data()
        print("Barang berhasil dihapus")
    else:
        print("Index tidak valid")
