def factorial(N):
    if (N == 0):
        return 1
    
    return N * factorial(N - 1) 

if __name__ == '__main__':
    N = int(input("Enter the number of factorials: "))
    answer = factorial(N)
    print(f"The factorial of {N} is {answer}")