from pathlib import Path
from random import randint
import logging
import json



logging.basicConfig(
    filename="riwayat_logging.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

data_baru = "data_simpan.json"
while True:
    input_data = input("Masukan perintah 1. membuat file baru , 2.menambah data baru, 3 membaca data ")
    if not input_data.isdigit():
        print("Harap masukkan angka 1, 2, atau 3!")
        continue
    
    data= int(input_data)
    
    
    if data == 1 :
        try:
            dataSimpan = {}
            with open(data_baru, "w", encoding="utf-8")as file :
                json.dump(dataSimpan, file , indent=4)
                print("telah membuat file baru ")

        except :
            print("terjadi masalah")

    elif data == 2: 
        try: 
            # 1. Muat (load) dulu data lama dari file JSON jika sudah ada
            try:
                with open(data_baru, "r", encoding="utf-8") as f:
                    dataSimpan = json.load(f)
            except FileNotFoundError:
                # Jika filenya belum pernah dibuat, mulai dengan dictionary kosong
                dataSimpan = {}

            # 2. Menerima input dari pengguna
            data_a = input("Masukkan nama = ")
            data_b = int(input("Masukkan usia = ")) # Diubah ke int agar valid
            
            # 3. Buat kunci acak 3 digit (misal: mhs482) dan masukkan ke dictionary
            kode_unik = f"mhs{randint(100, 999)}"
            dataSimpan[kode_unik] = {"nama": data_a, "usia": data_b}
            
            # 4. Simpan kembali seluruh data (data lama + data baru) ke file JSON
            with open(data_baru, "w", encoding="utf-8") as f:
                json.dump(dataSimpan, f, indent=4)
                print(f"Berhasil menambahkan data dengan kode unik: {kode_unik}")

        except ValueError:
            print("Gagal: Usia harus berupa angka (integer)!")
        except Exception as e:
            print(f"Gagal melakukan penambahan data baru: {e}")

    # MENU 3: Membaca isi data
    elif data == 3:
        try:
            with open(data_baru, "r", encoding="utf-8") as f:
                isi_file = json.load(f)
                print("\n--- ISI DATA SAAT INI ---")
                print(json.dumps(isi_file, indent=4))
                print("--------------------------")
        except FileNotFoundError:
            print("File data belum ditemukan. Silakan buat file terlebih dahulu di menu 1.")
    


