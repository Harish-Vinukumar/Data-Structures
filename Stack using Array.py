"""
A stack is an abstract data type that serves
as a collection of elements, with two principal
operations: push, which adds an element to the
collection, and pop, which removes the most
recently added element that was not yet removed.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return "Stack is empty! Nothing to pop.."
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

    def peek(self):
        if self.is_empty():
            return "Stack is empty! Nothing to peek for.."
        else:
            return self.stack[-1]

    def size_of_stack(self):
        return len(self.stack)

    def display(self):
        return self.stack


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
print(stack.display())

print(stack.peek())
print(stack.size_of_stack())