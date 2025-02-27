def unique_number_occurences():
    array = [1, 2, 2, 1, 1, 3]

    hashmap = {}
    
    for i in array:
        hashmap[i] = hashmap.get(i,0) + 1
        
    return False if len(hashmap.values()) != len(set(hashmap.values())) else True

unique_number_occurences()
