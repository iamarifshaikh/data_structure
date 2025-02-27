from collections import Counter
def first_unique_character():
    string = "lleetcode"
    hashmap = Counter(string)  # Automatically counts occurrences of each character

    print(hashmap)
    # for i in string:  
    #     hashmap[i] = hashmap.get(i,0) + 1
    # print(hashmap)

    for index,(key,value) in enumerate(hashmap.items()):
        if value == 1:
            print(index)
            return index

    return -1

    # for value in hashmap.values():
    #     pass

    # for value in hashmap.values():
    #     if value != 1:
    #         count += value
    #         print("if ",count)
    #     else:
    #         count = 0
    #         print("Else ",count)
    #         # return count
    # return -1

first_unique_character()
