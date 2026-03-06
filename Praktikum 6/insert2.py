#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan Sorting : Insertion Sort
#====================================================================

#====================================================================
#  Insertion Sort Descending
#====================================================================

def insertsort(data) :
    for index in range(1, len(data)) :

        currentValue = data[index]
        posisi = index

        while posisi < 0 and data[posisi - 1] < currentValue : # perbedaannya ada di sini, "<" ini untuk descending
            data[posisi] = data[posisi - 1]
            posisi = posisi - 1
            data[posisi] = currentValue

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertsort(data)
print(data)