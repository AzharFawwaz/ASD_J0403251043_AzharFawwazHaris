class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList :
    def __init__(self, data):
        self.head = None
        self.tail = None

    def insert_at_end(self, data) :
        new_node = Node(data)

        if not self.head :
            self.head = new_node
            self.tail = new_node

        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self) :
        print("\nTraversing Forward :")
        temp = self.head

        while temp :
            print(temp.data, end="->")
            temp = temp.next
        print("Null")

    def display_backward(self) :
        print("\nTraversing Backward :")
        temp = self.tail
        while temp :
            print(temp.data, end="->")
            temp = temp.prev
        print("Null")

    def search(self, key) :
        if self.head is None :
            print("Doubly Linked List kosong. Tidak ada yang bisa dicari")
            return False
        
        temp = self.head
        while temp :
            if temp.data == key :
                print(f"Elemen {key} ditemukan dalam Doubly Linked List")
                return True
            temp = temp.next
        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List")
        return False
    
    def delete_node(self, key) :
        temp = self.head

        if temp and temp.data == key :
            self.head = temp.next
            temp = None
            return
        prev = None

        while temp and temp.data != key :
            prev = temp
            temp = temp.next
        if temp is None :
            return
        prev.next = temp.next
        temp = None

dll = DoublyLinkedList(None)

dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)
dll.display_forward()
dll.display_backward()

print("\n=== Tampilan 1 ===")
dll.search(9)

print("\n=== Tampilan 2 ===")
dll.search(100)

dll.delete_node(2)
dll.delete_node(6)
dll.delete_node(9)
dll.delete_node(14)
dll.delete_node(20)

print("=== Tampilan 3 ===")
dll.display_forward()

dll.search(9)
