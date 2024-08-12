"""This problem can be solved using two approach either by using 3 loops or by creating two variables called "stars" and "space" respectively"""

"""
Spaces: The number of leading and trailing spaces in each row decreases as you move down. For the top row, you need the maximum number of spaces. As you move to subsequent rows, the number of spaces decreases.

Formula: N - i - 1
N is the total number of rows.
i is the current row index (starting from 0).
N - i - 1 gives the number of spaces before the stars in row i.

Stars: The number of stars increases as you move down the pyramid. For the top row, there is just one star. For the second row, there are three stars, and so on.

Formula: 2 * i + 1
i is the current row index (starting from 0).
2 * i + 1 gives the number of stars in row i.
"""

def star_pyramid(N):
    for i in range(N):
        # Print leading spaces
        spaces = N - i - 1
        print(' ' * spaces, end='')
        
        # Print Stars
        stars = 2 * i + 1
        print('*' * stars)
        
def pyramid_star(N):
    for i in range(N):
        for j in range(N - i -1):
            print(" ", end="")
        
        for k in range(2 * i + 1):
            print("*", end="")
            
        for l in range(N - i - 1): # Print trailing spaces (although it's unnecessary as the trailing spaces are not actually needed)
            print("" ,end="")
        
        print()
        
if __name__ == "__main__":
    N = 5
    pyramid_star(N)
    star_pyramid(N)