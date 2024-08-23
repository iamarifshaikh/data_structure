def recursion(i,number):
    if i > number:
        return
    
    print(i, end=" ")
    recursion(i+1, number) 
    
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    recursion(1, number)