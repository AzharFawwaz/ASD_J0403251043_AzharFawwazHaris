#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan Sorting : Quick Sort
#====================================================================

#====================================================================
#  Quick Sort Ascending
#====================================================================

def quickSort(data) :
    tolong(data, 0, len(data)-1)

def tolong(data, fisrt, last) :
    if fisrt < last :
        titikBelah = partisi(data, fisrt, last)
        tolong(data, fisrt, titikBelah - 1)
        tolong(data, titikBelah +1, last)

def partisi(data, first, last) :
    nilaiPivot = data[first]

    tandakiri = first + 1
    tandakanan = last

    done = False
    while not done :

        while tandakiri <= tandakanan and data[tandakiri] <= nilaiPivot : # "<=" dan "<=" untuk ascending
            tandakiri = tandakiri + 1

        while data[tandakanan] >= nilaiPivot and tandakanan >= tandakiri :  # ">=" dan ">=" untuk ascending
            tandakanan = tandakanan - 1

        if tandakanan < tandakiri :
            done = True
        else :
            temp = data[tandakiri]
            data[tandakiri] = data[tandakanan]
            data[tandakanan] = temp

    temp = data[first]
    data[first] = data[tandakanan]
    data[tandakanan] = temp

    return tandakanan

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(data)
print(data)