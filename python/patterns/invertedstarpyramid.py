def inverted_star_pyramid(N):
    for i in range(N):
        for j in range(i):
            print(" ",end="")
            
        for k in range(2 * (N - i) - 1):
            print("*",end="")
        
        for l in range(i):
            print(" ",end="")
            
        print()

def star_pyramid_inverted(N):
    for i in range(N):
        # Calculate spaces and stars
        spaces = i
        stars = 2 * (N - i) - 1
        
        # Print spaces and stars
        print(" " * spaces, end="")
        print("*" * stars)
        
if __name__ == "__main__":
    N = 5
    # inverted_star_pyramid(N)
    star_pyramid_inverted(N)