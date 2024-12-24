class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # This function searches for a node with a specified value in a Binary Search Tree(BST).
    def SearchTree(self,root,value):
        # Loop until either the tree is exhausted (None) or the value is found.
        while root is not None and root.value != value:
            """
            Check if the target value is
            less than the current node's value.
            If so, move to the left subtree
            (values smaller than the current node's value).
            Otherwise, move to the right subtree
            (values larger than the current node).
            """
            root = root.left if value < root.value else root.right
        # Return the node containing the target value, if found; otherwise, return None.
        return root

# Function to perform an in-order traversal of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node is None
    if root is None:
        return

    # Recursively call printInOrder for the left subtree
    printInOrder(root.left)

    # Print the value of the current node
    print(root.value, end="")

    # Recursively call printInOrder for the right subtree
    printInOrder(root.right)