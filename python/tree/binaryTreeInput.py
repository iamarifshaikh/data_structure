from collections import deque

class Node:
    """
    Represet a node in the binary search tree.
    Each node contains the data,left child and right child
    """
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    # Represents the root of the tree
    def __init__(self):
        self.root = None

    def insert(self,data,node=None):
        if self.root is None:
            self.root = Node(data)
        else:
            if node is None:
                node = self.root

            if data < node.data: # Insert in the left subtree
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.insert(data,node.left)

            elif data > node.data: 
                if node.right is None:
                    node.right = Node(data) # Insert in the right subtree
                else:
                    self.insert(data,node.right)

            else:
                print(f"Value {data} is already present in the Tree.")

    def search(self,data,node):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self.search(data, node.left)
        elif data > node.data:
            return self.search(data,node.right)
        else:
            return f"Key: {data}, is not present in the Binary Search Tree."
    
    def find_min(self,node):
        current = node
        while current is not None:
            current = current.left
        return current.left

    def delete(self,node,key):
        if self.root is None:
            print(f"No elements to be deleted!")
        else:
            if node.data > key:
                self.delete(node.left,key) # Search in the left BST.
            elif node.data < key:
                self.delete(node.right,key)
            else:
                # Case:1 Node is a leaf node.
                if node.left is None and node.right is None:
                    return None
                
                # Case 2: Node has only one child.
                if node.left is None:
                    return node.right
                
                if node.right is None:
                    return node.left
                
                # Case 3: Node has two children
                successor = self.find_min(node.right)
                # Replace the node's data with the successor's data
                node.data = successor.data
                # Delete the successor node
                node.right = self.delete(node.right,successor.data)

        return node

    def inorder(self,node,result):
        if node is not None:
            self.inorder(node.left,result)
            result.append(node.data)
            print(node.data, end=" ")
            self.inorder(node.right,result)

    def preorder(self,node,result):
        if node is not None:
            result.append(node.data)
            print(node.data, end=" ")
            self.preorder(node.left,result)
            self.preorder(node.right,result)
    
    def postorder(self,node,result):
        if node is not None:
            self.postorder(node.left,result)
            self.postorder(node.right,result)
            result.append(node.data)
            print(node.data,end=" ")
    
    def level_order_traversal(self,root):
        if self.root is None:
            return []
        
        result = []

        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                current = queue.popleft()
                level.append(current)

                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

            result.append(level)

        return result
    
    def find_floor(self,root,key):
        if root is None:
            return
        
        floor = -1
        # Here root (parameter/variable): A temporary reference to the current node being processed.
        # It starts as self.root in most cases but changes context as you move through the tree (either left or right).
        while root:
            if root.data == key:
                floor = root.data
                return floor
            elif key > root.data:
                # Update the floor with the current node's value and move to the right subtree
                floor = root.data
                root = root.right
            else:
                # If the key is smaller than the current's node value then move to the left subtree
                root = root.left

        # Return the computed floor value
        return floor

def main():
    bst  = BinaryTree()

    while True:
        print("\n\t 1.INSERT\n\t 2.SEARCH\n\t 3.DELETE\n\t 4.INORDER TRAVERSAL\n\t 5.PRE-ORDER TRAVERSAL \n\t 6.POST-ORDER TRAVERSAL \n\t 7.LEVEL ORDER TRAVERSAL \n\t 8. FIND YOUR FLOOR VALUE")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value to insert in the tree: "))
            bst.insert(value)
        elif choice == 2:
            key = int(input("Enter the value you are looking for: "))
            if bst.search(key,bst.root):
                print(f"Value {key} exist in the tree!")
            else:
                print(f"Value {key} is not present in the tree!")
        elif choice == 3:
            key = int(input("Which node you want to delete?"))
            bst.root = bst.delete(bst.root,key)
        elif choice == 4:
            print("\nInorder Traversals: ")
            bst.inorder(bst.root, [])
        elif choice == 5:
            print("\nPreorder Traversals: ")
            bst.preorder(bst.root, [])
        elif choice == 6:
            print("\nPostorder Traversals: ")
            bst.postorder(bst.root, [])
        elif choice == 7:
            print("\Level Order Traversals: ")
            bst.level_order_traversal()
        elif choice == 8:
           key = int(input("\nEnter the key number: "))
           floor_value = bst.find_floor(bst.root, key)
           if floor_value is not None:
                print(f"The floor value for the {key} is {floor_value}")
           else:
                print(f"No floor exists for {key} in the tree.")
        else:
            print("Exiting Program!")
            break

if __name__ == "__main__":
    main()