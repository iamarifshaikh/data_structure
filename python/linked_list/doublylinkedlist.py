import gc
class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self,data):
        new_node = Node(data)
            
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        
        while current.next:
            current = current.next
        
        current.next = new_node
        
        new_node.previous = current
                
        return
            
    def insertAtBeggining(self,data):
        new_node = Node(data)
        
        if self.head is None:
            # List is empty, so the new node becomes the head
            self.head = new_node
            return "Node Inserted At The Begining"
        else:
            # List is not empty, insert the new node at the beginning
            new_node.next = self.head
            self.head = new_node
            self.head.previous = new_node
        return "Node Inserted At The Begining"
                  
    def insertAtPosition(self,data,position):
        if position < 0:
            return "Invalid Position"
        
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.previous = new_node
            self.head = new_node
            return "Node Inserted At Position 0"
        
        current = self.head
        current_position = 0
        
        while current is not None and current_position < position -1:
            current = current.next
            current_position += 1
        
        if current is None:
            return "Theres no node in the list"
        
        new_node.next = current.next
        if current.next:
            current.next.previous = new_node    

    def reverse(self):
        current = self.head
        previous = None
        
        while current is not None:
            reverse_list_node = current.next
            current.next = previous
            current.previous = reverse_list_node  
            previous = current
            current = reverse_list_node
            
        # Update the head of the list
        self.head = previous