def inverted_right_star(N):
    for i in range(N):
        for j in range(N-i):
            print("*",end="")
        print()
        
if __name__ == "__main__":
    N = 10
    inverted_right_star(N)