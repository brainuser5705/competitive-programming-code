class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return i+1
        
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = (len(nums))*(len(nums)+1) // 2
             
        val = 0
        for i in nums:
             val += i
             
        return s-val