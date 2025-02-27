def upper_bound():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    length = len(array) - 1
    lower = 0
    higher = length
    answer = length
    target = 8

    while lower < higher:
        middle = (lower + higher) // 2
        if array[middle] > target:
            answer = middle
            higher = middle - 1
        else:
            lower = middle + 1
    print(answer)
    
upper_bound()