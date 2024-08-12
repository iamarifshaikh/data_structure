def right_angled_number_1(N):
    for i in range(1,N + 1):
        for j in range(1,i+1):  # Print numbers from 1 to the current row number
            print(j, end=" ")
        print() # Move to the next line

if __name__ == "__main__":
    N = 10
    right_angled_number(N)