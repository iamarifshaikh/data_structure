class Node:
    """
    Represent a node in the binary search tree &
    Each node contains the left and right child
    """
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        """
        Insert a value into the binary search tree
        If the root is none insert the value intot the root
        Otherwise insert the value into the appropriate position
        """
        if self.root is not None:
            self._insert_recursively(self.root,data)
        else:
            self.root = Node(data)
            
    def _insert_recursively(self,node,data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left,data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right,data)
        else:
            print(f"Value {data} already exists in the tree. No duplicates allowed!")   