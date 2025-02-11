def frequencyCount():
    array = ["apple","banana","orange","watermelon", "orange","apple" ,"orange"]
    dictionary = {}
    for i in array:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
        print(dictionary)
    print("The total frequency of all the element is ", dictionary)
    
if __name__ == '__main__':
    frequencyCount()