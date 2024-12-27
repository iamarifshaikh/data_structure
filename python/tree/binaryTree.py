from collections import deque

class Node:
    """
    Represents a node in the Binary Search Tree.
    Each node contains data, a left child, and a right child.
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
        If the root is None, the new value becomes the root.
        Otherwise, it inserts the value in the appropriate position.
        """
        if self.root is None:
            self.root = Node(data)  
        else:
            self._insert_recursively(self.root,data)

    def _insert_recursively(self,node,data):
        if data < node.data: #Smaller values go to the left
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left,data)
        elif data > node.data: # Larger values go to the right
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right,data)
        else:
            print(f"Value {data} already exists in the tree. No duplicates allowed!")

    def search(self,data):
        """
        Searches for a value in the BST.
        Returns True if the value exists, False otherwise.
        """
        return self._search_recursively(self.root,data)

    def _search_recursively(self,node,data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursively(node.left,data) # Search Left Sub Tree
        else:
                return self._search_recursively(node.right,data) # Search Right Sub Tree

    def inorder(self):
        """Public method to initiate inorder traversal and return the result."""
        result = []
        self._inorder_traversal(self.root,result)
        return result

    def _inorder_traversal(self,node,result):
        """Recursive helper function for inorder traversal."""
        if node is not None:
            self._inorder_traversal(node.left,result)
            result.append(node.data) # Visit the node
            print(node.data, end=" ")
            self._inorder_traversal(node.right,result)

    def preorder(self):
        """Public method to initiate preorder traversal and return the result."""
        result = []
        self._preorder_traversal(self.root,result)
        return result

    def _preorder_traversal(self,node,result):
        """Recursive helper function for preorder traversal."""
        if node is not None:
            result.append(node.data) # Visit the node
            print(node.data, end=" ")
            self._preorder_traversal(node.left,result)
            self._preorder_traversal(node.right,result)

    def postorder(self):
        """Public method to initiate postorder traversal and return the result."""
        result = []
        self._postorder_traversal(self.root,result)
        return result

    def _postorder_traversal(self,node,result):
        """Recursive helper function for postorder traversal."""
        if node is not None:
            self._postorder_traversal(node.left,result)
            self._postorder_traversal(node.right,result)
            result.append(node.data) # Visit the node
            print(node.data, end=" ")

    def level_order_traversal(self):
        """Public function to perform level-order traversal and group by levels"""
        if self.root is None:
            return []
        return self._level_order_traversal(self.root)

    def _level_order_traversal(self, start_node):
        """Actual function performing level-order traversal grouped by levels"""
        result = []
        queue = deque([start_node])  # Start with the initial node
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = []  # List to store the current level's values
            
            for _ in range(level_size):
                current = queue.popleft()
                level.append(current.data)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            result.append(level)  # Add the level to the final result
        
        return result

if __name__ == "__main__":
    # Initialize a binary search tree
    bst = BinaryTree()

    # Insert nodes
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(18)
    bst.insert(12)

    print("Postorder Traversals: ")
    bst.postorder()
    print("\nPreorder Traversals: ")
    bst.preorder()
    print("\nInorder Traversals: ")
    bst.inorder()
    print("\nLevel Order Traversal: ")
    print(bst.level_order_traversal())