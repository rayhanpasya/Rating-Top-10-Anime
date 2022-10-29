"""
Nama : Muhammad Rayhan Pasyaputra
Kelas : 2IA25
Npm : 51421048
"""

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedLIst:
    def __init__ (self):
        self.head = None

    def append(self, data):
        if self.head is None:

            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = node(data)
            new_node.next = self.head
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def outputan(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

angka_1 = int(input("Masukkan nilai : "))
angka_2 = int(input("Masukkan nilai : "))
angka_3 = int(input("Masukkan nilai : "))

list = DoubleLinkedLIst()
list.append(angka_1)
list.append(angka_2)
list.append(angka_3)

list.outputan()