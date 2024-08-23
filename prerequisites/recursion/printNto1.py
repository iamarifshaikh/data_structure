def recursion(i,number):
    if i < 1:
        return
    
    print(i)
    recursion(i - 1,number)

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    recursion(number,number)