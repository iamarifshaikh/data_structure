def diamond(number=5):
    for i in range(1,number):
        for j in range(i):
            print("* ",end=" ")
        print()
    
    for i in range(number):
        for j in range(number-i):
            print("* ",end=" ")
        print()

if __name__ == '__main__':
    
    diamond()