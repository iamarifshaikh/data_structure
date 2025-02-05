def NumberPyramid(number=10):
    num = 1
    for i in range(1,number+1):
        for _ in range(1,i+1):
            print(num,end=" ")
            num += 1
        print()

if __name__ == '__main__':
    NumberPyramid()