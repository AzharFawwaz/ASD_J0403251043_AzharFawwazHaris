#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan Sorting : Merge Sort
#====================================================================

#====================================================================
#  Merge Sort Descending
#====================================================================

def mergesort(data) :
    print("Splitting ", data)
    if len(data) > 1 :
        mid = len(data) // 2
        setengahKiri = data[:mid]
        setengahKanan = data[mid:]

        mergesort(setengahKiri)
        mergesort(setengahKanan)

        i = 0
        j = 0
        k = 0

        while i < len(setengahKiri) and j < len(setengahKanan) :
            if setengahKiri[i] >= setengahKanan[j] : # perbedaannya ada di sini, ">" ini untuk descending
                data[k] = setengahKiri[i]
                i = i + 1

            else :
                data[k] = setengahKanan[j]
                j = j + 1
            k = k + 1

        while i < len(setengahKiri) :
            data[k] = setengahKiri[i]
            i = i + 1
            k = k + 1

        while j < len(setengahKanan) :
            data[k] = setengahKanan[j]
            j = j + 1
            k = k + 1
    print("Merging ", data)

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergesort(data)
print(data)