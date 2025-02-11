class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display():
    temporary = head
    while temporary is not None:
        print(temporary.data, end=" -> ")
        temporary = temporary.next
    print(temporary)
    print()

def removeDuplicates():
    temporary = head
    
    while temporary.next is not None:
        if temporary.data == temporary.next.data:
            temporary.next = temporary.next.next 
        else:
            temporary = temporary.next
    
    return temporary

def circularLinkedList():
    temporary = head
    while temporary.next is not None:
        temporary = temporary.next
    temporary.next = head

head = Node(10)
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(20)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(30)
head.next.next.next.next.next.next = Node(30)

removeDuplicates()
circularLinkedList()
display()
