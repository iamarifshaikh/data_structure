def printArray(n, array):
    print("The reversed array is: ")
    for i in range(n):
        print(array[i], end=" ")
    print()


def reverseArray(n, array):
    p1 = 0
    p2 = n - 1

    while p1 < p2:
        # Swapping by using tuple notation
        array[p1], array[p2] = array[p2], array[p1]
        p1 += 1
        p2 -= 1

    printArray(n, array)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    n = len(array)
    reverseArray(n, array)