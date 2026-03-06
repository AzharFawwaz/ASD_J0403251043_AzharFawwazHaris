#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan Sorting : Selection Sort
#====================================================================

#====================================================================
#  Selection Sort Descending
#====================================================================

def selectionSort(data) :
    for fillslot in range(len(data)-1, 0, -1) :
        minPosition = 0
        for location in range(1, fillslot+1) :
            if data[location] < data[minPosition] : # perbedaannya ada di sini, "<" ini untuk descending
                minPosition = location

        # Swap

        temp = data[fillslot]
        data[fillslot] = data[minPosition]
        data[minPosition] = temp

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(data)
print(data)