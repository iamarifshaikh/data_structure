def increasing_number_pattern(number=10):
    for i in range(1,number+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

if __name__ == '__main__':
    increasing_number_pattern() 