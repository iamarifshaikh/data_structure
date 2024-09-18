def checkArrayIsSortedOrNot(array):
    n = len(array)
    
    for i in range(n):
        for j in range(i + 1,n):
            if array[j] < array[i]:
                return False
    
    return True

if __name__ == '__main__':
    array = [1,2,3,4,5,7,6]
    answer = checkArrayIsSortedOrNot(array)
    
    if answer:
        print("The Elements are sorted")
    else:
        print("The Elements are not sorted")