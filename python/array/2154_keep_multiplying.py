def keep_multiplying():
    original = 3
    nums = [5, 3, 6, 1, 12]
    num_set = set(nums)

    while original in num_set:
        original *= 2
    return original
keep_multiplying()
