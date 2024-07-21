class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addToNode(self,data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        
    def display(self):
        elements = []
        current = self.head
        while current != None:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements )))
        
    def insertAtPosition(self,data,position):
        if position < 0:
            return "Invalid Position"
        
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        current_position = 0
    
        while current is not None and current_position < position -1:
            current = current.next  
            current_position += 1
        
        if current is None:
            return "Position Out Of Bound"
        
        new_node.next = current.next
        current.next = new_node
        
    def reverse(self):
        previous = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        
    def deleteNode(self,value):
        if self.head is None:
            return "The list is empty"
        
        # If the head node contains the value to be deleted
        if self.head.data == value:
            self.head = self.head.next # Move head to the next node
            return "Node deleted"
        
        current = self.head
        previous = None
        
        while current is not None and current.data != value:
            previous = current
            current = current.next
                
        if current is None:
            return "Value not found"
            
        previous.next = current.next
        return "Node deleted"

def createLinkedListWithoutUserInput():
    linked_list = LinkedList()
    for i in range(1,6):
        linked_list.addToNode(i)
    return linked_list            
        
def createLinkedListWithUserInput():
    linked_list = LinkedList()
    while True:
        data = input("Enter a value (or press Enter to finish): ")
        if data == "":
            break
        try:
            data = int(data)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        linked_list.addToNode(data)
    return linked_list
    
if __name__ == "__main__":
    print("Creating a linked list without user input:")
    ll_without_input = createLinkedListWithoutUserInput()
    ll_without_input.display()
    
    print("\nReversing the linked list:")
    ll_without_input.reverse()
    ll_without_input.display()
    
     # Using the deleteNode function
    value_to_delete = 3
    print(f"\nDeleting node with value: {value_to_delete}")
    print(ll_without_input.deleteNode(value_to_delete))
    ll_without_input.display()
    
    # Trying to delete a node that doesn't exist
    # value_to_delete = 10
    # print(f"\nTrying to delete node with value {value_to_delete}:")
    # print(ll_without_input.deleteNode(value_to_delete))
    # ll_without_input.display()