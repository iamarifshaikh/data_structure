class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def finding_floor(self,root,key):
        if root is None:
            return
        
        floor = -1

        while root:
            if root.data == key:
                return root.data
            elif key > root.data:
                floor = root.data
                root = root.right
            else:
                root = root.left

        return floor