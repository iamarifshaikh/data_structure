def SmallerThanZero():
    array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    count = 0
    lower = 0
    length = len(array) - 1
    higher = length
    answer = length

    while lower <= higher:
        middle = (lower + higher) // 2
        if array[middle] < 0:
            answer = middle
            lower = middle + 1
        else:
            higher = middle - 1
    count = answer + 1
    print(count)


SmallerThanZero()