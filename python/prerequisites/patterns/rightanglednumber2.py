def right_angled_number_2(N):
    for i in range(N):
        for j in range(1,i+1):
            print(i,end="")
        print()

if __name__ == "__main__":
    N = 20
    right_angled_number_2(N)