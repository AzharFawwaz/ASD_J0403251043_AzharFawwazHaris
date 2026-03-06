#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan Sorting : Shell Sort
#====================================================================

#====================================================================
#  Shell Sort Ascending
#====================================================================

def masukJarak(data, start, gap) :
    for i in range(start + gap, len(data), gap) :

        currentValue = data[i]
        posisi = i

        while posisi >= gap and data[posisi - gap] > currentValue : # perbedaannya ada di sini, ">" ini untuk ascending
            data[posisi] = data[posisi - gap]
            posisi = posisi - gap

        data[posisi] = currentValue


def shellsort(data) :
    itungsub = len(data)//2
    while itungsub > 0 :

        for posAwal in range(itungsub) :
            masukJarak(data, posAwal, itungsub)

        print("Setelah penambahan ukuran", itungsub,
                                        "List data", data)
        
        itungsub = itungsub // 2

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellsort(data)
print(data)
        