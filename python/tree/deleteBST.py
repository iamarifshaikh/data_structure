class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarySearch:
    def __init__(self):
        self.root = None
        
    def find_min(self,node):
        current = node
        while current is not None:
            current = current.left
        return current.left

    def delete(self,node,key):
        if self.node is None:
            print(f"No elements to be deleted!")
        else:
            if node.data > key:
                self.delete(node.left,key)
            elif node.data < key:
                self.delete(node.right,key)
            else:
                # Case 1: If Node is a leaf node
                if node.left is None and node.right is None:
                    return None
                
                # Case 2: If Node has only one child
                if node.left is None:
                    return node.right
                
                if node.right is None:
                    return node.left
                
                # Case 3: If Node has two child
                successor = self.find_min(node.right)
                node.data = successor.right
                node.right = self.delete(node.right,successor.right)