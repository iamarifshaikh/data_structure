def borderPattern(number=10):
    for i in range(number):
        for j in range(number):
            if i == 0 or i == number - 1 or j == 0 or j == number - 1:
                print("*", end=" ")
            elif i == 1 or i == number - 2 or j == 1 or j == number - 2:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    borderPattern()
