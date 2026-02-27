#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan 3 : Mencari Nilai Maksimum
#====================================================================

def cari_maks(data, index=0) :
    # Base case
    if index == len(data) - 1 :   # Jika index sudah mencapai jumlah panjang data
        return data[index]   # mengembalikan nilai data ke-index
    
    # Recursive case
    Maks_sisa = cari_maks(data, index + 1)   # buak variabel untuk menampung nilai maksimum dari sisa index sekarang

    if data[index] > Maks_sisa :   # jika data ke index lebih besar dari variabel
        return data[index]   # Mengembalikan nilai data ke-index
    else :   # jika kondisi if tidak terpenuhi
        return Maks_sisa   # Mengembalikan nilai variabel
    
angka = [3, 7,2, 9, 5]
print("Nilai Maksimum : ", cari_maks(angka))

'''
Diskusi dan penjelasan alur program :

pertama kita buat bas case dulu supaya fungsi memili titik akhir
setelah itu kita akan membuat variabel untuk menampung nilai index terbesar saat ini
setelah itu kita akan terus membandingkan nilai di variabel tersebut ke sisa index yang tersisa
jika nilai variabel lebih kecil dari index yang di cek, maka nilai variabel akan berganti menjadi nilai yang di cek
jika nilai variabel lebih besar dari index yang di cek maka akan terus llanjur mengecek index selanjutnya

'''