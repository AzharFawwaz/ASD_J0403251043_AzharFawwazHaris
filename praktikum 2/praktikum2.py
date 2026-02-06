#================================================
#Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 1 : Membuat fungsi load dari data
#================================================


nama_file = "data_mahasiswa.txt"

def baca_data(nama_file) :
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file :
        for baris in file :
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            data_dict[nim] = {"nama" : nama, "nilai" : int(nilai)}
    return data_dict

buka_data = baca_data(nama_file)
#print("jumlah data terbaca : ", len(buka_data))

#================================================
#Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 2 : Menampilkan data
#================================================

def tampilan_data(data_dict) :
    print("\n===DAFTAR MAHASISWA===")
    print(f"{'nim' : <10} | {'nama' : <12} | {'nilai' : >5}")
    print("-"*35)

    for nim in sorted(data_dict.keys()) :
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {nilai : >5}")

#tampilan_data(buka_data)

#================================================
#Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 3 : Membuat fungsi mencari data
#================================================

def cari_data(data_dict) :
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat inout nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan nim mahasiswa yang ingin dicari : ").strip().title()

    if nim_cari in data_dict :
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM : {nim_cari} ")
        print(f"NAMA : {nama} ")
        print(f"NILAI : {nilai} ")
    else :
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

#cari_data(buka_data)

#================================================
#Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 4 : Membuat fungsi Update Data
#================================================

def ubah_data(data_dict) :
    #awali dengan mencari NIM/data mahasiswa yang ingi di updat
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya : ").strip()
    if nim not in data_dict :
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai yang baru : ").strip())
    except ValueError :
        print("Masukkan inout berupa integer")
        return
    if nilai_baru <0 or nilai_baru >100 :
        print("Rentang nilai hanya 0 - 100. Update dibatalkan")
        return
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
    tampilan_data(data_dict)
#ubah_data(buka_data)

#================================================
#Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 5 : Membuat fungsi Simpan Data
#================================================

def simpan_data(nama_file, data_dict) :
    with open(nama_file, "w", encoding="utf-8") as file :
        for nim in sorted(data_dict.keys()) :
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai} \n")

simpan_data(nama_file, buka_data)
#print("\nData Berhasil disimpan ke file : ", nama_file)

#================================================
#Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 5 : Membuat fungsi Simpan Data
#================================================

def main() :
    buka_data = baca_data(nama_file)

    while True :
        print("\n===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari data berdasarkan NIM")
        print("3.Ubah nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1" :
            tampilan_data(buka_data)
        elif pilihan == "2" :
            cari_data(buka_data)
        elif pilihan == "3" :
            ubah_data(buka_data)
        elif pilihan == "4" :
            simpan_data(nama_file, buka_data)
            print("Data Berhasil Disimpan")
        elif pilihan == "0" :
            print("Program Selesai")
            break
        else :
            print("Pilihan tidak valid")

if __name__=="__main__":
    main()