def printArray(n,array):
    print("The reversed array is:- ")
    for i in range(n):
        print(array[i], end=" ")
    print()

def reverseArray(array,start,end):
    if start < end:
        array[start], array[end] = array[end], array[start]
        reverseArray(array,start + 1,end - 1)
        
if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9]
    n = len(array)
    reverseArray(array, 0, n - 1)
    printArray(n,array)