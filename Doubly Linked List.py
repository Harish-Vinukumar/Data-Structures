"""
A Doubly linked list is a linear collection of data elements,
whose order is not given by their physical placement
in memory. Instead, each element points to the next and previous.
It is a data structure consisting of a collection
of nodes which together represent a sequence.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the start
    def insert_start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        new_node.prev = current_node
        current_node.next = new_node

    # Insert after a specified node
    def insert_after(self, data, prev_node):
        new_node = Node(data)
        current_node = self.head

        while current_node.data != prev_node:
            current_node = current_node.next

        current_node.next.prev = new_node
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

    # Insert before a specified node
    def insert_before(self, data, next_node):
        new_node = Node(data)
        current_node = self.head

        while current_node.data != next_node:
            current_node = current_node.next

        current_node.prev.next = new_node
        new_node.prev = current_node.prev
        current_node.prev = new_node
        new_node.next = current_node

    # Remove the specified node
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
            current_node.prev = None
        else:
            prev_node.next = current_node.next
            current_node.next.prev = prev_node

    # Traverse the list
    def traverse_list(self):

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


obj = DoublyLinkedList()

obj.insert_start(10)
obj.insert_end(12)
obj.insert_end(11)
obj.insert_end(17)
obj.insert_start(21)
obj.insert_start(40)
obj.insert_after(8, 10)
obj.insert_before(9, 12)
obj.insert_end(100)
print("---------------------")
obj.traverse_list()

obj.remove_node(17)
print("---------------------")
obj.traverse_list()