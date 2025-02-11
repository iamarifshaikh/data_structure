def singleNumber():
    array = [1, 1, 2, 2, 3, 3, 4,4, 5, 5,6,7,7]
    dictionary = {}
    
    for i in array:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary[i] + 1
    # print(dictionary)
    
    for key,value in dictionary.items():
        if value == 1:
            print(f"{key} occurs once in a list")
            return dictionary[key]
            
    
if __name__ == '__main__':
    singleNumber()