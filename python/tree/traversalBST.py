from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self,node,result):
        result = []

        if node is not None:
            result.append(node.data)
            print(node.data, end=" ")
            self.preorder_traversal(node.left,result)
            self.preorder_traversal(node.right,result)

    def inorder_traversal(self,node, result):
        result = []
        if node is not None:
            self.inorder_traversal(node.left,result)
            result.append(node.data)
            print(node.data, end=" ")
            self.inorder_traversal(node.right,result)

    def postorder_traversal(self,node,result):
        result = []

        if node is not None:
            self.postorder_traversal(node.left,result)
            self.postorder_traversal(node.right,result)
            result.append(node.data, end=" ")
            print(node.data, end=" ")

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

    def iterative_preorder_traversal(self,root):
        preorder = []

        if root is None:
            return preorder

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            preorder.append(node.data)
            print(node.data, end=" ")

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return preorder

    def iterative_inorder_traversal(self,root):
        result = []
        stack = []
        current = root

        if root is None:
            return stack

        while current is not None or stack is not None:
            
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current)

            current = current.right
        
        return result

    def iterative_postorder_traversal(self):
        pass