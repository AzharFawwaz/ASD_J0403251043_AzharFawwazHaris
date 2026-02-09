# # ==========================================================
# # TUGAS HANDS-ON MODUL 1
# # Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
# #
# # Nama : Azhar Fawwaz Haris
# # NIM : J0403251043
# # Kelas : A / P2
# # ==========================================================
# # -------------------------------
# # Konstanta nama file
# # -------------------------------
NAMA_FILE = "stok_barang.txt"

# # -------------------------------
# # Fungsi: Membaca data dari file
# # -------------------------------
def baca_stok(nama_file):
    stok_dict = {}
    with open(NAMA_FILE, "r", encoding="utf-8") as file :
        for baris in file :
            baris = baris.strip()
            kode, nama, jumlah = baris.split(",")
            stok_dict[kode] = {"nama" : nama, "jumlah" : int(jumlah)}
    return stok_dict

buka_data = baca_stok(NAMA_FILE)
# print("Jumlah data adalah : ", len(buka_data))

# # -------------------------------
# # Fungsi: Menyimpan data ke file
# # -------------------------------
def simpan_stok(NAMA_FILE, stok_dict):
    with open(NAMA_FILE, "w", encoding="utf-8") as file :
        for kode in sorted(stok_dict.keys()) :
            NamaBarang = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["jumlah"]
            file.write(f"{kode},{NamaBarang},{stok}\n")

simpan_stok(NAMA_FILE, buka_data)
# print("Data berhasil di simpan ke file : ", NAMA_FILE)

# # -------------------------------
# # Fungsi: Menampilkan semua data
# # -------------------------------

def tampilkan_stok(stok_dict) :
    if not stok_dict :
        print("\nStok kosong.")
        return

    print("\n===== DAFTAR BARANG =====")
    print(f"{'kode' : <10} | {'NamaBarang' : <20} | {'stok' : >5}")
    print("-"*35)

    for kode in sorted(stok_dict.keys()) :
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["jumlah"]
        print(f"{kode : <10} | {nama: <20} | {stok : >5}")

# tampilkan_stok(buka_data)

# # -------------------------------
# # Fungsi: Cari barang berdasarkan kode
# # -------------------------------

def cari_barang(stok_dict):
    kode_cari = input("Masukkan kode barang yang ingin di cari : ").strip()

    if kode_cari in stok_dict :
        NamaBarang = stok_dict[kode_cari]["nama"]
        stok = stok_dict[kode_cari]["jumlah"]

        print("===== BARANG DITEMUKAN =====")
        print(f"KODE : {kode_cari}")
        print(f"NAMA : {NamaBarang}")
        print(f"JUMLAH : {stok}")

    else :
        print("BARANG TIDAK DIEMUKAN")

# cari_barang(buka_data)

# # -------------------------------
# # Fungsi: Tambah barang baru
# # -------------------------------

def tambah_barang(stok_dict):
    kode_baru = input("Masukkan kode barang baru : ").strip()
    if kode_baru in stok_dict :
        print("kode sudah dipakai. update dibatalkan")
        return
    nama_baru = input("masukkan nama barang :").strip()

    try :
        stok_awal = int(input("Masukkan jumlah stok :"))
    except ValueError :
        print("jumlah stok harus integer.")
        return

    stok_dict[kode_baru] = {
        "nama" : nama_baru,
        "jumlah" : stok_awal
    }
    with open(NAMA_FILE, "a", encoding="utf-8") as file :
        file.write(f"{kode_baru},{nama_baru},{stok_awal}\n")

    print("Data berhasil ditambahkan.")

# tambah_barang(buka_data)

# # -------------------------------
# # Fungsi: Update stok barang
# # -------------------------------

def update_stok(stok_dict):
    cari_kode = input("Masukkan kode barang yang ingin di update : ").strip()
    
    if cari_kode not in stok_dict :
        print("Barang tidak ditemukan.Update dibatalkan")
        return
    
    print("=== Pilih jenis Update ===")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    pilihan = input("Masukkan pilihan anda(1/2) : ")

    try :
        ubahan = int(input("Masukkan jumalah : "))
    except ValueError :
        print("Jumlah harus angka.")
        return
    
    stok_lama = stok_dict[cari_kode]["jumlah"]
    
    
    if pilihan == "1" :
        stok_baru = stok_lama + ubahan

    elif pilihan == "2" :
        stok_baru = stok_lama - ubahan
        if stok_baru < 0 :
            print("Hasil tidak boleh negatif.Update dibatalkan")
            return
    else :
        print("Pilihan tidak valid.")
        return
    stok_dict[cari_kode]["jumlah"] = stok_baru

    print("Update berhasil dilakukan")

    with open(NAMA_FILE, "w", encoding="utf-8") as file :
        for kode, data in stok_dict.items() :
             file.write(f"{kode},{data["nama"]},{data["jumlah"]}\n")

# update_stok(buka_data)                           

# -------------------------------
# Program Utama
# -------------------------------

def main():
# Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
            
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_stok(buka_data)
        elif pilihan == "2":
            cari_barang(buka_data)
        elif pilihan == "3":
            tambah_barang(buka_data)
        elif pilihan == "4":
            update_stok(buka_data)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, buka_data)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()