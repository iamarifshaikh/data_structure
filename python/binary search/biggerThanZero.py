def BiggerThanZero():
    array = [5,6,7,8,10]
    length = len(array) - 1
    count = 0
    answer = length
    lower = 0

    higher = len(array) - 1

    while lower < higher:
        middle = (lower + higher) // 2
        if array[middle] >= 0:
            answer = middle
            higher = middle - 1
        else:
            lower = middle + 1

    count = length - middle
    print(count)

BiggerThanZero()