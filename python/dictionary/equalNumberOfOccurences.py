from statistics import mode

def equal_number_of_occurrences():
    string = "abacbcd"
    
    initial_value = string.count(string[0])

    for i in set(string):
        if string.count(i) != initial_value:
            return False

        return True
    # dictionary = {}
    # count = 0
    
    # for i in string:
    #    dictionary[i] = dictionary.get(i,0) + 1 
    
    # for value in dictionary.values():
    #     if count == 0:
    #         count = value
    #     elif value == count:
    #         continue
    #     else:
    #         return False
    # return True
    
    # print("The string have equal number of occurences"if len(set(dictionary.values())) == len(set(count)) else "It doesn't have equal number of occurences")
    
if __name__ == '__main__':
    equal_number_of_occurrences()