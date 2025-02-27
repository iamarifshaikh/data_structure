from collections import Counter
def luckyInteger():
    array = [2,2,3,3,3,4,4,5,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,8,8,8]
    counts = Counter(array)
    count = 0
    
    for key,value in counts.items():
        if key == value:
            if count < value:
                count = value
    
    if count == 0:
        return -1
    else:
        return count
            
if __name__ == "__main__":
    luckyInteger()