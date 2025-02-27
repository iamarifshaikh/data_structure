def targetIndices():
    nums = [1, 2, 2, 2, 3, 5]

    left = 0
    right = len(nums) - 1
    ans = []
    target = 2
    
    nums.sort()
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans.append(mid)
            for i in range(mid + 1 , right + 1):
                if nums[i] == target:
                    ans.append(i)
            
            if nums[mid] < target:
                if nums[left] == target:
                    ans.append(left)
                left = mid + 1
            else:
                if nums[right] == target:
                    ans.append(right)        
                right = mid - 1
        print(ans)
        return sorted(list(ans))    
    
    
    
    # target = 2
    # indices = []
    
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         indices.append(i)
    # print(indices)
    # nums.sort()

    # start = 0
    # end = len(nums)
    # indices = []
    # target = 2

    
    # while start <= end:
    #     middle = (start + end) // 2

    #     if nums[middle] == target:
    #         indices.append(middle)  

    #     elif nums[middle] < target:
    #         start = middle + 1

    #     elif nums[middle] > target:
    #         end = middle - 1

targetIndices()