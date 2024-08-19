def lowerBound(n,x,array):
    for i in range(n):
        if array[i] >= x:
            return i
    return n

if __name__ == "__main__":
    array = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ans = lowerBound(n,x,array)
    print("The lower bound is the index: ", ans)