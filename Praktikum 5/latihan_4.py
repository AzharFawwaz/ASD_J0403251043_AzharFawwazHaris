#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan 4 : Kombinasi Huruf
#====================================================================

def kombinasi(n, hasil = "") :
    # Base case
    if len(hasil) == n :   # Jika panjang variabel hasil sama dengan n
        print(hasil)   # print nilai hasil
        return   # keluar dari fungsi
    
    # Recursive case
    kombinasi(n, hasil + "A")   # tambah "A" ke string lalu lanjut rekursif
    kombinasi(n, hasil + "B")   # tambah "B" ke string lalu lanjut rekursif

kombinasi(2)

'''
Diskusi dan penjelasan alur kode :

pertama kita buat base case dimana jika panjang hasil adalah n, maka fungsi akan mengembalikan nilai hasil
setelah itu fungsi kombinasi akan menambahkan string A sampai panjang stirng mencapai n
setelah itu fungsi kombinasi akan menambahkan string B sampai panjang string mencapai n
'''