def starPattern(number):
    for i in range(number):
        for j in range(number-i):
            print("* ",end=" ")
        print()
    
if __name__ == '__main__':
    number = int(input("Enter a number: "))
    starPattern(number)