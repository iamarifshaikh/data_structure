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
    x = 30
    n = 6
    array = [15,28,35,65,75,100]
    ans = lower_bound(x,n,array)
    print("The lower bound is: ",ans)