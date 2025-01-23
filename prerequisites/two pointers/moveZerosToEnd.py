def moveZerosToEnd(array):
    zero_index = 0
    
    for current in range(len(array)):
        if array[current] != 0:
            array[zero_index],array[current] = array[current],array[zero_index]
            zero_index += 1
    
    return array
  
if __name__ == '__main__':
    array = [0,1,15,2,0,3,0,4]
    print("Array before moveZerosToEnd: " + str(array))
    moveZerosToEnd(array)
    print("Array after moveZerosToEnd: " + str(array))