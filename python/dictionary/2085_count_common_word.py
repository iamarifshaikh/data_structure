def arif():
    words1 = ["leetcode","is","amazing","as","is"] 
    words2 = ["amazing","leetcode","is"]    

    hashmap1 = {}
    hashmap2 = {}

    for i in words1,words2:
        hashmap1[i] = hashmap1.get(i, 0) + 1
    print(set(hashmap1))

    # for i in words2:
    #     hashmap2[i] = hashmap2.get(i, 0) + 1
    # print(set(hashmap2))
    
arif()