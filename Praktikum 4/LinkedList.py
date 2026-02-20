#===================================================================================
# Nama : Azhar Fawwaz Haris
# NIM : J0403251043
# Kelas : TPL A2
#===================================================================================

#===================================================================================
# Implementasi Dasar : Node pada Linked List
#===================================================================================

class node :
    # Konstruktor adalah fungsi yang dijalankan secara otomatif ketika class node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data paa list
        self.next = None # Menunjuk ke node berikutnya (awal = None)

# 1) membuat node dengan instantiasi class node
nodeA = node("A")
nodeB = node("B")
nodeC = node("C")

# 2)  Mendefinisikan head dan Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# 4) Traversl : Menelusuri node dari head sampai ke None
current = head
while current is not None :
    print(current.data) # Menampilkan data pda node saat ini
    current = current.next # Pindah ke node berikutnya

