def inverted_letter_triangle(N):
    for i in range(N):
        for ch in range(ord('A'), ord('A') + N - i - 1):
            print(chr(ch),end="")
        print()

if __name__ == "__main__":
    N = 10
    inverted_letter_triangle(N)