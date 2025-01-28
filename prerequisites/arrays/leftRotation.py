# def leftRotation(array,length):
#     temp = array[0]
#     for i in range(length - 1):
#         array[i] = array[i + 1]
#     array[length - 1] = temp
#     for j in range(length):
#         print(array[j],end=" ")

def leftRotation(array,length):
    temp = [0] * length
    
    for i in range(1,length):
        temp[i -1] = array[i]
    temp[length - 1] = array[0]
    for j in range(length):
        print(temp[j],end=" ")
    print()

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    length = len(array)
    
    leftRotation(array,length)
