class Stack:
    def __init__(self,size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.size - 1
    
    def push(self,value):
        if self.isFull():
            print("Stack Is Full!")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Pushed value: {value}")

    def pop(self):
        if self.isEmpty():
            print("Stack Is Empty!")
        else:
            value = self.stack[self.top]
            self.top -= 1
            print(f"Popped value: {value}")

    def display(self):
        if self.isEmpty():
            print("Stack Is Empty!")
        else:
            print("Stack Elements are: ")
            for i in range(0, len(self.stack)):
                print(self.stack[i], end = ", ")
# Main Function
size = int(input("Enter the size of the stack: "))
stack = Stack(size)

while True:
    print("\n\t 1.PUSH\n\t 2.POP\n\t 3.DISPLAY\n\t 4.EXIT \n\t")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to be push into the stack: "))
        stack.push(value)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    elif choice == 4:
        break
    else:
        print("Invalid Choice!! Please Enter  Again.")