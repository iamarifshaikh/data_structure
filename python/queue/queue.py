class Queue:
    def __init__(self,size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size
    
    def isEmpty(self):
        return self.front == -1 and self.rear == -1
    
    def isFull(self):
        return self.rear ==  self.size - 1
    
    def enqueue(self,value):
        if self.isFull():
            print("Queue is full!")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
            print(f"Enqueued value: {value}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            value = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1  # Increment the front index
        print(f"Dequeued value: {value}")
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty! Nothing to display!")
        else:
            print("Queue elements are: ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=", ")
            print(self.queue[self.rear])

# Main Function
size = int(input("Enter the size of the queue: "))
queue = Queue(size)

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
        break
    else:
        print("Invalid choice!")