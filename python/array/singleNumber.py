def singleOccurenceNumber():
    array = [1,1,2,2,3,3,4,4]
    count = 0   
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] == array[i]:
                count += 1
        if count == 1:
            print(f"{array[i]} has appeared once")
            return array[i]
                            
if __name__ == "__main__":
    singleOccurenceNumber()