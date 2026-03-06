#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan Soal Pengurutan
#====================================================================

skor = [43, 76, 12, 89, 33, 57, 98, 68, 9]

def bubble(data) :
    n = len(data)
    for i in range(n) :
        for j in range (0, n-i-1) :
            if data[j] < data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]

    print("Urutan nilai dari paling tinggi ke paling rendah : ",data)
    top5 = data[:5]
    print("5 nilai paling besar : ",top5)
    print("Selamat kepada kandidat dengan nilai ", top5, " Karena dinyatakan lolos seleksi pak budi.🥳🥳🥳")

bubble(skor)


        