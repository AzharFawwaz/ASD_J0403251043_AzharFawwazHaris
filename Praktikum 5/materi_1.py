#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Contoh Rekursif 1 : Faktorial
#====================================================================

def faktorial(n) :
    # Base case : berhenti ketika n = 0
    if n == 0 : 
        return 1
    
    # recursive case : masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n-1)

print(faktorial(0))
