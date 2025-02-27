def count_pairs():
    nums = [-1,1,2,3,1]
    nums.sort()
    target = 2
    count = 0
    i = 0

    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if i < j:
                if nums[i] + nums[j] == target:
                    count += 1

    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1

    print(nums)

count_pairs()
