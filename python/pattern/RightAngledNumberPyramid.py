def RightAngledNumberPyramid(number=10):
    for i in range(1,number):
        for j in range(i):
            print(i, end=" ")
        print()

if __name__ == "__main__":
    RightAngledNumberPyramid()