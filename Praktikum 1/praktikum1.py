#================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#================================================


#Membuka file dalam mode Read("r")
print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print("=== Hasil Read ===")
print("Tipe data : ", type(isi_file))

#Membuka file per baris
print("====Membuka file baris demi baris====")
jumlah_baris = 0 #inisialisas variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file :
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter garis baru
        print("Baris ke-", jumlah_baris)
        print("Isinya : ", baris)

#================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Parsing data
#================================================

#Parsing baris menjadi data satuan
jumlah_baris = 0 #inisialisas variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file :
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("NIM : ", nim, "| Nama : ", nama, "| Nilai : ", nilai) #Menampilkan satuan data dalam bentuk kolom

#========================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca data dan menyimpannya dalam struktur data List
#========================================================================

data_list = []
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file :
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim, nama, int(nilai)]) #Menyimpan data ke list
print("=== Menampilkan List ===")
print(data_list)
print("Contoh record Ke-1", data_list[0])
print("Contoh record Ke-2", data_list[1])

print("Jumlah record : ", len(data_list))

#========================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca data dan menyimpannya ke struktur data dictionary
#========================================================================

data_dict = {} #Inisialisasi dictionary untuk menampung data
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file :
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("=== Menampilkan Data Dictionary ===")
print(data_dict)
