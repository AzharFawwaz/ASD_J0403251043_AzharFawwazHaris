#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan 1 : Rekursi Pangkat
#====================================================================

def pangkat(a, n) :
    # Base case
    if n == 0 :   # jika n adalah 0
        return 1   # keluar dari fungsi dengan mengembalikan nilai 1
    
    # Recursive case
    return a * pangkat(a, n-1) # keluar fungsi dengan mengembalikan nilai a dikali funsi pangkat yang nilai n nya sudah dikurangi 1 dari nilai awal

print(pangkat(2, 4))

'''
Diskusi dan penjelasan alur program : 

pertama kita mendifisikan base case yaitu n == 0 suoaya fungsi nya memiliki titik akhir.
setelah itu fungsi akan terus memanggil dirinya sendiri hingga mencapai base case.


'''