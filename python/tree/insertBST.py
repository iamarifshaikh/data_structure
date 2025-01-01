class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data,node=None):
        if self.root is None:
            self.root = Node(data)
        else:
            if node is None:
                node = self.root
            
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.insert(data,node.left)
            
            if data > node.data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.insert(data,node.right)