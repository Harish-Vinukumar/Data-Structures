"""
A linked list is a linear collection of data elements,
whose order is not given by their physical placement
in memory. Instead, each element points to the next.
It is a data structure consisting of a collection
of nodes which together represent a sequence.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # operation 1 : Insert at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        self.size += 1

        new_node.next = self.head
        self.head = new_node

    # operation 2 : Insert at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        self.size += 1

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        else:
            current_node.next = new_node

    # operation 3 : Insert after a particular value of the list
    def insert_after_element(self, data, key):
        new_node = Node(data)
        self.size += 1

        current_node = self.head

        while current_node.data != key:
            current_node = current_node.next
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    # operation 4 : Remove an element from the list
    def remove_from_list(self, data):

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

    # operation 5 : Traverse through the list
    def traverse_the_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next


list_1 = LinkedList()

list_1.insert_at_start(10)
list_1.insert_at_start(12)
list_1.insert_at_end(122)
list_1.insert_at_end(31)
list_1.insert_at_start(57)
list_1.insert_after_element(8, 10)
list_1.insert_after_element(9, 10)
print("---------")
list_1.traverse_the_list()

list_1.remove_from_list(122)
list_1.remove_from_list(57)
print("---------")
list_1.traverse_the_list()