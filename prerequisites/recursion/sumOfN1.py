def sum_of_N_recurse(N):
    if N == 0:
        return N
    else:
        return N + sum_of_N_recurse(N - 1)

if __name__ == "__main__":
    N = int(input("Enter the number: "))
    result = sum_of_N_recurse(N)
    print("The Sum Of ", N," is ", result)