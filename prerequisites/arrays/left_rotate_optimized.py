def left_rotate_optimized(array,k):
    length = len(array)
    k = k % length
    return array[k:] + array[:k]

print(left_rotate_optimized([1, 2, 3, 4, 5], 2))  # Output: [3, 4, 5, 1, 2]