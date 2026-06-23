class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end = " -> ")
            current = current.next

        print("None")

    def count_nodes(linked_list):
        count = 0 
        current = linked_list.head

        while current:
            count += 1
            current = current.next

        return count

# TESTE
lista = LinkedList()

lista.append(10)
lista.append(20)
lista.append(30)
lista.append(50)
lista.print_list()

print("Números de nós:", count_nodes(lista))