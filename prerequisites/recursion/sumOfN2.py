def sum_of_N_recurse(N,sum):
    if N < 1 or N == 0:
        return sum
    else:
        return sum_of_N_recurse(N - 1, sum + N)

if __name__ == "__main__":
    N = int(input("Enter the number: "))
    answer = sum_of_N_recurse(N,0)
    print("The Sum Of ",N,"is", answer)