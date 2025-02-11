from collections import Counter

def checkAnagram():
    string1 = "silent"
    string2 = "listen"     

    dictionary= {}
    
    if len(string1) != len(string2):
        return False
    
    # for char in string1:
    #     if char in dictionary:
    #         dictionary[char] += 1
    #     else:
    #         dictionary[char] = 1                         
    
    # for char in string2:
    #     if char not in dictionary and dictionary[char] == 0:
    #         return False
    #     dictionary[char] -= 1
    
    print(dictionary)
    return True 
    
if __name__ == '__main__':
    checkAnagram()