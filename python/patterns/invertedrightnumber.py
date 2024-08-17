def inverted_right_number(N):
    for i in range(N):
        for j in range(N-i):
            print(j, end="")
        print()

if __name__ == "__main__":
    N = 10
    inverted_right_number(N)