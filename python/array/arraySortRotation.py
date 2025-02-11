class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[i+1]:
                count = count + 1
                i += 1
        
        if count == 1:
            return True
        else:
            return False