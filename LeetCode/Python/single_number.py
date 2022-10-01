class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        nums = sorted(nums)
        for i in range(len(nums)):
            
            if i == 0 and (nums[i+1] != nums[i]):
                return nums[i]
            elif i == len(nums)-1 and (nums[i-1] != nums[i]):
                return nums[i]
            elif not(nums[i] == nums[i+1] or nums[i] == nums[i-1]):
                return nums[i]
        