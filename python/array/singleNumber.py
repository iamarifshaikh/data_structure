def singleOccurenceNumber():
    nums = [1, 1, 2, 4, 4]
    
    hashmap = {}
    for i in nums:
        if i not in hashmap:
                hashmap[i] = 1
        else:
                hashmap[i] += 1
    print(hashmap)        
    for key,value in hashmap.items():
        if value < 2:
            print(key)
    # for i in range(len(array)):
    #     count = 0
    #     for j in range(len(array)):
    #         if array[j] == array[i]:
    #            count += 1
                # if count == 2:
                #     count = 0
        # if count == 1:
        #     print(f"{array[i]} has appeared once")
        #     return array[i]

if __name__ == "__main__":
    singleOccurenceNumber()