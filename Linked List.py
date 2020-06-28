"""
A linked list is a linear collection of data elements,
whose order is not given by their physical placement
in memory. Instead, each element points to the next.
It is a data structure consisting of a collection
of nodes which together represent a sequence.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Insert node at the start
    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert node at the last
    def insert_at_last(self, data):
        new_node = Node(data)

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    # Insert node at the after a specified value
    def insert_after(self, data, prev_data):
        new_node = Node(data)
        current_node = self.head

        while current_node.data != prev_data:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    # Remove a specified value from the list
    def remove_node(self, data):

        if self.head is None:
            return

        current_node = self.head

        prev_node = None
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if prev_node is None:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next

    # Traverse the list
    def traverse_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

obj = LinkedList()
obj.insert_at_start(10)
obj.insert_at_last(12)
obj.insert_at_last(11)
obj.insert_at_last(17)
obj.insert_at_start(21)
obj.insert_at_start(40)
obj.insert_after(8, 10)
print("---------------------")
obj.traverse_list()

obj.remove_node(17)
print("---------------------")
obj.traverse_list()