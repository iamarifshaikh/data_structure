def isPairSum(N,array,X):
    i = 0
    j = N - 1

    while i < j:
        if array[i] + array[j] == X:
            return True
        
        elif array[i] + array[j] < X:
            i += 1
            
        else:
            j -= 1
    
    return 0
        
if __name__ == "__main__":
    array = [3, 5, 9, 2, 8, 10, 11]
    X = 17
    N = len(array)
    
    isPairSum(N,array,X)