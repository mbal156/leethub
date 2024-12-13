class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i-1]==nums[i] and len(nums)>=2:
                return True
        return False    
