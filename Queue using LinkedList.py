"""
A queue is an abstract data type that serves
as a collection of elements, with two principal
operations: enqueue, which adds an element to the
collection, and dequeue, which removes the very
first element that was not yet removed.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty! Nothing to dequeue.."
        else:
            data = self.head.data
            current_node = self.head
            self.head = current_node.next

            return data

    def peek(self):
        if self.is_empty():
            return "Queue is empty! Nothing to peek for.."
        else:
            return self.head.data

    def size_of_queue(self):
        counter = 0
        current_node = self.head
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter

    def display(self):
        print_list = list()
        current_node = self.head
        while current_node is not None:
            print_list.append(current_node.data)
            current_node = current_node.next

        return print_list


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.peek())
print(queue.size_of_queue())
print(queue.display())

print("Dequeued off queue:\t", queue.dequeue())
print("Dequeued off queue:\t", queue.dequeue())

print(queue.peek())
print(queue.size_of_queue())
print(queue.display())