#===================================================================================
# Nama : Azhar Fawwaz Haris
# NIM : J0403251043
# Kelas : TPL A2
#===================================================================================

#===================================================================================
# Implementasi Dasar : Stack (Last in First out)
#===================================================================================

class node :
    # Konstruktor adalah fungsi yang dijalankan secara otomatif ketika class node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data paa list
        self.next = None # Menunjuk ke node berikutnya (awal = None)

# Stack ada operasi Push(Memasukkan head baru) dan Pop(Menghapus head)
# A -> B -> C -> None

class stack :
    def __init__(self, data):
        self.top = None # Top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self) :
        return self.top is None # Stack kosong jika top = None

    def push(self, data) : # Memasukkan data baru pada stack
        # 1 Membuat node baru
        NodeBaru = node(data) # Instantiasi/memanggil konstruktor pada class Node

        # 2 Node baru menunjuk ke top yang lama (head lama)
        NodeBaru.next = self.top

        # 3 Geser top pindah ke node baru
        self.top = NodeBaru

    def pop(self) : # Mengambil/menghapus node paling atas (Top/head)
        if self.top == None :
            print("Stack kosong, tidak bisa pop")
            return None


        data_terhapus = self.top.data # soroti dbagian top dan simpan di variabel
        self.top = self.top.next
        return data_terhapus
    
    def peek(self) :
        # Melihat data yang paling atas tanpa menghapus
        if self.is_empty() :
            return None
        return self.top.data

    def Tampilkan(self) :
        # Top -> A -> B
        current = self.top
        print("Top -> ", end=" ")
        while current is not None :
            print(current.data, end="->")
            current = current.next
        print("None")

# Instantiasi class Stack
s = stack(None)
s.push("A")
s.push("B")
s.push("C")
print("Peek (lihat Top) : ", s.peek())
s.pop()
s.Tampilkan()
s.pop()
s.Tampilkan()
print("Peek (lihat Top) : ", s.peek())

print("Data terhapus : ", s.pop())
s.Tampilkan()