#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Contoh Rekursif 3 : Menjumlahkan elemen list
#====================================================================

def jumlah_list(data, index=0) :
    # base case : jika index sudah mencapai panjang list
    if index == len(data) :
        return 0
    
    # recursive case : elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([2,4,6,8])) # output : 20