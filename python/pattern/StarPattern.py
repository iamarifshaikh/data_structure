def starPattern(number):
    for i in range(1,number+1):
        for j in range(i):
            print("* ",end=" ")
        print()

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    starPattern(number)