from collections import Counter

def majority_elements():
    array = [2, 2, 1, 1, 1, 1,1,2, 2]
    length = len(array)
    
    count = Counter(array)
    
    for key,count in count.items():
        if count > (length // 2):
            print(f"{key} has occured more than half times the size of the array")
            return key
    # dictionary = {}
    # length = len(array)
    # half = length // 2
    # count = Counter(dictionary)
    
    # for i in array:
    #     if i not in dictionary:
    #         dictionary[i] = 1
    #     else:
    #         dictionary[i] += 1
    #     print(dictionary)

    # for key,value in dictionary.items():
    #     if value > half:
    #         print(f"{key} has occured more than half time")
        
if __name__ == '__main__':
    majority_elements()
