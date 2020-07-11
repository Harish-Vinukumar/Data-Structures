"""
A queue is an abstract data type that serves
as a collection of elements, with two principal
operations: enqueue, which adds an element to the
collection, and dequeue, which removes the very
first element that was not yet removed.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty! Nothing to dequeue.."
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

    def peek(self):
        if self.is_empty():
            return "Queue is empty! Nothing to peek for.."
        else:
            return self.queue[0]

    def size_of_queue(self):
        return len(self.queue)

    def display(self):
        return self.queue


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