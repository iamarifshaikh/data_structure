def count_element():
    nums = [1, 2, 2, 3, 4, 5]
    total_frequency = 0
    hashmap = {}

    for i in nums:
        hashmap[i] = hashmap.get(i, 0) + 1

    max_freq = max(hashmap.values())

    for value in hashmap.values():
        if value == max_freq:
            total_frequency += value
    
    return total_frequency
    
count_element()
