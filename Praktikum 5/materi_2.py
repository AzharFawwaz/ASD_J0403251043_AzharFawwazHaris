#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Contoh Rekursif 2 : Tracing masuk/keluar
#====================================================================

def hitung(n) :
    # base case
    if n == 0 :
        print("Selesai")
        return
    
    print("Masuk : ", n)        # Fase stacking
    hitung(n-1)                 # Pemanggilan rekursif
    print("Keluar : ", n)       # Fase unwiding

hitung(3)