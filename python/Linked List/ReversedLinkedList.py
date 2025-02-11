class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display():
    temporary = head
    while temporary is not None:
        print(temporary.data, end=" -> ")
        temporary = temporary.next
    print()

def reverse():
    previous = None
    current = head
    while current is not None:
        next_element = current.next
        current.next = previous
        previous = current
        current = next_element
    return previous

def nthnode(n=3):
    slow = head
    fast = head
    
    temporary  = 0
    
    while temporary <= n:
        fast = fast.next
        temporary += 1
        
    while fast is not None:
        slow = slow.next
        fast = fast.next
    
    print(slow.data)

def addToNode():
    temporary = head
    while temporary.next is not None:
        temporary = temporary.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.next = Node(70)
# head = reverse()
nthnode()
display()