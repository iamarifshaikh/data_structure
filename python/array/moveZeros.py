def moveZerosToEnd():
    array = [0,0,3,5,8,2,0,0]
    i= -1
    for j in range(len(array)):
        if array[j] != 0:
            i +=1
            array[i],array[j] = array[j],array[i]
            
        # else:
        #     for k in range(j,len(array)):
        #         if array[k] != 0:
        #             array[j],array[k] = array[k],array[j]
    print(f"Array after modification: ", array)


if __name__ == '__main__':
    moveZerosToEnd()
