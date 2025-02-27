def contains_duplicate():
    nums = [1,2,3,1] 
    k = 3
    hashmap = {}
    
    for i in nums:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    print(hashmap)    
    
contains_duplicate()