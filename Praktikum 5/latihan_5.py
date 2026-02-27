#====================================================================
# Nama     : Azhar Fawwaz Haris
# NIM      : J0403251043
# Kelas    : TPL A / P2
#====================================================================

#====================================================================
# Latihan 5 : Generator pin
#====================================================================

def buat_pin(panjang, hasil="") :
    # Base case
    if len(hasil) == panjang :   # jika panjang hasil sama dengan nilai panjang
        print("PIN : ", hasil)   # print "PIN: " dilanjut dengan nilai hasil
        return   # keluar dari fungsi
    
    for angka in ["0", "1", "2"] :   # untuk setiap angka di list
        buat_pin(panjang, hasil + angka)   # panggil fungsi buat_pin dengan hasil yang ditambah dengan variabel dari list

buat_pin(3)

'''
Dsikusi dan penjelasan alur kode :

pertama kita buat base case dimana jika panjang hasik sama dengan batas panjnag pin maka fungsi akan berhenti
setelah itu untuk setiao angka di list,tambahkannangka tersebut ke hasil lalu panggil fungsi lagi
'''
