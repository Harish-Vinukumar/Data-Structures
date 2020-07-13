"""
A binary search tree, also called an ordered
or sorted binary tree, is a rooted binary tree
whose internal nodes each store a key greater
than all the keys in the node's left subtree
and less than those in its right subtree.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data)

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.left:
            return self.get_min(node.left)
        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right:
            return self.get_max(node.right)
        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)
        print(node.data)
        if node.right:
            self.traverse_in_order(node.right)

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self.remove_node(data, node.left)
        elif data > node.data:
            node.right = self.remove_node(data, node.right)
        else:
            if not node.left and not node.right:
                print("Removing the Leaf Node")
                del node
                return None
            if not node.left:
                print("Removing the node with 1 right child node")
                temp_node = node.right
                del node
                return temp_node
            elif not node.right:
                print("Removing the node with 1 left child node")
                temp_node = node.left
                del node
                return temp_node

            print("Removing the node with 2 children nodes")
            temp_node = self.get_predecessor(node.left)
            node.data = temp_node.data
            node.left = self.remove_node(temp_node.data, node.left)

        return node

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node


bst = BinarySearchTree()

bst.insert(10)
print(bst.get_max_value())
print(bst.get_min_value())
bst.insert(5)
bst.insert(15)
bst.insert(11)
bst.insert(1)
bst.insert(26)

bst.traverse()

bst.remove(10)
bst.remove(5)

bst.traverse()



