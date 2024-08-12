def right_angled_star(N):
    for i in range(N):
        for j in range(i):
            print("*", end="")
        print()
            
if __name__ == "__main__":
    N = 10
    right_angled_star(N)
    