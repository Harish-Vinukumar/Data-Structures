"""
A stack is an abstract data type that serves
as a collection of elements, with two principal
operations: push, which adds an element to the
collection, and pop, which removes the most
recently added element that was not yet removed.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty! Nothing to pop.."
        else:
            current_node = self.head
            prev_node = None
            while current_node.next is not None:
                prev_node = current_node
                current_node = current_node.next

            data = current_node.data
            if prev_node is None:
                self.head = current_node.next
            else:
                prev_node.next = current_node.next

            return data

    def peek(self):
        if self.is_empty():
            return "Stack is empty! Nothing to peek for.."
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            return current_node.data

    def size_of_stack(self):
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


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
print(stack.size_of_stack())
print(stack.display())

print("Popped off stack:\t", stack.pop())
print("Popped off stack:\t", stack.pop())



print(stack.peek())
print(stack.size_of_stack())
print(stack.display())