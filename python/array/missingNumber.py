def findMissingNumber():
    array = [1,2,4,5,6,7,8]
    N = 8
    for i in range(1,N+1):
        if i not in array:
            print(i)
            break
    # for i in range(len(array)):
    #     num = i  + 1
    #     if array[i] != num:
    #         print("Missing number in index ", i, "is ", num)

if __name__ == '__main__':
    findMissingNumber()
