def lower_bound(x,n,array):
    low = 0
    high = n - 1
    answer = n

    while low <= high:
        middle = (low + high) // 2
        # maybe an answer
        if array[middle] >= x:
            answer = middle
            high = middle - 1
        else:
            low = middle + 1  # look on the right

    return answer
 

if __name__ == "__main__":
    array = [15,28,35,65,75,100]
    n = len(array)
    x = 30
    ans = lower_bound(x,n,array)
    print("The lower bound is: ",ans)