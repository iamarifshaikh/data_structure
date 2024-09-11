from typing import List

def moveZerosToEnd(array: List[int]) -> List:
    # Length Of the array
    n = len(array)
    
    j = -1
    
    for i in range(n):
        if array[i] == j:
            break     

if __name__ == '__main__':
    array = [0, 0, 4, 2, 3, 7, 0, 5, 1, 8]
    moveZerosToEnd(array) 