def replace_element():
    array = [17,18,5,4,6,1]
    length = len(array)    
    
    for i in range(length-1,0,-1):
        if array[i] < array[i-1]:
            print(array)
        else:
            array[i-1] = array[i]
            print(array)

if __name__ == '__main__':
    replace_element()