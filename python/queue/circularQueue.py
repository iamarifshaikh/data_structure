class CircularQueue:
    def __init__(self,size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.count = 0

    def isEmpty(self):
        return self.front == 0 and self.rear == 0 

    def isFull(self):
        return self.count == self.size
    
    def enqueue(self,value):
        if self.isFull():
            print("Queue is full!")
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            self.count += 1 
            print(f"Enqueued value: {value}")
            
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            value = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = 0
            else:
                self.front = (self.front + 1) % self.size
            self.count -= 1
            print(f"Dequeued value: {value}")

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            value = self.queue[self.front]  # Get the value at the front index
            print(f"Front value: {value}")

    def display(self):
        if self.isEmpty():
            print("Queue is empty! Nothing to display!")
        else:
            print("Queue elements:")
            for i in range(self.count):
                index = (self.front + i) % self.size
                print(self.queue[index], end=" ")
            print()

# Main Function
size = int(input("Enter the size of the queue: "))
queue = CircularQueue(size)

while True:
    print("\n\t 1.ENQUEUE\n\t 2.DEQUEUE\n\t 3.DISPLAY\n\t 4.EXIT \n\t")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to be inserted in queue: "))
        queue.enqueue(value)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.display()
    elif choice == 4:
        queue.peek()
    elif choice == 5:
        break
    else:
        print("Invalid Choice!! Please Enter  Again.")