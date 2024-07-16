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
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements )))

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
        linked_list.addToNode(data)
    return linked_list
    
if __name__ == "__main__":
    print("Creating a linked list without user input:")
    ll_without_input = createLinkedListWithoutUserInput()
    ll_without_input.display()
    
    print("\nCreating a linked list with user input:")
    ll_with_input = createLinkedListWithUserInput()
    ll_with_input.display()