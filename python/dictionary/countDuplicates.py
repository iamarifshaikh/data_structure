def count_duplicates():
    nums = [1,2,3,1]
    return False if len(nums) == set(nums) else True
    
    #  return len(set(nums)) != len(nums)
    
    # if len(nums) == len(set(nums)):
    #         return False
    # else:
    #         return True
    
    
    
    # count = set(nums)
    # if len(count) == len(nums):
    #         return False
    # else:
    #         return True
    
    # for value in set(nums):
    #     if set == 1:
    #         print(True)
    #         return True
    #     else:
    #         return False

count_duplicates()