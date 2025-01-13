class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Function to search a key in the BST
    def search(self,root, key):
        # Base Cases: root is null or key is present at root
        if root is None or root.key == key:
            return root

        # Key is greater than root's key
        if root.key < key:
            return self.search(root.right,key) 

        # Key is less than root's key
        return self.search(root.left,key)
    
if __name__ == '__main__':
    bst = BinarySearchTree()