def NumberPyramid(number=10):
    for i in range(1,number):
        for j in range(number-i):
            print(j+1, end=" ")
        print()

if __name__ == '__main__':
    NumberPyramid()