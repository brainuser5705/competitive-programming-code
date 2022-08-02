class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)
        
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = total - left - nums[i]   # remove the pivot element
            
            if left == right:
                return i
            
        return -1