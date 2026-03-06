#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan Sorting : Bubble Sort
#====================================================================

#====================================================================
#  Bubble Sort Descending
#====================================================================

def shortBUbbleSort(list) :
    exchanges = True
    passnum = len(list) -1
    while passnum > 0 and exchanges : 
        exchanges = False
        for i in range(passnum) :
            if list[i] < list[i+1] : # perbedaannya ada di sini, "<" ini untuk descending
                exchanges = True
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        passnum = passnum - 1

list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110 ]
shortBUbbleSort(list)
print(list)
