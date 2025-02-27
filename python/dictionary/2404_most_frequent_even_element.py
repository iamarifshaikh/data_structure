def most_frequent_even_element():
    nums = [0, 0,0,0,0,0]

    hashmap = {}
    element = float('-inf')
    frequency = 0

    for i in nums:
        hashmap[i] = hashmap.get(i,0) + 1
        
    for key,value in hashmap.items():
        if key % 2 == 0:
            if element == float('-inf'):
                element = key
                frequency = value
            else:
                if value > frequency:
                    element = key
                    frequency = value
                elif value == frequency:
                    element = min(element,key)

    if element == float('-inf'):
        return -1
    else:
        return element

        # freq = {}
        # for i in nums:
        #     if i % 2 == 0:
        #         if i in freq:
        #             freq[i] += 1
        #         else:
        #             freq[i] = 1
        # count = 0
        # res = -1
        # for i in freq:
        #     if freq[i] > count:
        #         count = freq[i]
        #         res = i
        #     elif freq[i] == count:
        #         if res > i:
        #             res = i
        # return res
    
    
most_frequent_even_element()
