"""
An array is collection of items stored at
contiguous memory locations. The idea is
to store multiple items of same type together.
"""


array = []

# adding an element to a list at specific index
array.insert(0, 10)
array.insert(1, 5)
array.insert(2, 7)
array.insert(3, 2)
array.insert(2, 12)
print(array)

# traversing through array
for x in array:
    print(x)

# removing an element from a list
array.remove(10)
array.remove(7)
print(array)

# removing last element from a list
array.pop()
print(array)

# removing a specific index element from a list
array.pop(1)
print(array)