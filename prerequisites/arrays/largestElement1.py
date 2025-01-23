from typing import List

def largestElement(array:List[int]) -> int:
    array.sort()
    return array[-1]

if __name__ == '__main__':
    array1 = [5,10,2,3,32,12,105]
    array2 = [500,10,2,314,32,122,105]
    print(f"The largest element in the array of {array1} is ", largestElement(array1))
    print(f"The largest element in the array of {array2} is ", largestElement(array2))