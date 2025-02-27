def sum_of_unique_elements():
    array = [10]
    sum = 0
    dictionary = {}

    for num in array:
        dictionary[num] = dictionary.get(num, 0) + 1
    print(dictionary)

    for key,value in dictionary.items():
        if value == 1:
            sum += key
    return sum
    # if len(dictionary) == 1 and value == 1:
    #     sum += key
    #     return sum
    # elif len(dictionary) == 1:
    #     return sum
    # else:
    #     if value == 1:
    #         sum += key

    # print("Sum of unique elements in the dictionary is", sum)
    return sum

if __name__ == '__main__':
    sum_of_unique_elements()
