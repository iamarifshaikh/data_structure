def searchRange():
    nums = [5, 7, 7, 8, 8, 10]
    low = 0
    high = len(nums) -1 
    target = 8
    indices = []

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            indices.append(mid)
            for i in range(mid + 1, right + 1):
                if nums[i] == target:
                    indices.append(i)

            if nums[mid] < target:
                if nums[left] == target:
                    indices.append(left)
                left = mid + 1
            else:
                if nums[right] == target:
                    indices.append(right)
                right = mid - 1


searchRange()
