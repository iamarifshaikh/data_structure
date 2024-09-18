class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addNode(self,data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current is not None:
            current = current.next
        current.next = new_node
        
    def display(self):
        element = []
        current = self.head
        
        while current is not None:
            element.append(current)
            current = current.next
        print(" -> ".join(map(str, element)))
        
    def deleteNode(self,data):
        pass