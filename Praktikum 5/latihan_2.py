#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan 2 : Tracing Rekursif
#====================================================================

def countdown(n) :
    # Base case
    if n == 0 :   # jika n adalah 0
        print("selesai")   # cetak "Selesai"
        return   # Keluar dari fungsi
    
    # Recursive base
    print("Masuk : ", n) # fase stacking 

    countdown(n - 1)   # pemanggilan fungsi sampai base case tercapai

    print("Keluar : ", n)   # fase unwiding

countdown(3)

'''
Diskusi dan penjelasan alur program : 

saat fungsi memanggil dirinya sendiri call stack bertambah 
lalu setelah base case tercapai maka fungsi akan kembali satu persatu.
'''