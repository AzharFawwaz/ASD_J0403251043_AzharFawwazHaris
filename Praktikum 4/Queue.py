#===================================================================================
# Nama : Azhar Fawwaz Haris
# NIM : J0403251043
# Kelas : TPL A2
#===================================================================================

#===================================================================================
# Implementasi Dasar : Queue (First in First out)
#===================================================================================


class node :
    # Konstruktor adalah fungsi yang dijalankan secara otomatif ketika class node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data paa list
        self.next = None # Menunjuk ke node berikutnya (awal = None)

class Queue :
    # Buat Konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None # Node paling belakang

    def is_empty(self) :
        return self.front is None

    # Membuat fungsi untuk menambahkan data baru pada bagian belakang
    def enqueue(self, data) :
        NodeBaru = node(data)

        # Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty() :
            self.front = NodeBaru
            self.rear = NodeBaru
            return
        
        # Jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = NodeBaru # Letakkan data baru pada setelahnya rear
        self.rear = NodeBaru # Jadikan data baru sebagai rear

    def dequeue(self) :
        # Menghapus data dari depan/front
        data_terhapus = self.front.data # Lihat data paling depan
        self.front = self.front.next # geser front ke node berikutnya

        # Jika setelah geser front menjadi None, maka queue kosong
        # rear juga harus jadi None
        if self.front is None :
            self.rear = None

    def tampilkan(self) :
        current = self.front
        print("Front ->", end=" ")
        while current is not None :
            print(current.data, end="->")
            current = current.next
        print("Rear")

# Instantiasi class queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()

# print("Data terhapuskan : ", q.dequeue())
# q.tampilkan()

