class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList :
    def __init__(self, data):
        self.head = None

    def append(self, data) :
        new_node = Node(data)
        if not self.head :
            self.head = new_node
            return
        
        temp = self.head
        while temp.next :
            temp = temp.next
        temp.next = new_node

    def display(self) :
        temp = self.head

        while temp :
            print(temp.data, end="->")
            temp = temp.next

        print("Null")

    def reverse(self) :
        prev = None
        temp = self.head

        while temp :
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev


try :

    input_data = input("Masukkan elen untuk LInked List(Pisahkan setiap elemen dengan koma ',') : ")
    if "," not in input_data :
        raise ValueError("Input harus dipisahkan dengan koma(,). ")
    
    elemen = [int(x.strip()) for x in input_data.split(",")]

    ll = LinkedList(None)

    for el in elemen :
        ll.append(el)

    print("Linked List sebelum di revese : ", end=" ")
    ll.display()

    print("Linked List setelah di revese : ", end=" ")
    ll.reverse()
    ll.display()

except ValueError as e :
    print("Terjadi kesalahan : ", e)