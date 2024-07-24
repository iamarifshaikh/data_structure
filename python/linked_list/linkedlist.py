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

    def findMiddleUsingTwoPointers(self):
        if self.head is None:
            return "List is empty"
        
        slow = self.head
        fast = self.head 
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
        
    def findMiddleUsingTwoPass(self):
        if self.head is None:
            return "List Is Empty!"
        
        length = 0
        current = self.head
        
        #First Pass: Count the nodes
        while current is not None:
            length += 1
            current = current.next
            
        #Second Pass: Move to the middle
        middle_element = length // 2
        current  = self.head
        for i in range(middle_element):
            current = current.next
            
        return current.data
    
    
    def hasCycle(self):
        if self.head is None and self.head.next is None:
            return False
        
        slow = self.head
        fast = self.head.next
        
        while slow!=fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        
def mergeSortedList(list1,list2):
        start = Node(0)
        current = start
        
        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
             # If one list is exhausted, append the remainder of the other list
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return start.next  # Return the actual head of the merged list

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
    
    # Helper function to create a sorted linked list from a list of values
def create_sorted_linked_list(values):
    ll = LinkedList()
    for value in sorted(values):
        ll.addToNode(value)
    return ll
    
if __name__ == "__main__":
    list1 = create_sorted_linked_list([1, 3, 5])
    list2 = create_sorted_linked_list([2, 4, 6, 8, 10])
    
    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()

    # Merge the lists
    merged_head = mergeSortedList(list1.head, list2.head)

    # Create a new LinkedList object with the merged head
    merged_list = LinkedList()
    merged_list.head = merged_head
    
    print("Merged list:")
    merged_list.display()
    
    print("Creating a linked list without user input:")
    ll_without_input = createLinkedListWithoutUserInput()
    ll_without_input.display()