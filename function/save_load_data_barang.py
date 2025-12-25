import json
import os
import database.data as data

# Ambil folder function/
CURRENT_DIR = os.path.dirname(__file__)

# Naik satu level ke project/
BASE_DIR = os.path.dirname(CURRENT_DIR)

# Masuk ke folder database/
FILE_NAME = os.path.join(BASE_DIR, "database", "data_barang.json")


def load_data():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as f:
        db = json.load(f)

        data.kategori_barang = tuple(db.get("kategori", []))

        data.data_barang.clear()
        data.data_barang.extend(db.get("barang", []))


def save_data():
    db = {
        "kategori": list(data.kategori_barang),
        "barang": data.data_barang
    }

    with open(FILE_NAME, "w") as f:
        json.dump(db, f, indent=4)
