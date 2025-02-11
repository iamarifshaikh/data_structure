def twoSum():
    array = [1,2,3,4,5]
    target = 5

    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == target:
                print(i,j) 
    
if __name__ == '__main__':
    twoSum()